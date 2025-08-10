from tkinter import messagebox
import cv2
from att import *


dataPath = "data.txt"

def get_name_by_id(filepath, user_id):
    try:
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()
                if ":" in line:
                    key, value = line.split(":", 1)
                    if key.strip() == str(user_id):
                        return value.strip()
        return None  # ID not found
    except FileNotFoundError:
        print("File not found:", filepath)
        return None

# Set to track already marked IDs
already_marked_ids = set()

def recog():
    def draw_boundary(img, classifier, scalefactor, minNeighbour, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scalefactor, minNeighbour)
        coord = []
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            if confidence >= 75:
                fetchedName = get_name_by_id(dataPath, id)
                cv2.putText(img, f"Name : {fetchedName}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (230, 44, 155), 2)
                cv2.putText(img, f"ID : {id}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (230, 44, 155), 2)

                # Only write attendance if not already marked
                if id not in already_marked_ids:
                    write_attendance(fetchedName, id)
                    already_marked_ids.add(id)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
            coord = [x, y, w, h]
        return coord

    def rec(img, clf, faceCascade):
        coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
        return img

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    video_cap = cv2.VideoCapture(0)
    while True:
        ret, img = video_cap.read()
        img = rec(img, clf, faceCascade)
        cv2.imshow("Welcome to Face Recognition", img)
        if cv2.waitKey(1) == 13:  # Press Enter to exit
            break
    video_cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Result", "Successfully Taken Attendance")


if __name__ == "__main__":
    recog()

from tkinter import messagebox
import cv2
import os

def generate_dataset(id):
    try:
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
        # Ensure the data folder exists
        if not os.path.exists("data"):
            os.makedirs("data")

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                return img[y:y+h, x:x+w]  # Corrected cropping
            return None  # If no face is detected

        cap = cv2.VideoCapture(0)
        img_id = 0
        # id = 1  # This can be dynamic later

        while True:
            ret, my_frame = cap.read()
            if not ret:
                break

            face = face_cropped(my_frame)
            if face is not None:
                img_id += 1
                face = cv2.resize(face, (450, 450))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                file_name_path = f"data/user.{id}.{img_id}.jpg"
                cv2.imwrite(file_name_path, face)

                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Cropped face", face)

            if cv2.waitKey(1) == 13 or img_id == 100:  # Press ENTER key to break
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Dataset generation completed.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_dataset()

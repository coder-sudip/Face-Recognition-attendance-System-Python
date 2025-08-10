from tkinter import messagebox
import cv2
import os
import numpy as np
from PIL import Image

def train_classifier():
    try:
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append (imageNp)
            ids.append(id)
            cv2.imshow( "Training..." , imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train the classifier And save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")
                    
    
    except Exception as e:
        print(f"Error : {e}")



if __name__ == "__main__":
    train_classifier()
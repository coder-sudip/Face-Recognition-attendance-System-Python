from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk,ImageFilter
import os
from train import *
from generate import *
from data import *
from recognitions import *
import shutil

app=Tk()
app.iconbitmap("image/my_icon.ico")

def open_folder():
    path ="data" 
    if os.path.exists(path):
        os.startfile(path)
    else:
        print("Folder does not exist!")

def open_popup():
    popup = tk.Toplevel(app)
    popup.title("Enter Details")
    popup.geometry("300x200+600+200")
    popup.maxsize(300,200)
    popup.iconbitmap("image/my_icon.ico")
    

    # Name
    tk.Label(popup, text="Enter Name:").pack(pady=(10, 0))
    name_entry = tk.Entry(popup, width=25)
    name_entry.pack()

    # ID
    tk.Label(popup, text="Enter ID:").pack(pady=(10, 0))
    id_entry = tk.Entry(popup, width=25)
    id_entry.pack()
    def submit():
        name = name_entry.get().strip()
        uid = id_entry.get().strip()
        if name and uid:
            add_or_update(file_path, uid, name)
            generate_dataset(uid)
            messagebox.showinfo("Submitted", f"Name: {name}, ID: {uid}")
            popup.destroy()
        else:
            messagebox.showwarning("Error", "Please fill both fields")
    
    button_frame = tk.Frame(popup)
    button_frame.pack(pady=20)
    tk.Button(button_frame, text="Submit", command=submit).pack(side="left", padx=10)
    tk.Button(button_frame, text="Cancel", command=popup.destroy).pack(side="left", padx=10)



def open_delete_popup():
    # Create popup window
    popup = tk.Toplevel(app)
    popup.title("Confirm Deletion")
    popup.geometry("300x100+600+200")
    popup.transient(app)  # Keep popup above parent
    popup.grab_set()  # Make it modal
    popup.iconbitmap("image/my_icon.ico")


    # Message label
    tk.Label(popup, text="Are you sure you want to delete files?", wraplength=250, pady=10).pack()

    # Button frame
    btn_frame = tk.Frame(popup)
    btn_frame.pack(pady=10)

    def confirm_delete():
        if os.path.exists("data"):
            print("Deleting data directory...")
            shutil.rmtree("data",ignore_errors=True)
        files_to_delete = ["data.txt", "attendance.xlsx","classifier.xml"]
        for file in files_to_delete:
            if os.path.exists(file):
                os.remove(file)
        popup.destroy()
        messagebox.showinfo("Success", "Files deleted successfully!")


    def cancel_delete():
        popup.destroy()

    # Buttons
    tk.Button(btn_frame, text="Confirm", width=10, bg="red", fg="white", command=confirm_delete).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Cancel", width=10, command=cancel_delete).pack(side="left", padx=5)



scrnH=app.winfo_screenheight()
scrnW=app.winfo_screenwidth()
app.geometry(f"{scrnW}x{scrnH}+{0}+{0}")
app.title("Face Recogniction Project")

# ---------BACKGROUND IMAGE---------
bgImg=Image.open("image/bg.jpg")
blured_bg = bgImg.filter(ImageFilter.GaussianBlur(radius=20))
blured_bg=blured_bg.resize((scrnW,scrnH),Image.Resampling.LANCZOS)
bgImg=ImageTk.PhotoImage(blured_bg)
bgLbl=Label(app,image=bgImg)
bgLbl.place(x=0,y=0)



# ------------Important---------------
fontSize=15
placeX=150
placeY=380
btnTxt="#F4F4CC"

heading=Label(bgLbl,text="Face Recognition Attendance System",font=("times new roman",30,"bold"),bg="#140035",fg="#B6F810")
heading.place(x=placeX+300,y=placeY-150)


# ---------Button1-IMAGE1---------
img1=Image.open("image/reg.png")
img1=img1.resize((150,150),Image.Resampling.LANCZOS)
img1=ImageTk.PhotoImage(img1)
btn1=Button(bgLbl,image=img1,bg="#1c9d65",cursor="hand2",command=open_popup)
btn1.place(x=placeX,y=placeY)
btn1_1=Button(bgLbl,bg="#1c9d65",text="Registration",cursor="hand2",font=("times new roman",fontSize),fg=btnTxt,command=open_popup)
btn1_1.place(x=placeX,y=placeY+155,width=156,height=30)

# ---------Button2-IMAGE2---------
img2=Image.open("image/train.png")
img2=img2.resize((150,150),Image.Resampling.LANCZOS)
img2=ImageTk.PhotoImage(img2)
btn2=Button(bgLbl,image=img2,bg="#1c9d65",cursor="hand2",command=train_classifier)
btn2.place(x=placeX+210,y=placeY)
btn2_1=Button(bgLbl,bg="#1c9d65",text="Train Data",cursor="hand2",font=("times new roman",fontSize),fg=btnTxt,command=train_classifier)
btn2_1.place(x=placeX+210,y=placeY+155,width=156,height=30)


# ---------Button3-IMAGE3---------
img3=Image.open("image/att.jpg")
img3=img3.resize((150,150),Image.Resampling.LANCZOS)
img3=ImageTk.PhotoImage(img3)
btn3=Button(bgLbl,image=img3,bg="#1c9d65",cursor="hand2",command=recog)
btn3.place(x=placeX+420,y=placeY)
btn3_1=Button(bgLbl,bg="#1c9d65",text="Attendance",cursor="hand2",font=("times new roman",fontSize),fg=btnTxt,command=recog)
btn3_1.place(x=placeX+420,y=placeY+155,width=156,height=30)


# ---------Button4-IMAGE4---------
img4=Image.open("image/photos.png")
img4=img4.resize((150,150),Image.Resampling.LANCZOS)
img4=ImageTk.PhotoImage(img4)
btn4=Button(bgLbl,image=img4,bg="#1c9d65",cursor="hand2",command=open_folder)
btn4.place(x=placeX+630,y=placeY)
btn4_1=Button(bgLbl,bg="#1c9d65",text="Image Sample",cursor="hand2",font=("times new roman",fontSize),fg=btnTxt,command=open_folder)
btn4_1.place(x=placeX+630,y=placeY+155,width=156,height=30)


# ---------Button5-IMAGE5---------
img5=Image.open("image/reset.png")
img5=img5.resize((150,150),Image.Resampling.LANCZOS)
img5=ImageTk.PhotoImage(img5)
btn5=Button(bgLbl,image=img5,bg="#1c9d65",cursor="hand2",command=open_delete_popup)
btn5.place(x=placeX+840,y=placeY)
btn5_1=Button(bgLbl,bg="#1c9d65",text="Reset Data",cursor="hand2",font=("times new roman",fontSize),fg=btnTxt,command=open_delete_popup)
btn5_1.place(x=placeX+840,y=placeY+155,width=156,height=30)


# ---------Button6-IMAGE6---------
img6=Image.open("image/exit.png")
img6=img6.resize((150,150),Image.Resampling.LANCZOS)
img6=ImageTk.PhotoImage(img6)
btn6=Button(bgLbl,image=img6,bg="#1c9d65",cursor="hand2",command=app.destroy)
btn6.place(x=placeX+1050,y=placeY)
btn6_1=Button(bgLbl,bg="#1c9d65",text="Exit",cursor="hand2",font=("times new roman",fontSize),fg=btnTxt,command=app.destroy)
btn6_1.place(x=placeX+1050,y=placeY+155,width=156,height=30)


app.mainloop()

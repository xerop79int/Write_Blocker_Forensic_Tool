from tkinter import *
from re import S
import winreg  # "SYSTEM\CurrentControlSet\Control\StorageDevicePolicies
import os
import wmi
import copyusb
import shutil
from shutil import copytree

# class WriteBlocker:

#     copy_result_list = copyusb.copy()

#     c = wmi.WMI()

#     print("\nThe Following are the USB Devices Currently Connected To Your System : \n ")


#     for drive in c.Win32_DiskDrive():

#         print("---> Device Name :", drive.caption, "\n")

#         print("1-Device Type : ", drive.mediatype, "\n")

#         print("2-Device Model : ", drive.model, "\n")

#         print("3-Device Storage Size : ", drive.Size, "Bytes \n")

#         print("----------------------------------------------- \n")


#     o = input("Do You Want to Turn On Write Blocking On All Ports?(Yes/No)\n")

#     if o == "Yes":

#         registry_key = winreg.OpenKey(

#             winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\StorageDevicePolicies", 0, winreg.KEY_WRITE)

#         winreg.SetValueEx(registry_key, "WriteProtect", 0, winreg.REG_DWORD, 1)

#         print("Write Blocking Has Been Enabled On All Ports!\n")

#         print("----------------------------------------------- \n")


#     if o == "No":
#         print("Write Blocking Has Been Disabled On All Ports!\n")

#         registry_key = winreg.OpenKey(

#             winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\StorageDevicePolicies", 0, winreg.KEY_WRITE)

#         winreg.SetValueEx(registry_key, "WriteProtect",

#                         0, winreg.REG_DWORD, 0)

#         print("----------------------------------------------- \n")


#     choice = input(
#         "Do you want to make an image of the storage device? Press Y or N\n ")
#     if choice == "Y":
#         files = os.listdir("E:")
#         print("The files in the storage device are:\n ", files)
#         destination = ("Evidence Image")
#         try:
#             for f in files:
#                 source = ('E:')
#                 copytree(source, destination)
#         except Exception as e:
#             print(e)
#             print("----------------------------------------------- \n")
#             print("Image Made")
#             os.system("pause")
#     else:
#         print("Okay!")


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.resizable(False, False)
        self.image = "./download.png"
    
    def NoFunction(self):
        registry_key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\StorageDevicePolicies", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, "WriteProtect",
                      0, winreg.REG_DWORD, 0)
        
        self.SecondWindow()
    
    def FirstWindow(self):
        self.backGroundImage = PhotoImage(file=self.image)
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y = 0)

        self.title = Label(self, text="Write Blocker", font="Bold 30", fg="white")
        self.title.config(bg="#150424")
        self.title.place(x=230, y=100)

        self.title = Label(self, text="Saleh Bashir", font="200", fg="white")
        self.title.config(width= 15)
        self.title.config(bg="#150424")
        self.title.place(x=260, y=200)

        self.title = Label(self, text="Hammad Manzoor", font="200", fg="white")
        self.title.config( width= 15)
        self.title.config(bg="#150424")
        self.title.place(x=260, y=250)

        self.button = Button(self, text="Ok", font="50", fg="black", command=self.SecondWindow)
        self.button.config(width = 15)
        self.button.config(bg="white")
        self.button.place(x=260, y=300)
        
        
    
    def SecondWindow(self):
        self.geometry("700x500")
        self.resizable(False, False)

        self.backGroundImage = PhotoImage(file=self.image)
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y = 0)

        self.canvas = Canvas(self, width=400, height=330)
        self.canvas.place(x=150, y = 40)

        copy_result_list = copyusb.copy()

        c = wmi.WMI()

        self.title = Label(self, text="Connected Devices\n", font="50", fg="black")
        self.title.place(x=260, y=50)

        adjust = 80

        for drive in c.Win32_DiskDrive():

            self.title = Label(self, text="---> Device Name :" +  drive.caption + "\n", fg="black")
            self.title.place(x=150, y=adjust)
            adjust += 20

            self.title = Label(self, text="Device Type : " + drive.mediatype + "\n", fg="black")
            self.title.place(x=150, y=adjust)
            adjust += 20

            self.title = Label(self, text="Device Model : " + drive.model + "\n", fg="black")
            self.title.place(x=150, y=adjust)
            adjust += 20

            self.title = Label(self, text="Device Storage Size : " + drive.Size + "Bytes\n", fg="black")
            self.title.place(x=150, y=adjust)
            adjust += 20

            self.title = Label(self, text="----------------------------------------------- \n", fg="black")
            self.title.place(x=150, y=adjust)
            adjust += 20


        self.button = Button(self, text="Scan", font="50", fg="black", command=self.ThirdWindow)
        self.button.config(width = 15)
        self.button.config(bg="white")
        self.button.place(x=260, y=400)
    
    def ThirdWindow(self):
        self.geometry("700x500")
        self.resizable(False, False)

        self.backGroundImage = PhotoImage(file=self.image)
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y = 0)

        self.title = Label(self, text="Do you want to Enable Write blocking?", font="Bold 20", fg="white")
        self.title.config(bg="#150424")
        self.title.place(x=130, y=100)

        self.button = Button(self, text="Yes", font="50", fg="black", command=self.FourthWindow)
        self.button.config(width = 15)
        self.button.config(bg="white")
        self.button.place(x=150, y=300)

        self.button = Button(self, text="No", font="50", fg="black", command=self.NoFunction)
        self.button.config(width = 15)
        self.button.config(bg="white")
        self.button.place(x=360, y=300)
    
    def FourthWindow(self):

        registry_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\StorageDevicePolicies", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, "WriteProtect", 0, winreg.REG_DWORD, 1)

        self.geometry("700x500")
        self.resizable(False, False)

        self.backGroundImage = PhotoImage(file=self.image)
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y = 0)

        self.title = Label(self, text="Write blocking enabled", font="Bold 20", fg="white")
        self.title.config(bg="#150424")
        self.title.place(x=200, y=100)

        self.button = Button(self, text="Disable", font="50", fg="black", command=self.SecondWindow)
        self.button.config(width = 15)
        self.button.config(bg="white")
        self.button.place(x=150, y=300)

        self.button = Button(self, text="Proceed", font="50", fg="black", command=self.FifthWindow)
        self.button.config(width = 15)
        self.button.config(bg="white")
        self.button.place(x=360, y=300)

    def FifthWindow(self):

        self.geometry("700x500")
        self.resizable(False, False)

        self.backGroundImage = PhotoImage(file=self.image)
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y = 0)

        self.title = Label(self, text="Do you want to make a copy \nof the storage device?", font="Bold 20", fg="white")
        self.title.config(bg="#150424")
        self.title.place(x=180, y=100)

        self.button = Button(self, text="Yes", font="50", fg="black", command=self.SixthWindow)
        self.button.config(width = 15)
        self.button.config(bg="white")
        self.button.place(x=150, y=300)

        self.button = Button(self, text="No", font="50", fg="black", command=self.FourthWindow)
        self.button.config(width = 15)
        self.button.config(bg="white")
        self.button.place(x=360, y=300)

    def SixthWindow(self):


        self.backGroundImage = PhotoImage(file=self.image)
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y = 0)

        self.title = Label(self, text="Image Made", font="Bold 30", fg="white")
        self.title.config(bg="#150424")
        self.title.place(x=250, y=100)

        self.button = Button(self, text="Start Again", font="50", fg="black", command=self.FirstWindow)
        self.button.config(width = 15)
        self.button.config(bg="white")
        self.button.place(x=260, y=300)

        files = os.listdir("E:")
        print("The files in the storage device are:\n ", files)
        destination = ("Evidence Image")
        try:
            for f in files:
                source = ('E:')
                copytree(source, destination)
        except Exception as e:
            print(e)
            print("----------------------------------------------- \n")
            print("Image Made")

if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.FirstWindow()
    mainWindow.mainloop()
    


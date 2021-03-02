try: 
    import img2pdf
except:
    import os
    print("Requirements not found\n\nInstalling requirements now...\n")
    try:
        os.system("pip install img2pdf")
    except:
        try:
            os.system("pip3 install img2pdf")
        except:
            os.system("pip2 install img2pdf")
    print("\nRequirements have been installed. Run the applicaiton again.\n")
    exit()

import time
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.withdraw()

imgList = filedialog.askopenfilenames()

imgList = list(imgList)
print("This is the order your files will be converted to pdf in :")
    
for image in imgList:
    print(imgList.index(image) + 1, image)

if input("\nIs the order correct? (Y/n): ") == "n":
    try:
        correct_order = input("\nEnter correct order or images separated by commas. eg: 2,3,1,5,4: ").split(",")
    except Exception as e:
        print("Please enter order correcctly")
        correct_order = input("\nEnter correct order or images separated by commas. eg: 2,3,1,5,4: ").split(",")
    corrected_list = []
    for index in correct_order:
        print(index)
        corrected_list.append(imgList[int(index) - 1])
    print(corrected_list)


try:
    pdfData = img2pdf.convert(imgList)
    fileName = input("Enter pdf filename: ")
    with open(f"{fileName}.pdf", "wb") as pdffile:
        pdffile.write(pdfData)

    print("PDF Created!")
    print("Exiting now...")
    time.sleep(3)
except Exception as e:
    print("Filetype not supported.")
    time.sleep(3)
    

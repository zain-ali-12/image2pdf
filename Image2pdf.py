import img2pdf 
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.withdraw()

imgList = filedialog.askopenfilenames()

imgList = list(imgList)

print("This is the order your files will be converted to pdf in :")

for image in imgList:
    print(image)

try:
    pdfData = img2pdf.convert(imgList)

except Exception as e:
    print("Image has transparency which is not supported.")

fileName = input("Enter pdf filename: ")

with open(f"{fileName}.pdf", "wb") as pdffile:
    pdffile.write(pdfData)

print("PDF Created!")
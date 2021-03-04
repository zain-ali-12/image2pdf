import time
import tkinter as tk
from tkinter import filedialog
import subprocess
import random

import subprocess
try:
    subprocess.run(['wrongcommand'], check = True)
except subprocess.CalledProcessError:
    print ('wrongcommand does not exist')

try: 
    import colorama
    from colorama import Fore, Back, Style
except:
    print("Requirements not found\n\nInstalling requirements now...\n")
    try:
        subprocess.run(['pip install colorama'], check = True)
    except:
        subprocess.run(['pip3 install colorama'], check = True)
    print("\nRequirements have been installed. Run the applicaiton again.\n")
    exit()

try: 
    import img2pdf
except:
    print("Requirements not found\n\nInstalling requirements now...\n")
    try:
        subprocess.run(['pip install img2pdf'], check = True)
    except:
        subprocess.run(['pip3 install img2pdf'], check = True)
    print(f"\n{Fore.GREEN}[+]{Fore.RESET} Requirements have been installed. Run the applicaiton again.\n")
    exit()

colorama.init(autoreset=True)

try:
    subprocess.run(['cls'], check = True)
except:
    subprocess.run(['clear'], check = True)

banners = [
r'''
 M""M M"""""`'"""`YM MM'"""""`MM          d8888b.          MM"""""""`YM M""""""'YMM MM""""""""`M 
 M  M M  mm.  mm.  M M' .mmm. `M              `88          MM  mmmmm  M M  mmmm. `M MM  mmmmmmmM 
 M  M M  MMM  MMM  M M  MMMMMMMM          .aaadP'          M'        .M M  MMMMM  M M'      MMMM 
 M  M M  MMM  MMM  M M  MMM   `M 88888888 88'     88888888 MM  MMMMMMMM M  MMMMM  M MM  MMMMMMMM 
 M  M M  MMM  MMM  M M. `MMM' .M          88.              MM  MMMMMMMM M  MMMM' .M MM  MMMMMMMM 
 M  M M  MMM  MMM  M MM.     .MM          Y88888P          MM  MMMMMMMM M       .MM MM  MMMMMMMM 
 MMMM MMMMMMMMMMMMMM MMMMMMMMMMM                           MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM 
''',
r'''
 _________ _______  _______      _______        _______  ______   _______ 
 \__   __/(       )(  ____ \    / ___   )      (  ____ )(  __  \ (  ____ \
    ) (   | () () || (    \/    \/   )  |      | (    )|| (  \  )| (    \/
    | |   | || || || |      _____   /   )_____ | (____)|| |   ) || (__    
    | |   | |(_)| || | ____(_____)_/   /(_____)|  _____)| |   | ||  __)   
    | |   | |   | || | \_  )     /   _/        | (      | |   ) || (      
 ___) (___| )   ( || (___) |    (   (__/\      | )      | (__/  )| )      
 \_______/|/     \|(_______)    \_______/      |/       (______/ |/       
''',
r'''
 ██╗███╗   ███╗ ██████╗       ██████╗       ██████╗ ██████╗ ███████╗
 ██║████╗ ████║██╔════╝       ╚════██╗      ██╔══██╗██╔══██╗██╔════╝
 ██║██╔████╔██║██║  ███╗█████╗ █████╔╝█████╗██████╔╝██║  ██║█████╗  
 ██║██║╚██╔╝██║██║   ██║╚════╝██╔═══╝ ╚════╝██╔═══╝ ██║  ██║██╔══╝  
 ██║██║ ╚═╝ ██║╚██████╔╝      ███████╗      ██║     ██████╔╝██║     
 ╚═╝╚═╝     ╚═╝ ╚═════╝       ╚══════╝      ╚═╝     ╚═════╝ ╚═╝    
''']

print(random.choice(banners))

root = tk.Tk()

root.withdraw()

imgList = filedialog.askopenfilenames()

if imgList == None or imgList == "" or imgList == []:
    print(f"{Fore.RED}[+]{Fore.RESET} No files selected.\n\nExiting now...\n")
    time.sleep(2)
    exit()

imgList = list(imgList)
print("[+] This is the order your files will be converted to pdf in :")
    
for image in imgList:
    print(imgList.index(image) + 1, image)

if input("\n[+] Is the order correct? (Y/n): ") == "n":
    try:
        correct_order = input("\n[+]Enter correct order of images separated by commas. eg: 2,3,1,5,4: ").split(",")
    except:
        print(f"{Fore.RED}[+]{Fore.RESET} Please enter order correcctly")
        correct_order = input("\n[+] Enter correct order or images separated by commas. eg: 2,3,1,5,4: ").split(",")

    corrected_list = []
    try:
        for index in correct_order:
            corrected_list.append(imgList[int(index) - 1])
    except:
        print(f"{Fore.RED}[+]{Fore.RESET} Please enter order correcctly")
        correct_order = input("\n[+] Enter correct order or images separated by commas. eg: 2,3,1,5,4: ").split(",")

    print("[+] This is the order your files will be converted to pdf in :")
    
    for image in imgList:
        print(imgList.index(image) + 1, image)

try:
    pdfData = img2pdf.convert(imgList)
    fileName = input("\n[+] Enter pdf filename: ")

    with open(f"{fileName}.pdf", "wb") as pdffile:
        pdffile.write(pdfData)

    print(f"\n{Fore.GREEN}[+]{Fore.RESET} PDF Created!")
    print("\nExiting now...")
    time.sleep(2)

except Exception as e:
    print(f"\n{Fore.RED}[+]{Fore.RESET} Filetype not supported.")
    time.sleep(2)
    

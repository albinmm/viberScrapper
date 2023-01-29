import pyautogui
import csv
import os
import time
#import pyperclip

time.sleep(1) 


pyautogui.hotkey("alt", "tab")

def checkDialog():
    while True:
        image = "test.png"
        dialog_location = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.8)
with open('phone_numbers.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    with open('phone_numbers_with_copied_text.csv', 'w', newline='') as new_csvfile:
        writer = csv.writer(new_csvfile)
        writer.writerow(['phone_number', 'copied_text'])
        for row in reader:
            phone_number = row[0]
            for phone_number in row:
                #cordinates of the add contact button
                pyautogui.moveTo(x=1660, y=130)
                time.sleep(1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.typewrite(phone_number)
                #cordinates of the "Continue" button
                pyautogui.moveTo(x=918, y=409)
                pyautogui.click()
                #This variable contains the name of the image which is shown after you search for a number and it tells you to invite them to join viber
                image = "test.png"
                while True:
                    dialog_location = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.8)
                    if dialog_location:
                        #print("The dialog window is found on the screen.")
                        #cordinates of the "Cancel" button
                        pyautogui.moveTo(x=1122, y=620)
                        pyautogui.click()
                        #cordinates of the back button
                        pyautogui.moveTo(x=114, y=135)
                        pyautogui.click()

                        pyautogui.press('esc')
                        pyautogui.press('esc')
                        break
                    else:
                        #pyautogui.hotkey('ctrl', 'a')
                        pyperclip.copy(pyautogui.hotkey('ctrl', 'a'))
                        copied_text = pyperclip.paste()
                        writer.writerow([phone_number, copied_text])
                        if dialog_location:
                            copied_text = ""
                        pyautogui.press('esc')
                
            # Note: this script was designed to work with MEmu Emulator since the other emulators I tested
            # did't have the "Add contact" button on their contact Menu

            #Shenim: kjo script-e eshte e dizajnuar te punoj me MEmu Emulator perderisa emulatoret e tjere qe kam
            # testuar nuk kan pasur "Add contact" butonin ne menun e kontakteve

            #For the instructions how to use this script please follow the ReadMe.txt file

            #Per instrukcione se si te perdoret kjo script-e ju lutem ndiqni hapat ne ReadMe.txt


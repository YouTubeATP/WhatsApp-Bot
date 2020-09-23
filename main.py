import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
from http.client import CannotSendRequest, ResponseNotReady
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pyimgur
import os
from PIL import Image

print("Starting...")
options = []
driver = WhatsAPIDriver(client="chrome", username="Anson the pro!", chrome_options=options, autoconnect=False) ## Intialize webdriver ourself as API's is not working
driver.driver.get(driver._URL)
gotQR = False
try:
    driver.get_qr(filename="qr.png")
    gotQR = True
except NoSuchElementException: ## Try again after 3 seconds
    try:
        time.sleep(3)
        driver.get_qr(filename="qr.png")
        gotQR = True
    except NoSuchElementException:
        print("Failed to get QR code!") ## Give up, because it is likely that we have logged in
        gotQR = False
        pass
finally:
    if gotQR == True:
        CLIENT_ID = os.environ.get("CLIENT_ID")
        PATH = "./goodqr.png"
        img = Image.open("qr.png")
        background = Image.open("background.jpg")
        bg_w, bg_h = background.size
        img_w, img_h = img.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        background.paste(img, offset, img)
        background.save('goodqr.png',"PNG")
        imgur = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = imgur.upload_image(PATH, title="WhatsApp QR Code")
        print("QR code has been uploaded to:\n" + str(uploaded_image.link) + "\nPlease scan the QR code to login.")
    else:
        pass
try:
    driver.wait_for_login(timeout=5)
except TimeoutException:
    try:
        print("Awaiting login... YOU HAVE 90 SECONDS TO DO SO.")
        driver.wait_for_login(timeout=90)
    except TimeoutException:
        print("Ur too slow rip, try again")
        raise TimeoutException
print("Bot started!")

## Looping forever to check for new messages
while True:
    try:
        time.sleep(0.1)
        for contact in driver.get_unread():
            for message in contact.messages:
                if isinstance(message, Message):
                    if message.content.startswith("!salt"):
                        contact.chat.send_message("Ever had an annoying nerd flex their ass off in your group chat? No fear, just hit up Anson Salt Industries at 69-420-420 during work hours and a professional inquisitor shall be dispatched to fix your problem!")
                    elif message.content.startswith("!69-420-420"):
                        contact.chat.send_message("Hello, this is Anson Salt Industries. How may I assist you?")
                    elif message.content.startswith("!discord"):
                        contact.chat.send_message("Join the Discord Server here!\nhttps://discord.io/ansonthepro")
                    elif message.content.startswith("!channel"):
                        contact.chat.send_message("See my YouTube Channel here:\nhttps://youtube.com/user/anson0803aw")
                    elif "gay" in message.content:
                        contact.chat.send_message("No u")
    ## Ignore these errors as they are harmless!
    except CannotSendRequest:
        continue
    except ResponseNotReady:
        continue
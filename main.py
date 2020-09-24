import time
import decouple
from requests.api import head
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
from http.client import CannotSendRequest, ResponseNotReady
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import random
from random import choice
import traceback
import pyimgur
import os
from decouple import config
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
        CLIENT_ID = config("CLIENT_ID")
        print(CLIENT_ID)
        PATH = "./goodqr.png"
        img = Image.open("qr.png")
        background = Image.open("./assets/background.jpg")
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
                    elif message.content.startswith("!mask"):
                        contactdetails = config("DETAILS")
                        contact.chat.send_message(f"""嘉美健口罩 便宜多款式 保證高品質
本地海外 零售批發 自用送禮 樣樣行
BFE PFE VFE ASTM 品質保證
有意者請致電{contactdetails}""")
                    elif message.content.startswith("!ping"):
                        contact.chat.send_message("Pong!")
                    elif message.content.startswith("!pong"):
                        contact.chat.send_message("Ping!")
                    elif message.content.startswith("!random"):
                        randoms = message.content.split(":")
                        randoms.pop(0)
                        if len(randoms) > 1:
                            contact.chat.send_message(f"*_Randomizer results:_*\n{random.choice(randoms)}")
                        else:
                            contact.chat.send_message("You must provide at least 2 items for this command to work!")
                    elif message.content.startswith("!rannum"):
                        randoms = message.content.split(" ")
                        randoms.pop(0)
                        if len(randoms) != 2:
                            contact.chat.send_message("You must provide two numbers!")
                        else:
                            contact.chat.send_message(f"*_Random integer_*\n{str(random.randint(int(randoms[0])), int(randoms[1])))}")
                    elif message.content.startswith("!69-420-420"):
                        contact.chat.send_message("Hello, this is Anson Salt Industries. How may I assist you?")
                    elif message.content.startswith("!discord"):
                        contact.chat.send_message("Join the Discord Server here!\nhttps://discord.io/ansonthepro")
                    elif message.content.startswith("!channel"):
                        contact.chat.send_message("See my YouTube Channel here:\nhttps://youtube.com/user/anson0803aw")
                    elif message.content.startswith("!8ball"):
                        responses = [
                            "It is certain.",
                            "It is decidedly so.",
                            "Without a doubt.",
                            "Yes – definitely.",
                            "You may rely on it.",
                            "As I see it, yes.",
                            "Most likely.",
                            "Outlook good.",
                            "Yes.",
                            "Signs point to yes.",
                            "Reply hazy, try again.",
                            "Ask again later.",
                            "Better not tell you now.",
                            "Cannot predict now.",
                            "Concentrate and ask again.",
                            "Don't count on it.",
                            "My reply is no.",
                            "My sources say no.",
                            "Outlook not so good.",
                            "Very doubtful."
                        ]
                        contact.chat.send_message(f"*Question:* {message.content[7:]}\n\n*Answer:* {random.choice(responses)}")
                    elif message.content.startswith("!source"):
                        contact.chat.send_message("Check my source code here:\nhttps://github.com/YouTubeATP/WhatsApp-Bot")
                    elif message.content.startswith("!fortune"):
                        fortunes = [
                            "With integrity and consistency -- your credits are piling up.",
                            "Reach out your hand today to support others who need you.",
                            "It is not the outside riches bit the inside ones that produce happiness.",
                            "How dark is dark?, How wise is wise?",
                            "We can admire all we see, but we can only pick one.",
                            "The man who has no imagination has no wings.",
                            "To courageously shoulder the responsibility of one's mistake is character.",
                            "We can't help everyone. But everyone can help someone.",
                            "You discover treasures where others see nothing unusual.",
                            "Make all you can, save all you can, give all you can.",
                            "Understanding the nature of change, changes the nature.",
                            "You will be unusually successful in business.",
                            "Your spirit of adventure leads you down an exiting new path.",
                            "Genius is one percent inspiration and ninety-nine percent perspiration.",
                            "You are the master of every situation.",
                            "Be brave enough to live creatively.",
                            "Cookies go stake. Fortunes are forever.",
                            "Your ingenuity and imagination will get results.",
                            "Unnecessary possessions are unnecessary burdens.",
                            "Ability is not something to be shown off.",
                            "If you wish to see the best in others, show the best of yourself.",
                            "Your power is in your ability to decide.",
                            "Wherever you go, whenever you can, try to leave a gift.",
                            "Kind words can be shot and easy to speak, but their echoes are truly endless.",
                            "Your ingenuity and imagination will get results.",
                            "Age can never hope to with you while your heart is young.",
                            "Example is better than perception.",
                            "Idleness is the holiday of fools.",
                            "Don't be pushed by your problems. Be led by your dreams.",
                            "Many receive advice, only the wise profit from it.",
                            "You will have good luck and overcome many hardships.",
                            "A good way to keep healthy is to eat more Chinese food.",
                            "Today's profits are yesterday's good well ripened.",
                            "LSDBS - Let Something Good Be Said.",
                            "There is in the worst of fortunes the best change of a happy ending.",
                            "Service to many leads to greatness.",
                            "Desire, like the atom, is explosive with creative force.",
                            "I think and that is all that I am.",
                            "Judge each day not by the harvest you reap but by the seeds you plant.",
                            "Yesterday was a dare to struggle. Today is a dare to win.",
                            "Make everyday your best. You will improve yourself greatly.",
                            "You must be willing to act today in order to succeed.",
                            "Venture not all in one boat.",
                            "Suppressing a moment of anger may save a day of sorrow.",
                            "Never be less than your dreams.",
                            "The good times start when I count to 3: 1... 2... 3.",
                            "An inch of time is an inch of gold.",
                            "If you chase two rabbits both will escape.",
                            "You will soon be surrounded by good friends and laughter.",
                            "Haste does not bring success.",
                            "You will stumble into the path that will lead your life to happiness.",
                            "You will always be successful in you professional career.",
                            "Good news will come to you from far away.",
                            "Service is the rent you pay for having room on the Earth.",
                            "Be smart, but never show it.",
                            "The only certainty is that nothing is certain.",
                            "You or a close friend will be married soon.",
                            "We will not know the worth of water 'till the well is dry.",
                            "You are talented in many ways.",
                            "Do your best to make it happen",
                            "You will find great forces in unexpected places.",
                            "What you see in the mirror, and what you are can be two different images.",
                            "Excuses are easy to manufacture, and hard to sell.",
                            "Do onto others as you wish others do onto you.",
                            "Struggle as and hard as you can for whatever you believe in.",
                            "You have a pair of shining eyes.",
                            "You should be able to undertake and complete anything.",
                            "Your principles mean more to you than any money or success.",
                            "Forgiveness does not change the past, but it does enlarge the future.",
                            "Stand tall! Don't look down upon yourself.",
                            "Every truly great accomplishment is at first impossible.",
                            "Courage is not the absence of fear; it is the conquest of it.",
                            "Wise man seldom talks.",
                            "If you have a job without aggravations, you don't have a job.",
                            "You are broad minded and socially active.",
                            "Don't put off till tomorrow what can be enjoyed today.",
                            "A family reunion in the coming months will be a tremendous success!",
                            "Enthusiastic leadership gets you a promotion when you least expect it.",
                            "Calamity is the touchstone of a brave mind.",
                            "Everything you add to the truth subtracts from the truth.",
                            "You are going to take a vacation.",
                            "Commitment is the stuff character is made of; the power to change the face of things.",
                            "A friend asks only for your time not your money.",
                            "A friend asks only for your time not your money.",
                            "A handful of patience is worth more than a bushel of brains.",
                            "A handful of patience is worth more than a bushel of brains.",
                            "To be eighty years young is more cheerful and hopeful than forty years old.",
                            "To be eighty years young is more cheerful and hopeful than forty years old.",
                            "A person is not wise simply because one talks a lot.",
                            "It takes guts to get out of the ruts.",
                            "The greatest quality is seeking to serve others.",
                            "Most people, once they graduate from the school of Hard Knocks, automatically enroll.",
                            "Everyone needs to be loved, especially those do not deserve it.",
                            "Winning isn't everything but the will to win is.",
                            "You display the wonderful traits of charm and courtesy.",
                            "You will be awarded some great honor.",
                            "Don't build your happiness on other's sorrow.",
                            "The best thing about growing older is that it takes such a long time.",
                            "You have a deep interest in all that is artistic.",
                            "Kiss is not a kiss without the heart.",
                            "Don't be afraid of fear.",
                            "There's no point to being grown up if you can't be childish sometimes.",
                            "You will learn something new every day.",
                            "You can't go far in a rowboat without oars.",
                            "Failure is the virtual way to prepare you for great responsibilities.",
                            "Many receive advice only the wise profit by it.",
                            "A banker is someone who lends you an umbrella when the sun is shining.",
                            "Maturity: Do your duty without being supervised.",
                            "Your cheerful outlook is one of your assets.",
                            "You can't have everything... where would you put it all?",
                            "You have an unusually magnetic personality.",
                            "You have an unusually magnetic personality.",
                            "He who hurries cannot walk with dignity.",
                            "You never hesitate to tackle the most difficult problems.",
                            "Your emotional nature is strong and sensitive.",
                            "Serious trouble will bypass you.",
                            "If you're riding ahead of the heard, look back once in a while to make sure it's still there.",
                            "You have an iron will, which helps you succeed in everything.",
                            "Three can keep a secret if you get rid of two.",
                            "Everywhere you choose to go friendly faces will greet you.",
                            "Nothing gets in the way of your vision of yourself in the future.",
                            "To understand is hard. Once one understands, action is easy.",
                            "The philosophy of one century is the common sense of the next.",
                            "You will make many changes before settling satisfactorily.",
                            "When in anger, sing the alphabet.",
                            "Wealth is a means to an end... not the end itself.",
                            "It's high time for one of your most promising ideas.",
                            "Small opportunities are often the beginning of great enterprises.",
                            "People are drawn to you and look to you for advice.",
                            "Keep your feet on the ground even though friends flatter you.",
                            "Do a good deed anonymously. You will make a difference in your life.",
                            "Financial prosperity is coming your way!",
                            "A healthy body will benefit you forever.",
                            "Mental activity keeps you busy at this time.",
                            '''Say "I love you" and mean it. You can't do that enough.''',
                            "The world is always ready to receive talent with open arms.",
                            "Enjoy the small things you find on your path.",
                            "Good food brings good health and longevity.",
                            "The act of giving is more important than receiving.",
                            "Every burden is a blessing.",
                            "Prosperity is in your fortune.",
                            "Your next interview will result in a job.",
                            "Accept the challenges, so that you may feel the exhilaration of victory.",
                            "The future belongs to those who believe in the beauty of their dreams.",
                            "Peace begins with a smile.",
                            "Engage in group activities that further transformation.",
                            "Be satisfied with what you already own.",
                            "Your business will assume vast proportions.",
                            "You have a potential urge and the ability for accomplishment.",
                            "People find it difficult to resist your persuasive manner.",
                            "Action is worry's worst enemy.",
                            "Men do not fail... they give up trying.",
                            "Are your legs tired? You been running through someone's mind ALL day long.",
                            "You find beauty in ordinary things. Do not loose this ability.",
                            "Will you let compassion to manage your wishes.",
                            "A truly great person never puts away the simplicity of a child.",
                            "Home is where your heart is.",
                            "A huge fortune at home is not as good as money in use.",
                            "Humor is the affirmation of dignity.",
                            "Your heavy desire, only allow you to see what you are looking for.",
                            "TEAMS - Together Everyone Achieves More Success.",
                            "You have a heart of gold.",
                            "Life to you is a bold and dashing responsibility.",
                            "Want to learn how to love, start with the one you hate.",
                            "There is beauty in simplicity.",
                            "Learning is a treasure which accompanies us everywhere.",
                            "It is much easier to be critical than to be correct.",
                            "This person's love is just and true. You may rely on it.",
                            "You will be spending time outdoors, in the mountains, near water.",
                            "Friends long absent are coming back to you.",
                            "He joyfulness of a man prolongeth his days.",
                            "Regenerate your system through diet and exercise. Save the cookies!",
                            "Listen to the wisdom of the old.",
                            "Even the toughest of days have bright spots, just do your best.",
                            "Your talents will be recognized and suitably rewarded.",
                            "Fortitude is the guard and support of the other virtues.",
                            "When the moment comes, take the one from the right.",
                            "Old friends make best friends.",
                            "You have an ability to sense and know higher truth.",
                            "People learn little from success, but much from failure.",
                            "Keep in mind your most cherished dreams of the future.",
                            "You always do things the right way.",
                            "Act boldly and unseen forces will come to your aid.",
                            "Join a new club today, you'll be surprised.",
                            "Your many hidden talents will become obvious to those around you.",
                            "Some people never have anything except ideas, Go do it.",
                            "A real patriot is the fellow who gets a parking ticket and rejoices that the system works.",
                            "You are more likely to give than give in.",
                            "If you bite the hand that feeds you, it wont taste as good as the food you were fed.",
                            "The heart has its reasons, which the reasons dos not know.",
                            "Even the longest of days will come to an end.",
                            "You enjoy giving gifts of yourself to others, you will be rewarded!",
                            "There are no stupid questions, just stupid answer.",
                            "Success is an accumulation of successful days.",
                            "You have a friendly heart and are well admired.",
                            "Just because you put tap shoes on an elephant does not mean it can dance.",
                            "Start to look for you faults if you never made mistakes.",
                            "Good sense is the master of human life.",
                            "Your luck has been completely changed today.",
                            "Ask advice, but use your own common sense.",
                            "A judgment will rule in your favor.",
                            "Your winsome smile will be your sure protection.",
                            "Go confidently in the direction of your dreams.",
                            "The skills you have gathered will one day come in handy.",
                            "Look forward to great fortune and a new lease on life!",
                            "You will travel to many places.",
                            "You will enjoy a trip to Asia.",
                            "Better to do something imperfectly than to do nothing perfectly.",
                            "Pure logic is the ruin of the spirit.",
                            "You will have a long and wealthy life.",
                            "Your smile always brightens the cloudiest days.",
                            "A friend in the market is better than money in the purse.",
                            "A new venture will be a success.",
                            "It is by those who have suffered that the world is most advanced.",
                            "Everything must have a beginning.",
                            "The important thing is to express yourself.",
                            "The real meaning of enlightenment is to gaze with undimmed eyes on all undimmed.",
                            "New and rewarding opportunities will soon develop for you.",
                            "Seek to assert your devotion when a worthy situation arises.",
                            "The glass is not half-empty, it's just twice too big.",
                            "A feeling is an idea with roots.",
                            "Your present plans are going to succeed.",
                            "A sound mind and healthy body bring many happy events to your family.",
                            "Plan your work and work your plan.",
                            "Courage is rightly considered the foremost of the virtues, for upon it, all others depend.",
                            "Say hello to others. You will have a happier day.",
                            "Don't let your limitations overshadow your talents.",
                            "Love is the affinity which links and draws together the elements of the world.",
                            "You should be able to undertake and complete anything.",
                            "Character development is the true aim  of education.",
                            "Trust him, but sill keep your eyes open.",
                            "He who is shipwrecked the second time cannot lay the blame on Neptune.",
                            "To get respect from others, one must first give respect to others.",
                            "Walk the words you talk and talk the words you walk.",
                            "People forget how fast you did a job - but they remember how well you did it.",
                            "The time is right to make new friends.",
                            "Do what is right, not what you should.",
                            "Punctuality is the politeness of kings and the duty of gentle people everywhere.",
                            "If you wait too long for the perfect moment, the perfect moment will pass you by.",
                            "Your heart is pure, and your mind clear, and soul devout.",
                            "Walk with a good heart and you will run with success.",
                            "We should not let our fears hold us back from pursuing our hopes.",
                            "Do not mistake temptation for opportunity.",
                            "You will soon meet the person you admire.",
                            "A good time to start something new.",
                            "All generalities are false.",
                            "Come back later... I am sleeping. (yes, cookies need their sleep too)",
                            "If at first you do not succeed... try something harder.",
                            "Your good listening skills will open many doors.",
                            "Two people shorten a road.",
                            "Stop waiting! Buy that ticket take that special trip!",
                            "A problem clearly stated is a problem half solved.",
                            "Accept your independence and use it wisely.",
                            "May the warm winds of heaven blow softly upon your sprint."
                        ]
                        contact.chat.send_message("*_Fortune Cookie_*\n" + random.choice(fortunes))
                    elif "gay" in message.content:
                        contact.chat.send_message("No u")
                    elif "@85254177014" in message.content or message.content.startswith("!help"):
                        contact.chat.send_message("""*Anson's WhatsApp Bot - Help*
The prefix of this bot is ```!```. Custom prefixes are coming soon!

```!salt```
Gives salt.

```!69-420-420```
Calls 69-420-420.

```!discord```
Gives the link for my Discord Server.

```!channel```
Returns the link of my channel.

```!8ball```
The magic 8ball!

```!fortune```
Gives you a fortune cookie.

```!mask```
Get some masks for your pandemic needs!

```!random:item1:item2:item3```
Randomizes a list of items.

```!rannum [num1] [num2]```
Gives a random integer.

```!ping```
Returns pong.

```!source```
Shows the source code of this bot.

```!help```
This command.""")
    ## Ignore these errors as they are harmless!
    except CannotSendRequest:
        continue
    except ResponseNotReady:
        continue
    except AttributeError:
        continue
    except:
        x = traceback.format_exc()
        print(f"\nIgnoring exception:\n{x}")
        try:
            contact.chat.send_message(f"We're sorry, but an exception has occured.\nError details:\n```{x}```")
        except:
            x = traceback.format_exc()
            print(f"Exception occured when trying to return error report:\n```{x}```")
            pass
        continue
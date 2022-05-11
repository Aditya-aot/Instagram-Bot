from instabot import Bot
import os 
import glob

from PIL import Image,ImageDraw,ImageFont
import textwrap
import requests

import time


a=0

while True :

    a=a+1
    #################### api code ###############################
    #################### api code ###############################
    url = "https://facts-by-api-ninjas.p.rapidapi.com/v1/facts"

    headers = {
        "X-RapidAPI-Host": "facts-by-api-ninjas.p.rapidapi.com",
        "X-RapidAPI-Key": "fc10ca2471msh1436e5004570dd2p152fdfjsn953b9a54ea03"
    }

    response = requests.request("GET", url, headers=headers)

    fact=response.text

    raw_data=(fact[11:-3])
    #################### api code ###############################
    #################### api code ###############################


    #################### image code ###############################
    #################### image code ###############################
    image = Image.open('fact.jpg')

    font_type = ImageFont.truetype("arial.ttf", 30)
    draw = ImageDraw.Draw(image)


    # raw_data = "The smallest bone in the human body is the stirrup bone, which is located in the ear"

    wrapper = textwrap.TextWrapper(width=15)
    word_list = wrapper.wrap(text = raw_data)

    text_data="\n".join(word_list)

    draw.text(xy=(10,50),text=text_data ,fill=(0,0,0),font=font_type)


    image.show()
    image.save('fact_'+str(a)+'.jpg')
    ################### image code ###############################
    ################### image code ###############################



    cookie_del = glob.glob("config/*cookie.json")
    os.remove(cookie_del[0])

    bot = Bot()
    bot.login(username='',password='')

    bot.upload_photo('fact_'+str(a)+'.jpg', caption=raw_data+"  #explore #instafact #factz #corona #generalknowledge #fact #factsdaily #didyouknow #truefacts #knowledge #knowledgeable #gyan #theuntoldfact #doyouknow #dailyfact #mindblowing #knowledgebygooogle #factbyscience #interestingfacts #knowledgeispower #know #mindblown")

    os.remove("fact_"+str(a)+".jpg.REMOVE_ME") 

    for i in range(21600,0,-1):
        print(f"{i}", end="\r", flush=True)
        time.sleep(1)
    # time.sleep(21600)
 


from PIL import Image,ImageDraw,ImageFont
import textwrap
import requests



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
#################### image code ###############################
#################### image code ###############################
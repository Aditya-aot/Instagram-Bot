from PIL import Image,ImageDraw,ImageFont
import textwrap


image = Image.open('fact.jpg')


font_type = ImageFont.truetype("arial.ttf", 20)
draw = ImageDraw.Draw(image)


raw_data = "The smallest bone in the human body is the stirrup bone, which is located in the ear"

wrapper = textwrap.TextWrapper(width=20)
word_list = wrapper.wrap(text = raw_data)

text_data="\n".join(word_list)

draw.text(xy=(10,50),text=text_data ,fill=(0,0,0),font=font_type)


image.show()


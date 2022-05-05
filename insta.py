from instabot import Bot
import os 
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

bot = Bot()
bot.login(username='the_tips_the',password='uk123uk')

bot.upload_photo('zoro.jpg', caption='one piece wano arc -The Wano Country Arc (ワノ国編, Wano Kuni Hen?) is the thirty-first story arc in the series and the fourth in the Four Emperors Saga of One Piece-')


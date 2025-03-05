from instabot import Bot

bot = Bot()
bot.login(username ="drabble_dee", password ="Hudsonnbenhuraa2003.")
bot.follow("Uncommon.org")
bot.upload_photo("my_qr.png")

followers = bot.get_user_followers("drabble_dee")
for followers in followers:
    print(bot.get_user_info("followers"))
    

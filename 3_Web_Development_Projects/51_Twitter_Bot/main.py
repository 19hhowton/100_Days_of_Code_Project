from internet_speed_twitter_bot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider() 

# if internet speed is not as promised, then bot.tweet_at_provider() 

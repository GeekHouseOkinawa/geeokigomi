#!/usr/bin/env python
# coding: utf-8
import tweepy
import datetime

consumer_key = "YOUR CONSUMER KEY"
consumer_secret = "YOUR CONSUMER SECRET KEY"
access_token = "YOUR ACCESS TOKEN"
access_secret = "YOUR ACCESS SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth_handler=auth)

dt = datetime.date.today()
string = u"@kyo2_ @cota2n @gliese035 @hanachin_ @kimihito_ @tomo_hiko "

if dt.weekday() == 0:
  string += u"今日は燃えるゴミの日ですよ！"
elif dt.weekday() == 1:
  string += u"今日は缶・ビンの燃えないゴミの日！"
elif dt.weekday() == 2:
  string += u"今日はペットボトルの日！"
elif dt.weekday() == 3:
  string += u"今日は燃えるゴミの日ですよ！"
elif dt.weekday() == 4:
  string += u"今日は何の日かわかんない！"
elif dt.weekday() == 5: 
  string += u"ゴミはないけど、掃除しようぜ！"
else:
  string += u"今日はゆっくり休みましょ"


api.update_status(string)
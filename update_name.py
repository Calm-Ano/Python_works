# coding:utf-8

import tweepy
import urllib
import sys
import datetime
import dappun

t_ck = ''
t_cs = ''
t_tk = ''
t_ts = ''

def auth(ck, cs, tk, ts):
    auth = tweepy.OAuthHandler(ck, cs)
    try:
        auth.set_access_token(tk, ts)
        api = tweepy.API(auth)
    except:
        print('error in auth()')
    return api

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        rt_n = status.text.find('RT')
        if rt_n == 0:
            pass
        else:
            print(status.text)
            if 'update_name' in status.text:
                if status.text.find('update_name') > 0:
                    index = status.text.find('update_name')
                    new_name = status.text[index+11:]
                    if not("ゲイ" in status.text) and not("ホモ" in status.text):
                        try:
                            me.update_profile(new_name)
                            flag = True
                        except tweepy.error.TweepError as TE:
                            me.update_status("@{0} : {1}".format(status.user.screen_name, TE))
                        if flag:
                            message = '@'+status.author.screen_name+'名前を変更しました'
                            me.update_status(status=message, in_reply_to_status_id=status.id)
                    else:
                        me.update_status(status='@{} 不適切な語句です。しね。'.format(status.user.screen_name), in_reply_to_status_id=status.id)
            elif status.text.find("脱糞") > 0:
                index = status.text.find("脱糞")
                target_id = status.text[index+4:]
                try:
                    me.update_status(dappun.dappun(target_id))
                except tweepy.error.TweepError as TE:
                    me.update_status(TE)

            elif 'update_icon' in status.text:
                 if 'media' in status.entities :
                    medias = status.entities['media']
                    m =  medias[0]
                    media_url = m['media_url']
                    try:
                        urllib.request.urlretrieve(media_url, 'icon.jpg')
                    except IOError:
                        print("保存に失敗しました")
                    now = datetime.datetime.now()
                    time = now.strftime("%H:%M:%S")
                    message = '@'+status.author.screen_name+' アイコンを変更しました('+time+')'
                    try:
                        me.update_profile_image('icon.jpg')
                        me.update_status(status=message, in_reply_to_status_id=status.id)
                    except tweepy.error.TweepError as e:
                        print("error response code: " + str(e.response.status))
                        print("error message: " + str(e.response.reason))

if __name__ == "__main__":
    me = auth(t_ck, t_cs, t_tk, t_ts)
    print('Error Occured')
    mSL = MyStreamListener()
    mS = tweepy.Stream(auth = me.auth, listener=mSL)
    print('[*]Listenning')
    mS.filter(track=['account_name'])

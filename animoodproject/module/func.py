from django.conf import settings

from linebot import LineBotApi
from linebot.models import TemplateSendMessage, TextSendMessage, ButtonsTemplate, MessageTemplateAction, AudioSendMessage, PostbackTemplateAction

import random

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendTest(event):
    try:
        message = TemplateSendMessage(
            alt_text='心理測驗',
            template=ButtonsTemplate(
                thumbnail_image_url="https://i.imgur.com/6a09g4G.png",
                text='請點擊按鈕開始玩心理測驗吧！',
                actions=[
                    MessageTemplateAction(
                        label='Go！',
                        text='Go！',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendQ1(event):
    try:
        message = TemplateSendMessage(
            alt_text='第一題',
            template=ButtonsTemplate(
                title="第一題",
                text='如果要完成一件事，你比較偏向...',
                actions=[
                    MessageTemplateAction(
                        label='與一群人完成',
                        text='與一群人完成',
                        ),
                    MessageTemplateAction(
                        label='偏好獨力完成',
                        text='偏好獨力完成',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        
def sendQ2(event):
    try:
        message = TemplateSendMessage(
            alt_text='第二題',
            template=ButtonsTemplate(
                title="第二題",
                text='哪一種比較偏向你的交友狀況呢？',
                actions=[
                    MessageTemplateAction(
                        label='有很多不同領域的朋友！',
                        text='有很多不同領域的朋友！',
                        ),
                    MessageTemplateAction(
                        label='只有幾位深交的好友',
                        text='只有幾位深交的好友',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendQ3(event):
    try:
        message = TemplateSendMessage(
            alt_text='第三題',
            template=ButtonsTemplate(
                title="第三題",
                text='如果要完成一件事，你比較偏向...',
                actions=[
                    MessageTemplateAction(
                        label='在思考前就先衝了！',
                        text='在思考前就先衝了！',
                        ),
                    MessageTemplateAction(
                        label='要好好思考才會去行動',
                        text='要好好思考才會去行動',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendQ4(event):
    try:
        message = TemplateSendMessage(
            alt_text='第四題',
            template=ButtonsTemplate(
                title="第四題",
                text='你比較喜歡透過哪種方式來記住事物？',
                actions=[
                    MessageTemplateAction(
                        label='透過畫面、觸感等來記住',
                        text='透過畫面、觸感等來記住',
                        ),
                    MessageTemplateAction(
                        label='透過文字理解事物並記住它',
                        text='透過文字理解事物並記住它',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendQ5(event):
    try:
        message = TemplateSendMessage(
            alt_text='第五題',
            template=ButtonsTemplate(
                title="第五題",
                text='你在做課堂報告時，通常會...',
                actions=[
                    MessageTemplateAction(
                        label='仔細分析資料後在著手開始',
                        text='仔細分析資料後在著手開始',
                        ),
                    MessageTemplateAction(
                        label='有什麼靈感就來做',
                        text='有什麼靈感就來做',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendQ6(event):
    try:
        message = TemplateSendMessage(
            alt_text='第六題',
            template=ButtonsTemplate(
                title="第六題",
                text='你比較嚮往哪種工作時間？',
                actions=[
                    MessageTemplateAction(
                        label='朝九晚五的固定工時',
                        text='朝九晚五的固定工時',
                        ),
                    MessageTemplateAction(
                        label='彈性不固定的工作時間',
                        text='彈性不固定的工作時間',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendQ7(event):
    try:
        message = TemplateSendMessage(
            alt_text='第七題',
            template=ButtonsTemplate(
                title="第七題",
                text='你的朋友與別人在爭執，但過錯方是朋友，你會？',
                actions=[
                    MessageTemplateAction(
                        label='幫朋友說話',
                        text='幫朋友說話',
                        ),
                    MessageTemplateAction(
                        label='釐清來龍去脈，就事論事',
                        text='釐清來龍去脈，就事論事',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendQ8(event):
    try:
        message = TemplateSendMessage(
            alt_text='第八題',
            template=ButtonsTemplate(
                title="第八題",
                text='當你分享一部電影、小說或真實經歷，你比較偏向？',
                actions=[
                    MessageTemplateAction(
                        label='完整敘述它的來龍去脈',
                        text='完整敘述它的來龍去脈',
                        ),
                    MessageTemplateAction(
                        label='先說出讓你最感動的內容',
                        text='先說出讓你最感動的內容',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendQ9(event):
    try:
        message = TemplateSendMessage(
            alt_text='第九題',
            template=ButtonsTemplate(
                title="第九題",
                text='如果可以選擇一名偉大人物聊天？',
                actions=[
                    MessageTemplateAction(
                        label='愛因斯坦',
                        text='愛因斯坦',
                        ),
                    MessageTemplateAction(
                        label='佛洛依德',
                        text='佛洛依德',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendQ10(event):
    try:
        message = TemplateSendMessage(
            alt_text='第十題',
            template=ButtonsTemplate(
                title="第十題",
                text='我更關注跟相信甚麼？',
                actions=[
                    MessageTemplateAction(
                        label='真實和真真切切的資訊',
                        text='真實和真真切切的資訊',
                        ),
                    MessageTemplateAction(
                        label='直覺、靈感、想像和洞見',
                        text='直覺、靈感、想像和洞見',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendQ11(event):
    try:
        message = TemplateSendMessage(
            alt_text='第十一題',
            template=ButtonsTemplate(
                title="第十一題",
                text='怎樣的描述比較適合你呢？',
                actions=[
                    MessageTemplateAction(
                        label='我喜歡活在想像中',
                        text='我喜歡活在想像中',
                        ),
                    MessageTemplateAction(
                        label='我是個腳踏實地的人',
                        text='我是個腳踏實地的人',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendQ12(event):
    try:
        message = TemplateSendMessage(
            alt_text='第十二題',
            template=ButtonsTemplate(
                title="第十二題",
                text='如果送你一台單眼相機，你會？',
                actions=[
                    MessageTemplateAction(
                        label='先閱讀操作手冊',
                        text='先閱讀操作手冊',
                        ),
                    MessageTemplateAction(
                        label='直接嘗試拍一張照',
                        text='直接嘗試拍一張照',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendMusic(event):
    try:
        message = TemplateSendMessage(
            alt_text='心情歌單',
            template=ButtonsTemplate(
                title='嗨！想聽點音樂嗎',
                text='在聽歌之前，\n 想先問問你今天的心情如何？',
                actions=[
                    MessageTemplateAction(
                        label='今天很Happy',
                        text='今天很Happy',
                        ),
                    MessageTemplateAction(
                        label='今天蠻Chill',
                        text='今天蠻Chill',
                        ),
                    MessageTemplateAction(
                        label='今天有點Sad',
                        text='今天有點Sad',
                        ),
                    MessageTemplateAction(
                        label='今天感覺Mad',
                        text='今天感覺Mad',
                        ),
                    ]
                )
            )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendBack_happy(event):
    try:
        num = random.randrange(3)
        if num == 0:
            str = "https://youtu.be/ZbZSe6N_BXs"
        elif num == 1:
            str = "https://youtu.be/pRbxlpvXw2s"
        elif num == 2:
            str = "https://youtu.be/uSD4vsh1zDA"
        message = [
            AudioSendMessage(
                original_content_url='https://github.com/EmilyJie/Animood-LineBot/blob/be7b18f8d65278e3b20200da8560838eafbc2dfd/animoodproject/music/Good%20Day%20(Wake%20Up)%20-%20NEFFEX.mp3',
                duration=172000
            ),
            TextSendMessage(
                text = "或是也可以聽聽"
            ),
            TextSendMessage(
                text = str
            ),
            TextSendMessage(
                text = "一起開心的跳舞吧！"
            ),
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendBack_chill(event):
    try:
        message = [
            AudioSendMessage(
                original_content_url='https://github.com/EmilyJie/Animood-LineBot/blob/6c2e7fd84c2821ac573099a81dd84669bb51f7dd/animoodproject/music/Better%20Days%20-%20NEFFEX.mp3',
                duration=127000
            ),
            TextSendMessage(
                text = "或是也可以聽聽"
            ),
            TextSendMessage(
                text = "https://youtu.be/TbUFdS_tbZc"
            ),
            TextSendMessage(
                text = "好好享受這個Chill Moment"
            ),
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))

def sendBack_sad(event):
    try:
        message = [
            AudioSendMessage(
                original_content_url='https://github.com/EmilyJie/Animood-LineBot/blob/a605809214e72c03f5d6fe48d766b086d87aef62/animoodproject/music/Take%20Me%20Back%20-%20NEFFEX.mp3',
                duration=193000
            ),
            TextSendMessage(
                text = "或是也可以聽聽"
            ),
            TextSendMessage(
                text = "https://youtu.be/FskL-2jrgF0"
            ),
            TextSendMessage(
                text = "不管任何事，哭完就沒事"
            ),
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        
def sendBack_mad(event):
    try:
        message = [
            AudioSendMessage(
                original_content_url="https://github.com/EmilyJie/Animood-LineBot/blob/a605809214e72c03f5d6fe48d766b086d87aef62/animoodproject/music/It's%20Only%20Worth%20It%20If%20You%20Work%20For%20It%20(Clean)%20-%20NEFFEX.mp3",
                duration=183000
            ),
            TextSendMessage(
                text = "或是也可以聽聽"
            ),
            TextSendMessage(
                text = "https://youtu.be/NvPZ-wvUDdM"
            ),
            TextSendMessage(
                text = "跟著音樂嘶吼，釋放你的怒氣！"
            ),
        ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
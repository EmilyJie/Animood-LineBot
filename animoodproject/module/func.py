from django.conf import settings

from linebot import LineBotApi
from linebot.models import TemplateSendMessage, TextSendMessage, ButtonsTemplate, MessageTemplateAction, AudioSendMessage, PostbackTemplateAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

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
        message = [
            AudioSendMessage(
                original_content_url='https://drive.google.com/file/d/1aMPdpQBxiYeV-oHhHs4zN61x3fgw4rgv/view?usp=sharing',
                duration=172000
            ),
            TextSendMessage(
                text = "或是也可以聽聽"
            ),
            TextSendMessage(
                text = "https://youtu.be/pRbxlpvXw2s"
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
                original_content_url='https://youtu.be/tQ0yjYUFKAE',
                duration=197000
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
                original_content_url='https://youtu.be/tQ0yjYUFKAE',
                duration=197000
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
                original_content_url='https://youtu.be/tQ0yjYUFKAE',
                duration=197000
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
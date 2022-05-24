from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, PostbackEvent
from module import func
from urllib.parse import parse_qsl

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '@心理測驗':
                        func.sendTest(event)
    
                    elif mtext == '@心情歌單':
                        func.sendMusic(event)
                        
                    elif mtext == '今天很Happy':
                        func.sendBack_happy(event)
                    
                    elif mtext == '今天蠻Chill':
                        func.sendBack_chill(event)
                        
                    elif mtext == '今天有點Sad':
                        func.sendBack_sad(event)
                        
                    elif mtext == '今天感覺Mad':
                        func.sendBack_mad(event)
                        
                # if isinstance(event, PostbackEvent):
                #     backdata = dict(parse_qsl(event.postback.data))
                #     if backdata.get('action') == 'happy':
                #         func.sendBack_happy(event)
                #     elif backdata.get('action') == 'chill':
                #         func.sendBack_chill(event, backdata)
                #     elif backdata.get('action') == 'sad':
                #         func.sendBack_sad(event, backdata)
                #     elif backdata.get('action') == 'mad':
                #         func.sendBack_mad(event, backdata)    
        return HttpResponse()  
    
    else:
        return HttpResponseBadRequest()
 
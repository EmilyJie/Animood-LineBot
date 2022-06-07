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
            e = 0
            i = 0
            s = 0
            n = 0
            t = 0
            f = 0
            j = 0
            p = 0
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '@心理測驗':
                        func.sendTest(event)
                    
                    elif mtext == 'Go！':
                        func.sendQ1(event)
                    
                    elif (mtext == '與一群人完成') | (mtext =='偏好獨力完成'):
                        func.sendQ2(event)
                        if mtext == '與一群人完成':
                            e += 1
                        elif mtext =='偏好獨力完成':
                            i += 1
                    
                    elif (mtext == '有很多不同領域的朋友！') | (mtext =='只有幾位深交的好友'):
                        func.sendQ3(event)
                        if mtext == '有很多不同領域的朋友！':
                            e += 1
                        elif mtext =='只有幾位深交的好友':
                            i += 1
                        
                    elif (mtext == '在思考前就先衝了！') | (mtext =='要好好思考才會去行動'):
                        func.sendQ4(event)
                        if mtext == '在思考前就先衝了！':
                            e += 1
                        elif mtext =='要好好思考才會去行動':
                            i += 1
                    
                    elif (mtext == '透過畫面、觸感等來記住') | (mtext =='透過文字理解事物並記住它'):
                        func.sendQ5(event)
                        if mtext == '透過畫面、觸感等來記住':
                            n += 1
                        elif mtext =='透過文字理解事物並記住它':
                            s += 1
                        
                    elif (mtext == '仔細分析資料後在著手開始') | (mtext =='有什麼靈感就來做'):
                        func.sendQ6(event)
                        if mtext == '仔細分析資料後在著手開始':
                            s += 1
                        elif mtext =='有什麼靈感就來做':
                            n += 1
                        
                    elif (mtext == '朝九晚五的固定工時') | (mtext =='彈性不固定的工作時間'):
                        func.sendQ7(event)
                        if mtext == '朝九晚五的固定工時':
                            s += 1
                        elif mtext =='彈性不固定的工作時間':
                            n += 1
                        
                    elif (mtext == '幫朋友說話') | (mtext =='釐清來龍去脈，就事論事'):
                        func.sendQ8(event)
                        if mtext == '幫朋友說話':
                            f += 1
                        elif mtext =='釐清來龍去脈，就事論事':
                            t += 1
                        
                    elif (mtext == '完整敘述它的來龍去脈') | (mtext =='先說出讓你最感動的內容'):
                        func.sendQ9(event)
                        if mtext == '完整敘述它的來龍去脈':
                            t += 1
                        elif mtext =='先說出讓你最感動的內容':
                            f += 1
                        
                    elif (mtext == '愛因斯坦') | (mtext =='佛洛依德'):
                        func.sendQ10(event)
                        if mtext == '愛因斯坦':
                            t += 1
                        elif mtext =='佛洛依德':
                            f += 1
                        
                    elif (mtext == '真實和真真切切的資訊') | (mtext =='直覺、靈感、想像和洞見'):
                        func.sendQ11(event)
                        if mtext == '真實和真真切切的資訊':
                            j += 1
                        elif mtext =='直覺、靈感、想像和洞見':
                            p += 1
                        
                    elif (mtext == '我喜歡活在想像中') | (mtext =='我是個腳踏實地的人'):
                        func.sendQ12(event)
                        if mtext == '我喜歡活在想像中':
                            p += 1
                        elif mtext =='我是個腳踏實地的人':
                            j += 1
                        
                    elif (mtext == '先閱讀操作手冊') | (mtext =='直接嘗試拍一張照片'):
                        if mtext == '先閱讀操作手冊':
                            j += 1
                        elif mtext =='直接嘗試拍一張照片':
                            p += 1
                            
                        if e > i:
                            if s > n:
                                if j > p:
                                    if t > f:
                                        func.resultESJT(event)
                                    elif f > t:
                                        func.resultESJF(event)
                                elif p > j:
                                    if t > f:
                                        func.resultESPT(event)
                                    elif f > t:
                                        func.resultESPF(event)
                            elif n > s:
                                if j > p:
                                    if t > f:
                                        func.resultENJT(event)
                                    elif f > t:
                                        func.resultENJF(event)
                                elif p > j:
                                    if t > f:
                                        func.resultENPT(event)
                                    elif f > t:
                                        func.resultENPF(event)
                        elif i < e:
                            if s > n:
                                if j > p:
                                    if t > f:
                                        func.resultISJT(event)
                                    elif f > t:
                                        func.resultISJF(event)
                                elif p > j:
                                    if t > f:
                                        func.resultISPT(event)
                                    elif f > t:
                                        func.resultISPF(event)
                            elif n > s:
                                if j > p:
                                    if t > f:
                                        func.resultINJT(event)
                                    elif f > t:
                                        func.resultINJF(event)
                                elif p > j:
                                    if t > f:
                                        func.resultINPT(event)
                                    elif f > t:
                                        func.resultINPF(event)
                        
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
 
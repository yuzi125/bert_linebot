from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


from django.shortcuts import render
from Q_A.models import QA
from Q_A.bert  import *


# Create your views here.
def listall(request):  
	QAs= QA.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
	return render(request, "listall.html", locals())


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
            msg = event.message.text
            if '白上吹雪' in msg:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='他不是狐狸是貓'))
            elif predict_message(msg) is None:
                  line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你輸入的問題目前沒有解答'))
            else:
                message = TextSendMessage(text = predict_message(msg))
                line_bot_api.reply_message(event.reply_token, message)
            # else:
            #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

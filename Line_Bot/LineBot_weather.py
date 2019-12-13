# -*- coding: UTF-8 -*-

#Python module requirement: line-bot-sdk, flask
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError 
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import threading
import time
                
# LineBot

line_bot_api = LineBotApi('u9XQ2KL9EBO2OLK/M5gSA99diX39xfUruuSvXM+FcClBNKxFZv9RaIG4GJT974IaVm1N9rDWpGLrRpd5mdiCVuRejzUsH3DwQaaw5avl3MZ7ukbvdIYgtaA7+NQlP8naiBfSsoXoHp7P02xGHEHFewdB04t89/1O/w1cDnyilFU=') #LineBot's Channel access token
handler = WebhookHandler('0674da225d51246d3a057838b59813d3')        #LineBot's Channel secret
user_id_set=set()                                         #LineBot's Friend's user id 
app = Flask(__name__)

def loadUserId():
    try:
        idFile = open('idfile', 'r')
        idList = idFile.readlines()
        idFile.close()
        idList = idList[0].split(';')
        idList.pop()
        return idList
    except Exception as e:
        print(e)
        return None

def saveUserId(userId):
        idFile = open('idfile', 'a')
        idFile.write(userId+';')
        idFile.close()
        
        
def Push_String(arg) : 
    while True :
    #==================================
        MSG_O = DAN.pull('MSG-O')
        if MSG_O != None :
            print("MSG-O :",MSG_O)
            for userId in user_id_set:
                line_bot_api.push_message(userId, TextSendMessage(text=str(MSG_O)))  # Push API example
        time.sleep(15)
    
    


@app.route("/", methods=['GET'])
def hello():
    return "HTTPS Test OK."

@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']    # get X-Line-Signature header value
    body = request.get_data(as_text=True)              # get request body as text
    print("Request body: " + body, "Signature: " + signature)
    try:
        handler.handle(body, signature)                # handle webhook body
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    Msg = event.message.text
    if Msg == 'Hello, world': return
    print('Get Msg :',Msg)
    DAN.push('Msg-I',Msg)

    userId = event.source.user_id
    if not userId in user_id_set:
        user_id_set.add(userId)
        saveUserId(userId)
        

   
if __name__ == "__main__":
    #iottalk
    import DAN
    ServerURL = 'https://6.iottalk.tw' #with SSL connection
    Reg_addr =  'aaarrrooonnn'#if None, Reg_addr = MAC address
    
    DAN.profile['dm_name']='MSG'
    DAN.profile['df_list']=['Msg-I','MSG-O']
    DAN.profile['d_name']= 'MSG-I/O'
    DAN.device_registration_with_retry(ServerURL, Reg_addr)
    
    #LineBot
    idList = loadUserId()
    if idList: user_id_set = set(idList)
    try:
        for userId in user_id_set:
            line_bot_api.push_message(userId, TextSendMessage(text='LineBot is ready for you.'))  # Push API example
    except Exception as e:
        print(e)
    
    # open multi thread
    t = threading.Thread(target=Push_String,args=(user_id_set,))
    t.daemon = True # this ensures thread ends when main process ends
    t.start()
                
    app.run('127.0.0.1', port=32768, threaded=True, use_reloader=False)

# 物聯網(12/11)LineBot
###### tags: `IoT`
    
### (一)課程環境設定
    https://hackmd.io/
1. 課程主題：LineBot-basic
    - 傳送訊息給手機 ex: 下雨警報 ... 
    - 下載網址 :https://github.com/IoTtalk/LineBot-basic
     
    ```
    $ cd Desktop/IoT
    $ git clone https://github.com/IoTtalk/LineBot-basic
    ```
    - 教學檔案：[CreateYourLineBot.pdf](https://github.com/IoTtalk/LineBot-basic/blob/master/CreateYourLineBot.pdf)
    <br />
    
    
2. 申請LineBot
     - line Developer <br />
    ![](https://i.imgur.com/fH1je1d.png)
        - log in 
        - 使用line帳號登入
        - Create Account <br />
        ![](https://i.imgur.com/LFp2sAS.png)
        - Create New Provider <br />
        ![](https://i.imgur.com/D2Cv535.png)
        - Create Messaging API channel<br />
        ![](https://i.imgur.com/cMG7Xdk.png)
        ![](https://i.imgur.com/laA4S1G.png)
        - passwd <br />
        ![](https://i.imgur.com/FyapxzZ.png)
        ![](https://i.imgur.com/1jycE2J.png)
        - Auto Reply Disable<br />
        ![](https://i.imgur.com/BjcwX41.png)
        ![](https://i.imgur.com/861Wp89.png)
        - Scan QR code  (手機line加入好友)<br />
        ![](https://i.imgur.com/Ap0E26C.png)
        <br />
        
3. ngrok 
    - Download ngrok <br />
    ![](https://i.imgur.com/30rVD0h.png)
    ![](https://i.imgur.com/pY4jSPs.png)
    
    - 執行ngrok
    `cd Desktop/IoT`
    `$ ./ngrok http 32768`
    複製forwarding url : https://63914537.ngrok.io
    ![](https://i.imgur.com/HhCzQ1Z.png)
    <br />
    
4. IoT talk linebot 
    - 修改 LineBot_basic.py
        ```
        $ pip install line-bot-sdk
        ```
        ![](https://i.imgur.com/4TbbcB0.png)
        ![](https://i.imgur.com/Rsaw3rS.png)
    - 執行 LineBot_basic.py (有error是正常)<br />
        ![](https://i.imgur.com/u082hRT.png)
    
    <br />
    
5. Webhook
    ![](https://i.imgur.com/GjfNahl.png)
    ![](https://i.imgur.com/Nl2jGwD.png)
    ![](https://i.imgur.com/v0Yh1wH.png)
    <br />
    ![](https://i.imgur.com/RGU7kDw.png)
    - 測試：<br />
    ![](https://i.imgur.com/8W1lv52.png)



    
### (二)課程實作
1. 作業目標：
	- 做一個LineBot連接IoTTalk
	- 爬蟲的weather傳輸資料
	- 藉由LineBot提醒溫度>23度
2. 作業實作：
	* 前置作業
		- 複製一個 LineBot_basic.py :arrow_right: LineBot_weather.py 
		- 複製 csmapi.py / DAN.py 到 LineBot_basic 資料夾
	* Tainan.py Code
	    :arrow_right:直接執行，不做任何修改
	* LineBot_weather.py Code
        :arrow_right: 執行LineBot_weather.py
    * Line_Out.py
        :arrow_right: 執行 Line_Out.py
	* IoTTalk <br />
	![](https://i.imgur.com/X2kHLAJ.png)
    
		
		
	  



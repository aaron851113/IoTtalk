#  物聯網(09/18) Flip Bulb
###### tags: `IoT`

1. Introduction to IoTtalk
2. Lab01 : 手機遙控燈的開關
	* 選擇 「[IoTtalk Homepage](http://6.iottalk.tw)」6.iottalk.tw (6為port)
	* Add project -> 設定名稱與密碼
    ![](https://i.imgur.com/k0SQNGX.png)


	* Mode選擇Smartphone，選擇Acc(加速度)
	-> 使用手機上網到6.iottalk.tw，連接到對應的port(11)
    ![](https://i.imgur.com/0Wan4XJ.png)


	* Mode選擇Bulb(燈泡)  選擇Luminance(亮度)
	-> 電腦多開一個網頁到6.iottalk.tw
	-> 選擇Bulb並將控制中心連結到該port(04)
    ![](https://i.imgur.com/jffGMg8.png)


	* 以下為成功連結的畫面
    ![](https://i.imgur.com/ihe6yiF.png)


	* 設定參數 -> 將x3改為sample -> 因為翻轉軸為x3
    ![](https://i.imgur.com/A5Scnnk.png)


	* 點擊Luminance(亮度)觀看預設參數  -> 亮度為0~99
    ![](https://i.imgur.com/8FOJiOi.png)

    
	* 點擊回到join，Function改為add new function
    ![](https://i.imgur.com/RWV2Dlo.png)

	*  選擇 flip 將下方程式碼改為 return 99 
	( args[2]=x3 ). ( x3 = 9.8 -> 正面) ( x3 = -9.8 -> 反面)
	按下Save -> 回到主畫面點擊 Save -> 點擊 Simulation
    ![](https://i.imgur.com/4S36pUT.png)


	* Try it !


	

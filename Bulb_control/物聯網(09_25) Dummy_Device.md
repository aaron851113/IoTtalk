# 物聯網(09/25) Dummy_Device 
###### tags: `IoT`

1. Introduction IoT pdf
Start from p.10~
![](https://i.imgur.com/y09cxX1.png)


2. IDF/ODF: 進入Homepage -> 選擇「 Device Feature Management 」
![](https://i.imgur.com/4qMHFZX.png)


	* IDF : Min/Max不設定也沒關係
	* ODF : Min/Max -> 若輸入的不是0/10，則會強制IDF送進來的值轉為0~10 (ex:若為燈泡，則可以改為0/99)
	若不清楚他的功能 -> 就盡量保持0/0
![](https://i.imgur.com/YHffOgg.png)

   

 3. 實作Time : 
	*  自訂IDF與ODF並儲存
    ![](https://i.imgur.com/kGyBAUK.png)![](https://i.imgur.com/HgF1KgJ.png)

    
	* 按左上角 -> 改為 Device Model -> add New DM
		1. 選擇 IDF -> Category = Sight -> 選自己剛剛建IDF
		![](https://i.imgur.com/SJScc8z.png)

        
		2. 選擇 ODF -> Category = Sight -> 選自己剛剛建ODF
		![](https://i.imgur.com/HuOzGf8.png)


4. Github -> Iottalk ->  [Dummy_Device_IoTtalk_v1_py](https://github.com/IoTtalk/Dummy_Device_IoTtalk_v1_py)  -> Download fold
![](https://i.imgur.com/QhH4OeO.png)
![](https://i.imgur.com/0TWi2Ge.png)

	* 打開DAI.py 改你的ServerURL  (更正：https:)
    ![](https://i.imgur.com/88ik4fZ.png)

    * 打開terminal -> cd Desktop/IoT/Dummy_Device
	% python3 DAI.py
    ![](https://i.imgur.com/pxcnr2M.png)

    
    * 	回到 iottalk.tw -> Model -> Dummy_Device
	![](https://i.imgur.com/AMF81Vy.png) ![](https://i.imgur.com/SeUe2rU.png)
    ![](https://i.imgur.com/DD8DegD.png) -> Successful !
	回到terminal  檢查是否開始跑數據了
	

5. 更改  DAI.py 
	* 方法一：Red_addr = “自己隨意打一個帳號”
	方法二：Red_addr = None  -> 使用”MAC address”
			(open)  DAN.deregister()
			(open)  exit()   
	* Dummy_Sensor -> T0858610-I
	* Dummy_Control -> T0858610-O
	* Dummy_Device -> T0858610

6. Course Work : 
延續上週作業 改為一對多連線，並在terminal上顯示目前亮度職
	* (記得關掉Simulation)
	* 開啟到上週手機控制燈泡的介面
	![](https://i.imgur.com/AfYqdxJ.png)
	* 增加自己新增的Model -> Model -> T0858610 -> 選 ODA就好
	* 更改Function 
	![](https://i.imgur.com/Xkj9O9R.png)
	* 更改 IDA.py (若不更改，則亮燈時會一直跑99/關燈時則一直跑0)
        -> 希望他
	![](https://i.imgur.com/A92uL3p.png)
	* 目標：轉亮 -> terminal 顯示亮度 (99)
		    轉暗 -> terminal 顯示0
	* 成果：
	![](https://i.imgur.com/ZUoF1n6.png) ![](https://i.imgur.com/le7Gnys.png)


	

 	
	
	



			
	
	
	
	
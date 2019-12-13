# 物聯網(11/13) Bootstrap
###### tags: `IoT`

1. 教學主題：Bootstrap

2. Bootstrap下載套件 在你的網頁使用
(但只能在local上跑)
-> 所以使用CDN

3. 搜尋： “ Bootstrap button ”
[Buttons · Bootstrap](https://getbootstrap.com/docs/4.0/components/buttons/)
-> 可以外加線上編輯 

4. 將上週功課的keypad / Botton / color 套上bootstrap
	* 使用這些控制燈泡
	* keypad決定亮度
	* Switch設定on/off
	* color控制顏色

5. 作業步驟：
	* 架好iot平台
	![](https://i.imgur.com/6CBXpxD.png)

	* 開始用bootstrap改樣式
	打開SwitchSet.html
	[Introduction · Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
	![](https://i.imgur.com/Cc3Gcux.png)

	複製這行CSS進html
		1. 改keypad樣式 
		![](https://i.imgur.com/7AD54Hs.png)
		2. 改button樣式
		![](https://i.imgur.com/pUGsLzc.png)
		3. 改Color樣式
		![](https://i.imgur.com/0SzhtxE.png)
		4. 執行結果
		![](https://i.imgur.com/hab5HTQ.png)![](https://i.imgur.com/3DlZyeV.png)

	* 將HTML按鈕的資料送入IOT平台
		1. 改keypad輸出值
		[image:7B846618-26A3-48B4-B9D2-D3C297B73D5C-12108-0000A27BE925CAEB/螢幕快照 2019-11-13 下午5.06.43.png]		
		2. 改Color輸出值 
		[image:FC049256-5CCB-4F67-9F90-553849AC8C21-12108-0000A2ACD994F979/螢幕快照 2019-11-13 下午5.10.16.png]

	* 	更改function
	![](https://i.imgur.com/gIXpqNp.png)
    ![](https://i.imgur.com/LoGJhA5.png)
    ![](https://i.imgur.com/iOsj6r7.png)

# 物聯網(10/02) Control Bulb Luminance
###### tags: `IoT`

## Target 1 :  做一個控制器
功能一：Flip on 開燈 / Flip off 關燈 (手機ACC的z值)
功能二：開燈時旋轉 -> 隨旋轉方位調整燈的明暗 (手機Ori的a值) 


---

1. Iottalk 開啟上週Model
![](https://i.imgur.com/3MJ3KmC.png)

 
2.  多個感測器做判斷時 -> 使用多對一連線
![](https://i.imgur.com/2rpckqJ.png)

而下方的 input IDF -> 代表感測器控制的順序

3. 更改Function -> 使數值接傳入 input UDF
![](https://i.imgur.com/pr5oYGN.png)

更改function -> 將Acc的值傳入 input IDF 的 args[0]
更改function -> 將Ori的值傳入 input IDF 的 args[1]
![](https://i.imgur.com/tJSZEd7.png)

更改兩者的function
![](https://i.imgur.com/sOoR23z.png)

4. 更改 input IDF 的 Function(主要控制功能者)
![](https://i.imgur.com/pjC5GkP.png)


5. Done !
[file:B2A8112F-2B47-4C8D-A4FE-3B622282A86B-2687-000038402BA4F6AB/10:2Demo.mov]


---

## Target 2：使用js > 改變bulb顏色
1. 下載：https://github.com/IoTtalk/Dummy_Device_WebVer_for_IoTtalk_v1
2. 建立Model
![](https://i.imgur.com/OAWohYH.png)
5.49.54.png]
3. 解壓縮後更改 ida.js -> 更改網址
![](https://i.imgur.com/YL5QjGk.png)
4.  開啟index.html -> 找到號碼
![](https://i.imgur.com/vBwtcPg.png)
5. 連接Model
![](https://i.imgur.com/480hSCR.png)
6. 新增一行「console.log(data[0])」在ida.js中
![](https://i.imgur.com/wUi488E.png)
7. 重新整理網頁 -> 打開「檢查 -> Console 」
![](https://i.imgur.com/hNWvj0M.png)
8. 去e3載檔案
![](https://i.imgur.com/odHYDUz.png)




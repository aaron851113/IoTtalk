# 物聯網(10/09) Control Bulb Color
###### tags: `IoT`

* 課程目標：
-> 自己建一個燈泡的Model
做一個手機連結燈泡
-> 翻轉使燈泡開關
-> 旋轉使燈泡改變顏色

---


* 開啟 ida.js -> 這個Function是用來傳資料的
![](https://i.imgur.com/vVZKIqi.png)
* 進color.js 更改燈泡顏色與亮度
lum = 亮度
![](https://i.imgur.com/acPqzOt.png)
打開index.html檢查顏色
![](https://i.imgur.com/f2rGP2O.png)
-> Right!

* 來開始製作燈泡的iottalk Model
-> 先來建亮度的Feature
![](https://i.imgur.com/rekoBMj.png)

-> 再來建Color的Feature
![](https://i.imgur.com/dbyIOHY.png)

-> 建立一個Device Model 把兩個Feature input進去
![](https://i.imgur.com/0NkLzkS.png)

-> 回到Project 看能不能建立成功 -> 建立一個Smart Phone 接起來
![](https://i.imgur.com/qZCrqSW.png)


* 更改model裡的Function
![](https://i.imgur.com/EUzJNU9.png)
![](https://i.imgur.com/jsYYbSq.png)
(後面這個不改，交由ida來做正規化)


---


* 來開始製作連接用的網頁
-> 把這些複製到Bulb_origin -> js 裡
![](https://i.imgur.com/pzCBiiE.png)
-> 檢查Bulb_origin/js
![](https://i.imgur.com/AbzfmRx.png)
-> 更改index.html
![](https://i.imgur.com/ja3rfBn.jpg)
![](https://i.imgur.com/kZjduzN.png)
(把這跟欄位交由ida去控制，配合ida中的
```
$(‘.title’)[0].innerText=profile.d_name;)
```
才能有以下畫面
![](https://i.imgur.com/jAPEQBN.png)

-> 更改ida.js (Most Important !) 
![](https://i.imgur.com/tkt4KMN.png)
![](https://i.imgur.com/hp50Jg4.png)










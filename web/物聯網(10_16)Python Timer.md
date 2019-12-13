# 物聯網(10/16)Python Timer
###### tags: `IoT`

1. 回顧上週課程：JS的部分
HTML中，使用 ajax 的 async (同步)
將其改為  async : false (非同步模式)
能使網頁更流暢
```
var a = $.ajax({type:"GET",url:window.location.origin + '/p.txt' , async:false}).responseText;

console.log('a=',a);
```
但若要即時取資料又怕同步有問題：使用JS的...“ .done “
```
$.get(window.location.origin + '/p.txt')
.done(
	function(result)
	{ console.log(result); }
);
```
 
2. 到 E3 IOT -> 10/16 Reference Code -> 下載三個檔案



---


3. 今天課程主題：以Python寫計時器用於物聯網
 -> Cyber device development (Python-based)
	* 作業目標：
	-> 做一個控制器 -> 輸入時間後，可以設定燈泡開關時間
	-> IDF Name : Time1
	-> Device Name : Time-0858610
	* 打開 timeCheck.py
	![](https://i.imgur.com/5ZaMq1g.png)
	* 打開 StringSplit.py
	![](https://i.imgur.com/8zMORXP.png)
	* 建一個Dummy Device Input -> 修改其Name
	![](https://i.imgur.com/08y6syP.png)
	* 打開getAlias.py
	![](https://i.imgur.com/e3KS1xB.png)
    
    
	* 先建立一個Model
	 Device名稱：Time-0858610
	 IDF 名稱 :  Time1  
	![](https://i.imgur.com/yUkFrUJ.png)

	* 建立 燈泡的Function 
	IDF Start time 傳入1 -> 燈泡亮(99)
	IDF End time 傳入0 -> 燈泡暗(0)
	![](https://i.imgur.com/RxAM6Io.png)

    
	* 	修改 getAlias.py
```
import requests, time
import csmapi, DAN

ServerURL = 'https://3.iottalk.tw' #Change to your IoTtalk IP or None for autoSearching
Reg_addr='aaron851113' # if None, Reg_addr = MAC address

DAN.profile['dm_name']='Time-0858610'
DAN.profile['df_list']=['Time1', 'Dummy_Control',]
#DAN.profile['d_name']= 'Assign a Device Name' 

DAN.device_registration_with_retry(ServerURL, Reg_addr)

from datetime import datetime as dt

while 1:
    try:
        IDFname = DAN.get_alias('Time1')
        print(IDFname)
        IDFname = "".join(IDFname)
        Time = IDFname.split('~')
        try : 
            Tmp = dt.strptime(Time[0],'%H:%M:%S')
        except Exception :
            print("輸入錯誤：請輸入正確的時間!")
        Start = dt.strptime(Time[0],'%H:%M:%S')
        End = dt.strptime(Time[1],'%H:%M:%S')
        #從系統拿時間出來>只抽取小時/分鐘
        stime = dt.now().strftime('%H:%M:%S')
        Sys_Time  = dt.strptime(stime,'%H:%M:%S')
        if Sys_Time == End :
            print("時間到：回傳0到IDF")
            DAN.push("Time1",0)
            break
        if Sys_Time == Start :
            print("回傳1到IDF")
            DAN.push("Time1",1)
            
    except Exception as e :
        print(e)

    time.sleep(1)

```
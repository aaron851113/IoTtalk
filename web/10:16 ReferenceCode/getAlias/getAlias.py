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
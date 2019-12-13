# 物聯網(11/20) Crawler
###### tags: `IoT`

1. 教學主題：Beautifulsoup (網路爬蟲)

2. 練習
執行 crawl_weather.py 
執行 parse_weather.py
![](https://i.imgur.com/TVNFXsz.png)


3. 把DAN.py / csmapi.py 複製到資料夾


4. 作業：取溫度 風向 風力  當作snesor put到iottalk上
	* 先建device (IDF/ODF各六個)
	![](https://i.imgur.com/vcXzQIC.png)
    ![](https://i.imgur.com/FgtTRUH.png)

	* 開一個python3 : Tainan.py
	* 更改爬取網頁 -> 檢查爬蟲後df的輸出
	* 把DAI.py複製進code
	* DAN Push 進平台
	* DAN PULL出來 然後印出
	
```
import requests
import time
from io import open

region = 'Tainan'
url = 'https://www.cwb.gov.tw/V7/observe/24real/Data/46741.htm'


def f(url, fn):
	headers = {
     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
	}
	res = requests.get(url, headers=headers)
	res.encoding = 'utf-8'

	open(fn,'wb').write(res.text.encode('utf-8'))

fn = region+ '.html'.format(0,0)
f(url, fn)


from bs4 import BeautifulSoup

def get_element(soup, tag, class_name):
    data = []
    table = soup.find(tag, attrs={'class':class_name})
    rows = table.find_all('tr')
    del rows[0]
    
    for row in rows:
        first_col = row.find_all('th')
        cols = row.find_all('td')
        cols.insert(0, first_col[0])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) 
    return data

   
file_name = region+".html"

f = open (file_name,'r', encoding='utf-8')
s = f.readlines()
s = ''.join(s)

soup = BeautifulSoup(s, "lxml")

df_tmp = get_element(soup, 'table','BoxTable')

#########################################################################################
import pandas as pd
print ('Region :', region,'Building table ...')
col_list = ['觀測時間', '溫度(°C)', '溫度(°F)', '天氣', '風向', '風力 (m/s)|(級)', '陣風 (m/s)|(級)', '能見度(公里)', '相對溼度(%)', '海平面氣壓(百帕)', '當日累積雨量(毫米)', '日照時數(小時)']
df = pd.DataFrame(columns = col_list)
df_tmp = pd.DataFrame(df_tmp)
df_tmp.columns = col_list
df = pd.concat([df, df_tmp], axis=0)   
df = df.reset_index(drop=True)    

print("時間：",df.iloc[0,0])
temperature = df.iloc[0,1]
print("溫度：",temperature)
wind1 = df.iloc[0,4]
print("風向：",wind1)
wind2 = df.iloc[0,5]
print("風力(m/s)|(級):",wind2)
wet = df.iloc[0,8]
print("相對濕度:",wet)
rain = df.iloc[0,10]
print("當日累積雨量:",rain)   

df.to_csv(( region + '.csv'), encoding = 'utf-8')
###################################################################################

#DAI.py
import time, random, requests
import DAN

#ServerURL = 'http://IP:9999'      #with non-secure connection
ServerURL = 'https://3.iottalk.tw' #with SSL connection
Reg_addr =  None#if None, Reg_addr = MAC address

DAN.profile['dm_name']='temperature-0858610'
DAN.profile['df_list']=['rain','temperature','wet','wind_direction','wind_power','rain_out','temperature_out','wet_out','wind_direction_out','wind_power_out']
#DAN.profile['d_name']= 'Assign a Device Name' 

DAN.device_registration_with_retry(ServerURL, Reg_addr)
#DAN.deregister()  #if you want to deregister this device, uncomment this line
#exit()            #if you want to deregister this device, uncomment this line

last = 0
while True:
    try:
        data = [rain,temperature,wet,wind1,wind2]
        DAN.push('rain',rain)
        DAN.push('temperature',temperature) #Push data to an input device feature "Dummy_Sensor"
        DAN.push('wet',wet)
        DAN.push('wind_direction',wind1)
        DAN.push('wind_power',wind2)
        #==================================
        
        data1 = DAN.pull('rain_out')
        data2 = DAN.pull('temperature_out')
        data3 = DAN.pull('wet_out')
        data4 = DAN.pull('wind_direction_out')
        data5 = DAN.pull('wind_power_out')
        print ("現在時間 : , ",df.iloc[0,0])
        print ("累積雨量 ：",data1)
        print ("現在溫度(度C) :",data2)
        print ("相對濕度 :",data3)
        print ("風向 :",data4)
        print ("風力 :",data5)
        time.sleep(30)
        
        
                
    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

      
```

---	
* 程式輸出結果
![](https://i.imgur.com/DmTcGia.png)

	
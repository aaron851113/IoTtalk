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
wind2 = float(wind2.split('|')[0])
print("風力(m/s):",wind2)
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
ServerURL = 'https://6.iottalk.tw' #with SSL connection
Reg_addr =  'aaaarrrroooonnnn'#if None, Reg_addr = MAC address

DAN.profile['dm_name']='temperature-0858610'
DAN.profile['df_list']=['rain','temperature','wet','wind_direction','wind_power','RainMeter-O','Temperature-O','Humidity-O','WindDirection-O','WindSpeed-O','MSG-O']
DAN.profile['d_name']= 'Aaron' 

DAN.device_registration_with_retry(ServerURL, Reg_addr)
#DAN.deregister()  #if you want to deregister this device, uncomment this line
#exit()            #if you want to deregister this device, uncomment this line

last = 0
while True:
    try:
        DAN.push('rain',rain)
        DAN.push('temperature',temperature) #Push data to an input device feature "Dummy_Sensor"
        DAN.push('wet',wet)
        DAN.push('wind_direction',wind1)
        DAN.push('wind_power',wind2)
        #==================================
        time.sleep(10)
                
    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

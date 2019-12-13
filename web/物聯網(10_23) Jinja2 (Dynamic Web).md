# 物聯網(10/23) Jinja2 (Dynamic Web)
###### tags: `IoT`

1. 課程主題：Jinja2 (Dynamic Web)
2. 事前準備：
    ```
	$ pip install flask
	$ cd Desktop/IoT/SwitchSet
	$ sudo python3 app.py 
	```
    ![](https://i.imgur.com/oWKojvQ.png)
	* IoT -> static -> SwitchSet.js
    ![](https://i.imgur.com/LmGDjQt.png)
	* (http://127.0.0.1/aaron-device/3/)
	![](https://i.imgur.com/6eYYM6k.png)

	

    
3. 打開 Iottalk 
	* 建立一個 Remote-control model (選擇switch數量)
	![](https://i.imgur.com/UKCGVZR.png)

	* 連到自己剛剛開的網頁 
	![](https://i.imgur.com/I41urne.png)


4. 解說 app.py
	* render_template  ： Jinja2動態網頁
	* app.route
	* linux / MacOS 若要使1024以下的port ：要 $sudo
5. 解說SwitchSet.html 
( Bootstrap -> 寫網頁用)

6. 作業：
	* 如何將HTML上Switch數量 修正為model上的Switch數量 
	![](https://i.imgur.com/DhxjVCz.png)

	
7. 作業解答 app.py 
![](https://i.imgur.com/uZoG3wF.png)


```
##########################################################################################################################
import csmapi
from flask import Flask, request, abort
from flask import render_template
from flask import make_response

app = Flask(__name__)

csmapi.ENDPOINT  = 'https://3.iottalk.tw'  #Please fill the used IoTtalk server URL.

@app.route('/<mac_addr>/<count>', methods=['GET', 'POST'])
def SwitchSetCount(mac_addr, count):
    try:
        registered_address = mac_addr
        profile = csmapi.pull(registered_address, 'profile') #Pull the profile of RemoteControl
        if profile:
            device_feature_list = profile['df_list']
            print("Device feature list = ", device_feature_list)
        
        control_channel_output = csmapi.pull(registered_address, '__Ctl_O__') #Pull the Output of Control Channel
        if control_channel_output:
            selected_device_feature_flags = control_channel_output[0][1][1]['cmd_params'][0]
            print("Selected device feature flags = ", selected_device_feature_flags)
        num = selected_device_feature_flags.count('1')
        print("Iottalk Switch's Count :",num)
        return make_response(render_template('SwitchSet.html', mac_addr=registered_address, count=num))
        
    except Exception as e:
        print('Error:',e)
        return make_response(render_template('SwitchSet.html', mac_addr=mac_addr, count=int(count)))
        
if __name__ == "__main__":
    app.run('127.0.0.1', port=8000, threaded=True, use_reloader=False)

```
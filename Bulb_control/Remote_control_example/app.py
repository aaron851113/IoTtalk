##########################################################################################################################
import csmapi
from flask import Flask, request, abort
from flask import render_template
from flask import make_response

app = Flask(__name__)

csmapi.ENDPOINT  = 'https://3.iottalk.tw'  #Please fill the used IoTtalk server URL.

@app.route('/<mac_addr>/', methods=['GET', 'POST'])
def SwitchSetCount(mac_addr, count=1 ,count1=1 ,count2=1 ,count3=1 ,count4=1):
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
       
            button_string = selected_device_feature_flags[18:27]
            button_num = button_string.count('1')
            print("Button String :",button_string)
            print("Iottalk Button Count :",button_num )
            
            color_string = selected_device_feature_flags[36:45]
            color_num = color_string.count('1')
            print("Color String :",color_string)
            print("Iottalk Color Count :",color_num )
            
            key_string = selected_device_feature_flags[9:18]
            key_num = key_string.count('1')
            print("keypad String :",key_string)
            print("Iottalk keypad Count :",key_num )
            
            knob_string = selected_device_feature_flags[27:36]
            knob_num = knob_string.count('1')
            print("knob String :",knob_string)
            print("Iottalk knob Count :",knob_num )
            
            switch_string = selected_device_feature_flags[0:9]
            switch_num = switch_string.count('1')
            print("Switch String :",switch_string)
            print("Iottalk Switch Count :",switch_num )
        
        
        return make_response(render_template('SwitchSet.html', mac_addr=registered_address, 
                                             count=switch_num,count1=key_num,
                                             count2=button_num,count3=knob_num,
                                             count4=color_num))
        
    except Exception as e:
        print('Error:',e)
        return make_response(render_template('SwitchSet.html', mac_addr=mac_addr, 
                                             count=int(count),count1=int(count1),
                                             count2=int(count2),count3=int(count3),
                                             count4=int(count4)))
        
if __name__ == "__main__":
    app.run('127.0.0.1', port=8000, threaded=True, use_reloader=False)


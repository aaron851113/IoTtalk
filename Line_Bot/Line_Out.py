#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:08:15 2019

@author: aaron-mb
"""

import DAN
import time

ServerURL = 'https://6.iottalk.tw' #with SSL connection
Reg_addr =  'aarroonn'#if None, Reg_addr = MAC address

DAN.profile['dm_name']='Line'
DAN.profile['df_list']=['Line_Out']
DAN.profile['d_name']= 'Line_Out' 

DAN.device_registration_with_retry(ServerURL, Reg_addr)
while True:
    try:
        data = DAN.pull('Line_Out')
        if data != None : 
            print(data)
        #==================================
                
    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

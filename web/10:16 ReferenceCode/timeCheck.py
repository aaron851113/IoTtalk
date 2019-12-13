from datetime import datetime as dt

if __name__ == '__main__':

    try:
        #設定時間字串
        TimeStr1 = '14:59'
        #用strptime把字串轉成時間物件 格式"小時/分鐘"
        TimeObj1 = dt.strptime(TimeStr1,'%H:%M')
        print(TimeObj1)
        print(type(TimeObj1))
        
        #從系統拿時間出來>只抽取小時/分鐘
        TimeStr2 = dt.now().strftime('%H:%M')
        TimeObj2 = dt.strptime(TimeStr2,'%H:%M')
        print(TimeObj2)
        
    #檢查格式是否有誤
    except Exception as e:
        print('ErrMsg:', e)
  
    print(TimeObj1 == TimeObj2)



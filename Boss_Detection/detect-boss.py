from sklearn.preprocessing import LabelEncoder
import numpy as np
import imutils
import cv2
import time
import datetime
import pandas as pd 
##############################################
import DAN
ServerURL = 'https://6.iottalk.tw' #with SSL connection
Reg_addr =  'AAaaaAAaaa'#if None, Reg_addr = MAC address
DAN.profile['dm_name']='HKA_BOSS'
DAN.profile['df_list']=['HKA_STAFF_NUM','HKA_STRING']
DAN.profile['d_name']= 'Sensor' 
DAN.device_registration_with_retry(ServerURL, Reg_addr)

#####################################################################
detectType = 1   # 0 for any face, 1 for boss's face only
bossName = "boss"
cam_id = 0
monitor_winSize = (640, 480)
cam_resolution = (1024,768)
fake_screenFile = "objects/desktop.jpg"
cascade = "haarcascade_frontalface_default.xml"  # lbpcascade_frontalface.xml / haarcascade_frontalface_default.xml
#Face detect
face_size = (47, 62)
scaleFactor = 1.3
minNeighbors = 10

save_path = 'office_time/'
#####################################################################

face_cascade = cv2.CascadeClassifier('objects/' + cascade)
last_detect = 0
target = np.loadtxt('objects/target.out', delimiter=',', dtype=np.str)

le = LabelEncoder()
le.fit_transform(target)
print("The model is loading , please wait...")

recognizer = cv2.face.LBPHFaceRecognizer_create(radius=2, neighbors=16, grid_x=8, grid_y=8)
recognizer.read("objects/boss.yaml")

camera = cv2.VideoCapture(cam_id)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, cam_resolution[0])
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_resolution[1])

def putText(image, text, x, y, color=(255,255,255), thickness=1, size=1.2):
    if x is not None and y is not None:
        cv2.putText( image, text, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, size, color, thickness)
    return image

def faceDisplay(img1, txt):
    black = [0,0,0]     #---Color of the border---
    constant=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=black )

    violet= np.zeros((80, constant.shape[1], 3), np.uint8)
    violet[:] = (255, 0, 180) 
    vcat = cv2.vconcat((violet, constant))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(vcat,txt,(5,30), font, 1,(0,0,0), 1, 0)
    cv2.imshow(txt, vcat)
    cv2.waitKey(1)

def fakeScreen():
    cv2.namedWindow("Desktop", cv2.WND_PROP_FULLSCREEN)        # Create a named window
    cv2.setWindowProperty("Desktop", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);
    cv2.moveWindow("Desktop", 0,0)
    cv2.imshow("Desktop", cv2.imread(fake_screenFile))
    cv2.waitKey(1)


status = -1 

while True:
    (grabbed, img) = camera.read()    

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor= scaleFactor,
        minNeighbors=minNeighbors,
        minSize=face_size,
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    

    i = 0
    
    for (x,y,w,h) in faces:
        roi_color = img[y:y+h, x:x+w]        
		
        now=datetime.datetime.now()
        detectTime = '%s-%s-%s_%s-%s-%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        
        if(w>face_size[0] and h>face_size[1]):
            roi_gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
            face = cv2.resize(roi_gray, face_size)
    
            (prediction, conf) = recognizer.predict(face)
            namePredict = []
            if prediction == 0 :
                namePredict = 'boss'               
            elif prediction == 1 : 
                namePredict = 'staff_Kevin'
            elif prediction == 2 :
                namePredict = 'staff_Hank'
            
            
            # diff face only
            if conf < 203 :
            #if status != prediction and conf < 210 :
                
                # Create Time
                t = datetime.datetime.now()
                office_time = str(t.year)+'/'+str(t.month)+'/'+str(t.day)+'/'+str(t.hour)+':'+str(t.minute)
                
                if bossName in namePredict :
                    last_detect = time.time()
                    cv2.imshow("Boss", roi_color)
                    putText(img, namePredict, x, y-20, (255,0,0), thickness=2, size=2)
                    print('Prediction :',prediction,'[',namePredict,']','Time :',office_time,'Conf:',conf)
                    DAN.push('HKA_STAFF_NUM',prediction)                
                    DAN.push('HKA_STRING',office_time)
                    status = 0
                    time.sleep(1.5)
                
                elif 'staff' in  namePredict :
                    cv2.imshow("staff", roi_color)
                    putText(img, namePredict, x, y-20, (0,255,0), thickness=2, size=2)
                    print('Prediction :',prediction,'[',namePredict,'] ','Time :',office_time,'Conf:',conf)
                    # to IoT
                    DAN.push('HKA_STAFF_NUM',prediction)                
                    DAN.push('HKA_STRING',office_time)
                    namePredict = namePredict.replace("staff_","")
                    # write to csv
                    df = pd.read_csv("office_time.csv")
                    df = df.append({'staff' : namePredict , 'office_time' :office_time} ,ignore_index=True)
                    df.to_csv("office_time.csv", sep="," , index=False)
                    time.sleep(1.5)
                
                # change Status
                status = prediction
                time.sleep(1)
            else:
                # Create Time
                t = datetime.datetime.now()
                office_time = str(t.year)+'/'+str(t.month)+'/'+str(t.day)+'/'+str(t.hour)+':'+str(t.minute)
                
                cv2.imshow("Unkown", roi_color)
                putText(img, "Unkown" , x, y-20, (0,0,255), thickness=2, size=2)
                print('Prediction :','Unkown','Conf:',conf)
                print("TAKE CARE TAKE CARE TAKE CARE !")
                # to IoT
                prediction = 3 
                DAN.push('HKA_STAFF_NUM',prediction)                
                DAN.push('HKA_STRING',office_time)
                time.sleep(1)

    if(last_detect>0 and detectType==1):
        last_boss_time = datetime.datetime.fromtimestamp( int(last_detect) ).strftime('%Y-%m-%d %H:%M:%S')
        putText(img, last_boss_time + " boss is here!", 5, 40, (255,35,35), thickness=2, size=1)  
    			
    r = monitor_winSize[1] / img.shape[1]
    dim = (monitor_winSize[0], int(img.shape[0] * r))
    img2 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("Frame", img2)
    key = cv2.waitKey(1)
# 物聯網(11/27) Dashboard
###### tags: `IoT`

1. Gitlab[Sign in · GitLab](https://gitlab.com/IoTtalk/FarmDashboard)
帳號：dashboardclass
密碼：dashboard2019
![](https://i.imgur.com/kTsnXO3.png)


2.``` $ git clone https://gitlab.com/IoTtalk/FarmDashboard.git ```
![](https://i.imgur.com/u3k6j7M.png)


3. 建立環境/安裝套件
```
$ conda activate IoT
$ cd Desktop/Fram…
$ sudo pip install -r requirements.txt
```

4. 安裝MySQL >= 5.7
	* [MySQL :: Begin Your Download](https://dev.mysql.com/downloads/file/?id=490317)
	* $ vim ~/.zshrc 
	* [按a 貼上這一行] export PATH=“/usr/local/mysql/bin:$PATH”
	* [按esc] -> [shift] -> [:wq]
	* $ source ~/.bash_profile
	
5. 新增MySQL User  / Database
 	* [DashBoard - HackMD](https://hackmd.io/5LqVk4MBSCinRXQderD_Jw) 詳細說明
[進入MySQL]
    ```
	$ mysql -u root -p  
	$ status
	$ CREATE USER ‘dashboard’@‘%’ IDENTIFIED BY ‘12345678’; 
	$ GRANT ALL PRIVILEGES ON *.* TO ‘dashboard’@‘%’ ;
	$ flush privileges;
	$ create database dashboard ;
    ```
	
6. *dashboard*
	* ctrl + D (離開SQL)
	```
    $ cd Desktop/FarmDashboard
    ```
	* 修改 config.py
	(第8/14行)
	8: DB_CONFIG = 'mysql+pymysql://dashboard:12345678@localhost:3306/dashboard?charset=utf8'
	14 : CSM_HOST = ‘3.iottalk.tw’
	* python3 db.py init
---
* dashboard 從這開始
	```
    $ conda activate IoT
    
    $ cd Desktop/IoT/crawler/
    $ python Tainan.py
    $ cd ../..
    
    $ cd Desktop/FarmDashboard/
    $ bash startup.sh
	$ tmux a
    control+b 1
    ```
	![](https://i.imgur.com/QmW5qXr.png)
    
    * 帳號：admin 密碼：123456789
    ![](https://i.imgur.com/2NY36j5.png)

    
	* 127.0.0.1:5000 -> 打開dashboard
	![](https://i.imgur.com/hepNpWE.png)
    

	*  Field Management
	![](https://i.imgur.com/d4Ykt8k.png)

	*  User Management
	![](https://i.imgur.com/64nJN4W.png)

    ```
	$ cd Desktop/FarmDashboard/
	$ bash startup.sh
	```
7. IOT talk : 左邊為上次作業的Input (Tanian.py) 
右邊為DataServer
![](https://i.imgur.com/BtuoUJF.png)


8. 執行結果：
![](https://i.imgur.com/cSR9iEa.png)
![](https://i.imgur.com/Vf50473.png)




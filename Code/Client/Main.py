# -*- coding: utf-8 -*-
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sys
import math
from ui_led import Ui_led
from ui_face import Ui_Face
from ui_client import Ui_client
from ui_calibration import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Client import *

class MyWindow(QMainWindow,Ui_client):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('Picture/logo_Mini.png'))
        self.Video.setScaledContents (True)
        self.Video.setPixmap(QPixmap('Picture/Spider_client.png'))

        self.client=Client()
        file = open('IP.txt', 'r')
        self.lineEdit_IP_Adress.setText(str(file.readline()))
        file.close()

        self.Key_W = False
        self.Key_A = False
        self.Key_S = False
        self.Key_D = False
        self.Key_Space = False

        #Button click event
        self.Button_Connect.clicked.connect(self.connect)
        self.Button_Video.clicked.connect(self.video)
        self.Button_IMU.clicked.connect(self.imu)
        self.Button_Calibration.clicked.connect(self.showCalibrationWindow)
        self.Button_LED.clicked.connect(self.showLedWindow)
        self.Button_Face_ID.clicked.connect(self.showFaceWindow)
        self.Button_Face_Recognition.clicked.connect(self.faceRecognition)
        self.Button_Sonic.clicked.connect(self.sonic)
        self.Button_Relax.clicked.connect(self.relax)
        self.Button_Buzzer.pressed.connect(self.buzzer)
        self.Button_Buzzer.released.connect(self.buzzer)
        self.Button_Attack.pressed.connect(self.attack)
        self.button_leg1_front_plus.pressed.connect(self.posture, 1)
        self.button_leg1_front_minus.pressed.connect(self.posture, 2)
        self.button_leg1_middle_plus.pressed.connect(self.posture, 3)
        self.button_leg1_middle_minus.pressed.connect(self.posture, 4)
        self.button_leg1_back_plus.pressed.connect(self.posture, 5)
        self.button_leg1_back_minus.pressed.connect(self.posture, 6)
        self.button_leg2_front_plus.pressed.connect(self.posture, 7)
        self.button_leg2_front_minus.pressed.connect(self.posture, 8)
        self.button_leg2_middle_plus.pressed.connect(self.posture, 9)
        self.button_leg2_middle_minus.pressed.connect(self.posture, 10)
        self.button_leg2_back_plus.pressed.connect(self.posture, 11)
        self.button_leg2_back_minus.pressed.connect(self.posture, 12)
        self.button_leg3_front_plus.pressed.connect(self.posture, 13)
        self.button_leg3_front_minus.pressed.connect(self.posture, 14)
        self.button_leg3_middle_plus.pressed.connect(self.posture, 15)
        self.button_leg3_middle_minus.pressed.connect(self.posture, 16)
        self.button_leg3_back_plus.pressed.connect(self.posture, 17)
        self.button_leg3_back_minus.pressed.connect(self.posture, 18)
        self.button_leg4_front_plus.pressed.connect(self.posture, 19)
        self.button_leg4_front_minus.pressed.connect(self.posture, 20)
        self.button_leg4_middle_plus.pressed.connect(self.posture, 21)
        self.button_leg4_middle_minus.pressed.connect(self.posture, 22)
        self.button_leg4_back_plus.pressed.connect(self.posture, 23)
        self.button_leg4_back_minus.pressed.connect(self.posture, 24)
        self.button_leg5_front_plus.pressed.connect(self.posture, 25)
        self.button_leg5_front_minus.pressed.connect(self.posture, 26)
        self.button_leg5_middle_plus.pressed.connect(self.posture, 27)
        self.button_leg5_middle_minus.pressed.connect(self.posture, 28)
        self.button_leg5_back_plus.pressed.connect(self.posture, 29)
        self.button_leg5_back_minus.pressed.connect(self.posture, 30)
        self.button_leg6_front_plus.pressed.connect(self.posture, 31)
        self.button_leg6_front_minus.pressed.connect(self.posture, 32)
        self.button_leg6_middle_plus.pressed.connect(self.posture, 33)
        self.button_leg6_middle_minus.pressed.connect(self.posture, 34)
        self.button_leg6_back_plus.pressed.connect(self.posture, 35)
        self.button_leg6_back_minus.pressed.connect(self.posture, 36)

        #Slider
        self.slider_head.setMinimum(50)
        self.slider_head.setMaximum(180)
        self.slider_head.setSingleStep(1)
        self.slider_head.setValue(90)
        self.slider_head.valueChanged.connect(self.headUpAndDown)

        self.slider_head_1.setMinimum(0)
        self.slider_head_1.setMaximum(180)
        self.slider_head_1.setSingleStep(1)
        self.slider_head_1.setValue(90)
        self.slider_head_1.valueChanged.connect(self.headLeftAndRight)

        self.slider_speed.setMinimum(2)
        self.slider_speed.setMaximum(10)
        self.slider_speed.setSingleStep(1)
        self.slider_speed.setValue(8)
        self.slider_speed.valueChanged.connect(self.speed)
        self.client.move_speed = str(self.slider_speed.value())

        self.slider_twist.setMinimum(-15)
        self.slider_twist.setMaximum(15)
        self.slider_twist.setSingleStep(1)
        self.slider_twist.setValue(0)
        self.slider_twist.valueChanged.connect(self.setRoll)

        self.slider_height.setMinimum(-20)
        self.slider_height.setMaximum(20)
        self.slider_height.setSingleStep(1)
        self.slider_height.setValue(0)
        self.slider_height.valueChanged.connect(self.setZ)

        #checkbox
        self.ButtonActionMode1.setChecked(True)
        self.ButtonActionMode1.toggled.connect(lambda: self.actionMode(self.ButtonActionMode1))
        self.ButtonActionMode2.setChecked(False)
        self.ButtonActionMode2.toggled.connect(lambda: self.actionMode(self.ButtonActionMode2))
        self.ButtonGaitMode1.setChecked(True)
        self.ButtonGaitMode1.toggled.connect(lambda: self.gaitMode(self.ButtonGaitMode1))
        self.ButtonGaitMode2.setChecked(False)
        self.ButtonGaitMode2.toggled.connect(lambda: self.gaitMode(self.ButtonGaitMode2))

        #Timer
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.refresh_image)

        self.timer_power = QTimer(self)
        self.timer_power.timeout.connect(self.power)

        self.timer_sonic = QTimer(self)
        self.timer_sonic.timeout.connect(self.getSonicData)

        #Variable
        self.power_value= [100,100]
        self.move_point = [750, 1050]
        self.move_flag = False
        self.drawpoint = [[1890, 1050], [1410, 1050]]
        self.action_flag = 1
        self.gait_flag = 1

    # keyboard
    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_C):
            print("C")
            self.connect()
        if (event.key() == Qt.Key_V):
            try:
                print("V")
                self.video()
            except Exception as e:
                print(e)

        if (event.key() == Qt.Key_R):
            print("R")
            self.relax()
        if (event.key() == Qt.Key_L):
            print("L")
            self.showLedWindow()
        if (event.key() == Qt.Key_B):
            print("B")
            self.imu()
        if (event.key() == Qt.Key_F):
            print("F")
            self.faceRecognition()
        if (event.key() == Qt.Key_U):
            print("U")
            self.sonic()
        if (event.key() == Qt.Key_I):
            print("I")
            self.showFaceWindow()
        if (event.key() == Qt.Key_T):
            print("T")
            self.showCalibrationWindow()
        if (event.key() == Qt.Key_Y):
            print("Y")
            self.buzzer()

        if event.isAutoRepeat():
            pass
        else:
            if event.key() == Qt.Key_W:
                self.Key_W = True
                print("W")
                self.move_point = [750, 950]
                self.move()
            elif event.key() == Qt.Key_S:
                self.Key_S = True
                print("S")
                self.move_point = [750, 1150]
                self.move()
            elif event.key() == Qt.Key_A:
                self.Key_A = True
                print("A")
                self.move_point = [650, 1050]
                self.move()
            elif event.key() == Qt.Key_D:
                self.Key_D = True
                print("D")
                self.move_point = [850, 1050]
                self.move()
    # When you stop pressing a key the move point goes back to it's starting point.

    def keyReleaseEvent(self, event):
        if (event.key() == Qt.Key_W):
            if not (event.isAutoRepeat()) and self.Key_W == True:
                print("release W")
                self.Key_W = False
                self.move_point = [750, 1050]
                self.move()
        elif (event.key() == Qt.Key_A):
            if not (event.isAutoRepeat()) and self.Key_A == True:
                print("release A")
                self.Key_A = False
                self.move_point = [750, 1050]
                self.move()
        elif (event.key() == Qt.Key_S):
            if not (event.isAutoRepeat()) and self.Key_S == True:
                print("release S")
                self.Key_S = False
                self.move_point = [750, 1050]
                self.move()
        elif (event.key() == Qt.Key_D):
            if not (event.isAutoRepeat()) and self.Key_D == True:
                print("release D")
                self.Key_D = False
                self.move_point = [750, 1050]
                self.move()
    def paintEvent(self,e):
        try:
            qp=QPainter()
            qp.begin(self)
            qp.setPen(QPen(Qt.white,2,Qt.SolidLine))
            qp.drawRect(1740, 900, 300, 300)
            qp.drawRect(1260, 900, 300, 300)
            qp.setRenderHint(QPainter.Antialiasing)

            #steering wheel
            qp.setPen(Qt.NoPen)
            qp.setBrush(QColor(212, 208, 205))
            qp.drawEllipse(QPoint(750, 1050), 150, 150)
            qp.setBrush(QBrush(QColor(138, 99, 83)))
            qp.drawEllipse(QPoint(self.move_point[0], self.move_point[1]), 15, 15)
            qp.setPen(QPen(QColor(138, 99, 83), 2, Qt.SolidLine))
            x1 = round(math.sqrt(150**2-(self.move_point[1]-1050)**2)+750)
            y1 = round(math.sqrt(150 ** 2 - (self.move_point[0] - 750) ** 2) + 1050)
            qp.drawLine(x1, self.move_point[1], 1500-x1, self.move_point[1])
            qp.drawLine(self.move_point[0], 2100-y1, self.move_point[0], y1)

            #tilt
            qp.drawLine(self.drawpoint[0][0], 900, self.drawpoint[0][0], 1200)
            qp.drawLine(1740, self.drawpoint[0][1], 2040, self.drawpoint[0][1])
            pitch = round((1050-self.drawpoint[0][1]) / 150.0 * 15)
            yaw = round((self.drawpoint[0][0] - 1890) / 150.0 * 15)
            self.label_tilt_value.setText(str((yaw, pitch)))

            #position
            qp.drawLine(self.drawpoint[1][0], 900, self.drawpoint[1][0],1200)
            qp.drawLine(1260, self.drawpoint[1][1], 1560, self.drawpoint[1][1])
            y = round((1050-self.drawpoint[1][1] ) / 150.0 * 40)
            x = round((self.drawpoint[1][0] - 1410) / 150.0 * 40)
            self.label_pane_value.setText(str((x, y)))
            qp.end()
        except Exception as e:
            print(e)

    def mouseMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        # In this condition we hover the mouse in the tilt box
        if ( x >= 1740 and x <= 2040) and (y >= 900 and y <= 1200):
            try:
                self.drawpoint = [[1890, 1050], [1410, 1050]]
                if  self.move_flag:
                    self.move_point = [750, 1050]
                    self.move_flag = False
                    self.move()
                if self.Button_IMU.text() == "Close":
                    self.Button_IMU.setText("Balance")
                self.drawpoint[0][0] = x
                self.drawpoint[0][1] = y
                self.update()
                self.attitude()
            except Exception as e:
                print(e)
        # In this condition we hover the mouse in the pan box
        if (x >= 1260 and x <= 1560) and (y >= 900 and y <= 1200):
            try:
                self.drawpoint = [[1890, 1050], [1410, 1050]]
                if self.move_flag:
                    self.move_point = [750, 1050]
                    self.move_flag = False
                    self.move()
                if self.Button_IMU.text() == "Close":
                    self.Button_IMU.setText("Balance")
                self.move_point = [750, 1050]
                self.drawpoint[1][0] = x
                self.drawpoint[1][1] = y
                self.update()
                self.position()
            except Exception as e:
                print(e)
        # In this condition we hover the mouse in the movement box
        elif x >= 600 and x <= 900 and y >= 900 and y <= 1200:
            r = (x - 750) ** 2 + (1050-y) ** 2
            self.drawpoint = [[1890, 1050], [1410, 1050]]
            if self.Button_IMU.text() == "Close":
                self.Button_IMU.setText("Balance")
            if r < 22500:
                self.move_flag = True
                self.move_point[0] = x
                self.move_point[1] = y
                self.move()
                self.update()
            else:
                x = x - 750
                y = 1050 - y
                angle = math.atan2(y, x)
                self.move_point[0] = 150*math.cos(angle)+750
                self.move_point[1] = 1050-150*math.sin(angle)
                self.move()
                self.update()
        elif self.move_flag == True:
            x = x - 750
            y = 1050 - y
            angle = math.atan2(y, x)
            self.move_point[0] = 150 * math.cos(angle) + 750
            self.move_point[1] = 1050 - 150 * math.sin(angle)
            self.move()
            self.update()

    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        # In this condition we press mouse button in the tilt box
        if ( x >= 1740 and x <= 2040) and (y >= 900 and y <= 1200):
            try:
                self.drawpoint = [[1890, 1050], [1410, 1050]]
                if self.move_flag:
                    self.move_point = [750, 1050]
                    self.move_flag = False
                    self.move()
                if self.Button_IMU.text() == "Close":
                    self.Button_IMU.setText("Balance")
                self.drawpoint[0][0] = x
                self.drawpoint[0][1] = y
                self.update()
                self.attitude()
            except Exception as e:
                print(e)
        # In this condition we press the mouse button in the pane box
        if (x >= 1260 and x <= 1560) and (y >= 900 and y <= 1200):
            try:
                self.drawpoint = [[1890, 1050], [1410, 1050]]
                if self.move_flag:
                    self.move_point = [750, 1050]
                    self.move_flag = False
                    self.move()
                if self.Button_IMU.text() == "Close":
                    self.Button_IMU.setText("Balance")
                self.drawpoint[1][0] = x
                self.drawpoint[1][1] = y
                self.update()
                self.position()
            except Exception as e:
                print(e)
        # In this condition we press the mouse button int he movement box
        elif x >= 600 and x <= 900 and y >= 900 and y <= 1200:
            r = (x - 750) ** 2 + (1050 - y) ** 2
            self.drawpoint = [[1890, 1050], [1410, 1050]]
            if self.Button_IMU.text() == "Close":
                self.Button_IMU.setText("Balance")
            if r < 22500:
                self.move_flag = True
                self.move_point[0] = x
                self.move_point[1] = y
                self.move()
                self.update()
            else:
                x = x - 750
                y = 1050 - y
                angle = math.atan2(y, x)
                self.move_point[0] = 150 * math.cos(angle) + 750
                self.move_point[1] = 1050 - 150 * math.sin(angle)
                self.move()
                self.update()
        elif self.move_flag == True:
            x = x - 750
            y = 1050 - y
            angle = math.atan2(y, x)
            self.move_point[0] = 150 * math.cos(angle) + 750
            self.move_point[1] = 1050 - 150 * math.sin(angle)
            self.move()
            self.update()

    def mouseReleaseEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        # print(x,y)
        if self.move_flag:
            self.move_point = [750, 1050]
            self.move_flag = False
            self.move()
        self.update()

    def map(self, value, fromLow, fromHigh, toLow, toHigh):
        return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow

    def faceRecognition(self):
        try:
            if self.Button_Face_Recognition.text()=="Face Recog":
                self.client.fece_recognition_flag = True
                self.Button_Face_Recognition.setText("Close")
            elif self.Button_Face_Recognition.text() == "Close":
                self.client.fece_recognition_flag = False
                self.Button_Face_Recognition.setText("Face Recog")
        except Exception as e:
            print(e)

    def move(self):
        try:
            x = self.map((self.move_point[0]-750),0,150,0,35)
            y = self.map((1050 - self.move_point[1]),0,150,0,35)
            if self.action_flag == 1:
                angle = 0
            else:
                if x!=0 or y!=0:
                    angle=math.degrees(math.atan2(x,y))

                    if angle < -90 and angle >= -180:
                        angle=angle+360
                    if angle >= -90 and angle <=90:
                        angle = self.map(angle, -90, 90, -10, 10)
                    else:
                        angle = self.map(angle, 270, 90, 10, -10)
                else:
                    angle=0
            speed=self.client.move_speed
            command = cmd.CMD_MOVE+ "#"+str(self.gait_flag)+"#"+str(round(x))+"#"+str(round(y))\
                      +"#"+str(speed)+"#"+str(round(angle)) +'\n'
            self.label_move_value.setText(str((round(x), round(y))))
            print(command)
            self.client.send_data(command)
        except Exception as e:
            print(e)
    def relax(self):
        try:
            if self.Button_Relax.text() == "Relax":
                self.Button_Relax.setText("Relaxed")
                command = cmd.CMD_SERVOPOWER + "#" + "0" + '\n'
            else:
                self.Button_Relax.setText("Relax")
                command = cmd.CMD_SERVOPOWER + "#" + "1" + '\n'
            print(command)
            self.client.send_data(command)
        except Exception as e:
            print(e)

   #ATTACK
    def attack(self):
        try:
            if self.Button_Attack.text() == 'Attack':
                self.Button_Attack.setText('Attacking')
                command=cmd.CMD_ATTACK+'#1'+'\n'
                self.client.send_data(command)
            else:
                self.Button_Attack.setText('Attack')
                command=cmd.CMD_ATTACK+'#0'+'\n'
            print (command)
            self.client.send_data(command)
        except Exception as e:
            print(e)
    def posture(self, type):
        try:
            if type == 1:
                command=cmd.CMD_ATTACK+'#13'+'\n''#1'+'\n'
            elif type == 2:
                command=cmd.CMD_ATTACK+'#13'+'\n''#0'+'\n'
            elif type == 3:
                command=cmd.CMD_ATTACK+'#14'+'\n''#1'+'\n'
            elif type == 4:
                command=cmd.CMD_ATTACK+'#14'+'\n''#0'+'\n'
            elif type == 5:
                command=cmd.CMD_ATTACK+'#15'+'\n''#1'+'\n'
            elif type == 6:
                command=cmd.CMD_ATTACK+'#15'+'\n''#0'+'\n'



            print (command)
            self.client.send_data(command)
        except Exception as e:
            print(e)

    def attitude(self):
        r = self.map((self.drawpoint[0][0]-1890), -150, 150, -15, 15)
        p = self.map((1050-self.drawpoint[0][1]), -150, 150, -15, 15)
        y=self.slider_twist.value()
        # print("Tilt - r: " + str(round(r)) + ", p: " + str(round(p)) + ", z: " + str(round(y)))
        command = cmd.CMD_ATTITUDE+ "#" + str(round(r)) + "#" + str(round(p)) + "#" + str(round(y)) + '\n'
        print(command)
        self.client.send_data(command)
    def position(self):
        x = self.map((self.drawpoint[1][0]-1410), -150, 150, -40, 40)
        y = self.map((1050-self.drawpoint[1][1]), -150, 150, -40, 40)
        z=self.slider_height.value()
        # print("Position - x: " + str(round(x)) + ", y: " + str(round(y)) + ", z: " + str(round(z)))
        command = cmd.CMD_POSITION+ "#" + str(round(x)) + "#" + str(round(y)) + "#" + str(round(z)) + '\n'
        print(command)
        self.client.send_data(command)
    def closeEvent(self,event):
        try:
            self.timer.stop()
            self.timer_power.stop()
        except Exception as e:
            print(e)
        try:
            stop_thread(self.videoThread)
        except Exception as e:
            print(e)
        try:
            stop_thread(self.instructionThread)
        except Exception as e:
            print(e)
        self.client.turn_off_client()
        QCoreApplication.instance().quit()
        #os._exit(0)

    def restriction(self,var,v_min,v_max):
        if var < v_min:
            return v_min
        elif var > v_max:
            return v_max
        else:
            return var

    def video(self):
        if self.Button_Video.text() == 'Open Video':
            self.timer.start(10)
            self.Button_Video.setText('Close Video')
        else:
            self.timer.stop()
            self.Button_Video.setText('Open Video')

    def power(self):
        try:
            command = cmd.CMD_POWER + '\n'
            self.client.send_data(command)
            self.progress_Power1.setFormat(str(self.power_value[0])+"V")
            self.progress_Power2.setFormat(str(self.power_value[1]) + "V")
            self.progress_Power1.setValue(self.restriction(round((float(self.power_value[0]) - 5.00) / 3.40 * 100), 0, 100))
            self.progress_Power2.setValue(self.restriction(round((float(self.power_value[1]) - 7.00) / 1.40 * 100), 0, 100))
            #print (command)
        except Exception as e:
            print(e)

    def receive_instruction(self,ip):
        try:
            self.client.client_socket1.connect((ip,5002))
            self.client.tcp_flag=True
            print ("Connecttion Successful !")
        except Exception as e:
            print ("Connect to server Faild!: Server IP is right? Server is opend?")
            self.client.tcp_flag=False
        while True:
            try:
                alldata=self.client.receive_data()
            except:
                self.client.tcp_flag=False
                break
            #print(alldata)
            if alldata=='':
                break
            else:
                cmdArray=alldata.split('\n')
                #print(cmdArray)
                if cmdArray[-1] !="":
                    cmdArray==cmdArray[:-1]
            for oneCmd in cmdArray:
                data=oneCmd.split("#")
                print(data)
                if data=="":
                    self.client.tcp_flag=False
                    break
                elif data[0]==cmd.CMD_SONIC:
                    self.label_sonic.setText('Obstacle:'+data[1]+'cm')
                elif data[0]==cmd.CMD_POWER:
                    try:
                        if len(data)==3:
                            self.power_value[0] = data[1]
                            self.power_value[1] = data[2]

                    except Exception as e:
                        print(e)

    #CONNECT
    def connect(self):
        try:
            file=open('IP.txt','w')
            file.write(self.lineEdit_IP_Adress.text())
            file.close()
            if self.Button_Connect.text()=='Connect':
                self.IP = self.lineEdit_IP_Adress.text()
                self.client.turn_on_client(self.IP)
                self.videoThread=threading.Thread(target=self.client.receiving_video,args=(self.IP,))
                self.instructionThread=threading.Thread(target=self.receive_instruction,args=(self.IP,))
                self.videoThread.start()
                self.instructionThread.start()
                #self.face_thread = threading.Thread(target=self.client.face_recognition)
                #self.face_thread.start()
                self.Button_Connect.setText('Disconnect')
                #self.time_out.start(11000)
                self.timer_power.start(3000)
            else:
                try:
                    stop_thread(self.videoThread)
                except:
                    pass
                try:
                    stop_thread(self.instructionThread)
                except:
                    pass
                self.client.tcp_flag=False
                self.client.turn_off_client()
                self.Button_Connect.setText('Connect')
                self.timer_power.stop()
        except Exception as e:
            print(e)
    #Mode
    #actionMode
    def actionMode(self,mode):
        if mode.text() == "Turn":
            if mode.isChecked() == True:
                # print(mode.text())
                self.ButtonActionMode1.setChecked(False)
                self.ButtonActionMode2.setChecked(True)
                self.action_flag = 2
        elif mode.text() == "Strafe":
            if mode.isChecked() == True:
                # print(mode.text())
                self.ButtonActionMode1.setChecked(True)
                self.ButtonActionMode2.setChecked(False)
                self.action_flag = 1
    # gaitMode
    def gaitMode(self,mode):
        if mode.text() == "Walk":
            if mode.isChecked() == True:
                # print(mode.text())
                self.ButtonGaitMode1.setChecked(False)
                self.ButtonGaitMode2.setChecked(True)
                self.gait_flag = 2
        elif mode.text() == "Run":
            if mode.isChecked() == True:
                # print(mode.text())
                self.ButtonGaitMode1.setChecked(True)
                self.ButtonGaitMode2.setChecked(False)
                self.gait_flag = 1
    #Slider
    def speed(self):
        self.client.move_speed=str(self.slider_speed.value())
        self.label_speed.setText(str(self.slider_speed.value()))
    def setZ(self):
        self.label_height_value.setText(str(self.slider_height.value()))
        self.position()
    def setRoll(self):
        self.label_twist_value.setText(str(self.slider_twist.value()))
        self.attitude()
    def headUpAndDown(self):
        try:
            angle = str(self.slider_head.value())
            self.label_head.setText(angle)
            command = cmd.CMD_HEAD + "#" +"0" +"#"+angle + '\n'
            self.client.send_data(command)
            print(command)
        except Exception as e:
            print(e)
    def headLeftAndRight(self):
        try:
            angle = str(180-self.slider_head_1.value())
            self.label_head_1.setText(angle)
            command = cmd.CMD_HEAD + "#" +"1" +"#"+angle + '\n'
            self.client.send_data(command)
            print(command)
        except Exception as e:
            print(e)
    #BUZZER
    def buzzer(self):
        if self.Button_Buzzer.text() == 'Buzzer':
            command=cmd.CMD_BUZZER+'#1'+'\n'
            self.client.send_data(command)
            self.Button_Buzzer.setText('Noise')
            #print (command)
        else:
            command=cmd.CMD_BUZZER+'#0'+'\n'
            self.client.send_data(command)
            self.Button_Buzzer.setText('Buzzer')
            #print (command)

 

    #BALANCE
    def imu(self):
        if self.Button_IMU.text()=='Balance':
            command=cmd.CMD_BALANCE+'#1'+'\n'
            self.client.send_data(command)
            self.Button_IMU.setText("Close")
            #print (command)
        else:
            command=cmd.CMD_BALANCE+'#0'+'\n'
            self.client.send_data(command)
            self.Button_IMU.setText('Balance')
            #print (command)
    #SONIC
    def sonic(self):
        if self.Button_Sonic.text() == 'Sonar':
            self.timer_sonic.start(100)
            self.Button_Sonic.setText('Close')

        else:
            self.timer_sonic.stop()
            self.Button_Sonic.setText('Sonar')
            #
    def getSonicData(self):
        command=cmd.CMD_SONIC+'\n'
        self.client.send_data(command)
        #print (command)

    def showCalibrationWindow(self):
        command = cmd.CMD_CALIBRATION + '\n'
        self.client.send_data(command)
        self.calibrationWindow=calibrationWindow(self.client)
        self.calibrationWindow.setWindowModality(Qt.ApplicationModal)
        self.calibrationWindow.show()

    #LED
    def showLedWindow(self):
        try:
            self.ledWindow=ledWindow(self.client)
            self.ledWindow.setWindowModality(Qt.ApplicationModal)
            self.ledWindow.show()
        except Exception as e:
            print(e)

    # Face
    def showFaceWindow(self):
        try:
            self.faceWindow = faceWindow(self.client)
            self.faceWindow.setWindowModality(Qt.ApplicationModal)
            self.faceWindow.show()
            self.client.fece_id = True
        except Exception as e:
            print(e)

    def refresh_image(self):
        if self.client.video_flag == False:
            height, width, bytesPerComponent=self.client.image.shape
            #print (height, width, bytesPerComponent)
            cv2.cvtColor(self.client.image, cv2.COLOR_BGR2RGB, self.client.image)
            QImg = QImage(self.client.image.data.tobytes(), width, height, 3 * width, QImage.Format_RGB888)
            self.Video.setPixmap(QPixmap.fromImage(QImg))
            self.client.video_flag = True

class faceWindow(QMainWindow,Ui_Face):
    def __init__(self,client):
        super(faceWindow,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('Picture/logo_Mini.png'))
        self.Button_Read_Face.clicked.connect(self.readFace)
        self.client = client
        self.face_image=''
        self.photoCount=0
        self.timeout=0
        self.name = ''
        self.readFaceFlag=False
        # Timer
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.faceDetection)
        self.timer1.start(10)

        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.facePhoto)

    def closeEvent(self, event):
        self.timer1.stop()
        self.client.fece_id = False

    def readFace(self):
        try:
            if self.Button_Read_Face.text()=="Read Face":
                self.Button_Read_Face.setText("Reading")
                self.timer2.start(10)
                self.timeout=time.time()
            else:
                self.timer2.stop()
                if self.photoCount!=0:
                    self.Button_Read_Face.setText("Waiting ")
                    self.client.face.trainImage()
                    QMessageBox.information(self, "Message", "success", QMessageBox.Yes)
                self.Button_Read_Face.setText("Read Face")
                self.name = self.lineEdit.setText("")
                self.photoCount == 0
        except Exception as e:
            print(e)

    def facePhoto(self):
        try:
            if self.photoCount==30:
                self.photoCount==0
                self.timer2.stop()
                self.Button_Read_Face.setText("Waiting ")
                self.client.face.trainImage()
                QMessageBox.information(self, "Message", "success", QMessageBox.Yes)
                self.Button_Read_Face.setText("Read Face")
                self.name = self.lineEdit.setText("")
            if len(self.face_image)>0:
                self.name = self.lineEdit.text()
                if len(self.name) > 0:

                    height, width= self.face_image.shape[:2]
                    QImg = QImage(self.face_image.data.tobytes(), width, height,3 * width,QImage.Format_RGB888)
                    self.label_photo.setPixmap(QPixmap.fromImage(QImg))

                    second=int(time.time() - self.timeout)
                    if second > 1:
                        self.saveFcaePhoto()
                        self.timeout=time.time()
                    else:
                        self.Button_Read_Face.setText("Reading "+str(1-second)+"S   "+str(self.photoCount)+"/30")
                    self.face_image=''
                else:
                    QMessageBox.information(self, "Message", "Please enter your name", QMessageBox.Yes)
                    self.timer2.stop()
                    self.Button_Read_Face.setText("Read Face")
        except Exception as e:
            print(e)

    def saveFcaePhoto(self):
        cv2.cvtColor(self.face_image, cv2.COLOR_BGR2RGB, self.face_image)
        cv2.imwrite('Face/'+str(len(self.client.face.name))+'.jpg', self.face_image)
        self.client.face.name.append([str(len(self.client.face.name)),str(self.name)])
        self.client.face.Save_to_txt(self.client.face.name, 'Face/name')
        self.client.face.name = self.client.face.Read_from_txt('Face/name')
        self.photoCount += 1
        self.Button_Read_Face.setText("Reading "+str(0)+" S "+str(self.photoCount)+"/30")

    def faceDetection(self):
        try:
            if len(self.client.image)>0:
                gray = cv2.cvtColor(self.client.image, cv2.COLOR_BGR2GRAY)
                faces = self.client.face.detector.detectMultiScale(gray, 1.2, 5)
                if len(faces) > 0:
                    for (x, y, w, h) in faces:
                        self.face_image = self.client.image[y-5:y + h+5, x-5:x + w+5]
                        cv2.rectangle(self.client.image, (x-20, y-20), (x + w+20, y + h+20), (0, 255, 0), 2)
                if self.client.video_flag == False:
                    height, width, bytesPerComponent = self.client.image.shape
                    cv2.cvtColor(self.client.image, cv2.COLOR_BGR2RGB, self.client.image)
                    QImg = QImage(self.client.image.data.tobytes(), width, height, 3 * width, QImage.Format_RGB888)
                    self.label_video.setPixmap(QPixmap.fromImage(QImg))
                    self.client.video_flag = True
        except Exception as e:
            print(e)

class calibrationWindow(QMainWindow,Ui_calibration):
    def __init__(self,client):
        super(calibrationWindow,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('Picture/logo_Mini.png'))
        self.label_picture.setScaledContents (True)
        self.label_picture.setPixmap(QPixmap('Picture/Spider_calibration.png'))
        self.point=self.Read_from_txt('point')
        self.set_point(self.point)
        self.client=client
        self.leg='one'

        self.x=0
        self.y=0
        self.z=0

        self.radioButton_one.setChecked(True)
        self.radioButton_one.toggled.connect(lambda: self.leg_point(self.radioButton_one))
        self.radioButton_two.setChecked(False)
        self.radioButton_two.toggled.connect(lambda: self.leg_point(self.radioButton_two))
        self.radioButton_three.setChecked(False)
        self.radioButton_three.toggled.connect(lambda: self.leg_point(self.radioButton_three))
        self.radioButton_four.setChecked(False)
        self.radioButton_four.toggled.connect(lambda: self.leg_point(self.radioButton_four))
        self.radioButton_five.setChecked(False)
        self.radioButton_five.toggled.connect(lambda: self.leg_point(self.radioButton_five))
        self.radioButton_six.setChecked(False)
        self.radioButton_six.toggled.connect(lambda: self.leg_point(self.radioButton_six))

        self.Button_X1.clicked.connect(self.X1)
        self.Button_X2.clicked.connect(self.X2)
        self.Button_Y1.clicked.connect(self.Y1)
        self.Button_Y2.clicked.connect(self.Y2)
        self.Button_Z1.clicked.connect(self.Z1)
        self.Button_Z2.clicked.connect(self.Z2)

        self.Button_Save.clicked.connect(self.save)

    def X1(self):
        self.get_point()
        self.x += 1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        self.set_point()

    def X2(self):
        self.get_point()
        self.x -= 1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        self.set_point()

    def Y1(self):
        self.get_point()
        self.y += 1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        self.set_point()

    def Y2(self):
        self.get_point()
        self.y -= 1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        self.set_point()

    def Z1(self):
        self.get_point()
        self.z += 1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        self.set_point()

    def Z2(self):
        self.get_point()
        self.z -= 1
        command=cmd.CMD_CALIBRATION+'#'+self.leg+'#'+str(self.x)+'#'+str(self.y)+'#'+str(self.z)+'\n'
        self.client.send_data(command)
        self.set_point()

    def set_point(self,data=None):
        if data==None:
            if self.leg== "one":
                self.one_x.setText(str(self.x))
                self.one_y.setText(str(self.y))
                self.one_z.setText(str(self.z))
                self.point[0][0]=self.x
                self.point[0][1]=self.y
                self.point[0][2]=self.z
            elif self.leg== "two":
                self.two_x.setText(str(self.x))
                self.two_y.setText(str(self.y))
                self.two_z.setText(str(self.z))
                self.point[1][0]=self.x
                self.point[1][1]=self.y
                self.point[1][2]=self.z
            elif self.leg== "three":
                self.three_x.setText(str(self.x))
                self.three_y.setText(str(self.y))
                self.three_z.setText(str(self.z))
                self.point[2][0]=self.x
                self.point[2][1]=self.y
                self.point[2][2]=self.z
            elif self.leg== "four":
                self.four_x.setText(str(self.x))
                self.four_y.setText(str(self.y))
                self.four_z.setText(str(self.z))
                self.point[3][0]=self.x
                self.point[3][1]=self.y
                self.point[3][2]=self.z
            elif self.leg== "five":
                self.five_x.setText(str(self.x))
                self.five_y.setText(str(self.y))
                self.five_z.setText(str(self.z))
                self.point[4][0]=self.x
                self.point[4][1]=self.y
                self.point[4][2]=self.z
            elif self.leg== "six":
                self.six_x.setText(str(self.x))
                self.six_y.setText(str(self.y))
                self.six_z.setText(str(self.z))
                self.point[5][0]=self.x
                self.point[5][1]=self.y
                self.point[5][2]=self.z
        else:
            self.one_x.setText(str(data[0][0]))
            self.one_y.setText(str(data[0][1]))
            self.one_z.setText(str(data[0][2]))
            self.two_x.setText(str(data[1][0]))
            self.two_y.setText(str(data[1][1]))
            self.two_z.setText(str(data[1][2]))
            self.three_x.setText(str(data[2][0]))
            self.three_y.setText(str(data[2][1]))
            self.three_z.setText(str(data[2][2]))
            self.four_x.setText(str(data[3][0]))
            self.four_y.setText(str(data[3][1]))
            self.four_z.setText(str(data[3][2]))
            self.five_x.setText(str(data[4][0]))
            self.five_y.setText(str(data[4][1]))
            self.five_z.setText(str(data[4][2]))
            self.six_x.setText(str(data[5][0]))
            self.six_y.setText(str(data[5][1]))
            self.six_z.setText(str(data[5][2]))

    def get_point(self):
        if self.leg== "one":
            self.x = int(self.one_x.text())
            self.y = int(self.one_y.text())
            self.z = int(self.one_z.text())
        elif self.leg== "two":
            self.x = int(self.two_x.text())
            self.y = int(self.two_y.text())
            self.z = int(self.two_z.text())
        elif self.leg== "three":
            self.x = int(self.three_x.text())
            self.y = int(self.three_y.text())
            self.z = int(self.three_z.text())
        elif self.leg== "four":
            self.x = int(self.four_x.text())
            self.y = int(self.four_y.text())
            self.z = int(self.four_z.text())
        elif self.leg== "five":
            self.x = int(self.five_x.text())
            self.y = int(self.five_y.text())
            self.z = int(self.five_z.text())
        elif self.leg== "six":
            self.x = int(self.six_x.text())
            self.y = int(self.six_y.text())
            self.z = int(self.six_z.text())

    def save(self):
        command=cmd.CMD_CALIBRATION+'#'+'save'+'\n'
        self.client.send_data(command)

        self.point[0][0] = self.one_x.text()
        self.point[0][1] = self.one_y.text()
        self.point[0][2] = self.one_z.text()

        self.point[1][0] = self.two_x.text()
        self.point[1][1] = self.two_y.text()
        self.point[1][2] = self.two_z.text()

        self.point[2][0] = self.three_x.text()
        self.point[2][1] = self.three_y.text()
        self.point[2][2] = self.three_z.text()

        self.point[3][0] = self.four_x.text()
        self.point[3][1] = self.four_y.text()
        self.point[3][2] = self.four_z.text()

        self.point[4][0] = self.five_x.text()
        self.point[4][1] = self.five_y.text()
        self.point[4][2] = self.five_z.text()

        self.point[5][0] = self.six_x.text()
        self.point[5][1] = self.six_y.text()
        self.point[5][2] = self.six_z.text()

        self.Save_to_txt(self.point,'point')

        reply = QMessageBox.information(
            self,
            "Message",
            "Saved successfully",
            QMessageBox.Yes)
        #print(command)

    def Read_from_txt(self,filename):
        file1 = open(filename + ".txt", "r")
        list_row = file1.readlines()
        list_source = []
        for i in range(len(list_row)):
            column_list = list_row[i].strip().split("\t")
            list_source.append(column_list)
        for i in range(len(list_source)):
            for j in range(len(list_source[i])):
                list_source[i][j] = int(list_source[i][j])
        file1.close()
        return list_source

    def Save_to_txt(self,list, filename):
        file2 = open(filename + '.txt', 'w')
        for i in range(len(list)):
            for j in range(len(list[i])):
                file2.write(str(list[i][j]))
                file2.write('\t')
            file2.write('\n')
        file2.close()

    def leg_point(self,leg):
        if leg.text() == "One":
            if leg.isChecked() == True:
                self.leg = "one"
        elif leg.text() == "Two":
            if leg.isChecked() == True:
                self.leg = "two"
        elif leg.text() == "Three":
            if leg.isChecked() == True:
                self.leg = "three"
        elif leg.text() == "Four":
            if leg.isChecked() == True:
                self.leg = "four"
        elif leg.text() == "Five":
            if leg.isChecked() == True:
                self.leg = "five"
        elif leg.text() == "Six":
            if leg.isChecked() == True:
                self.leg = "six"

class ColorDialog(QtWidgets.QColorDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOptions(self.options() | QtWidgets.QColorDialog.DontUseNativeDialog)
        for children in self.findChildren(QtWidgets.QWidget):
            classname = children.metaObject().className()
            if classname not in ("QColorPicker", "QColorLuminancePicker"):
                children.hide()

class ledWindow(QMainWindow,Ui_led):
    def __init__(self,client):
        super(ledWindow,self).__init__()
        self.setupUi(self)
        self.client = client
        self.setWindowIcon(QIcon('Picture/logo_Mini.png'))
        self.hsl = [0, 0, 1]
        self.rgb = [0, 0, 0]
        self.dial_color.setRange(0, 360)
        self.dial_color.setNotchesVisible(True)
        self.dial_color.setWrapping(True)
        self.dial_color.setPageStep(10)
        self.dial_color.setNotchTarget(10)
        self.dial_color.valueChanged.connect(self.dialValueChanged)
        composite_2f = lambda f, g: lambda t: g(f(t))
        self.hsl_to_rgb255 = composite_2f(self.hsl_to_rgb01, self.rgb01_to_rgb255)
        self.hsl_to_rgbhex = composite_2f(self.hsl_to_rgb255, self.rgb255_to_rgbhex)
        self.rgb255_to_hsl = composite_2f(self.rgb255_to_rgb01, self.rgb01_to_hsl)
        self.rgbhex_to_hsl = composite_2f(self.rgbhex_to_rgb255, self.rgb255_to_hsl)
        self.colordialog = ColorDialog()
        self.colordialog.currentColorChanged.connect(self.onCurrentColorChanged)
        lay = QtWidgets.QVBoxLayout(self.widget)
        lay.addWidget(self.colordialog, alignment=QtCore.Qt.AlignCenter)

        self.pushButtonLightsOut.clicked.connect(self.lightsOut)
        self.radioButtonOne.setChecked(True)
        self.radioButtonOne.toggled.connect(lambda: self.ledMode(self.radioButtonOne))
        self.radioButtonTwo.setChecked(False)
        self.radioButtonTwo.toggled.connect(lambda: self.ledMode(self.radioButtonTwo))
        self.radioButtonThree.setChecked(False)
        self.radioButtonThree.toggled.connect(lambda: self.ledMode(self.radioButtonThree))
        self.radioButtonFour.setChecked(False)
        self.radioButtonFour.toggled.connect(lambda: self.ledMode(self.radioButtonFour))
        self.radioButtonFive.setChecked(False)
        self.radioButtonFive.toggled.connect(lambda: self.ledMode(self.radioButtonFive))

    def lightsOut(self):
        command = cmd.CMD_LED_MOD + '#' + '0' + '\n'
        self.client.send_data(command)
    def ledMode(self,index):
        if index.text() == "Mode 1":
            if index.isChecked() == True:
                command = cmd.CMD_LED_MOD + '#' + '1' + '\n'
                self.client.send_data(command)
        elif index.text() == "Mode 2":
            if index.isChecked() == True:
                command = cmd.CMD_LED_MOD + '#' + '2' + '\n'
                self.client.send_data(command)
        elif index.text() == "Mode 3":
            if index.isChecked() == True:
                command = cmd.CMD_LED_MOD + '#' + '3' + '\n'
                self.client.send_data(command)
        elif index.text() == "Mode 4":
            if index.isChecked() == True:
                command = cmd.CMD_LED_MOD + '#' + '4' + '\n'
                self.client.send_data(command)
        elif index.text() == "Mode 5":
            if index.isChecked() == True:
                command = cmd.CMD_LED_MOD + '#' + '5' + '\n'
                self.client.send_data(command)
    def mode1Color(self):
        if (self.radioButtonOne.isChecked() == True) or (self.radioButtonThree.isChecked() == True):
            command = cmd.CMD_LED + '#' + str(self.rgb[0]) + '#' + str(self.rgb[1]) + '#' + str(self.rgb[2]) + '\n'
            self.client.send_data(command)
    def onCurrentColorChanged(self, color):
        try:
            self.rgb = self.rgbhex_to_rgb255(color.name())
            self.hsl = self.rgb255_to_hsl(self.rgb)
            self.changeHSLText()
            self.changeRGBText()
            self.mode1Color()
            self.update()
        except Exception as e:
            print(e)

    def paintEvent(self, e):
        try:
            qp = QPainter()
            qp.begin(self)
            brush = QBrush(QColor(self.rgb[0], self.rgb[1], self.rgb[2]))
            qp.setBrush(brush)
            qp.drawRect(20, 10, 80, 30)
            qp.end()
        except Exception as e:
            print(e)

    def dialValueChanged(self):
        try:
            self.lineEdit_H.setText(str(self.dial_color.value()))
            self.changeHSL()
            self.hex = self.hsl_to_rgbhex((self.hsl[0], self.hsl[1], self.hsl[2]))
            self.rgb = self.rgbhex_to_rgb255(self.hex)
            self.changeRGBText()
            self.mode1Color()
            self.update()
        except Exception as e:
            print(e)

    def changeHSL(self):
        self.hsl[0] = float(self.lineEdit_H.text())
        self.hsl[1] = float(self.lineEdit_S.text())
        self.hsl[2] = float(self.lineEdit_L.text())

    def changeHSLText(self):
        self.lineEdit_H.setText(str(int(self.hsl[0])))
        self.lineEdit_S.setText(str(round(self.hsl[1], 1)))
        self.lineEdit_L.setText(str(round(self.hsl[2], 1)))

    def changeRGBText(self):
        self.lineEdit_R.setText(str(self.rgb[0]))
        self.lineEdit_G.setText(str(self.rgb[1]))
        self.lineEdit_B.setText(str(self.rgb[2]))

    def rgb255_to_rgbhex(self, rgb:np.array) -> str:
        f = lambda n: 0 if n < 0 else 255 if n > 255 else int(n)
        return '#%02x%02x%02x' % (f(rgb[0]), f(rgb[1]), f(rgb[2]))

    def rgbhex_to_rgb255(self, rgbhex: str) -> np.array:
        if rgbhex[0] == '#':
            rgbhex = rgbhex[1:]
        r = int(rgbhex[0:2], 16)
        g = int(rgbhex[2:4], 16)
        b = int(rgbhex[4:6], 16)
        return np.array((r, g, b))

    def rgb01_to_rgb255(self, rgb: np.array) -> np.array:
        return rgb * 255

    def rgb255_to_rgb01(self, rgb: np.array) -> np.array:
        return rgb / 255

    def rgb01_to_hsl(self, rgb: np.array) -> np.array:
        r, g, b = rgb
        lmin = min(r, g, b)
        lmax = max(r, g, b)
        if lmax == lmin:
            h = 0
        elif lmin == b:
            h = 60 + 60 * (g - r) / (lmax - lmin)
        elif lmin == r:
            h = 180 + 60 * (b - g) / (lmax - lmin)
        elif lmin == g:
            h = 300 + 60 * (r - b) / (lmax - lmin)
        else:
            h = 0
        s = lmax - lmin
        l = (lmax + lmin) / 2
        hsl = np.array((h, s, l))
        return hsl

    def hsl_to_rgb01(self, hsl: np.array) -> np.array:
        h, s, l = hsl
        lmin = l - s / 2
        lmax = l + s / 2
        ldif = lmax - lmin
        if h < 60:
            r, g, b = lmax, lmin + ldif * (0 + h) / 60, lmin
        elif h < 120:
            r, g, b = lmin + ldif * (120 - h) / 60, lmax, lmin
        elif h < 180:
            r, g, b = lmin, lmax, lmin + ldif * (h - 120) / 60
        elif h < 240:
            r, g, b = lmin, lmin + ldif * (240 - h) / 60, lmax
        elif h < 300:
            r, g, b = lmin + ldif * (h - 240) / 60, lmin, lmax
        else:
            r, g, b = lmax, lmin, lmin + ldif * (360 - h) / 60
        rgb = np.array((r, g, b))
        return rgb

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())

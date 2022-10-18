##  The author assumes no responsibility for the topicality, correctness, completeness or quality of
##  informa;on provided. Liability claims against the author which relate to material or immaterial
##  nature caused by the use or misuse of any informa;on provided through the use of incorrect or
##  incomplete information are excluded unless the author is not intenonal or grossly negligent
##  fault.


 
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
                             QMenu, QPushButton, QRadioButton, QHBoxLayout, QWidget, QSlider, QLabel, QLineEdit)

import serial
import time
import threading

class mfc_system(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.hbox = QGridLayout()
        
        ## slider initialization
        
        self.maxpt = 100
        
        ## slider initialization for setpoint 
        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setRange(0, self.maxpt)
        self.sld.setSingleStep(1)
        self.sld.valueChanged.connect(self.updateLabel1)
        
        ## slider initialization for range of flowrate 
        self.sld_2 = QSlider(Qt.Horizontal, self)
        self.sld_2.setRange(0, 6)
        self.sld_2.setTickInterval(10)
        self.sld_2.valueChanged.connect(self.updateLabel2)
        
        ## slider initialization for channel selection
        self.sld_3 = QSlider(Qt.Horizontal, self)
        self.sld_3.setRange(0, 3)
        self.sld_3.setPageStep(1)
        self.sld_3.valueChanged.connect(self.updateLabel3)
        ## slider initialization done 
        
        ## current value of sliders initialization
        self.cur_val_1 = QLabel('0', self)
        self.cur_val_1.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.cur_val_1.setMinimumWidth(80)
        
        self.cur_val_2 = QLabel('0', self)
        self.cur_val_2.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.cur_val_2.setMinimumWidth(80)
        
        self.cur_val_3 = QLabel('0', self)
        self.cur_val_3.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.cur_val_3.setMinimumWidth(80)
        
        ## current value of sliders initialization done 
                                    
        
        self.label_1 = QLabel("flowrate ",self)
        self.label_2 = QLabel("Range ", self)
        self.label_3 = QLabel("channel ", self)
        
        
        self.hbox.addWidget(self.label_1, 1, 0)
        self.hbox.addWidget(self.sld, 1, 1)
        self.hbox.addWidget(self.cur_val_1, 1, 2)
        
        self.hbox.addWidget(self.label_2, 2, 0)
        self.hbox.addWidget(self.sld_2, 2, 1)
        self.hbox.addWidget(self.cur_val_2, 2, 2)
        
        self.hbox.addWidget(self.label_3, 3, 0)
        self.hbox.addWidget(self.sld_3, 3, 1)
        self.hbox.addWidget(self.cur_val_3, 3, 2)
        
        ## Button to switch ON and OFF channel 1 to 4 respectively 
        self.ch1_e = QPushButton("ON")
        self.ch1_e.clicked.connect(self.ON_Ch1)
        
        self.ch1_d = QPushButton("OFF")
        self.ch1_d.clicked.connect(self.OFF_Ch1)
        
        self.ch2_e = QPushButton("ON")
        self.ch2_e.clicked.connect(self.ON_Ch2)
        
        self.ch2_d = QPushButton("OFF")
        self.ch2_d.clicked.connect(self.OFF_Ch2)
        
        self.ch3_e = QPushButton("ON")
        self.ch3_e.clicked.connect(self.ON_Ch3)
        
        self.ch3_d = QPushButton("OFF")
        self.ch3_d.clicked.connect(self.OFF_Ch3)
        
        self.ch4_e = QPushButton("ON")
        self.ch4_e.clicked.connect(self.ON_Ch4)
        
        self.ch4_d = QPushButton("OFF")
        self.ch4_d.clicked.connect(self.OFF_Ch4)
        
        ## Button to switch ON and OFF for all channel 
        self.switch_e = QPushButton("ON")
        self.switch_e.clicked.connect(self.ON_switch)
        
        self.switch_d = QPushButton("OFF")
        self.switch_d.clicked.connect(self.OFF_switch)
        
        self.ch1 = QLabel("Channel 1")
        self.ch2 = QLabel("Channel 2")
        self.ch3 = QLabel("Channel 3")
        self.ch4 = QLabel("Channel 4")
        self.sw = QLabel("Switch")
        
        self.dispx_1 = QLabel("flow rate=")
        self.dispy_1 = QLabel(" ")
        
        self.dispx_2 = QLabel("flow rate=")
        self.dispy_2 = QLabel(" ")
    
        self.dispx_3 = QLabel("flow rate=")
        self.dispy_3 = QLabel(" ")
        
        self.dispx_4 = QLabel("flow rate=")
        self.dispy_4 = QLabel(" ")
        
        self.hbox.addWidget(self.ch1, 1, 4)
        self.hbox.addWidget(self.ch1_e, 1, 5)
        self.hbox.addWidget(self.ch1_d, 1, 6)
        self.hbox.addWidget(self.dispx_1, 1, 7)
        self.hbox.addWidget(self.dispy_1, 1, 8)
        
        self.hbox.addWidget(self.ch2, 2, 4)
        self.hbox.addWidget(self.ch2_e, 2, 5)
        self.hbox.addWidget(self.ch2_d, 2, 6)
        self.hbox.addWidget(self.dispx_2, 2, 7)

        self.hbox.addWidget(self.dispy_2, 2, 8)

        
        self.hbox.addWidget(self.ch3, 3, 4)
        self.hbox.addWidget(self.ch3_e, 3, 5)
        self.hbox.addWidget(self.ch3_d, 3, 6)
        self.hbox.addWidget(self.dispx_3, 3, 7)

        self.hbox.addWidget(self.dispy_3, 3, 8)

        
        self.hbox.addWidget(self.ch4, 4, 4)
        self.hbox.addWidget(self.ch4_e, 4, 5)
        self.hbox.addWidget(self.ch4_d, 4, 6)
        self.hbox.addWidget(self.dispx_4, 4, 7)

        self.hbox.addWidget(self.dispy_4, 4, 8)
        
        self.hbox.addWidget(self.sw, 5, 4)
        self.hbox.addWidget(self.switch_e,5,5)
        self.hbox.addWidget(self.switch_d, 5, 6)
        
        
        self.label_mfc_port = QLabel('setting')
        
        self.accept = QLineEdit()
        
        self.confirm_mfc_port = QPushButton('confirm')
        self.confirm_mfc_port.clicked.connect(self.mfc_port)
        
        self.hbox.addWidget(self.label_mfc_port, 6,0)
        self.hbox.addWidget(self.accept,6,1)
        self.hbox.addWidget(self.confirm_mfc_port, 6,2)
        
        
        self.ser_mfc = ''
        

        self.ch1_d.setEnabled(False)
        self.ch2_d.setEnabled(False)
        self.ch3_d.setEnabled(False)
        self.ch4_d.setEnabled(False)
        
        self.ch = '1'
        self.cur = " "
        
        self.setGeometry(300, 300, 1000, 600)
        
        self.setLayout(self.hbox)
        self.setWindowTitle('QSlider')
        self.val_1 = 0
        self.constant = 0
        
    ## check your device manager which port your computer host has established gateway with the multi gas controller 
    def mfc_port(self):
        port = 'COM' + self.accept.text()
        
        ## the parity, stopbits and baudrate can be checked at option 6. 
        self.ser_mfc = serial.Serial(port, 9600, parity=serial.PARITY_ODD, stopbits = serial.STOPBITS_ONE)

    
    
    def ON_switch(self):
        self.ON(self.switch_e, self.switch_d, "0")

    def OFF_switch(self):
        self.OFF(self.switch_e, self.switch_d, "0")
        
    def ON(self, option_1, option_2, option_3):
        option_1.setEnabled(False)
        option_2.setEnabled(True)
        data_ON = "ON " + option_3 + "\r\n"
        try:
             self.ser_mfc.write(data_ON.encode())
        except:
            pass

    def OFF(self, option_1, option_2, option_3):
        option_1.setEnabled(True)
        option_2.setEnabled(False)
        data_OFF = "OF " + option_3 + "\r\n"
        try:
            self.ser_mfc.write(data_OFF.encode())
        except:
            pass
    ## function to switch ON channel 1 to 4 
    ###############################################################
    def ON_Ch1(self):
        self.ON(self.ch1_e, self.ch1_d, "1")
        
    def ON_Ch2(self):
        self.ON(self.ch2_e, self.ch2_d, "2")
        
    def ON_Ch3(self):
        self.ON(self.ch3_e, self.ch3_d, "3")
        
    def ON_Ch4(self):
        self.ON(self.ch4_e, self.ch4_d, "4")
    
    ## function to switch OFF channel 1 to 4 
    ################################################################
        
    def OFF_Ch1(self):
        self.OFF(self.ch1_e, self.ch1_d, "1")
    
    def OFF_Ch2(self):
        self.OFF(self.ch2_e, self.ch2_d, "2")
    
    def OFF_Ch3(self):
        self.OFF(self.ch3_e, self.ch3_d, "3")
    
    def OFF_Ch4(self):
        self.OFF(self.ch4_e, self.ch4_d, "4")

    #################################################################
    
    def thread_func(self, data):
        self.ser_mfc.write(data.encode())
        
        print(data)
        
    ## This function is to update the current set-point 
    def updateLabel1(self, value):
        self.cur_val_1.setText(str(value) + " sccm")
        self.val_1 = 0
        
        ## based on the function updateLabel3, if the user set to channel 3, this function will update the setpoint
        ## of channel 3 
        if self.ch == 1:
            self.dispy_1.setText(str(value) + " sccm")
        elif self.ch == 2:
            self.dispy_2.setText(str(value) + " sccm")
        elif self.ch == 3:
            self.dispy_3.setText(str(value) + " sccm")
        
        elif self.ch == 4:
            self.dispy_4.setText(str(value) + " sccm")
        
        data_range = "FS " + str(self.ch) + " " + str(value*self.constant) + "0\r\n"
        self.cur = data_range
        print(data_range)
        x = threading.Thread(target=self.thread_func, args=(self.cur,))
        x.start()
        
    ## This function is to update the range of flowrate 
    def updateLabel2(self, value):
        set_range_1 = [0, 1, 2, 3, 4, 5, 6]        ##    
        set_range_2 = [1, 2, 5, 10, 20, 50, 100]   ## The flow rate range of implementation is up till 100 sccm. 
        factor_conv = [80,40,20,10,5,2, 1]       ## factor to allow the user to set to his/her desired set point in 
                                                 ## a given range 
        for i in range(len(set_range_1)):        
            if value == set_range_1[i]:
                self.cur_val_2.setText(str(set_range_2[i]) + " sccm")
                self.sld.setRange(0, set_range_2[i])
                self.constant = factor_conv[i]
                
                ## the required command syntax
                ## RA 1 6  ->  set range of flowrate for channel 1 up till 100 sccm 
                data_range = "RA " + str(self.ch) + " "+ str(value) + "\r\n"  
                self.cur = data_range
                try:
                    x = threading.Thread(target=self.thread_func, args=(self.cur,)) 
                    x.start()
                    
                    ## the implementation of multi-threading in transmitting the serial command is to avoid the delay
                    ## response of (pyqt5) slider. 
                except:
                    pass 
                
    def updateLabel3(self, value):
        set_channel_1 = [0, 1, 2, 3]
        set_channel_2 = [1, 2, 3, 4]
        for i in range(len(set_channel_1)):
            if value == set_channel_1[i]:
                self.cur_val_3.setText(str(set_channel_2[i]) )
                self.ch = set_channel_2[i]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mfc_system()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pbtest.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import Mylib as prototool
import logging
import GlobalVar as cfg

global select_ssid, select_login_pass, select_root_pass

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(389, 316)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setSizeIncrement(QtCore.QSize(20, 20))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 301, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setSizeIncrement(QtCore.QSize(20, 0))
        self.label.setBaseSize(QtCore.QSize(10, 10))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.WiFiListBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.WiFiListBox.addItem("WiFiListBox")


        self.horizontalLayout.addWidget(self.WiFiListBox)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.FreshpB = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FreshpB.sizePolicy().hasHeightForWidth())
        self.FreshpB.setSizePolicy(sizePolicy)
        self.FreshpB.setObjectName("FreshpB")
        self.horizontalLayout.addWidget(self.FreshpB)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 70, 301, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.selectWiFiSSID = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.selectWiFiSSID.setObjectName("selectWiFiSSID")
        self.horizontalLayout_2.addWidget(self.selectWiFiSSID)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 200, 301, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(46, 15, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.PB_SN = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_SN.sizePolicy().hasHeightForWidth())
        self.PB_SN.setSizePolicy(sizePolicy)
        self.PB_SN.setAlignment(QtCore.Qt.AlignCenter)
        self.PB_SN.setObjectName("PB_SN")
        self.gridLayout.addWidget(self.PB_SN, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(46, 15, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(19, 0))
        self.label_3.setBaseSize(QtCore.QSize(20, 10))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(52, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        self.PB_MAC = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_MAC.sizePolicy().hasHeightForWidth())
        self.PB_MAC.setSizePolicy(sizePolicy)
        self.PB_MAC.setSizeIncrement(QtCore.QSize(1, 0))
        self.PB_MAC.setBaseSize(QtCore.QSize(0, 0))
        self.PB_MAC.setAlignment(QtCore.Qt.AlignCenter)
        self.PB_MAC.setObjectName("PB_MAC")
        self.gridLayout.addWidget(self.PB_MAC, 1, 3, 1, 1)
        self.PB_VER = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_VER.sizePolicy().hasHeightForWidth())
        self.PB_VER.setSizePolicy(sizePolicy)
        self.PB_VER.setSizeIncrement(QtCore.QSize(1, 0))
        self.PB_VER.setBaseSize(QtCore.QSize(0, 0))
        self.PB_VER.setAlignment(QtCore.Qt.AlignCenter)
        self.PB_VER.setObjectName("PB_VER")
        self.gridLayout.addWidget(self.PB_VER, 2, 3, 1, 1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 150, 301, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LinkWiFi = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LinkWiFi.sizePolicy().hasHeightForWidth())
        self.LinkWiFi.setSizePolicy(sizePolicy)
        self.LinkWiFi.setObjectName("LinkWiFi")
        self.horizontalLayout_3.addWidget(self.LinkWiFi)
        self.PullPowerBank = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PullPowerBank.sizePolicy().hasHeightForWidth())
        self.PullPowerBank.setSizePolicy(sizePolicy)
        self.PullPowerBank.setObjectName("PullPowerBank")
        self.horizontalLayout_3.addWidget(self.PullPowerBank)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 110, 301, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(38, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.selectWiFiPass = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.selectWiFiPass.setObjectName("selectWiFiPass")
        self.horizontalLayout_4.addWidget(self.selectWiFiPass)

        self.retranslateUi(Form)
        self.FreshpB.clicked.connect(self.Pb_getwifi)
        self.WiFiListBox.currentIndexChanged['QString'].connect(self.GetListBoxValue)
        self.LinkWiFi.clicked.connect(self.Connect_Wifi)
        self.PullPowerBank.clicked.connect(self.Getout_All_PowerBank)
        self.pushButton.clicked.connect(self.Get_Ver)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "美团1代充电宝管理软件"))
        self.label.setText(_translate("Form", "WiFi列表"))
        self.FreshpB.setText(_translate("Form", "刷新"))
        self.label_2.setText(_translate("Form", "当前选择的WiFi"))
        self.selectWiFiSSID.setText(_translate("Form", "SSID"))
        self.label_9.setText(_translate("Form", "软件版本"))
        self.label_4.setText(_translate("Form", "MAC地址"))
        self.PB_SN.setText(_translate("Form", "B00100100278"))
        self.label_3.setText(_translate("Form", "机柜SN"))
        self.PB_MAC.setText(_translate("Form", "MAC"))
        self.PB_VER.setText(_translate("Form", "V3.0"))
        self.LinkWiFi.setText(_translate("Form", "连接"))
        self.PullPowerBank.setText(_translate("Form", "弹出充电宝"))
        self.pushButton.setText(_translate("Form", "获取版本信息"))
        self.label_7.setText(_translate("Form", "登陆密码"))
        self.selectWiFiPass.setText(_translate("Form", "PASSWORD"))

    def Pb_getwifi(self):
        global wifi
        wifi_list=[]
        wifi = prototool.WiFi()
        wifi_dict = wifi.scan_wifi()
        for v in wifi_dict.values():
            if(v!=""):
                wifi_list.append(v)
        print(wifi_list)
        self.WiFiListBox.clear()
        self.WiFiListBox.addItems(wifi_list)
        #self.WiFiListBox.removeItem(0)


    def GetListBoxValue(self):
        global wifi
        global select_ssid, select_login_pass, select_root_pass
        select_ssid = self.WiFiListBox.currentText()
        select_login_pass,select_root_pass = wifi.get_wifi_pass(select_ssid)
        print("\n-------------------------------\n")
        print(" ssid %s|  login_pass %s |   root_pass %s " %(select_ssid,select_login_pass,select_root_pass))
        print("\n-------------------------------\n")
        self.selectWiFiSSID.setText(select_ssid)
        self.selectWiFiPass.setText(select_login_pass)
        sys_cfg.set_value("login_pass",select_login_pass)
        sys_cfg.set_value("root_pass", select_root_pass)

    def Connect_Wifi(self):
        global select_ssid, select_login_pass, select_root_pass
        status = wifi.connect_wifi(select_ssid,select_login_pass)
        host_ip =sys_cfg.get_value("host_ip")
        # 远程主机用户名
        username = sys_cfg.get_value("user_name")
        # 远程主机密码
        password = sys_cfg.get_value("root_pass")
        print(status)
        #status = wifi.connect_wifi(select_ssid, "bjj6485200")

    def Get_Ver(self):
        host_ip =sys_cfg.get_value("host_ip")
        # 远程主机用户名
        username = sys_cfg.get_value("user_name")
        # 远程主机密码
        password = sys_cfg.get_value("root_pass")
        # 要执行的shell命令；换成自己想要执行的命令
        # 自己使用ssh时，命令怎么敲的command参数就怎么写
        command1 = sys_cfg.get_value("cmd1")  #cmd1: mtdbg loan 1       get out all powerbank
        command2 = sys_cfg.get_value("cmd2")  #cmd2: cat /tmp/sys_info  get systerm info
        # 实例化
        my_ssh_client = prototool.proproMySshClient()
        # 登录，如果返回结果为1000，那么执行命令，然后退出
        if my_ssh_client.ssh_login(host_ip, username, password) == 1000:
            logging.warning(f"{host_ip}-login success, will execute command：{command2}")
            my_ssh_client.execute_some_command(command2)
            my_ssh_client.ssh_logout()
        pass

    def Getout_All_PowerBank(self):
        print("get all powerbank")
        host_ip =sys_cfg.get_value("host_ip")
        # 远程主机用户名
        username = sys_cfg.get_value("user_name")
        # 远程主机密码
        password = sys_cfg.get_value("root_pass")
        # 要执行的shell命令；换成自己想要执行的命令
        # 自己使用ssh时，命令怎么敲的command参数就怎么写
        command1 = sys_cfg.get_value("cmd1")  #cmd1: mtdbg loan 1       get out all powerbank
        command2 = sys_cfg.get_value("cmd2")  #cmd2: cat /tmp/sys_info  get systerm info
        # 实例化
        my_ssh_client = prototool.proproMySshClient()
        # 登录，如果返回结果为1000，那么执行命令，然后退出
        if my_ssh_client.ssh_login(host_ip, username, password) == 1000:
            logging.warning(f"{host_ip}-login success, will execute command：{command2}")
            my_ssh_client.execute_some_command(command1)
            res=my_ssh_client.execute_some_command(command2) #return response
            my_ssh_client.ssh_logout()
        pass

if __name__=="__main__":
    import sys
    global sys_cfg
    #Mywifi = prototool.WTen_WiFi()
    #Mywifi.Wifi_Scan()
    sys_cfg=cfg.GlobalConfig("config.yaml")
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
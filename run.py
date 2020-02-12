
from pbtest1 import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
global wifi
global select_ssid,select_login_pass,select_root_pass
class mywindow(QWidget,ui):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
    def Pb_getwifi(self):
        global wifi
        wifi = prototool.WiFi()
        wifi_dict = wifi.scan_wifi()
        for k,v in wifi_dict:
            self.WiFiListBox.AddItem(v)
            print("the"+k+"value is"+v)
    def GetListBoxValue(self):
        global wifi
        global select_ssid, select_login_pass, select_root_pass
        select_ssid = self.WiFiListBox.currentText()
        select_login_pass,select_root_pass = wifi.get_wifi_pass(select_ssid)
    def Connect_Wifi(self):
        global select_ssid, select_login_pass, select_root_pass
        status = wifi.connect_wifi(select_ssid,select_login_pass)
        


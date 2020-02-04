import time
import tkinter as tk
from pywifi import const, PyWiFi, Profile
import paramiko
from paramiko import AuthenticationException
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import NoValidConnectionsError
import logging
import hashlib

import yaml


class MySshClient():
    def __init__(self):
        self.ssh_client = SSHClient()

    # 此函数用于输入用户名密码登录主机
    def ssh_login(self, host_ip, username, password):
        try:
            # 设置允许连接known_hosts文件中的主机（默认连接不在known_hosts文件中的主机会拒绝连接抛出SSHException）
            self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
            self.ssh_client.connect(host_ip, port=22, username=username, password=password)
        except AuthenticationException:
            logging.warning('username or password error')
            return 1001
        except NoValidConnectionsError:
            logging.warning('connect time out')
            return 1002
        except:
            logging.warning('unknow error')
            print("Unexpected error:", sys.exc_info()[0])
            return 1003
        return 1000

    # 此函数用于执行command参数中的命令并打印命令执行结果
    def execute_some_command(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        print(stdout.read().decode())

    # 此函数用于退出登录
    def ssh_logout(self):
        logging.warning('will exit host')
        self.ssh_client.close()


class WiFi(object):
    # 创建对象自动初始化，类似Java的构造函数
    def __init__(self):
        wifi = PyWiFi()                     # 创建一个无线对象
        print(wifi.interfaces())
        self.iface = wifi.interfaces()[0]   # 获取当前机器第一个无线网卡

    # 查看wifi的连接状态
    def wifi_connect_status(self):
        """
        判断本机是否有无线网卡，以及连接状态
        :return:已连接或存在网卡返回1，否则返回0
        """
        ret_list = []
        # 判断是否连接成功
        if self.iface.status() in \
                [const.IFACE_CONNECTED, const.IFACE_CONNECTING, const.IFACE_INACTIVE]:
            return self.iface.name()        # 连接成功显示连接设备
        else:
            return "not connected!"        # 连接失败返回失败信息

    """
    扫描附近wifi
        乱码问题：
        把wifi_info.ssid重新编码为gb18030
        wifi_info.ssid.encode('raw_unicode_escape','strict').decode('gb18030')
        我也不清楚他为什么不全用unicode
        ssid出来应该是unicode  但是  你往profile里面写的时候  必须是gb18030
        所以这么一个操作
        你会发现gb18030在控制台和py的某些控件上输出是乱码  是因为 控制台是utf-8
        想在这上面输出中文的话你得encode('raw_unicode_escape','strict').decode()
    """
    def scan_wifi(self, scantime=5):
        """
        :param scantime:    指定扫描时间，默认扫描时间为5秒
        :return:            返回的是一个network dictionary,key=bssid,value=ssid
        """
        self.iface.scan()                                           # 扫描附近wifi
        time.sleep(scantime)
        basewifi = self.iface.scan_results()
        dict = {}
        for i in basewifi:
            dict[i.bssid] = \
                i.ssid.encode(encoding='raw_unicode_escape', errors='strict').decode()
        return dict
    def get_wifi_pass(self,wifi_ssid):
        tmp = "mt-ddgj12-6EFD"
        # tmp = hashlib.md5(tmp.encode('latin1')).hexdigest()

        for i in range(3):
            tmp = tmp + '\n'
            md5_obj = hashlib.md5() #need to every time new object
            md5_obj.update(tmp.encode('utf-8'))
            tmp = md5_obj.hexdigest()
        wifi_pass = tmp[0:7]
        root_pass = tmp[26:32]

        print(tmp)
        print(wifi_pass)
        print(root_pass)
        return wifi_pass,root_pass
    # 链接到指定wifi
    def connect_wifi(self, wifi_ssid, password):
        profile = Profile()                                         # 配置文件
        profile.ssid = wifi_ssid                                    # wifi名称
        profile.auth = const.AUTH_ALG_OPEN                          # 需要密码
        profile.akm.append(const.AKM_TYPE_WPA2PSK)                  # 加密类型
        profile.cipher = const.CIPHER_TYPE_CCMP                     # 加密单元
        profile.key = password                                      # wifi密码

        self.iface.remove_all_network_profiles()                    # 删除其他配置
        tmp_profile = self.iface.add_network_profile(profile)       # 加载配置

        self.iface.connect(tmp_profile)                             # link start
        time.sleep(10)                                              # 尝试10s是否成功
        isok = True
        if self.iface.status() == const.IFACE_CONNECTED:
            return isok                                             # 连接成功
        else:
            isok = False                                            # 连接失败设置isok = False
        self.iface.disconnect()                                     # 避免超时后连接成功手动断开一下，因为在一定时间内连接失败用户会继续重试连接
        time.sleep(1)
        return isok
    def Get_Param(self):
        yamlPath = "config.xml"
        f = open(yamlPath, 'r', encoding='utf-8')
#if __name__ == "__main__":

#    wifi = WiFi()
#    wifi.get_wifi_pass(wifi_ssid="mt-ddgj12-6EFD")
    # print(wifi.wifi_connect_status())
    # print(wifi.scan_wifi())
    # print(wifi.connect_wifi(r"mt7628-B7E1", r"ddgj1234"))
    # 远程主机IP
    # host_ip = '192.168.29.1'
    # # 远程主机用户名
    # username = 'root'
    # # 远程主机密码
    # password = 'ddgj12'
    # # 要执行的shell命令；换成自己想要执行的命令
    # # 自己使用ssh时，命令怎么敲的command参数就怎么写
    # command = 'mtdbg loan 1'
    # command1 = 'cat /tmp/sys_info'
    # # 实例化
    # my_ssh_client = MySshClient()
    # # 登录，如果返回结果为1000，那么执行命令，然后退出
    # if my_ssh_client.ssh_login(host_ip, username, password) == 1000:
    #     logging.warning(f"{host_ip}-login success, will execute command：{command}")
    #     #my_ssh_client.execute_some_command(command)
    #     my_ssh_client.execute_some_command(command1)
    #     my_ssh_client.ssh_logout()
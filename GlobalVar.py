# -*- coding: utf-8 -*-
import yaml
import os
class GlobalConfig(object):
    def __init__(self,cfgname):#初始化
        global _global_dict
        _global_dict = {}
        self.config_name=cfgname
        print(cfgname)
    def set_value(self,key,value):
        """ 定义一个全局变量 """
        self._global_dict[key] = value

    def get_value(self,key,defValue=None):
        try:
            return self._global_dict[key]
        except KeyError:
            return defValue

    def get_conf(self):
        curPath = os.path.dirname(os.path.realpath(__file__))
            # 获取yaml文件路径
        yamlPath = os.path.join(curPath, self.config_name)
        print(yamlPath)
        # open方法打开直接读出来
        f = open(yamlPath, 'r', encoding='utf-8')
        cfg = f.read()
        # print(type(cfg))  # 读出来是字符串
        #print(cfg)
        conf_dict = yaml.load(cfg)  # 用load方法转字典
        #print(conf_dict)

        return conf_dict
    def load_globalVar(self):
        dict=self.get_conf()
        for i in dict:
            self.set_value(i,dict[i])
            print("has set %s value is %s" %(i,dict[i]))

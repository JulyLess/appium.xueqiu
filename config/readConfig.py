import os
import sys
import configparser
import codecs

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir,'config.ini')

class readConfig:
    def __init__(self):
        with open (configPath) as fp:
            data = fp.read()

        if data[:3] ==codecs.BOM_UTF8:
            data = data [3:]
            file = codecs.open(configPath,'w')
            file.write(data)
            file.close()
        fp.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_Desired_caps(self,name):
        values = self.cf.get("Desired_caps",name)
        return values

    def get_URL(self,name):
        values = self.cf.get("Http",name)
        return values


if __name__ =="__main__":
    operation = readConfig()
    a = operation.get_Desired_caps("platformName")
    print(a)

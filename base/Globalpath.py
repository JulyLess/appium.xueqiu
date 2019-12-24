import os,sys

proDir = os.path.dirname(os.path.abspath(__file__)) #返回文件路径
sys.path.append(proDir)

#yaml配置路径文件
yamlPath = os.path.join(proDir,'conf','driver_config.yaml')

# 🐱🐕分类的简单实现
基于tensorflow的猫狗分类的简单实现


## 环境配置
    1.conda create --name <yourenvname> python==3.9  #创建python版本为3.9的conda环境
    2.conda activate <yourenvname>  #进入到你的环境之中
    3.pip install matplotlib==3.9.4 numpy==2.0.2 tensorflow==2.19.0

## 更改文件路径
    在你运行代码之前，你需要手动更改mkdir.py和prepro.py中的文件路径，使其指向你的实际文件路径

## 下载相应的数据集
    1.从百度网盘下载相应的数据集通过网盘分享的文件：dogs-vs-cats-train1.zip链接: https://pan.baidu.com/s/1DWx-1MlE9O0uWMZzh7mCLA?pwd=h9c8 提取码: h9c8
    2.解压后将其放置于项目文件夹下

## 运行代码
    1.cd + 项目路径
    2.python mkdir.py  #生成训练，测试，验证三个数据集
    3.python train.py  #开始训练

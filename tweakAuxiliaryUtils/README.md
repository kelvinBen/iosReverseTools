# tweakAuxiliaryUtils.py 
### 项目背景:

在使用Monkey的时候往往需要先使用class-dump工具dump出头文件，然后使用logify.pl工具生成Tweak.xm文件(即初始hook代码),经过这一系列的操作还是比较费时的。现在你只需要使用tweakAuxiliaryUtils.py 工具你就可以一键生成你想要的Tweak.xm文件了。

### 项目简介:

tweakAuxiliaryUtils.py采用python3语音进行开发，基于正则表达式以及常用命令行快速生成指定关键字的tweak.xm文件。

### 使用方法:

#### 有环境变量的写法：

```
python tweakAuxiliaryUtils.py -b ipa文件或者砸壳后的二进制文件 -d h头文件存放位置 -x tweak.xm文件存放位置
```
##### 例子：

```
python tweakAuxiliaryUtils.py -b ~/Desktop/weixin.ipa -d ~/Desktop/h -x ~/Desktop/tweak.xml
```


#### 无环境变量的写法：

```
python tweakAuxiliaryUtils.py -b ipa文件或者砸壳后的二进制文件 -d h头文件存放位置 -c 指定class-dump所在目录 -p 需要生成tweak.xm文件内容的正则表达式 -l 指定logify.pl所在目录 -x tweak.xm文件存放位置
```
##### 例子：

```
python tweakAuxiliaryUtils.py -b ~/Desktop/weixin.ipa -d ~/Desktop/h -c /opt/class-dump -p /opt/tweak.xm -l /opt/logify.pl -x ~/Desktop/tweak.xml
```

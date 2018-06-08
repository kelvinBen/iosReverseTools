# iosReverseTools是ios逆向渗透测试辅助工具集合

### [tweakAuxiliaryUtils.py ](https://github.com/kelvinBen/iosReverseTools/tree/master/tweakAuxiliaryUtils)

项目背景:

在使用Monkey的时候往往需要先使用class-dump工具dump出头文件，然后使用logify.pl工具生成Tweak.xm文件(即初始hook代码),经过这一系列的操作还是比较费时的。现在你只需要使用tweakAuxiliaryUtils.py 工具你就可以一键生成你想要的Tweak.xm文件了。

### [otoolTest.sh](https://github.com/kelvinBen/iosReverseTools/tree/master/otoolTest)

项目背景：

在做iOS渗透测试的时候经常需要使用otool对ipa的二进制文件进行静态检测，每次需要输入多次命令，此工具(otoolTest.sh)的目的在于简化输入命令的次数。

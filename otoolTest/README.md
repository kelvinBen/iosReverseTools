### [otoolTest.sh](https://github.com/kelvinBen/iosReverseTools/tree/master/otoolTest)

#### 项目背景：

在做iOS渗透测试的时候经常需要使用otool对ipa的二进制文件进行静态检测，每次需要输入多次命令，此工具(otoolTest.sh)的目的在于简化输入命令的次数。

#### 项目简介:

本工具可以做iOS的地址随机化检测、堆栈保护检测、自动引用计数检测等检测项。

#### 使用方法:
前提条件: Mac OS操作系统，并安装Xcode工具


```
1. chmod +x ./otoolTest.sh
2. ./otoolTest.sh ipa的二进制文件
```
例子:

```
1. chmod +x ./otoolTest.sh
2. ./otoolTest.sh ~/Desktop/wexin/PayLoad/weixinApp/weixinApp
```

#### 输出结果解析:

- 输出结果中包含PIE说明该ipa采用了地址随机进行打包

- 输出结果中包含_objc_release说明该ipa采用了堆栈保护进行打包

- 输出结果中包含___stack_chk_guard说明该ipa采用了自动引用计数进行打包

#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import re
import pathlib
import argparse
import shutil

'''
tweak辅助工具类
项目背景:
    在使用Monkey的时候往往需要先使用class-dump工具dump出头文件，然后使用logify.pl工具生成Tweak.xm文件(即初始hook代码),经过这一系列的操作还是比较费时的。现在你只需要使用tweakAuxiliaryUtils.py 工具你就可以一键生成你想要的Tweak.xm文件了。
简介：
    tweakAuxiliaryUtils.py采用python3语音进行开发，基于正则表达式以及常用命令行快速生成指定关键字的tweak.xm文件
'''
class TweakAuxiliaryUtils:

    '''
    将头文件dump到指定目录
    参数说明：
      headerOutDir: dump出.h文件存放目录
      binaryFilePath: ipa的二进制文件
      xmFileOutPath: teeak.xm存放路径
      classDumpPath: class-dump所在目录
      logifyPath:  logify.pl所在目录
      pattern: 正则匹配检索的关键字
    '''
    def classDumpHeader(self, headerOutDir, binaryFilePath, xmFileOutPath, classDumpPath, logifyPath, pattern):
        xmFilePath = pathlib.Path(xmFileOutPath)
        if xmFilePath.exists() and xmFilePath.is_file():
            os.remove(xmFileOutPath)

        headerOutPath = pathlib.Path(headerOutDir)
        if headerOutPath.exists() and headerOutPath.is_dir():
            shutil.rmtree(headerOutPath)

        print(binaryFilePath,'---',headerOutDir)
        ol = '"%s" -H "%s" -o "%s"' % (classDumpPath, binaryFilePath, headerOutDir)
        if os.system(ol) == 0:
            self.getHeaderFile(headerOutDir, xmFileOutPath, logifyPath, pattern)

    ''' 
    获取头文件
    参数说明：
       headerFileDir：dump出.h文件存放目录
       logifyPath： logify.pl所在目录
       pattern： 正则匹配检索的关键字
       xmFileOutPath：teeak.xm存放路径
    '''
    def getHeaderFile(self, headerFileDir, xmFileOutPath, logifyPath, pattern):
        if os.path.isdir(headerFileDir):
            for headerFile in os.listdir(headerFileDir):
                headerFileStr = os.path.join(headerFileDir, headerFile)
                self.analyzeHeaderFile(headerFileStr, logifyPath, pattern, xmFileOutPath)
                if os.path.isdir(headerFile):
                    self.getHeaderFile(headerFile)
        else:
            print(headerFileDir, " is not a directory!")


    '''
    正则解析头文件
    参数说明：
      headerFileDir: dump出.h文件存放目录
      xmFileOutPath: teeak.xm存放路径
      logifyPath:  logify.pl所在目录
      pattern: 正则匹配检索的关键字
    '''
    def analyzeHeaderFile(self, headerFileDir, logifyPath, pattern, xmFileOutPath):
        openHeaderFile = open(headerFileDir)
        try:
            headerFileContent = openHeaderFile.read()
            result = re.search(pattern, headerFileContent)
            if result:
                self.createXMSuffixFile(openHeaderFile.name, logifyPath, xmFileOutPath)
        finally:
            openHeaderFile.close()

    '''
     生成teeak.xm文件
     参数说明：
       headerFile: h文件
       xmFileOutPath: teeak.xm存放路径
       logifyPath:  logify.pl所在目录
    '''
    def createXMSuffixFile(self, headerFile, logifyPath, xmFileOutPath):
        ol = '"%s" "%s" >>  "%s"' %(logifyPath, headerFile, xmFileOutPath)
        os.system(ol)

if __name__ == "__main__":
    binaryFilePath = None
    headerFileDir = None

    parser = argparse.ArgumentParser(prog='TweakAuxiliaryUtils', description='此工具类用于快速生成指定tweak文件', prefix_chars='-')
    parser.add_argument('-b', dest="binary_file_path", required=True, type=str, help='ipa的二进制文件')
    parser.add_argument('-d', dest="header_file_dir", required=True, type=str, help='dump出的.h文件存放目录')
    parser.add_argument('-c', dest="class_dump_path", default='class-dump', type=str, help='class-dump所在目录')
    parser.add_argument('-p', dest="pattern", default='crypt', type=str, help='正则匹配检索的关键字')
    parser.add_argument('-l', dest="logify_path", default='logify.pl', type=str, help='logify.pl所在目录')
    parser.add_argument('-x', dest="xm_file_out_path", default='~/Desktop/tweak.xm', type=str, help='teeak.xm存放路径')

    args = parser.parse_args()
    if args.binary_file_path:
        binaryFilePath = args.binary_file_path

    if args.header_file_dir:
        headerFileDir = args.header_file_dir

    print(args.class_dump_path)

    tau = TweakAuxiliaryUtils()
    tau.classDumpHeader(headerFileDir, binaryFilePath, args.xm_file_out_path, args.class_dump_path,  args.logify_path, args.pattern)

#!/bin/bash

usage(){
	echo -e "Erroe:" $errorInfo
	echo -e "Usage: $0 <Object file>"
	exit 1
}

if [ ! -n "$1" ];then
	errorInfo="请填写参数"
	usage $errorInfo
fi

echo "======* 地址随机化检测 *======"
otool -hv "$1" 
echo "======* 堆栈保护检测 *======"
otool -Iv "$1" | grep objc_release
echo "======* 自动引用计数检测 *======"
otool -Iv "$1" | grep stack_chk_guard

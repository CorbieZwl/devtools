#!/bin/zsh
# 复制到对应到目录下 生成python虚拟环境
# pydevenv
env_path="/pydevenv"
root_path=`pwd`
echo $root_path$env_path
virenv_path=$root_path$env_path
echo $virenv_path
virtualenv $virenv_path

# 进入环境 方式:source pydevenv/bin/activat
# 退出环境 deactivate
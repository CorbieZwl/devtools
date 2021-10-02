#!/usr/bin/python
# coding:utf-8
'''
生成虚拟环境配置参数
复制到项目虚拟环境目录下执行

@author：zwl
@email：1057926872@qq.com
'''

import os
import time
import re

"""
export WORKON_HOME='/Users/你的用户名/Documents/python_envs'
# 上面是我想创建的地址的位置 可根据自己的需要调整
export VIRTUALENVWRAPPER_PYTHON='/usr/local/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh
"""
TS_PATH = os.getcwd()
PYTHON_ENV = "python3"
# 环境变量文件
ENVIRONMENT_VARIABLE_FILE = "~/.bash_profile"
# 文件名
file_name = "add_args.sh"


def get_this_virtualenv_args():
    """
    获取当前目录env参数
    :return:
    """
    line1 = """export WORKON_HOME='{}'\n""".format(TS_PATH)
    line2 = """export VIRTUALENVWRAPPER_PYTHON='/usr/local/bin/{}'\n""".format(PYTHON_ENV)
    line3 = """source /usr/local/bin/virtualenvwrapper.sh\n"""

    add_args = line1+line2+line3
    return add_args

def copy_file_topath(filepath,topath=""):
    """
    复制文件到指定目录 生成备份文件
    :param filepath: 目标文件路径
    :param topath: 指定目录路径
    :return:
    """
    if not topath:
        topath = re.findall(".*/", filepath)[0]
    else:
        if topath[-1] != "/":
            topath += "/"
    tofile_name = filepath.split("/")[-1]
    tofilepath = topath+tofile_name+".bak"

    if os.path.exists(topath) == False and topath != "~/":
        raise Exception("目录不存在")
    print("cp {} {}".format(filepath,tofilepath))
    # os.system("cp {} {}".format(filepath,tofilepath))




def main():
    """
    入口函数
    """
    print("该脚本会在当前目录生成参数shell文件")
    print("需要将shell文件中的参数加入到~/.bash_profile中")
    print("脚本支持自动将参数添加到~/.bash_profile")
    print("若选择自动添加,会在~/.bash_profile同级目录生成备份(~/.bash_profile.bak)")
    print("若出现异常,可用备份文件恢复bash_profile")
    time.sleep(1)
    # user_input = str(input("是否自动写入~/.bash_profile(输入1确认,除1外任意值):"))

    add_args = get_this_virtualenv_args()

    add_args_b = add_args.encode(encoding="utf-8")

    with open("./{}".format(file_name),"wb") as f:
        f.write(add_args_b)
    print("生成成功")
    #
    # if user_input == "1":
    #     # 备份文件
    #     copy_file_topath(ENVIRONMENT_VARIABLE_FILE)
    #
    #     print("cat ./{} >> {}".format(file_name,ENVIRONMENT_VARIABLE_FILE))
    #     os.system("cat ./{} >> {}".format(file_name,ENVIRONMENT_VARIABLE_FILE))
    #
    #     print("source {}".format(ENVIRONMENT_VARIABLE_FILE))
    #     print(os.system("source {}".format(ENVIRONMENT_VARIABLE_FILE)))

    return "执行完毕"


# TODO 检测是否存在 需要优化


if __name__ == '__main__':
    try:
        print(main())
    except KeyboardInterrupt:
        print("\n进程结束...")
    # env_content = os.system("cat {}".format(ENVIRONMENT_VARIABLE_FILE))
    # print(env_content)

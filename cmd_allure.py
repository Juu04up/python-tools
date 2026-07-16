# 1. 导包
import os

# 2. 配置cmd下执行命令（生成allure执行命令）
# 把这里改成你实际的 allure.exe 完整路径
run_cmd = r".\allure-2.27.0\bin\allure generate ./report -o ./new_report --clean"
# 通过os.system(命令)方法运行终端命令（相当于在终端运行上述命令）
os.system(run_cmd)
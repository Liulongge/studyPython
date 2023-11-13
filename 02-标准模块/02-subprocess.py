import subprocess

# 执行系统命令
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
# 获取命令的输出
output = result.stdout
print(output)


# 不通过shell执行命令并使用管道
command1 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
# 获取命令2的输出
output = command1.communicate()[0]
# 打印输出结果
print(output.decode())


subprocess.call(['ls','-la'])


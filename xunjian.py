import paramiko
import time


def device_connect(ip, username, password):
    """连接设备并返回 SSH 客户端"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=ip, username=username, password=password)
        return ssh
    except Exception as e:
        print(f"连接 {ip} 失败：{str(e)}")
        return None


def execute_commands(ssh, cmds, ip):
    """在设备上执行命令并记录结果"""
    command = ssh.invoke_shell()
    time.sleep(3)
    command.send('N\n')  # 非必须命令
    command.send('screen-length 0 temporary\n')  # 取消分屏显示

    log_file = f"d:\\Python\\xunjian\\{ip}.txt"
    start_time = time.strftime('%Y-%m-%d %T')
    end_time = time.strftime('%Y-%m-%d %T')

    with open(log_file, 'a') as log:
        log.write(f"巡检开始时间：{start_time}\n\n")

        for cmd in cmds:
            command.send(cmd + '\n')
            time.sleep(5)
            output = command.recv(65535).decode()
            log.write(output + '\n\n')

        log.write(f"巡检结束时间：{end_time}\n")


def main():
    dev_filepath = r"d:\\Python\\xunjian\\device_info.txt"
    cmd_filepath = r"d:\\Python\\xunjian\\cmd.txt"

    # 读取命令
    with open(cmd_filepath, 'r') as cmd_file:
        cmds = cmd_file.readlines()

    # 读取设备信息
    with open(dev_filepath, 'r') as dev_file:
        while True:
            dev_info = dev_file.readline()
            if not dev_info:
                break
            devs = dev_info.split(',')
            ip = devs[0]
            username = devs[1]
            password = devs[2].strip()

            ssh = device_connect(ip, username, password)
            if ssh:
                execute_commands(ssh, cmds, ip)
                ssh.close()
                print(f"成功连接并执行命令到 {ip}")


if __name__ == "__main__":
    main()
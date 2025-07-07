import paramiko
import time
import os


def device_connect(ip, username, password):
    """连接设备并返回SSH客户端"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=ip,
                    username=username,
                    password=password,
                    look_for_keys=False)
        return ssh
    except Exception as e:
        print(f"连接 {ip} 失败：{str(e)}")
        return None


def restore_config(ssh, ip, backup_dir):
    """执行还原操作"""
    backup_file = os.path.join(backup_dir, f"{ip}_config.cfg")

    if not os.path.exists(backup_file):
        print(f"找不到备份文件：{backup_file}")
        return

    # 读取备份配置
    with open(backup_file) as f:
        config_commands = [line.strip() for line in f if line.strip()]

    # 获取交互式shell
    channel = ssh.invoke_shell()

    # 进入系统视图
    channel.send("system-view\n")
    time.sleep(1)

    # 逐条发送配置命令
    for cmd in config_commands:
        channel.send(f"{cmd}\n")
        time.sleep(0.5)

    # 保存配置
    time.sleep(1)
    channel.send("return\n")  # 退出系统视图
    time.sleep(0.5)
    channel.send("save\n")  # 执行保存命令
    time.sleep(1)
    channel.send("Y\n")  # 确认保存
    time.sleep(1)
    channel.send("\n")  # 确认文件名
    time.sleep(2)

    print(f"{ip} 配置还原完成")


def main():
    devices_file = r"D:\Python\xunjian\device_info.txt"
    backup_directory = r"D:\Python\xunjian\backup_configs"

    # 读取设备信息
    with open(devices_file) as f:
        devices = [line.strip().split(",") for line in f]

    # 遍历所有设备进行还原
    for ip, username, password in devices:
        print(f"正在还原 {ip}...")
        ssh_client = device_connect(ip, username, password)
        if ssh_client:
            restore_config(ssh_client, ip, backup_directory)
            ssh_client.close()


if __name__ == "__main__":
    main()
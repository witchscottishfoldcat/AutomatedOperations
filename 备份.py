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


def backup_config(ssh, ip, backup_dir):
    """执行备份操作"""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_path = os.path.join(backup_dir, f"{ip}_config.cfg")

    # 获取交互式shell
    channel = ssh.invoke_shell()

    # 发送备份命令
    channel.send("screen-length 0 temporary\n")  # 禁用分页
    time.sleep(1)
    channel.send("display current-configuration\n")

    # 等待配置输出完成（根据实际情况调整等待时间）
    time.sleep(8)

    # 读取配置输出
    config_data = b""
    while channel.recv_ready():
        config_data += channel.recv(4096)
        time.sleep(0.5)

    # 清理输出内容
    clean_config = []
    for line in config_data.decode().split("\n"):
        if not line.strip().startswith("<"):
            clean_config.append(line)

    # 保存到文件
    with open(backup_path, "w") as f:
        f.write("\n".join(clean_config))

    print(f"配置已备份至：{backup_path}")


def main():
    devices_file = r"d:\\Python\\xunjian\\device_info.txt"
    backup_directory = r"D:\Python\\xunjian\\backup_configs"

    # 读取设备信息
    with open(devices_file) as f:
        devices = [line.strip().split(",") for line in f]

    # 遍历所有设备进行备份
    for ip, username, password in devices:
        print(f"正在备份 {ip}...")
        ssh_client = device_connect(ip, username, password)
        if ssh_client:
            backup_config(ssh_client, ip, backup_directory)
            ssh_client.close()


if __name__ == "__main__":
    main()
    print("所有设备备份完成。")
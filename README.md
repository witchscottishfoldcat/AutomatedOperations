1. 巡检命令模板 (cmd.txt)
# Network Device Inspection Commands
display device
display environment
display alarm urgent
display memory-usage
display cpu-usage
display logbuffer level 0
display logbuffer level 1
display logbuffer level 2
display logbuffer level 3
display logbuffer level 4
2. 设备资产清单 (device_info.txt)
# IP, SSH用户名, SSH密码
192.168.1.252,huawei,huawei
192.168.1.253,huawei,huawei
使用说明
​巡检命令模板​
保存为 cmd.txt，每行一条命令
设备 SSH 连接成功后自动逐行执行
​设备资产清单​
保存为 device_info.txt，每行一台设备
格式：IP地址,SSH用户名,SSH密码
支持多设备批量操作
实际应用示例

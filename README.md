# 巡检脚本需要配置两个文件分别为  
1. 巡检命令模板 (cmd.txt)
2. 设备资产清单 (device_info.txt)
格式分别如下
(cmd.txt)  
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
(device_info.txt)  
# IP, SSH用户名, SSH密码
192.168.1.252,huawei,huawei
192.168.1.253,huawei,huawei

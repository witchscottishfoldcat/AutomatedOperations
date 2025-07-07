需要配置设备ssh链接后使用
需要2个txt文本
cmd文本为巡检内容模板如下
display device
display environment
display alarm urgen
display memory-usage
display cpu-usage
display logbuffer level 0
display logbuffer level 1
display logbuffer level 2
display logbuffer level 3
display logbuffer level 4
device_info文本为资产清单模板如下（ip，ssh账号，ssh密码）
192.168.1.252,huawei,huawei
192.168.1.253,huawei,huawei

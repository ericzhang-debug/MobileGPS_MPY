# MobileGPS_MPY

## 介绍
MicroPython的MobileGPS程序，实现OLED + LCD1602的位置坐标、时间、高度、航迹信息等的实时输出

## 软件架构
MicroPython + Raspberry PICO

引用第三方库 
|Package|Function|
|---|---|
|micropyGPS|解析GPS的NMEA 0183报文|
|ssd1306|OLED(I2C)驱动|
|lcd_api|LCD1602(I2C)驱动|
|pico_i2c_lcd|LCD1602(I2C)驱动|

## 使用说明

推荐使用Thony，如果使用VisualCode，可以从Thony的安装目录里找到Pico的官方库函数放在项目根目录下即可实现代码高亮和自动补全，但是不能自动上传和调试。

MPY开机自动运行```main.py```程序

```my_gps```对象创建前必须完成外部设备的初始化操作，而且创建前必须延时，否则有几率开机直接停止运行（原因未知，可能这就是靠BUG运行起来的）

## 已知问题

开机搜星正常稳定运行后数据刷新频率不正常，时间不同步，有的时候会出现秒数跳跃的情况。

运行过程中I2C线接触不好程序会直接停止运行，暂不支持热重启，只能断电重启。
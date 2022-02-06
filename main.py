import machine
from machine import I2C,Pin,UART
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from ssd1306 import SSD1306_I2C
from micropyGPS import MicropyGPS
import time

#开始初始化

# ===OLED===
# I2C
oled_i2c_sda = machine.Pin(10)
oled_i2c_scl = machine.Pin(11)
oled_i2c_i2c = machine.I2C(1,sda=oled_i2c_sda,scl=oled_i2c_scl, freq=400000)

oled = SSD1306_I2C(128, 64, oled_i2c_i2c)
oled.fill(0)
oled.show()
oled.text('Initializing...', 0, 32)
oled.show()
    
# ===LCD1602===
# I2C
lcd1602_i2c_sda = machine.Pin(16)
lcd1602_i2c_scl = machine.Pin(17)
lcd1602_i2c_i2c = machine.I2C(0,sda=lcd1602_i2c_sda,scl=lcd1602_i2c_scl, freq=400000)
    
I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
lcd = I2cLcd(lcd1602_i2c_i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.clear()
lcd.move_to(0,0)
lcd.putstr("Initializing...")
lcd.move_to(0,1)
lcd.putstr('Powered By Eric')
    
# ===UART===
uart_tx=machine.Pin(4)
uart_rx=machine.Pin(5)
com = UART(1, baudrate=9600, tx=uart_tx, rx=uart_rx)    
    

time.sleep(2)

my_gps = MicropyGPS(8)#东八区修正

# 初始化OK清空显示
oled.fill(0)
oled.show()

lcd.clear()


def get_GPS_values():
    global rtc,lat,long
    time.sleep_ms(100)
    cc = com.readline()
    for x in cc:
        my_gps.update(chr(x))
        #lat&long
    
    lat=str(my_gps.latitude[0] + (my_gps.latitude[1] / 60))
    long=str(my_gps.longitude[0] + (my_gps.longitude[1] / 60))
    
    #datetime
    date = my_gps.date
    timestamp = my_gps.timestamp
    hour = timestamp[0]
    rtc = str(int(timestamp[0]))+":"+str(int(timestamp[1]))+":"+str(int(timestamp[2]))
    #return 0 #lat,long,rtc

# 开始显示
while True:
    time.sleep_ms(100)
    get_GPS_values()
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr(lat)
    lcd.move_to(0,1)
    lcd.putstr(long)
    
    oled.fill(0)
    
    oled.text('Date:', 0, 0)
    oled.text(my_gps.date_string(), 40, 0)
    
    oled.text('Time:', 0, 10)
    oled.text(rtc, 40, 10)
    
    oled.text('Current:', 0, 20)
    oled.text(str(my_gps.satellites_in_use), 70, 20)
    
    oled.text('Alt:', 0, 30)
    oled.text((str(my_gps.altitude)+"m"), 32, 30)
    
    oled.text('Course:', 0, 40)
    oled.text(str(my_gps.course), 55, 40)
    
    oled.text('Speed:', 0, 50)
    oled.text(str(my_gps.speed[2]), 50, 50)

    oled.show()
    time.sleep_ms(100)
    
    




# LCD1602显示经纬度
'''
lcd.move_to(0,0)
lcd.putstr("Hello")
lcd.move_to(0,1)
lcd.putstr("Hello this")'''

# OLED显示其他信息
'''oled.text('Hello', 0, 0)
oled.text('World', 0, 10)
oled.show()'''






import time
from RPLCD.i2c import CharLCD

# 初始化 LCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8)

def show(lcd,text):
    lcd.clear()
    lcd.write_string(text)
    time.sleep(2)
    lcd.clear()

def marquee_text(lcd, text,row=0, delay=0.3):
    lcd_width = 16
    text = ' '*lcd_width + text + ' '*lcd_width
    while True:
        for i in range(len(text) - lcd_width+1):
            lcd.cursor_pos = (row, 0)
            lcd.write_string(text[i:i+lcd_width])
            time.sleep(delay)
    lcd.clear()
    
# 主程式
if __name__ == "__main__":
    lcd.clear()  # 清空 LCD
    lcd.write_string("init...") 
    show(lcd, "hello world")
    #marquee_text(lcd, "Raspberry Pi LCD！", row=0, delay=0.2)


from flask import Flask, request, jsonify
import lock_control  # 引入解鎖控制模組
import lcd_show
from RPLCD.i2c import CharLCD

app = Flask(__name__)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8)

@app.route('/unlock', methods=['POST'])
def unlock():
    try:
        lock_control.unlock()
        lcd_show.show(lcd, "unlock success")
        
    except Exception as e:
        lcd_show.show(lcd, "unlock fail")
        return jsonify({"message":e})
    
@app.route('/lock', methods=['POST'])
def lock():
    try:
        lock_control.lock()
        lcd_show.show(lcd, "lock success")
    except Exception as e:
        lcd_show.show(lcd, "lock fail")
        return jsonify({"message":e})

def cleanup():
    """清理 GPIO 設置"""
    lock_control.cleanup()  # 清理 GPIO 設置

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5001)  # 讓樹梅派伺服器接受外部請求
    except KeyboardInterrupt:
        print("\n手動中止程式")
    finally:
        cleanup()


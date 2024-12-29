import RPi.GPIO as GPIO
import time

# 設定 GPIO 腳位
RELAY_PIN = 14  # 使用 GPIO 14

# GPIO 初始化
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def unlock():
    """
    控制電磁鎖解鎖，解鎖後不立即上鎖。
    """
    print("解鎖中...")
    GPIO.setup(RELAY_PIN, GPIO.OUT)  
    GPIO.output(RELAY_PIN, GPIO.LOW)  # 啟動繼電器（NO 和 COM 閉合）
    print("解鎖完成，等待上鎖")

def lock():
    """
    控制電磁鎖鎖定。
    """
    GPIO.setup(RELAY_PIN, GPIO.IN)
    print("已鎖定")

def cleanup():
    """清理 GPIO 設置"""
    GPIO.cleanup()
    print("GPIO 清理完成")

if __name__ == "__main__":
    try:
        while True:
            command = input("輸入 'unlock' 解鎖，或 'lock' 上鎖，'exit' 離開程式：").strip().lower()
            if command == "unlock":
                unlock()  # 解鎖
            elif command == "lock":
                lock()  # 手動上鎖
            elif command == "exit":
                break
            else:
                print("無效的指令，請重新輸入")
    except KeyboardInterrupt:
        print("\n手動中止程式")
    finally:
        cleanup()


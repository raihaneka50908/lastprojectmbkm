import RPi.GPIO as GPIO
from gpiozero import AngularServo
from time import sleep
import time

servo = AngularServo(18,min_pulse_width=6e-4,max_pulse_width=23e-4)
GPIO.setmode(GPIO.BCM)

def deteksi_jarak():
    TRIG=23
    ECHO=24
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    try:
        while True:
            
            GPIO.output(TRIG,False)
            time.sleep(2)
            
            GPIO.output(TRIG,True)
            time.sleep(1e-5)
            GPIO.output(TRIG,False)
            
            while GPIO.input(ECHO)==0:
                pulse_start=time.time()
            while GPIO.input(ECHO)==1:
                pulse_end=time.time()
            pulse_duration=pulse_end-pulse_start
            distance=pulse_duration*17150
            distance=round(distance,2)
            if distance<=5:
                break
            print(distance)
            
    except KeyboardInterrupt:
        GPIO.cleanup()

def arah_putar_organik():
    servo.angle=45
    sleep(2)
    servo.angle=0
    sleep(2)

def arah_putar_anorganik():
    servo.angle=-45
    sleep(2)
    servo.angle=0
    sleep(2)

if __name__=="__main__":
    deteksi_jarak()
    arah_putar_anorganik()
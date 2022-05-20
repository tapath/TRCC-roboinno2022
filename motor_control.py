import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
in3 = 21
in4 = 20

in1b = 19
in2b = 13
in3b = 2
in4b = 3


en = 25
en2 = 16
en3 = 26
en4 = 4

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(25)

GPIO.setmode(GPIO.BCM)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p2=GPIO.PWM(en2,1000)
p2.start(25)

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1b,GPIO.OUT)
GPIO.setup(in2b,GPIO.OUT)
GPIO.setup(en3,GPIO.OUT)
GPIO.output(in1b,GPIO.LOW)
GPIO.output(in2b,GPIO.LOW)
p3=GPIO.PWM(en3,1000)
p3.start(25)

GPIO.setmode(GPIO.BCM)
GPIO.setup(in3b,GPIO.OUT)
GPIO.setup(in4b,GPIO.OUT)
GPIO.setup(en4,GPIO.OUT)
GPIO.output(in3b,GPIO.LOW)
GPIO.output(in4b,GPIO.LOW)
p4=GPIO.PWM(en4,1000)
p4.start(25)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         GPIO.output(in1b,GPIO.HIGH)
         GPIO.output(in2b,GPIO.LOW)
         GPIO.output(in3b,GPIO.HIGH)
         GPIO.output(in4b,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         GPIO.output(in1b,GPIO.LOW)
         GPIO.output(in2b,GPIO.HIGH)
         GPIO.output(in3b,GPIO.LOW)
         GPIO.output(in4b,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in1b,GPIO.LOW)
        GPIO.output(in2b,GPIO.LOW)
        GPIO.output(in3b,GPIO.LOW)
        GPIO.output(in4b,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in1b,GPIO.HIGH)
        GPIO.output(in2b,GPIO.LOW)
        GPIO.output(in3b,GPIO.HIGH)
        GPIO.output(in4b,GPIO.LOW)
        temp1=1
        
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in1b,GPIO.LOW)
        GPIO.output(in2b,GPIO.HIGH)
        GPIO.output(in3b,GPIO.LOW)
        GPIO.output(in4b,GPIO.HIGH)
        temp1=0
        x='z'
    elif x=='sl':
        print("slide")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in1b,GPIO.HIGH)
        GPIO.output(in2b,GPIO.LOW)
        GPIO.output(in3b,GPIO.LOW)
        GPIO.output(in4b,GPIO.HIGH)
        x='z'
        
    elif x=='ror':
        print("rotate right")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in1b,GPIO.HIGH)
        GPIO.output(in2b,GPIO.LOW)
        GPIO.output(in3b,GPIO.LOW)
        GPIO.output(in4b,GPIO.HIGH)
        x='z'
        
    elif x=='rol':
        print("rotate left")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in1b,GPIO.LOW)
        GPIO.output(in2b,GPIO.HIGH)
        GPIO.output(in3b,GPIO.HIGH)
        GPIO.output(in4b,GPIO.LOW)
        x='z'

    elif x=='10':
        print("10%")
        p.ChangeDutyCycle(10)
        p2.ChangeDutyCycle(10)
        p3.ChangeDutyCycle(10)
        p4.ChangeDutyCycle(10)
        x='z'


    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        p3.ChangeDutyCycle(25)
        p4.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        p3.ChangeDutyCycle(50)
        p4.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        p3.ChangeDutyCycle(75)
        p4.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
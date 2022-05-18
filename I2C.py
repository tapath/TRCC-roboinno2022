
# CorgiDude | From AiDude.io, https://www.aiiotshop.com/b/26
import sensor, image, lcd, time

lcd.init()
sensor.reset(freq=24000000,dual_buff=True)
sensor.set_auto_gain(False,10) # ตัวนี้ฟิกแสงและสีที่ปรับ เพิ่มจะสว่าง
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1)
#sensor.set_vflip(2)
sensor.run(1)
sensor.skip_frames(30)
#y_threshold = (88, 100, -31, 2, 16, 79)
#y_threshold   = (27, 100, -30, 21, 26, 79) #Yellow
#y_threshold = (60, 100, -128, 5, -128, 0)
#y_threshold = (72, 100, -127, -4, -128, -3)
y_threshold = (97, 100, -128, 2, -128, 1)

while True:
    img=sensor.snapshot()
    #img = img.rotation_corr(z_rotation=90.0)

    img_cut=img.cut(0,140,320,100)

    blobs = img_cut.find_blobs([y_threshold],pixels_threshold=20, area_threshold=20, merge=True)

    land = []
    numland = []
    if blobs:
        pot1 = blobs[0][5] - 160
        potout1 = (0.263*(pot1))
        print(pot1)
        if potout1 >-45 and potout1 < 45 :
            land.append(potout1)
            numland.append(1)
        #tmp=img_cut.draw_cross(int(pot1+145), 5,thickness = 4,color = (255,0,0))
        #for b in blobs:
            #tmp=img.draw_cross(b[5], 145,thickness = 4,color = (255,0,0))
    print(land)
    print(numland)
    lcd.display(img)
    #Serial.print(a)

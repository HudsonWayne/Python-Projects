import qrcode 

my_qr = qrcode.make("https://www.youtube.com/watch?v=2vjPBrBU-TM&list=RDZSM3w1v-A_Y&index=10")
my_qr.save("my_qr.png", scare = 8)
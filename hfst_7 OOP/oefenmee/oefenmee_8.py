# Maak een klasse om het gebruiken van een led op RPi te vereenvoudigen.
# Je kan de RPI via deze website simuleren: https://create.withcode.uk 

" Startcode: "

# # import raspberry pi GPIO module
# import RPi.GPIO as GPIO
# import time

# # setup pin 7 & 31 as output
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(31, GPIO.OUT)

# # Turn on pin 7 & 31
# GPIO.output(7, GPIO.HIGH)
# GPIO.output(31, GPIO.HIGH)


" Via onderstaande code kan je de klasse Led testen. "

# # Maak een led aan op pin 5 en pin 21
# led_5 = Led(5)
# led_21 = Led(21)

# # Schakel de leds afwisselend aan/uit.
# while True:
#     led_5.aan()
#     led_21.uit()
#     time.sleep(1)

#     led_5.uit()
#     led_21.aan()
#     time.sleep(1)

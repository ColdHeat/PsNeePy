import machine
import time
import utime

# http://problemkaputt.de/psx-spx.htm#cdromprotectionmodchips

# DATA is responsible for transferring the SCEX data
# MM3 Equivalent is Pin 6
DATA = 14 # GPIO14 - D5

# GATE is required to be LOW to allow the modchip to inject
# MM3 Equivalent is Pin 5
GATE = 12 # GPIO12 - D6

# LID is whether or not the LID is connected
# MM3 Equivalent is Pin 7
LID = 13 # GPIO13 - D7


# MM3 for GND is Pin 8
# MM3 for VCC/PWR is Pin 1

FIRST_BOOT = True
NEW_PS_MODEL = False

SCEE_data = (1,0,0,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0)
SCEA_data = (1,0,0,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,0)
SCEI_data = (1,0,0,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0)


def inject():
    utime.sleep_ms(6900)

    machine.Pin(DATA, machine.Pin.OUT)
    machine.Pin(DATA).value(0)

    utime.sleep_ms(100)

    machine.Pin(GATE, machine.Pin.OUT)
    machine.Pin(GATE).value(0)


    for i in range(8):
        for data in (SCEA_data, SCEE_data, SCEI_data):
            for bit in data:
                if bit:
                    machine.Pin(DATA, machine.Pin.IN)
                    utime.sleep_us(4000)
                else:
                    if NEW_PS_MODEL:
                        # machine.Pin(DATA, machine.Pin.OUT)
                        # now = utime.ticks_ms()
                        # while ( (utime.ticks_ms() - now) < 4000 ):
                        #     pass
                        machine.Pin(DATA, machine.Pin.OUT)
                        machine.Pin(DATA).value(0)
                        utime.sleep_us(4000)
                    else:
                        machine.Pin(DATA, machine.Pin.OUT)
                        machine.Pin(DATA).value(0)
                        utime.sleep_us(4000)
            utime.sleep_ms(90)


    machine.Pin(DATA, machine.Pin.IN)
    machine.Pin(GATE, machine.Pin.IN)
    utime.sleep_ms(11000)


    machine.Pin(GATE, machine.Pin.OUT)
    machine.Pin(GATE).value(0)

    for i in range(20):
        for data in (SCEA_data, SCEE_data, SCEI_data):
            for bit in data:
                if bit:
                    machine.Pin(DATA, machine.Pin.IN)
                    utime.sleep_us(4000)
                else:
                    if NEW_PS_MODEL:
                        # machine.Pin(DATA, machine.Pin.OUT)
                        # now = utime.ticks_ms()
                        # while ( (utime.ticks_ms() - now) < 4000 ):
                        #     pass
                        machine.Pin(DATA, machine.Pin.OUT)
                        machine.Pin(DATA).value(0)
                        utime.sleep_us(4000)
                    else:
                        machine.Pin(DATA, machine.Pin.OUT)
                        machine.Pin(DATA).value(0)
                        utime.sleep_us(4000)
            utime.sleep_ms(90)

    machine.Pin(DATA, machine.Pin.IN)
    machine.Pin(GATE, machine.Pin.IN)


machine.Pin(DATA, machine.Pin.IN)
machine.Pin(GATE, machine.Pin.IN)
machine.Pin(LID, machine.Pin.IN)




high_count = 0
low_count = 0
now = utime.ticks_ms()

while ( (utime.ticks_ms() - now) < 1000 ):
    if machine.Pin(GATE).value() == 1:
        high_count += 1
    if machine.Pin(GATE).value() == 0:
        low_count += 1
    utime.sleep_us(200)

if low_count > 100:
    NEW_PS_MODEL = True
# else: NEW_PS_MODEL is False by default





time.sleep_ms(1200)

while True:
    lid_status = machine.Pin(LID).value()

    # LID=1 means CD drive is open
    # LID=0 means CD drive is closed

    if FIRST_BOOT:
        inject()
        FIRST_BOOT = False
    else:
        time.sleep_ms(50)
        if lid_status != 0:
            time.sleep_ms(100)
            inject()
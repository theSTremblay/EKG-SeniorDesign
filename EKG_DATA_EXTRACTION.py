import spidev

import time
import sys
import spidev

local_maximmum_previous =0
local_maximmum_current = 0

spi = spidev.SpiDev()
spi.open(0, 0)


def buildReadCommand(channel):
    startBit = 0x01
    singleEnded = 0x08

    # Return python list of 3 bytes
    #   Build a python list using [1, 2, 3]
    #   First byte is the start bit
    #   Second byte contains single ended along with channel #
    #   3rd byte is 0
    return []


def processAdcValue(result):
    '''Take in result as array of three bytes.
       Return the two lowest bits of the 2nd byte and
       all of the third byte'''
    pass


def readAdc(channel):
    if ((channel > 7) or (channel < 0)):
        return -1
    r = spi.xfer2(buildReadCommand(channel))
    return processAdcValue(r)


def ECG_GET_BPM(void):
    global local_maximmum_previous


    global local_maximmum_current
    BPM = 0

    if (local_maximmum_current >= local_maximmum_previous):
        BPM = (60 * 1000) / (local_maximmum_current - local_maximmum_previous)
    else:
        BPM = (60 * 1000) / (local_maximmum_previous - local_maximmum_current)

    local_maximmum_previous = local_maximmum_current
    return BPM

if __name__ == '__main__':
    try:
        while True:
            val = readAdc(0)

            print("ADC Result: ", str(val))

            #Time Delay 10000 HZ
            time.sleep(.0001)
    except KeyboardInterrupt:
        spi.close()
        sys.exit(0)

def SPI_GET(spi):
    value = 0
    myList = []
    print(myList)
    while value != "\n":
        value = spi.readbytes(1)
        myList.append(value)
    return(myList)

def read_files(filename):
    f = open(filename,"r") #opens file with name of "test.txt"
    myList = []
    for line in f:
        myList.append(line)
    print(myList)



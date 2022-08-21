import serial
from time import sleep
from enum import Enum
#Can be Downloaded from this Link
#https://pypi.python.org/pypi/pyserial

#Global Variables
ser = 0
#Command Sequence
class currentSequence(Enum):
    FATCORY_RESTORE=0
    CHECK=1
    SOFTWAREVERSION=2
    IMEI=3
    SIMSTATUS=4
    SIMIDENTIFICATION=5
    SIGNALSTRENGTH=6
    NETWORK_REGISTRATION=7
    NETWORK_REGISTRATION_QUERY=8
    NETWORK_REGISTRATION_DEFAULT=9
    GPRS_ATTACHMENT=10
    GPRS_ATTACHMENT_QUERY=11
    APN_REGISTRATION=12
    PPP_LINK_REGISTRATION=13
    PPP_LINK_REGIRATION_QUERY=14
    URL_SETUP=15
    PORT_SETUP=16
    LINK_SETUP=17
    GET_ACTION=18


#Function to Initialize the Serial Port
def init_serial():
    global ser          #Must be declared in Each Function
    ser = serial.Serial(timeout=1.5)
    ser.baudrate = 9600
    ser.port = 'COM7'   #COM Port Name Start from 0
    #ser.port = '/dev/ttyUSB0' #If Using Linux
    #Specify the TimeOut in seconds, so that SerialPort
    #Doesn't hangs
    ser.timeout = 1.5
    ser.open()          #Opens SerialPort
    # print port open or closed
    if ser.isOpen():
        print('Open: ' + ser.portstr)
#Function Ends Here

#Call the Serial Initilization Function, Main Program Starts from here
init_serial()

def enumResolution(currentSequenceCommand):
    if currentSequenceCommand==currentSequence.FATCORY_RESTORE:
        print(currentSequence.FATCORY_RESTORE.value,end=" ")
        print(currentSequence.FATCORY_RESTORE.name)
        ser.write(b'AT&F\r\n')
    if currentSequenceCommand== currentSequence.CHECK:
        print(currentSequence.CHECK.value, end=" ")
        print(currentSequence.CHECK.name)
        ser.write(b'AT\r\n')
    if currentSequenceCommand== currentSequence.SOFTWAREVERSION:
        print(currentSequence.SOFTWAREVERSION.value, end=" ")
        print(currentSequence.SOFTWAREVERSION.name)
        ser.write(b'AT+CGMR\r\n')
    if currentSequenceCommand== currentSequence.IMEI:
        print(currentSequence.IMEI.value, end=" ")
        print(currentSequence.IMEI.name)
        ser.write(b'AT+CGSN\r\n')
    if currentSequenceCommand==currentSequence.SIMSTATUS:
        print(currentSequence.SIMSTATUS.value, end= " ")
        print(currentSequence.SIMSTATUS.name)
        ser.write(b'AT+CPIN?\r\n')
    if currentSequenceCommand== currentSequence.SIMIDENTIFICATION:
        print(currentSequence.SIMIDENTIFICATION.value, end= " ")
        print(currentSequence.SIMIDENTIFICATION.name)
        ser.write(b'AT+CIMI\r\n')
    if currentSequenceCommand==currentSequence.SIGNALSTRENGTH:
        print(currentSequence.SIGNALSTRENGTH.value, end=" ")
        print(currentSequence.SIGNALSTRENGTH.name)
        ser.write(b'AT+CSQ\r\n')
    if currentSequenceCommand==currentSequence.NETWORK_REGISTRATION:
        print(currentSequence.NETWORK_REGISTRATION.value, end=" ")
        print(currentSequence.NETWORK_REGISTRATION.name)
        ser.write(b'AT+CREG=2\r\n')
    if currentSequenceCommand==currentSequence.NETWORK_REGISTRATION_QUERY:
        print(currentSequence.NETWORK_REGISTRATION_QUERY.value, end=" ")
        print(currentSequence.NETWORK_REGISTRATION_QUERY.name)
        ser.write(b'AT+CREG?\r\n')
    if currentSequenceCommand==currentSequence.NETWORK_REGISTRATION_DEFAULT:
        print(currentSequence.NETWORK_REGISTRATION_DEFAULT.value, end=" ")
        print(currentSequence.NETWORK_REGISTRATION_DEFAULT.name)
        ser.write(b'AT+CREG=0\r\n')
    if currentSequenceCommand==currentSequence.GPRS_ATTACHMENT:
        print(currentSequence.GPRS_ATTACHMENT.value, end=" ")
        print(currentSequence.GPRS_ATTACHMENT.name)
        ser.write(b'AT+CGATT=1\r\n')
    if currentSequenceCommand ==currentSequence.GPRS_ATTACHMENT_QUERY:
        print(currentSequence.GPRS_ATTACHMENT_QUERY.value, end=" ")
        print(currentSequence.GPRS_ATTACHMENT_QUERY.name)
        ser.write(b'AT+CGATT?\r\n')
    if currentSequenceCommand == currentSequence.APN_REGISTRATION:
        print(currentSequence.APN_REGISTRATION.value, end=" ")
        print(currentSequence.APN_REGISTRATION.name)
        ser.write(b'AT+CGDCONT=1,"IP","M2MISAFE"\r\n')
    if currentSequenceCommand == currentSequence.PPP_LINK_REGISTRATION:
        print(currentSequence.PPP_LINK_REGISTRATION.value, end= " ")
        print(currentSequence.PPP_LINK_REGISTRATION.name)
        ser.write(b'AT+XIIC=1\r\n')
    if currentSequenceCommand == currentSequence.PPP_LINK_REGIRATION_QUERY:
        print(currentSequence.PPP_LINK_REGIRATION_QUERY.value, end=" ")
        print(currentSequence.PPP_LINK_REGIRATION_QUERY.name)
        ser.write(b'AT+XIIC?\r\n')
    if currentSequenceCommand ==currentSequence.URL_SETUP:
        print(currentSequence.URL_SETUP.value, end=" ")
        print(currentSequence.URL_SETUP.name)
        ser.write(b'AT+HTTPPARA=url,\"iot.elecssol.com/interval.php\"\r\n')
    if currentSequenceCommand == currentSequence.PORT_SETUP:
        print(currentSequence.PORT_SETUP.value, end=" ")
        print(currentSequence.PORT_SETUP.name)
        ser.write(b'AT+HTTPPARA=Port,80\r\n')
    if currentSequenceCommand == currentSequence.LINK_SETUP:
        print(currentSequence.LINK_SETUP.value, end=" ")
        print(currentSequence.LINK_SETUP.name)
        ser.write(b'AT+HTTPSETUP\r\n')
    if currentSequenceCommand == currentSequence.GET_ACTION:
        print(currentSequence.GET_ACTION.value, end=" ")
        print(currentSequence.GET_ACTION.name)
        ser.write(b'AT+HTTPACTION=0\r\n')

check = currentSequence.FATCORY_RESTORE
n=0
newText=""
while 1:
        enumResolution(check)
        if n==17:
            responseText = ser.read_until('OK')
            responseText = str(responseText)
            print(responseText)
            print()
            pass;
        if n==18:
            while True:
                responseText = ser.read_until()
                print(str(responseText))
        if n<17:
            bytes=ser.read_until('\n');
            bytes=str(bytes)
            print(str(n), end=" ")
            print(bytes)
            print()
        
        if n<19:
            n=n+1;
            if n==19:
                break;
            check=currentSequence(check.value+1)
        else:
            break;
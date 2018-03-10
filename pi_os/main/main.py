import pybluez
import bluetooth
import time 

#TODO: Testing!!!!
BUFFER_SIZE = 256

def setup_gpio_pins():
    # We can play around with what does what and add more here
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    
audio_buffer = []

def read_buffer():
    return -1

if name == "__main__":   
    setup_gpio_pins()
    while 1: 
        # Write high to issue sending cmd 
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.001)
       

        # start the Bluetooth service
        server_sock = BluetoothSocket(RFCOMM)
        server_sock.bind(("", PORT_ANY))
        server_sock.listen(1)
        port = server_sock.getsockname()[1]
        uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

        advertise_service( server_sock, "oxysis-bt",
                           service_id = uuid,
                           service_classes = [uuid, SERIAL_PORT_CLASS],
                           profiles = [SERIAL_PORT_PROFILE] )
     

        # wait for connection
        client_sock, client_info = server_sock.accept()
       # perform the heart rate algo.
        
   
       # send out heart rate via bluetooth
       







        if GPIO.input(17):
            print("Pin 11 is HIGH")
        else:
            print("Pin 11 is LOW")
        GPIO.cleanup()



import pybluez
import bluetooth
import time 

#TODO: Testing!!!!!



def setup_gpio_pins():
    # We can play around with what does what and add more here
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    
audio_buffer = []

def read_buffer():
    return -1

if name == "__main__":
    GPIO.setmode(GPIO.BCM)  
  
    
    # Write high to issue sending cmd 
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.001)
    
    
    
      
    
    
    
    
    
    if GPIO.input(17):
        print("Pin 11 is HIGH")
    else:
        print("Pin 11 is LOW")
    GPIO.cleanup()
    
    

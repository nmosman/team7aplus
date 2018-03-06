import pybluez
import socket
import pyaudio
import bluetooth

# Ok so default audio data info
# May not actually need this, but will experiment with this further
CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
#------------------------------------------------------------------#
class DataTransmitter(object):
    """
        @TODO: Some basic documentation lul 
    """

def __init__(self,
             protocol="TCP",
             addr=None,
             port=None,
             tcp_socket=None,
             bt_socket=None,
             stream_obj=None):
    self.protocol = protocol
    self.addr = addr
    self.port = port
    self.tcp_socket = tcp_socket
    self.bt_socket = bt_socket
    self.stream_obj = stream_obj

    def search_devices(self, duration_len):
        if (self.protocol != "BLE") or (self.protocol!= "BT"):
            raise ValueError("Transmission protocol must be set to bluetooth!")
        else:
            return bluetooth.discover_devices(duration=duration_len, lookup_names=True)

    def connect(self, HOST, PORT):
        if self.protocol == "TCP":
            self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_socket.connect((HOST, PORT))
            
            # This crap I need to try out properly later
            """
            stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

            stream.start_stream()
            """

        elif self.protocol == "BT":
            # This gotta be hardcoded for now...
            serverMACAddress = "Some MAC ADDR OF THE DEVICE"
            bt_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            bt.connect((serverMACAddress, PORT))
            
            # debugging will be soon

    def send_byte(self):
        return -1

    def send_buffer(self):
        return -1

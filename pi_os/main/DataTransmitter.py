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
	
	
	# Some info pertaining to like the connection and stuff 
    protocol = "TCP"
    addr = ""
    port = ""
	tcp_socket = ""
	bt_socket = ""
	
	# Again may not need this
	stream_obj = ""
	

def __init__(self, protocol, addr, port):
    self.protocol = protocol
    self.addr = addr
    self.port = port


def search_devices(duration_len):
    if self.protocol != "BLE" or self.protocol!= "BT":
        return "Transmission protocol must be set to bluetooth!"
    else:
         devices = bluetooth.discover_devices(duration=duration_len, lookup_names = True)
         return devices



def connect(HOST, PORT):
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
		serverMACAddress = 'Some MAC ADDR OF THE DEVICE'
		bt_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		bt.connect((serverMACAddress, PORT))
		
		# debugging will be soon
	
	
	
def set_protocol(protocol):
    self.protocol = protocol

def get_protocol():
    return self.protocol

def send_byte():
    return -1

def send_buffer():
    return -1

	
def get_connection_state():
	return connected 
	
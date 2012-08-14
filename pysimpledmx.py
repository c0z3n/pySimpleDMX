import serial, sys, time

START_VAL = 0x7E
END_VAL = 0xE7

COM_BAUD = 57600
COM_TIMEOUT = 1
COM_PORT = 7

LABELS = {     
               'GET_WIDGET_PARAMETERS' :3,  #unused
               'SET_WIDGET_PARAMETERS' :4,  #unused
               'RX_DMX_PACKET'         :5,  #unused
               'TX_DMX_PACKET'         :6,
               'TX_RDM_PACKET_REQUEST' :7,  #unused
               'RX_DMX_ON_CHANGE'      :8,  #unused
          }
          
          
class DMXConnection(object):
    
    def __init__(self, comport=None):
        
        self.com = 0
        self.dmx_frame = list()
        
      #setup channel output list
        for i in xrange (511):
            self.dmx_frame.append(0)
        
      #open com
        if comport is not None: port_num = comport-1
        else:port_num = COM_PORT-1
            
        try:
            self.com = serial.Serial(port_num, baudrate=COM_BAUD, timeout=COM_TIMEOUT)
        except:
            print "Could not open COM%s, quitting application" % (port_num+1)
            sys.exit(0)
            
        print "Opened %s" % (self.com.portstr)

    
    def setChannel(self, chan, val, autorender=False):
    #  takes channel and value arguments to set a channel level in the local 
    #  dmx frame, to be rendered the next time the render() method is called
        if (chan > 512) or (chan < 1):
            print "invalid channel"
            return
        if val > 255: val=255
        if val < 0: val=0
        self.dmx_frame[chan] = val
        if autorender:
            self.render()
    
    def clear(self, chan=0):
    #  clears all channels to zero. blackout.
    #  with optional channel argument, clears only one channel
        if chan==0:
            for i in xrange (1, 512, 1):
                self.dmx_frame[i]=0
        else:
            self.dmx_frame[chan]=0
            
    
    def render(self):
    #  updates the dmx output from the USB DMX Pro with the values from self.dmx_frame
        packet = []
        packet.append(chr(START_VAL))
        packet.append(chr(LABELS['TX_DMX_PACKET']))
        packet.append(chr(len(self.dmx_frame) & 0xFF))
        packet.append(chr((len(self.dmx_frame) >> 8) & 0xFF))
        
        for j in xrange(len(self.dmx_frame)):
            packet.append(chr(self.dmx_frame[j]))
            
        packet.append(chr(END_VAL))
        
        self.com.write(''.join(packet)) 
        
    def close(self):
        self.com.close()
        
      
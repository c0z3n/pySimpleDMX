pySimpleDMX
===========

### c0z3n 2012, GPL v3 ###


pySimpleDMX is a simple python module designed to make basic DMX control in python easy.

pySimpleDMX is designed for and requires an [Enttec USB DMX Pro](http://www.enttec.com/index.php?main_menu=Products&pn=70304&show=description&name=dmxusbpro) or compatible hardware for communication over a DMX network.

#### Installation ####
Simply take a copy of pysimpledmx.py and stick it either in your project directory, or in your python `site packages` directory. Nothing fancy.

#### Initialization ####
To initialize pySimpleDMX, initialize a `pysimpledmx.DMXConnection()` object, using the com port number of your enttec DMX USB Pro as an argument. For example, if our DMX USB Pro is on com port 3, we would initialize our dmx connection using `dmx = pysimpledmx.DMXConnection(3)`

If for any reason the dmx connection fails to initialize on the provided com port, pysimpledmx will let you know via the console and close. 

    # example    
    import pysimpledmx
    mydmx = pysimpledmx.DMXConnection(3)
    ...


#### Usage ####
DMX output through pySimpleDMX is managed using a local list of size 512 in the `DMXConnection()` object, which represents the values for all 512 dmx channels in a single universe. When initialized, the default value for each channel is zero. to push the current list of values out over the dmx network, or 'update' the network, you must call the `.render()` method on your `DMXConnection()` object.

to change the value for a channel, use the `setChannel()` method on your `DMXConnection()` object. `setChannel()` requires `chan` (channel) and `val` (value) arguments, as well as an optional `autorender` argument, which should be set to `True` if you wish to have PySimpleDMX automatically update the dmx output immediately upon changing the specified channel value.

the `chan` and `val` arguments should be between 1 and 512 and between 0 and 255, respectively.

unless the `autorender` argument is specified `True`, the `.render()` method must be called to update the dmx output. because of the serial communication with the DMX USB Pro, this is a relatively slow operation, and thus rendering should be done sparingly to avoid bottlenecking and setting `autorender` is not reccomended.


    # example    
    import pysimpledmx
    mydmx = pysimpledmx.DMXConnection(3)
    
    mydmx.setChannel(1, 255) # set DMX channel 1 to full
    mydmx.setChannel(2, 128) # set DMX channel 2 to 128
    mydmx.setChannel(3, 0)   # set DMX channel 3 to 0
    mydmx.render() render    # render all of the above changes onto the DMX network

    mydmx.setChannel(4, 255, autorender=True) # set channel 4 to full and render to the network

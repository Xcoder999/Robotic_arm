#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# This is the name of the remote EV3 or PC we are connecting to.
server = 'ev3dev'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('establishing connection...')
client.connect(server)
print('connected!')
new_message = ""
ulm = Motor(Port.A)
urm = Motor(Port.B)
w = Motor(Port.D)

while True:

    mbox.wait()
    new_message = mbox.read()

    if new_message == "move upper joint":
        print(mbox.read())
        ulm.run(1000)
        urm.run(-1000)
    if new_message == "stop upper joint":
        print(mbox.read())
        urm.hold()
        ulm.hold()
    if new_message == "move upper joint 1":
        print(mbox.read())
        ulm.run(-1000)
        urm.run(1000)
    if new_message == "move wrist":
        print(mbox.read())
        w.run(-100)
    if new_message == "move wrist 1":
        print(mbox.read())
        w.run(100)
    if new_message == "stop wrist":
        print(mbox.read())
        w.hold()
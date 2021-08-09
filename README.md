# perfectpark
A smart sensor for you garage which will indicate, via colored LEDs, how far your car needs to pull in to the garage to close the door safely. The distance sensing is accomplished with an ultrasonic sensor, and control is handled with a Raspberry Pi. The ultrasonic sensor is only activated when the garage door is opened, which is determined via an MQTT message. The source of the MQTT message is a Home Assistant instance with a garage door sensor, but that is outside of this project.


from pubnub import Pubnub
import json,time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print "Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script"


#Setup GPIO
GPIO.setmode(GPIO.BOARD)

#Setup PubNub
pubnub = Pubnub(publish_key="pub-c-b72e8d8e-4e01-4896-ae5a-ad671c84ebc2",subscribe_key="sub-c-74baf600-439b-11e5-a9f1-02ee2ddab7fe")
pubnubChannelName = 'gpio-raspberry-control'


#Setup Glow Status Flow
forward = False
backward = False
left = False
right = False

#GPIO ports (BOARD mode)
#R Wheel    -> 19    (ON/OFF)
#R Dir      -> 22    (Forward/Backward)
#L Wheel    -> 11
#L Dir      -> 7



#PubNub Channel Subscribe Callback
def gpioCallback(msg,channel):

	global forward
	global backward
	global left
	global right

	respstring = ''
	command = msg

	print "Command is : " + str(command)

	if('req' in command):
		if(command['req'] == 'forward'):

			if(forward):
				respstring = 'forward stop'
				forward = False
				backward = False
				left = False
				right = False   				
				gpiostop()			
			else:
				forward = True
				respstring = 'forward'
				
				GPIO.output(19, True)
				GPIO.output(22, True)
				GPIO.output(11, True)
				GPIO.output(7, True)					

			respmsg = {"resp" : respstring }
			pubnub.publish(pubnubChannelName, respmsg)
		
		elif(command['req'] == 'backward'):

			if(backward):
				respstring = 'backward stop'
				forward = False
				backward = False
				left = False
				right = False   				
				gpiostop()
				
				
			else:
				backward = True;
				respstring = 'backward'
				
				GPIO.output(19, True)
				GPIO.output(22, False)
				GPIO.output(11, True)
				GPIO.output(7, False)				


			respmsg = {"resp" : respstring }
			pubnub.publish(pubnubChannelName, respmsg)
			
		elif(command['req'] == 'left'):

			if(left):
				respstring = 'left stop'
				forward = False
				backward = False
				left = False
				right = False   				
				gpiostop()
		
			else:
				left = True
				respstring = 'left'
				
				GPIO.output(19, True)
				GPIO.output(22, True)
				GPIO.output(11, True)
				GPIO.output(7, False)					

			respmsg = {"resp" : respstring }
			pubnub.publish(pubnubChannelName, respmsg)
			
		elif(command['req'] == 'right'):

			if(right):
				respstring = 'right stop'
				forward = False
				backward = False
				left = False
				right = False   				
				gpiostop()			
			else:
				right = True
				respstring = 'right'
				
				GPIO.output(19, True)
				GPIO.output(22, False)
				GPIO.output(11, True)
				GPIO.output(7, True)					


			respmsg = {"resp" : respstring }
			pubnub.publish(pubnubChannelName, respmsg)
			
		elif(command['req'] == 'stop'):

			respstring = 'stop'
			forward = False
			backward = False
			left = False
			right = False   			
			gpiostop()

			respmsg = {"resp" : respstring }
			pubnub.publish(pubnubChannelName, respmsg)
		
		elif(command['req'] == 'kill'):

			respstring = 'Shutdown'		
			forward = False
			backward = False
			left = False
			right = False   			
			gpiostop()
			GPIO.cleanup()

			respmsg = {"resp" : respstring }
			pubnub.publish(pubnubChannelName, respmsg)		


#PubNub Channel Subscribe Callback
#def gpioError(msg):
#	print 'Error :' + msg

def gpiostop():
 
    GPIO.output(19, False)
    GPIO.output(22, False)
    GPIO.output(11, False)
    GPIO.output(7, False)    



if __name__ == '__main__':

	GPIO.setup(19, GPIO.OUT)
	GPIO.setup(22, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(7, GPIO.OUT)

	pubnub.subscribe(pubnubChannelName, gpioCallback, {"resp":"Error"})

	while True:

		time.sleep(5000)

		if(GPIO.gpio_function(19) or GPIO.gpio_function(22) or
		   GPIO.gpio_function(11) or GPIO.gpio_function(7)):
			##All is over
		        break

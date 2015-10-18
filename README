*****ANDROID FILES FOUND AT https://github.com/OwenSawyer/Pibot_Android
*****You must enter/substitute in your own PubNub API Keys to use this code


PiBot: How To & Guide
August 31, 2015	

The Bot -> Build guide
I bought the basics of the robot as a kit from
https://abra-electronics.com/educational-kits/raspberry-pi/raspberry-pi-2wd-robot-instructional-pack-includes-the-pi-pi-2wd-kit.html?sl=en. 
The kit includes (almost) everything,

Including:


    Chassis And Motorized Wheels
    Raspberry Pi B+ (and Raspbian OS SD card)
    Motor Control Board


Not Included but used:


    Wifi Dongle
    Webcam
    (Keyboard + Mouse + Monitor for first-time setup)


Building instructions for the chassis are included in the kit. Since Rapsbian is pre-loaded on the SD card, you 
can just put it in the Pi and it will start the first time boot.

Additional PiBot Programs
I Highly recommend using a wif dongle, and setting up a static ip for the Pi so that you can take advantage of SSH 
(allowing you to run the Pi from just the command line on your computer). I personally use PuTTY for SSH but any 
client will work. Additionally, for my live-feed webcam, I use the Motion software. A good guide for setting up 
the webcam is *this one* http://pimylifeup.com/raspberry-pi-webcam-server/

The Bread and Butter – The Pubnub API

The Pubnub API is a service that links and allows ‘Publishers’ and ‘Subscribers’ to communicate. In short, 
for my purposes it allows me to send messages between the PiBot and the Web/Android Client to control the 
robot. The Pubnub website contains many helpful resources for installing and use with Python/Javascript/Java 
and much more.


Quick walkthrough of each Component

Python: The Pibot Driver
The driver works by parsing the Pubnub request sent by the client. For example, {‘req’: ‘forward’} is 
interpreted as forward. From there, the Driver activates the appropriate GPIO ports. In this case, it 
tells both motors to turn on, and go forwards. Turning left would have the left motor going backwards, 
while the right motor moves forwards.



JavaScript: The Web Client

On A button click, the appropriate message is sent through pubnub to be interpreted by the python driver.
*Note*: Motion (live webcam) is not directly compatible with Google Chrome. Firefox does work however, and is 
a good simple workaround (if you do not require cross-browser compatibility)



Java: The Android Client

Simple Mjpeg View
As I noted for the web client, Chrome (the android browser) does not support Motion. The code for Simple MJPEG 
view is a workaround I found that addresses this by loading the live-feed webcam as a series of changing JPEG images.

Besides this, the Android client is very similar to the web client, involving using pubnub to publish messages when 
a button is clicked.

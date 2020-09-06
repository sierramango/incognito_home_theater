**Disclaimer:** This is not a finished solution, just the first, v1, iteration which I had time for. The finished solution will have encrypted data transmission as well as position sensors and power protection built in.

**Project background:** I'm not a big fan of TVs. Firstly, I don't haev time to watch TV but also, I don't like what they look like in a space. They are big black slabs grabbing attention in living rooms and I simply don't like that look. That said, I would still like to watch a movie and laptops too much of a compromise. So the natural solution would be to use a projector. As can see from the video, there isn't a clean wall around my living room so I would either have to take one of the paintings down to use the wall as a screen or install the roll-down screen. Once again, I don't like either of those. So the idea I came up with is to integrate the projector and the "screen" into the existing space. Projector is housed in one of the drawers that flip up on command and the full "screen" is revealed as the painting slides up. 
______________________________
**Flip-up Drawer:**

The drawer runs entirely on 5V DC, there is a 220VAC-to-5VDC power adapter driving the ESP8266 as well as the motor controller and motors.
Motors are just regular hobby motors with a 48:1 gear transmission adding extra torque to the winch. The winch wheels as well as wheel catchers are 3D printed and the STL files can ben found in the repository.

Micropython is flashed on the ESP8266 and two files are running the show. The boot.py runs on boot and connects the device to wifi. The main.py creates a server that listens on port 80 and tells motors what to do.

![ ](/IMG_4312.jpg)

You can find the STL files of the 3D printed objectsin the pepository.

![ ](/IMG_4310.jpg)

![ ](/IMG_4311.jpg)

______________________________
**Sliding Painting:**

![ ](/IMG_4292.jpg)

![video](https://j.gifs.com/5QPnvR.gif)

![ ](/IMG_4336.jpg)

The linear actuators are slightly angled away from the wall. The reason for this is that 1. if they were not, I would have to cut tracks out from a wall and you would see them, and 2. more importantly, it keeps the painting away from the wall when it's moving so that way, the painting is not getting damaged and neither is the wall and there are no color streaks on the white paint of the wall.

![ ](/IMG_4338.jpg)

These nails fit into the holes of the actuator pistons and they prevent the painting from sliding out and falling.

![ ](/IMG_4337.jpg)

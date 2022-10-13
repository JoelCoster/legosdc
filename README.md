# RDW Lego Self Driving Challenge

```
 _|_|_|    _|_|_|    _|          _|     _|        _|_|_|_|    _|_|_|    _|_|         _|_|_|  _|_|_|      _|_|_|  
 _|    _|  _|    _|  _|          _|     _|        _|        _|        _|    _|     _|        _|    _|  _|        
 _|_|_|    _|    _|  _|    _|    _|     _|        _|_|_|    _|  _|_|  _|    _|       _|_|    _|    _|  _|        
 _|    _|  _|    _|    _|  _|  _|       _|        _|        _|    _|  _|    _|           _|  _|    _|  _|        
 _|    _|  _|_|_|        _|  _|         _|_|_|_|  _|_|_|_|    _|_|_|    _|_|       _|_|_|    _|_|_|      _|_|_|                                                                                                         
```

**Welcome to the RDW Lego Self Driving Challenge event!**

Your goal is to write software that enables the vehicle you have received to complete the racetrack that has been built in the quickest time, in comparison to competing teams. If no team manages to sucessfully complete a lap, the team that manages to drive the furthest without crashing will win. Your vehicle will need to sound a beep before it starts racing, to allow laptiming.

## 1. General information and documentation

You have been provided with a vehicle. The vehicle is constructed using Lego blocks and works with the Lego Mindstorms EV3 platform.
The computer in the roof of the vehicle runs a linux-based operating system called [ev3dev](https://www.ev3dev.org/), which contains a [micropython](http://micropython.org/) interpreter. 
Using the API Library from Lego, you can interface with the vehicles sensors and actuators to control your vehicle.

You can view the API documentation on [the official pybricks website](https://pybricks.com/ev3-micropython/index.html).

### Sensor mapping
| Port | Type       | Description                                                                                                                                          |
| ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `2`  | `Colour`   | A colour sensor, mounted in the front bumper of the vehicle.                                                                                         |
| `3`  | `Touch`    | A button sensor, mounted under the rear bumper of the vehicle, activated when the rear bumper is being pressed.                                      |
| `4`  | `Infrared` | A distance sensor, mounted in the front bumper of the vehicle, which returns the distance sensed between the sensor and any obstacle in front of it. |

### Actuator mapping
| Port   | Type    | Description                                                                            |
| ------ | ------- | -------------------------------------------------------------------------------------- |
| `outD` | `Motor` | A motor controlling the direction of the steering wheels. Needs centering/calibrating. |
| `outB` | `Motor` | A motor driving the left rear wheel.                                                   |
| `outC` | `Motor` | A motor driving the right rear wheel.                                                  |

## 2. Development Setup
To setup your device for use with Lego Mindstorms EV3 platform, we use a subset of [the instructions provided by Lego](https://pybricks.com/ev3-micropython/startinstall.html). The vehicle should already have been flashed with the appropriate firmware.

### Prequesites:
- A Windows, macOS or Linux laptop with Visual Studio Code and a USB-A port.

### Setting up your IDE:
1. Open Visual Studio Code and install the extension [MicroPython for LEGO® MINDSTORMS® EV3](https://marketplace.visualstudio.com/items?itemName=lego-education.ev3-micropython).
2. Download or copy the example project code from the repository you're currently viewing.
3. Physically connect the vehicle using the provided USB-A (laptop) to Mini-USB (vehicle) cable. 
4. Within vscode, use the "EV3DEV Device Browser" in the left sidebar to connect the software to the vehicle.

## 3. Running your software

You're now able to browse files that are stored on the vehicles controller. It might be a good idea to clear any leftover folders from previous projects. Using the "download" button, you can copy your currently opened file with the software you wrote to the vehicle.

When the file is copied to the vehicle, you can use the LCD-screen and buttons to navigate to and run the file, or use the vscode "run and debug" feature to execute your software. If your vehicle remains connected to your laptop, console output will be available when using the "Run and debug" feature from within vscode, which can be useful for debugging your code.

## 4. Useful notes

To quickly get to a competitive race, below are some important notes to keep in mind when developing your autonomous driving lego vehicle:

- The values you can read and write from and to sensors and actuators may not correspond to any real-life unit and may need calibration or homing, even between runs. How would you command your vehicle to steer "straight"? The example script contains code to "home" the steering motor.

- You only have one sensor measuring the distance in a straight line from the front of the vehicle, however you want to know if your vehicle should drive left, straight or right. Have a brainstorm with your team about how you could achieve this with one sensor.

- The colour sensor may not be useful in the workshop you're attending.

- When using the 'run and debug' feature, `print()` works as usual and you'll get to view any errors that might exist in your software in the console output. It's also possible to use the on-board LCD screen, lights, beeps and text-to-speech modules.

- The diameter of the wheels is roughly 40 mm. The track of the wheels is roughly 120 mm.

- Be careful: using Google you may land on the stable pybricks documentation - however, this differs from the implementaton you're using: you need the [EV3 Documentation](https://pybricks.com/ev3-micropython/)!

- The computer block is reffered to as the "hub" or "EV3 brick" under "[Programmable Hubs](https://pybricks.com/ev3-micropython/hubs.html)" in the documentation, and the sensors and actuators can be found under "[EV3 Devices](https://pybricks.com/ev3-micropython/ev3devices.html)". Using a "DriveBase" object, found under "[Robotics](https://pybricks.com/ev3-micropython/robotics.html)", you can combine two wheel motors into one object. Note that the `turn()` function of the DriveBase object does not refer to using your steering wheels, but rather means "skid-steering" (like a tank) which may not be useful for your case.
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font

# Get sensor instances
colour_sensor = ColorSensor(Port.S2)
bumper_sensor = TouchSensor(Port.S3)
infrared_sensor = InfraredSensor(Port.S4)

# Get motor instances
left_wheel = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.C, Direction.COUNTERCLOCKWISE)
steer = Motor(Port.D, Direction.COUNTERCLOCKWISE)

# Get brick instance
brick = EV3Brick()

def home_steer(steering_motor, duty_limit = 60, speed = 100):
    """
    Home the steering wheel.
    This will recalibrate the steering wheel to make sure that it is centered on 0.
    """
    steering_motor.run_until_stalled(-speed, Stop.COAST, duty_limit) # Rotate the steering motor as far left as possible, until it stalls.
    negative_limit = steering_motor.angle() # Record the current angle as the leftmost angle

    steering_motor.run_until_stalled(speed, Stop.COAST, duty_limit) # Rotate the steering motor as far left as possible, until it stalls.
    positive_limit = steering_motor.angle() # Record the current angle as the rightmost angle

    center_angle = (negative_limit + positive_limit) // 2 # The center angle is the average of the leftmost and rightmost limits.

    steering_motor.run_target(150, center_angle, then = Stop.COAST) # Straighten the wheels
    steering_motor.reset_angle(0) # Set the curent angle as the 0-point

    max_left_angle = int((negative_limit - center_angle) * .9) # Set the leftmost angle, from our new centered point, as the distance between the limit and the center points. Keep a little margin (10%) for error.
    max_right_angle = int((positive_limit - center_angle) * .9) # Set the rightmost angle, from our new centered point, as the distance between the limit and the center points. Keep a little margin (10%) for error.

    return max_left_angle, max_right_angle

def output_text(text):
    """
    Writes text to the LCD screen and debug output.
    """
    brick.screen.print(text)
    print(text)

def main():
    """
    Code body that will be executed on startup.
    """
    # Prepare the LCD-screen
    brick.screen.clear()
    brick.screen.set_font(Font(size=12))

    # Some vehicle settings
    wheel_diameter_mm = 40
    wheel_track_mm = 120
    engine_acceleration = 250
    engine_speed = 200
    steer_speed = 250

    # Print some text to the LCD screen and the debug output
    output_text("RDW Lego")
    output_text("Self Driving Challenge")

    # Prepare the steering of the vehicle by calibrating/homing the steering motor
    output_text("Homing steering wheels...")
    max_left_angle, max_right_angle = home_steer(steer)
    output_text("Done!")

    # Prepare the engine by combining both motors
    output_text("Configuring drivetrain...")
    engine = DriveBase(left_wheel, right_wheel, wheel_diameter_mm, wheel_track_mm)
    engine.settings(straight_speed=engine_speed, straight_acceleration=engine_acceleration, turn_rate=0, turn_acceleration=0)
    output_text("Done!")

    # Make some room by driving backwards until the distance sensor is reporting atleast "50"
    while (infrared_sensor.distance() < 50):
        output_text("Too little space, moving backwards...")
        engine.straight(-100)

    # Wait for bumper touch sensor press
    output_text("Ready.... Set....")
    output_text("(waiting for bumper press)")
    while (not bumper_sensor.pressed()):
        wait(100)
    # Sound a beep, which is required for the competition to allow accurate lap-timing.
    brick.speaker.beep(500, 250)
    # Drive one centimeter
    output_text("GO!")
    engine.straight(10)

    # Dance sequence for demo purposes
    output_text("Starting dancing...")
    brick.speaker.say("Dancing the Self Driving Challenge Dance!")
    brick.speaker.play_notes(['E4/4', 'C4/4', 'D4/4', 'E4/4', 'D4/4', 'C4/4', 'C4/4', 'E4/4', 'B4/4', 'B4/4', 'A4/4', 'A4/4'], tempo=240)
    while (True):
        steer.run_target(steer_speed // 2, max_left_angle // 2)
        steer.run_target(steer_speed // 2, max_right_angle // 2)
        steer.run_target(steer_speed // 2, 0)

        steer.run_target(steer_speed * 2, max_left_angle // 2)
        steer.run_target(steer_speed * 2, max_right_angle // 2)
        steer.run_target(steer_speed * 2, 0)

        steer.run_target(steer_speed * 2, max_left_angle // 2)
        steer.run_target(steer_speed * 2, max_right_angle // 2)
        steer.run_target(steer_speed * 2, 0)

        engine.straight(100)
        engine.straight(-100)

        engine.straight(50)
        engine.straight(-50)

        engine.straight(50)
        engine.straight(-50)

        steer.run_target(steer_speed, max_left_angle)
        engine.straight(100)
        steer.run_target(steer_speed, max_right_angle)
        engine.straight(100)
        steer.run_target(steer_speed, 0)

        steer.run_target(steer_speed, max_left_angle)
        engine.straight(-100)
        steer.run_target(steer_speed, max_right_angle)
        engine.straight(-100)
        steer.run_target(steer_speed, 0)

        steer.run_target(steer_speed, max_right_angle)
        engine.straight(100)
        steer.run_target(steer_speed, max_left_angle)
        engine.straight(100)
        steer.run_target(steer_speed, 0)

        steer.run_target(steer_speed, max_right_angle)
        engine.straight(-100)
        steer.run_target(steer_speed, max_left_angle)
        engine.straight(-100)
        steer.run_target(steer_speed, 0)

if __name__ == '__main__':
    main()
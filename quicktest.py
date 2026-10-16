"""
Quick test: controller input
----------------------------

Checks that the LightTrack connection and the controller work.

What it does:

    1. Connects to LightTrack (1 m to 19 m, 30 LEDs/m).
    2. Uses the first controller pygame finds.
       If there is none, it opens a small window and uses the keyboard:
       Up/Down arrows act like the joystick, Space acts like A.
    3. Prints the joystick, D-pad and A button values ten times per second.

The LEDs do not light up yet. Moving the marker is added in the next steps.

Stop the script with Ctrl+C in the terminal.
"""

from time import sleep

import pygame

from lighttrack import LightTrack

track = LightTrack("/dev/cu.usbmodem1101", 1, 19, 30) # first LED 1m from participant, last LED 19m from participant, 30 LEDs / m

# Use the first controller pygame can find, or the keyboard if there is none.
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() > 0:
    controller = pygame.joystick.Joystick(0)
    controller.init()
    print("Controller:", controller.get_name())
else:
    controller = None

    # pygame only receives key presses while one of its own windows is
    # selected, so open a small one.
    window = pygame.display.set_mode((400, 100))
    pygame.display.set_caption("LightTrack: arrow keys to move, Space to confirm")
    window.fill((30, 30, 30))
    pygame.display.flip()
    print("No controller found, using the keyboard.")
    print("Click the pygame window, then use the arrow keys and Space.")

# Read the input over and over and print what it reports.
# Stop with Ctrl+C in the terminal.
while True:
    pygame.event.pump()

    if controller is not None:
        stick_y = controller.get_axis(1)
        dpad_y = controller.get_hat(0)[1]
        a_pressed = controller.get_button(0)
    else:
        keys = pygame.key.get_pressed()

        # Up/Down arrows act like the stick pushed all the way.
        # Like the stick, up is negative.
        stick_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        dpad_y = 0
        a_pressed = keys[pygame.K_SPACE]

    print(f"stick: {stick_y:+.2f}   dpad: {dpad_y:+d}   A: {a_pressed}")

    sleep(0.1)

import pygame
from picamera2 import Picamera2, Preview
import time
import os

# Initialize Pygame
pygame.init()

# Set up the screen for keyboard input
screen = pygame.display.set_mode((500, 500))

# Initialize the camera
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(camera_config)

# Start the camera preview
picam2.start_preview(Preview.QTGL)
picam2.start()

# Initialize image counter
image_counter = 0

# Set the directory name
directory_name = "amir"

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Take a picture
                directory_path = os.path.join(os.path.dirname(__file__), "dataset", directory_name)
                filename = os.path.join(directory_path, f"image_{image_counter}.jpg")
                picam2.capture_file(filename)
                print(f"Captured {filename}")
                image_counter += 1
            elif event.key == pygame.K_q:  # Quit the program
                running = False

# Cleanup
picam2.stop_preview()
picam2.stop()
pygame.quit()

from picamera import PiCamera
from time import sleep

def test_camera():
    try:
        # Initialize the camera
        camera = PiCamera()
        camera.start_preview()  # Start camera preview
        print("Camera preview started. Testing for 5 seconds...")
        sleep(5)  # Keep the preview running for 5 seconds
        print("Test completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the camera is closed properly
        camera.stop_preview()
        camera.close()

if __name__ == "__main__":
    test_camera()
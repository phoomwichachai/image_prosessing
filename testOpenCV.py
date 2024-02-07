try:
    import cv2
except ImportError as e:
    print(f'install OpenCV using"pip install opencv-python" command')
else:
    print(f'OpenCV installed version: {cv2.__version__}')
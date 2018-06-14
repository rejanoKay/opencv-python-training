import cv2
import numpy as np

def apply_invert(frame):
    return cv2.bitwise_not(frame)

def apply_sepia(frame, intensity=0.5):
    blue, green, red = 20, 66 ,112
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    frame_height, frame_width, frame_channel = frame.shape
    sepia_bgra = (blue,green,red,1)
    
    overlay = np.full((frame_height, frame_width, 4), sepia_bgra, dtype='uint8')
    
    frame = cv2.addWeighted(overlay, intensity, frame, 1.0, 0)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    return frame

cap = cv2.VideoCapture(0) 

while True:
    _, frame = cap.read()
    invert = apply_invert(frame)
    sepia = apply_sepia(frame)
    
    cv2.imshow('frame', frame)
    cv2.imshow('invert', invert)
    cv2.imshow('sepia', sepia)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break
        
cap.release()
cv2.destroyAllWindows()
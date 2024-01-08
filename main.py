

import tensorflow as tf
import mediapipe as mp
from pynput.keyboard import Key, Controller
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import math

# mediapipe varaiable inits
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

#pynbut
keyboard = Controller


# For webcam input:
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    height, width, _ = image.shape ##
    
    if results.multi_hand_landmarks:
      hand_centers = []
      for hand_landmarks in results.multi_hand_landmarks:
        hand_centers.append(
          [int(hand_landmarks.landmark[9].x * width), 
           int(hand_landmarks.landmark[9].y * height)]
          )
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
      if len(hand_centers) == 2:
        cv2.line(image, (hand_centers[0][0], hand_centers[0][1]), (hand_centers[1][0], hand_centers[1][1]),
                 (0,255,0), 5)
        center_x = (hand_centers[0][0] + hand_centers[1][0]) // 2
        center_y = (hand_centers[0][1] + hand_centers[1][1]) // 2
        radius = int(math.sqrt((hand_centers[0][0] - hand_centers[1][0]) ** 2 +
                               (hand_centers[0][1] - hand_centers[1][1]) ** 2) / 2)
        cv2.circle(image, (center_x, center_y), radius, (0,255,0), 5)
        
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
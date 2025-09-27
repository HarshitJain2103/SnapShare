import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
import time
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource (for PyInstaller compatibility). """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

# ==============================================================================
# FINAL, AMBIDEXTROUS GESTURE LOGIC
# ==============================================================================

def is_fist(hand_landmarks, handedness):
    """STRICT VERSION: Checks for a fist on either hand."""
    # Check fingers are curled
    finger_tips = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP
    ]
    pip_joints = [
        mp_hands.HandLandmark.INDEX_FINGER_PIP, mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
        mp_hands.HandLandmark.RING_FINGER_PIP, mp_hands.HandLandmark.PINKY_PIP
    ]
    for i in range(4):
        if hand_landmarks.landmark[finger_tips[i]].y < hand_landmarks.landmark[pip_joints[i]].y:
            return False

    # Check thumb is tucked based on handedness
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]

    if handedness == 'Right':
        if thumb_tip.x < index_finger_mcp.x: return False
    elif handedness == 'Left':
        if thumb_tip.x > index_finger_mcp.x: return False

    return True

def is_open_palm(hand_landmarks, handedness):
    """STRICTER VERSION: Checks for an open palm on either hand."""
    # Check fingers are open
    finger_tips = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP
    ]
    pip_joints = [
        mp_hands.HandLandmark.INDEX_FINGER_PIP, mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
        mp_hands.HandLandmark.RING_FINGER_PIP, mp_hands.HandLandmark.PINKY_PIP
    ]
    for i in range(4):
        if hand_landmarks.landmark[finger_tips[i]].y > hand_landmarks.landmark[pip_joints[i]].y:
            return False

    # Check thumb is out based on handedness
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]

    if handedness == 'Right':
        if thumb_tip.x > index_finger_mcp.x: return False
    elif handedness == 'Left':
        if thumb_tip.x < index_finger_mcp.x: return False
        
    return True

def detect_gesture():
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    window_size = 20
    gesture_window = []
    gesture = None
    last_detected_gesture = None 

    while cap.isOpened() and time.time() - start_time < 7:
        success, image = cap.read()
        if not success:
            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        frame_gesture = None

        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, handedness_info in zip(results.multi_hand_landmarks, results.multi_handedness):
                handedness = handedness_info.classification[0].label

                # Pass handedness to the logic functions
                if is_fist(hand_landmarks, handedness):
                    frame_gesture = "copy"
                elif is_open_palm(hand_landmarks, handedness):
                    frame_gesture = "paste"
        
        if frame_gesture is not None and last_detected_gesture != frame_gesture:
            gesture_window.clear()

        last_detected_gesture = frame_gesture
        gesture_window.append(frame_gesture)
        
        if len(gesture_window) > window_size:
            gesture_window.pop(0)

        # --- OPTIONAL DEBUGGER ---
        # Uncomment the lines below to see the debug text on the screen again
        # copy_count = gesture_window.count("copy")
        # paste_count = gesture_window.count("paste")
        # cv2.putText(image, f"Copy Count: {copy_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        # cv2.putText(image, f"Paste Count: {paste_count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        valid_gestures = [g for g in gesture_window if g is not None]
        if valid_gestures:
            most_common = max(set(valid_gestures), key=valid_gestures.count)
            count = valid_gestures.count(most_common)
            if count / window_size >= 0.8 and len(gesture_window) == window_size:
                gesture = most_common
                break

    cap.release()
    cv2.destroyAllWindows()
    print("detected gesture is :",gesture)
    return gesture

import tensorflow as tf
import mediapipe as mp
from pynput.keyboard import Key, Controller
import multiprocessing as _mp
from src.utility import load_graph, detect_gesture, predict, racing_car
import cv2
import math

# mediapipe varaiable inits
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
# pynput
keyboard = Controller()

# set tf flags
tf.compat.v1.flags.DEFINE_integer("width", 640, "Screen width")
tf.compat.v1.flags.DEFINE_integer("height", 480, "Screen height")
tf.compat.v1.flags.DEFINE_float("threshold", 0.6, "Threshold for score")
tf.compat.v1.flags.DEFINE_float("alpha", 0.3, "Transparent Level")
tf.compat.v1.flags.DEFINE_string("pre_trained_model_path", "src/pretrained_model.pb", "Path to pre_trained_model")
FLAGS = tf.compat.v1.flags.FLAGS


def main():
    graph, sess = load_graph(FLAGS.pre_trained_model_path)
    
if __name__ == '__main__':
    main()



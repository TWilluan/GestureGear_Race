import tensorflow as tf
import mediapipe as mp
from pynput.keyboard import Key, Controller
import multiprocessing as _mp
from utility import load_graph, detect_gesture, predict, racing_car
import cv2
import math

# mediapipe varaiable inits
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
# pynput
keyboard = Controller()
# set tf flags
tf.flags.DEFINE_integer("width", 640, "Screen width")
tf.flags.DEFINE_integer("height", 480, "Screen height")
tf.flags.DEFINE_float("alpha", 0.3, "Transparent Level")
FLAGS = tf.flag.FLAGS


def main():
    # graph, sess = load_graph(FLAGS.pre_trained_model_path)
	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, FLAGS.width)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FLAGS.height)
	mp = _mp.get_context("spawn")
	v = mp.Value('i', 0)
	lock = mp.Lock()
	process = mp.Process(target=racing_car, args=(v, lock))
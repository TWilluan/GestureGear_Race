
import gym
from nes_py.wrappers import JoypadSpace
import tensorflow as tf

def load_graph(path):
    detection_graph = tf.Graph()
    
def detect_gesture():
    print()
    
def predict():
    print()
    
def racing_car(v, lock):
    env = gym.make("CarRacing-v2")
    done = True
    while True:
        if done:
            env.reset(options={"randomize":True})
            with lock:
                v.value = 0
        with lock:
            u = v.value
        _, _, done, _ = env.step(u)
    


import gym
from nes_py.wrappers import JoypadSpace
import tensorflow as tf

# def load_graph(path):
#     detection_graph = tf.Graph()
#     with detection_graph.as_default():
#         graph_def = tf.raw_ops(dtype=tf.dtypes.string, value=path)
#         tf.raw_ops.ParseTensor(dtype=tf.dtypes.string, serialized=graph_def, name="graph_def")
#         tf.raw_ops.ImportGra
        
def load_graph(path):
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        graph_def = tf.compat.v1.GraphDef()
        with tf.compat.v1.gfile.GFile(path, 'rb') as fid:
            graph_def.ParseFromString(fid.read())
            tf.compat.v1.import_graph_def(graph_def, name='')
        sess = tf.compat.v1.Session(graph=detection_graph)
    return detection_graph, sess
    
def detect_gesture(image, graph, session):
    print()
    
def predict(boxes, scores, classes, threshold, width, height, num_hands=2):
    print()
    
def racing_car(v, lock):
    print()
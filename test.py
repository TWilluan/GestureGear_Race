import tensorflow as tf
import os
import urllib3
import numpy as np

import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

print(tf.reduce_sum(tf.random.normal([1000, 1000])))
print("Hello world")
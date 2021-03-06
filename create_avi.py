#!/bin/python
'''
Usage (from parent directory):
# python create_avi --model=Sand
python -m create_avi --model=WaterDropSample

Attention: The folder can currently only contain .pkl files. Otherwise it outputs an error.
'''
from learning_to_simulate.render_rollout_and_save_to_avi import render_rollout 

import pickle

from absl import app
from absl import flags

from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

flags.DEFINE_string("model", None, help="Path to rollout pickle file")
flags.DEFINE_string("base_path", None, help="Path to rollout pickle file")
FLAGS = flags.FLAGS

def render_all(unused_argv):
  
  import os
  
  FLAGS.base_path='./rollouts/'+FLAGS.model
  
  FILES = os.listdir(FLAGS.base_path)
  print('Running over:')
  print(FILES)
  for i in FILES:
    FLAGS.rollout_path = FLAGS.base_path+'/'+i
    render_rollout(None)	
  

if __name__ == "__main__":
  app.run(render_all)
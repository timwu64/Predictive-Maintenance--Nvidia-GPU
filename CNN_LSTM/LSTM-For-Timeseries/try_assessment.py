import unittest
import os
import subprocess
import json
import random
import contextlib
import sys
import numpy as np

import imp
import assignment
imp.reload(assignment)
from assignment import get_model

class TestTask1(unittest.TestCase):
    def test_task1_assess(self):
        pass

#supress output
class DummyFile(object):
    def write(self, x): pass

@contextlib.contextmanager
def nostdout():
        save_stdout = sys.stdout
        save_err = sys.stderr
        sys.stdout = DummyFile()
        sys.stderr = DummyFile()
        try:
            yield
            sys.stdout = save_stdout
            sys.stderr = save_err
        except Exception as e:
            sys.stdout = save_stdout
            sys.stderr = save_err
            raise
    
def runtest():
    try:
        output = -1
        with nostdout():
            x = np.random.rand(3,5,6)
            model = get_model(x)
            
            correct = True
            
            if( not model.layers[0].name.startswith('lstm') or model.layers[0].output_shape != (None, 5, 128)):
                correct = False
            if( not model.layers[1].name.startswith('lstm') or model.layers[1].output_shape != (None, 128)):
                correct = False
            if( not model.layers[2].name.startswith('dense') or model.layers[2].output_shape != (None, 256)):
                correct = False
            if( not model.layers[3].name.startswith('dropout') or model.layers[3].output_shape != (None, 256)):
                correct = False
            if( not model.layers[4].name.startswith('dense') or model.layers[4].output_shape != (None, 128)):
                correct = False
            if( not model.layers[5].name.startswith('dense') or model.layers[5].output_shape != (None, 6) ):
                correct = False

            if (not correct):
                raise ValueError
            
        response = {'score': 100, 'message': 'Your function is correct!'}
        
    except ValueError:
        response = {'score': 0, 'message': 'Your function is incorrect!'}
    except Exception as e:
        response = {'score': 0, 'message': 'Error running assessment: {}'.format(e)}

    return response

print(json.dumps(runtest()))

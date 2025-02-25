"""implementing activation functions described at https://en.wikipedia.org/wiki/Activation_function"""
    
import numpy as np


class ReLU:
    """f(x)= {0  x <=0
              x  x > 0}
    """
    def __call__(self, pre_activated_output):
        return np.where(pre_activated_output <= 0, 0, 1) * pre_activated_output
    
    
class Sigmoid:
    """_summary_
    """
    
class Softmax:
    pass

"""implementing activation functions described at https://en.wikipedia.org/wiki/Activation_function"""
    
import numpy as np


class ReLU:
    """f(x)= {0  x <=0
              x  x > 0}
    """
    def __call__(self, pre_activated_output):
        return np.where(pre_activated_output <= 0, 0, 1) * pre_activated_output
    
    
class Sigmoid:
    """
    f(x) = 1 / (1 + e^(-x))
    """
    
    def __call__(self, pre_activated_output):
        return 1 / (1 + np.exp(- pre_activated_output))
    
    
class Softmax:
    """_summary_ pre_activated_output = [1,2,-3]
       ReLU -> [1,2,0]
    """

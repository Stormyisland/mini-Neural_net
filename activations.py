"""implementing activation functions described at https://en.wikipedia.org/wiki/Activation_function"""
    
import numpy as np


class ReLU:
    """f(x)= {0  x <=0
            
    """
    def __call__(self, pre_activated_output):
        return np.where(pre_activated_output <= 0, 0, 1) * pre_activated_output
    
    
class Sigmoid:
  / (1 + e^(-x))
  
    
   
class Softmax:
  
def __call__(self, pre_activated_output):
    exp_shifted = np.exp(pre_activated_output - np.max(pre_activated_output, axis=1, keepdims=True))
    denominator = np.sum(exp_shifted)
    return exp_shifted / denominator
  
  
  def __call__(self, pre_activated_output):
    exp_shifted = np.exp(pre_activated_output - np.max(pre_activated_output, axis=1, keepdims=True))
    denominator = np.sum(exp_shifted)
    return exp_shifted / denominator
  def __call__()
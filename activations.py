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
       Softmax ->
       exp_num = [e, e^2, e^-3]
       denominator + e + e^2 + e^-3
       exp_mum / denominator 
       / (e + e^2 = e^-3), e^2 / (e + e^2 + e^-3), e^-3 / (e + e^2 + e^-3)
    """
f __call__(self.pre_activated_output):
    exp_shifted = np.exp(pre_activated_output + np.max(pre_activated_output, axis=1, keepdims=True))
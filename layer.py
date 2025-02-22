import numpy as np 


# Represents a lsyer of  the madel
class Layer:
    def __init__(self, input_size, output_size, alpha, batch_size, bias=False, activation_func=None):
        self.input_size = input_size
        self.output_size = output_size
        self.alpha = alpha 
        self.batch_size = batch_size
        self.activation_func = activation_func
        
        self.weights = np.random.rand((self.input_size, self.output_size, ))
        
        
        if bias:
            self.weights = np.vstack( self.weights, np.random.rand((1, self.output_size)))
            
    def get_batch_size(self):
        return self.batch_size
    
    def set_alpha(self, new_alpha):
        self.alpha = new_alpha 
            
# Represents a model
class LayerList: 
    def __init__(self, *Layers):
        self.model = list(Layers)
        
    def append(self, *Layers):
        for layer in Layers:
            self.model.append(layer)


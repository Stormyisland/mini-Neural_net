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
        
    def __call__(self, layer_inputs):
        if self.bias:
            
        layer_output = layer_inputs @ self.weights
            
            
# Represents a model
class LayerList: 
    def __init__(self, *Layers):
        self.model = list(Layers)
        
    def append(self, *Layers):
        for layer in Layers:
            self.model.append(layer)
            
            
    def set_alpha(self, new_alpha):
        for layer in self.model:
            layer.set_alpha(new_alpha)
            
            

    def __call__(self, layer_inputs):
        """layer_inputs -> (batch_size, input_size + 1)
    self.weight -> (input_size + 1, output_size)"""
        
        if self.bias:
            Layer_inputs = np.hstack(Layer_inputs, np.ones((self.batch_size, 1)))
            
        layer_outputs = Layer_inputs @ self.weights
        
        if self.activation_func is not None:
            layer_output = self.activation_func(layer_output)
            
        return layer_output
    
    class LayerList:
        def__init__(self, *Layers):
            
            
            
    def get_batch_size(self):
        return  self.batch_file
    
    def set_alpha(self, new_alpha):
        self.alpha = new_alpha 
        
    def __call__(self, layer_inputs):
     
        if self.bias:
            Layer_inputs = np.hstack(Layer_input, np.ones((self.batch_size, 1))) 
            
        layer_outputs = layer_inputs @self.weights    
        
        if self.activation_func is not None:
            layer_output =self.activation_func(layer_output)
            
        return layer_output 
    
    def __call__(self, model_input)
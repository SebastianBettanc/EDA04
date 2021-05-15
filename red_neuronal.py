import math as mt
import random 

class Neuron:
    def __init__(self,value,layer,weights):
        self.value=value
        self.layer=layer
        self.weights=weights

    def activation(self):
        f=1/(1+mt.exp(-self.value))
        return f

    def derivate(self):
        f=self.activation()*(1-self.activation())
        return f      

class Red:

    def __init__(self,layers):
        self.layers=layers

    def CrearRedVacia(self):
        self.layers=list()
        return None

    def AgregarCapa(self,numero_neuronas):

        layer=list()
        l=len(self.layers)

        if l>0:
            
            for i in range(numero_neuronas):
                
                weights=list()

                for neuron in self.layers[-1]:
                    weight=random.uniform(0,100)
                    weights.append(weight)
                A=Neuron(None,self.layers[-1],weights)
                layer.append(A)

        else:        
            for i in range(numero_neuronas):  
                A=Neuron(None,None,None)
                layer.append(A)

        self.layers.append(layer)    

        return None

    def calculaValor(self,Neuron):
        Layer=Neuron.layer
        Weights=Neuron.weights
        total=0
        for i in range(len(Layer)):
            total+=Layer[i].activation()*Weights[i]
        return total

    def predict(self,input):

        
        for i in range(len(self.layers[0])):
            self.layers[0][i].value=input[i]

        for k in range(1,len(self.layers)):
            for j in range(len(self.layers[k])):
                Neuron=self.layers[k][j]
                self.layers[k][j].value=self.calculaValor(Neuron)
    
        predict=list()

        for n in range(len(self.layers[-1])):
            values=self.layers[-1][n].value 
            predict.append(values)

        return predict


r =Red(None)
r.CrearRedVacia()
r.AgregarCapa(5)
r.AgregarCapa(4)
r.AgregarCapa(5)
r.AgregarCapa(2)

ini_output=[30,40,60,10,4]
output= r.predict(ini_output)

print (output)
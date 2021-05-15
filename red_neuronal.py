import math as mt
import random 

class Neuron:
    def __init__(self,value,layer,weights,weights_aux,next_layer):#
        self.value=value
        self.layer=layer
        self.weights=weights
        self.weights_aux=weights_aux
        self.next_layer=next_layer

    def activation(self):
        f=1/(1+mt.exp(-self.value))
        return f

    def derivate(self):
        f=self.activation()*(1-self.activation())
        return f

    def calculaNuevoPeso(self,learningRate,valorESperado):

        if self.next_layer==None:
            delta=(self.activation()-valorESperado)*self.derivate()
        else:
            sumatoria=0
            for neuron in self.next_layer:

                delta_i= (neuron.activation()-valorESperado)

                for weight in self.weights:
                    sumatoria+=delta_i*weight
            delta=sumatoria*self.derivate()

        gradient=delta*self.activation()
        aux=list()

        for weight in self.weights:
            new_weight=weight -learningRate*gradient
            aux.append(new_weight)
            
        self.weights_aux=aux

        return None          

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
                    weight=random.random()
                    weights.append(weight)
                A=Neuron(None,self.layers[-1],weights,None,None)
                layer.append(A)

        else:        
            for i in range(numero_neuronas):  
                A=Neuron(None,None,None,None,None)
                layer.append(A)

        self.layers.append(layer)    

        return None

    def next_layers(self):

        for i in range(len(self.layers)-1):
            for neuron in self.layers[i]:
                neuron.next_layer=self.layers[i+1]

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
r.next_layers()

ini_output=[30,40,60,10,4]
output= r.predict(ini_output)

print (output)


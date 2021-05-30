import random
import leercsv
import matplotlib.pyplot as plt
import numpy as np
import math as mt

class Neuron:

    def __init__(self,value,prev_layer,weights,next_layer,delta,aux_w):#
        self.value=value
        self.prev_layer=prev_layer #layer de la capa anterior
        self.weights=weights #pesos hacia atras
        self.next_layer=next_layer
        self.delta=delta
        self.aux_w=aux_w

def sigmoid(value):
    f=1/(1+np.exp(-value))
    return f

def derivate(value):
    f=sigmoid(value)*(1-sigmoid(value))
    return f


class Red:

    def __init__(self,layers):
        self.layers=layers

    def CrearRedVacia(self):
        self.layers=list()
        return None

    def AgregarCapa(self,numero_neuronas):

        layer=list()

        if len(self.layers)>0:
            
            for i in range(numero_neuronas):

                weights=list()
                weights=np.random.randn(len(self.layers[-1]))
                new_neuron=Neuron(None,self.layers[-1],weights,None,None,None)
                layer.append(new_neuron)

            for neuron in self.layers[-1]:
                neuron.next_layer=layer
            
        else:        
            for i in range(numero_neuronas):  
                new_neuron=Neuron(None,None,None,None,None,None)
                layer.append(new_neuron)

        self.layers.append(layer)    

        return None

    def calculaValor(self,neuron):

        layer=neuron.prev_layer
        weights=neuron.weights
        total=0
        bias=0.0 #

        for i in range(len(layer)):
            total+=layer[i].value*weights[i]

        return (sigmoid(total+bias))

    def forward_propagation(self,input):
        layers=self.layers
        first_layer=layers[0]
        for i in range(len(first_layer)): 
            self.layers[0][i].value=input[i]

        for layer in layers[1:] :
            for neuron in layer:
                neuron.value=self.calculaValor(neuron)         

        predict=list()
        for neuron in layers[-1]:
            predict.append(neuron.value)

        return predict

    def back_propagation(self,expected,learningRate):

        for layer in reversed(self.layers[1:]):

            pos=0
            for neuron in layer:

                if (neuron.next_layer!=None):
                    delta=0

                    for x in range(len(neuron.next_layer)):
                        delta+=neuron.next_layer[x].delta*neuron.next_layer[x].weights[pos]
                        
                    neuron.delta=delta
                    new_weights=list()

                    for y in range(len(neuron.prev_layer)):
                        gradient=delta*neuron.prev_layer[y].value
                        new_w=neuron.weights[y]-learningRate*gradient
                        new_weights.append(new_w)

                    neuron.aux_w=new_weights

                else:

                    delta=(expected-neuron.value)*(neuron.value)*(1-neuron.value)
                    neuron.delta=delta
                    new_weights=list()

                    for x in range(len(neuron.prev_layer)):
                        gradient=delta*neuron.prev_layer[x].value
                        new_w=neuron.weights[x]-learningRate*gradient
                        new_weights.append(new_w)
                    neuron.aux_w=new_weights

                pos+=1
        
    def update_weights(self):
        
        for layer in reversed(self.layers[1:]):
            
            for neuron in layer:  
                neuron.weights=neuron.aux_w

    def training(self,samples,learningRate,epoch):

        error_plot=[]

        for x in range(epoch):
            for sample in samples:
            
                expected_value=sample[0]
                input=sample[1]
                self.forward_propagation(input)
                self.back_propagation(expected_value,learningRate)
                self.update_weights()
            ecm=0
            for node in self.layers[-1]: 
                ecm+=( node.value-expected_value )**2
            error_plot.append(ecm)

        return error_plot
    def accuracy(self,samples):

        right=0
        for sample in samples:
            expected_value=sample[0]
            input=sample[1]
            self.forward_propagation(input)
            for node in self.layers[-1]: 
                error=( node.value-expected_value )
            if (error<=0.01):
                right+=1




        acc=(right/len(samples))*100

        return acc

learningRate=0.1  #0.05
path="data.csv"
input_lenght=13

r =Red(None)                
r.CrearRedVacia()          
r.AgregarCapa(input_lenght)
r.AgregarCapa(10)
r.AgregarCapa(7)
r.AgregarCapa(1)

A=leercsv.read_dataset(path)
samples=random.sample(A,len(A))



sample_train=samples[0:1401]
sample_test=samples[1401:]


 
training=r.training(sample_train,learningRate,100)
acurracy=r.accuracy(sample_test)


print("el acurracy es de :",acurracy)

plt.grid()
plt.plot(range(100),training)
plt.title('Error vs numero de iteraciones')
plt.xlabel('Numero de iteracion') 
plt.ylabel('Error cuadrado')
plt.show()


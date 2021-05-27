import math as mt
import random
import leercsv
import matplotlib.pyplot as plt

class Neuron:

    def __init__(self,value,layer,weights,weights_aux,next_layer,delta):#
        self.value=value
        self.layer=layer
        self.weights=weights #pesos hacia atras
        self.weights_aux=weights_aux#pesos hacia atras
        self.next_layer=next_layer
        self.delta=delta

    def activation(self):
        f=1/(1+mt.exp(-self.value))
        return f

    def derivate(self):
        f=self.activation()*(1-self.activation())
        return f

    def calculaNuevoPeso(self,learningRate,valorESperado):

        delta=0
        aux=list()  #pos
        
        if self.next_layer==None:
            
            delta=(self.activation()-valorESperado)*self.derivate()
            self.delta=delta

            for i in range(len(self.layer)): #layer anterior
                gradient=self.layer[i].activation()*delta
                new_weight= self.weights[i]-(learningRate*gradient)
                aux.append(new_weight)
            self.weights_aux=aux
        else:       

            sumatoria=0

            layer=self.next_layer

            for i in range(len(layer)): #neuron  
                weights=layer[i].weights
                for j in range(len(weights)): # pesos de cada neurona                                               
                    sumatoria+=layer[i].delta*weights[i]
           
            delta=(sumatoria)*self.derivate() #cambiar deltas
            self.delta=delta

            for i in range(len(self.layer)): 
                gradient=self.layer[i].activation()*delta
                new_weight= self.weights[i]-(learningRate*gradient)
                aux.append(new_weight)
            self.weights_aux=aux

        return None

    def new_weights(self):
        self.weights=self.weights_aux
           
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
                new_neuron=Neuron(None,self.layers[l-1],weights,None,None,None)
                layer.append(new_neuron)

        else:        
            for i in range(numero_neuronas):  
                new_neuron=Neuron(None,None,None,None,None,None)
                layer.append(new_neuron)

        self.layers.append(layer)    

        return None

    def calculaValor(self,neuron):

        layer=neuron.layer
        weights=neuron.weights
        total=0
        for i in range(len(layer)):
            total+=layer[i].activation()*weights[i] 
        value= total #+ bias
        return total

    def predict(self,input):
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

    def next_layers(self):

        for i in range(len(self.layers)-1): 

            for j in range(len(self.layers[i])):

                self.layers[i][j].next_layer=self.layers[i+1]
        return None


    def actualizaPesos(self,learningRate,valorEsperado): 
        
        aux=self.layers[1:]
        aux.reverse()

        for layer in aux: 
            for neuron in layer:
                neuron.calculaNuevoPeso(learningRate,valorEsperado)
                neuron.weights=neuron.weights_aux


        return None

    def entrenar(self,instancias_entrenamiento,learningRate): #lista de tests

        L=instancias_entrenamiento      #numIteraciones = len de instancias_entrenamiento
        tests=random.sample(L,len(L))

        input=tests[0][1]
        expected_value=tests[0][0]
        data_predicted=self.predict(input)#                 retorna el valor de la prediccion hecha

        self.actualizaPesos(learningRate,expected_value)#   valor_esperado de la instancia_entrenamiento aqui xd

        errors=[]
        ecm=0
        for node in self.layers[-1]: 
            ecm+=(1/len(self.layers[-1]))*( node.value-expected_value )**2
            errors.append(ecm*0.5)
        #print("numero de iteracion :",1,"\nvalor predicho por la red :" ,data_predicted,"\nvalor esperado de la red :",expected_value)
        #print("error cuadrado medio :",ecm)  

        x=2
        for test in tests[1:]:#                                     largo del dataset
            input=test[1]
            expected_value=test[0]
            data_predicted=self.predict(input)#                 retorna el valor de la prediccion hecha
            

            self.actualizaPesos(learningRate,expected_value)#   valor_esperado de la instancia_entrenamiento aqui xd

            ecm=0
            for node in self.layers[-1]: 
               ecm+=(1/len(self.layers[-1]))*( node.value-expected_value )**2
            errors.append(ecm*0.5)
            #print("numero de iteracion :",x,"\nvalor predicho por la red :" ,data_predicted,"\nvalor esperado de la red :",expected_value)
            #print("error cuadrado medio :",ecm)
            x+=1               

        return errors

    def tests (self,instancias_pruebas,numIteraciones):

        L=instancias_pruebas
        tests=random.sample(L,len(L))
        predictions=list() # lista para guardar , inutil x ahora

        for x in range(numIteraciones):

            date_predicted=self.predict(tests[x][1])#retorna el valor de la prediccion hecha #predictions.append(date_predicted) # lista con valores de la neurona #retorna lista pre
            data_red=round(date_predicted[-1],2) #error del 1%
            print("numero de iteracion :"+x+"\nvalor predicho por la red :" + label(data_red)+"\nvalor esperado de la red :"+label(tests[x][0]))
        return None    


def generate_text(key):

    texts={1:""

    }

    return texts[key]

def label(key): #crear epsilon 



    
    dictionary={0.0: "Polera"   ,
                1.0: "Pantalón",
                2.0: "sweater",
                3.0: "Vestido",
                4.0: "Saco",
                5.0: "Sandalia",
                6.0: "Camisa",
                7.0: "Zapatilla",
                8.0: "Bolso/cartera",
                9.0: "Bota"}

    if key in dictionary:
        return dictionary[key]
    else:
        return "No es ropa"

learningRate=0.05
pixels_total=784
archive_1="fashion-1.csv"
archive_2="fashion-2.csv"

r =Red(None)                #70% del dataset = entrenamiento ; 30% del dataset siguiente es para test ( ver que wea es con los pixeles que le doi) , funcion leer dataset
r.CrearRedVacia()           #predecir cuando este entrenada la red , por default aun esta sin entrenar (pesos aleatorios tira cualquier wea),
r.AgregarCapa(pixels_total) # CALMAO 
r.AgregarCapa(10) #pixels_total
r.AgregarCapa(10)
r.AgregarCapa(1)
r.next_layers()#calculo y la wea
#
#void calculaNuevoPeso(learningRate, valorEsperado):
#    List neuronas
#    List pesosNeuronasAux
#    for neurona in neuronas:
#       delta_actual = ((1/(1+e^-x))- valorEsperado)*    ((1/(1+e^-x)(1 - (1/(1+e^-x)))
#       Gradiente = delta * neurona.retornaValor()
#       nuevo_peso = neurona.peso - learningRate*Gradiente
#       pesosNeuronasAux.push(nuevo_peso)
#


A=leercsv.read_dataset(archive_1) # me retorna solo training por ahora


#A=[(1,[100,40,50]),(2,[33,70,200]),(3,[200,160,102]),(4,[33,40,130])]

mc=r.entrenar(A,learningRate)


plt.grid()
plt.plot(range(2000),mc)
plt.title('Error vs numero de iteraciones')
plt.xlabel('Numero de iteracion') 
plt.ylabel('Error cuadrado')
plt.show()

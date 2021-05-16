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
                new_neuron=Neuron(None,self.layers[-1],weights,None,None)
                layer.append(new_neuron)

        else:        
            for i in range(numero_neuronas):  
                new_neuron=Neuron(None,None,None,None,None)
                layer.append(new_neuron)

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
            for neuron in self.layers[k]:
                neuron.value=self.calculaValor(neuron)
    
        predict=list()

        for neuron in self.layers[-1]:
            predict.append(neuron.value)

        return predict

    def actualizaPesos(self,learningRate,valorEsperado):

        for layer in reversed(self.layers):
            for neuron in layer:
                neuron.calculaNuevoPeso(learningRate,valorEsperado)

        for layer in self.layers:
            for neuron in layer:
                neuron.weights.clear()
                neuron.weights=neuron.weights_aux

        return None

    def entrenar(self,instancias_entrenamiento,numIteraciones,learningRate): #lista de inputs , valor esperado numero 0 del csv # ,valor_esperado 

        L=instancias_entrenamiento      #numIteraciones = len de instancias_entrenamiento
        tests=random.sample(L,len(L))
        predictions=list()

        
        for x in range(numIteraciones):         #700

            date_predicted=self.predict(tests[x][1])#retorna el valor de la prediccion hecha
            self.actualizaPesos(learningRate,tests[x][0]) #valor_esperado de la instancia_entrenamiento aqui xd
                                                #predictions.append(date_predicted)

            if x%5==0:
                #calcular_error
                ecm=0
                print("numero de iteracion :"+x+"\nvalor predicho por la red :" + date_predicted+"\nvalor esperado de la red :"+tests[x][0])
                for node in self.layers[-1]: 
                    ecm+=(1/len(self.layers[-1][-1]))*(node.value-tests[x][0])**2
                print("error cuadrado medio :"+ecm)                   #IMPRIMIR EN PANTALLA 
                #print('cls') limpiar pantalla



        return None
    def tests (self,instancias_pruebas,numIteraciones):

        L=instancias_pruebas
        tests=random.sample(L,len(L))
        predictions=list() # lista para guardar , inutil x ahora

        for x in range(numIteraciones):

            date_predicted=self.predict(tests[x][1])#retorna el valor de la prediccion hecha #predictions.append(date_predicted) # lista con valores de la neurona #retorna lista pre
            data_red=round(date_predicted[-1],2) #error del 1%
            print("numero de iteracion :"+x+"\nvalor predicho por la red :" + label(data_red)+"\nvalor esperado de la red :"+label(tests[x][0]))
        return None    



def leer_dataset():
    ruta="ruta.png"# funcion get para instalar #70% de las lineas es para entrenar (le paso pixeles y paso el valor esperado (0 a 9), el otro 30% de los casos le paso pixeles)
                    # y me retorna el numero de que cree que es

    L=list()
    L.append(1)
    L.append(2)
    L.append(3)
    return L

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

#ini_output=[30,40,60,10,4]  # en ini input, van los pixeles ## LEER CSV  

#accurracy (%de diferencia xd)

#L=leer_dataset()
#tests_entrenamiento=L[0] # =[ A_1,A_2 ],lista con todos los tests de entrenamiento cada elemento es una  
#tests_pruebas=L[1]       # lista con el dataset y el valor esperado([1,2,3,4,etc.],9) =A
learningRate=0.7
pixels_total=784

r =Red(None)                #70% del dataset = entrenamiento ; 30% del dataset siguiente es para test ( ver que wea es con los pixeles que le doi) , funcion leer dataset
r.CrearRedVacia()           #predecir cuando este entrenada la red , por default aun esta sin entrenar (pesos aleatorios tira cualquier wea),
r.AgregarCapa(pixels_total) # CALMAO 
r.AgregarCapa(pixels_total)
r.AgregarCapa(pixels_total)
r.AgregarCapa(pixels_total)
r.AgregarCapa(1)
r.next_layers()

#r.entrenar(tests_entrenamiento,len(tests_entrenamiento),learningRate)
#r.tests(tests_pruebas,len(tests_pruebas))




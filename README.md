# EDA04

🟦Nombre:Sebastian Bettancourt Villaseca Rut:19341715-9


Estructura de datos y algoritmos avanzados , Problema 4 redes neuronales

Instrucciones para instalar

Tener instalado python 3.6; 3.7 o 3.8

Correr el archivo neuron.py

-----------------------------------------------------


# 🟥Explicacion problema

Nuestro problema consiste en predecir si una cancion le gusta a un usuario , dado distintos parametros de esta

Nuestro dataset estara conformado por aproximandamente 2018 canciones , a continuacion veremos como esta conformado:

![dataset](https://user-images.githubusercontent.com/82010968/120158518-390e8080-c1c2-11eb-8bf8-bb320cd1d39f.png)

Donde a nosotros no nos interesa ni la id ni el nombre, trabajeremos con los demas parametros de a continuacion:


atributo | valores
-------------|----------------------------------------------------------------------------------------------
Acoustiness  		|[0-1] medida de qué tan acústica es la canción.
danceability  |Float [0-1] medida de qué tan bailable es la canción.
duration_ms 	|Entero. duración en ms de la canción. **valor max=1004627**
energy  		|Float [0-1] medida conceptual de la intensidad y actividad de una canción.
instrumentalness|Float [0-1] medida de qué tan seguro está el algoritmo de que no hay partes vocales en la canción.
key 			|Entero [0-11] el tono de la canción
liveness  	|Float [0-1] medida de qué tan seguro está el algoritmo de que hay público en vivo.
loudness 	 |Float. el promedio en ruidez de una canción, el rango tiende a ser entre -60 y 0 db **valor max=-33**
mode   			|Entero modalidad (mayor o menor)(1 o 0 respectivamente) de la canción.
speechiness	 |Float [0-1] medida de qué tan presente son las palabras habladas dentro de la canción
tempo 		|Float. el tempo estimado de la canción, en bpm. **valor max=219.331**
time_signature|Entero [1-5] medida del compás de la canción.
valence 	|Float [0-1] medida que está relacionada con la positividad de una canción.
**target** |Binario [0-1] si al usuario le gustó la canción o no. *Valor Esperado*


Para predecir si una cancion en particular le gusta o no al usuario utlizaremos una red neuronal.

Esta red neuronal predice valores dado un vector. 

Estos valores predichos en un principio seran muy inexactos (seran muy distintos al valor esperado), para que estos valores predichos sean mas precisos a nuestra red la alimentaremos con casos de pruebas para que asi "aprenda" a predecir mejores valores, estos casos de prueba corresponderan a 1400 canciones tomadas al azar del dataset. 




---------------------------------------------------

 
# 🟩Neural network 

Una red neuronal


consiste de neuronas dentro de capas , existen 3 tipos de capas , input layer , hidden layers y output layers. 


![Hidden-layrs-1-i2tutorials](https://user-images.githubusercontent.com/82010968/120152084-090faf00-c1bb-11eb-817a-b5ecde4f29d4.jpg)


la capa de input layer , recibe el vector de valores y cada valor del vector se lo asigna a cada neurona de la capa de input.

Para nuestro caso particular input layer sera de largo 13 y recibira el onehotcoding del vectorA *(ver figura 1)*:


**onehotcoding(A)** consiste en que el vectorA solo entrege valores entre 0 y 1(normalizarlo)

Para la primera iteracion los pesos seran aletorios.












las capas hidden layer , calculan sus valores 



------------------------------------------


  

------------------------------






-------------------------

🟪Seccion1


🔴Resultados


------


⬛VIDEO EXPLICATIVO LINK = https://youtu.be/3fYE5sh8Ijw


Coevaluacion 
Sebastian :+0

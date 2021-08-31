# EDA04

🟦Nombre:Sebastian B.

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

***tabla1***


Para predecir si una cancion en particular le gusta o no al usuario utlizaremos una red neuronal.

Esta red neuronal predice valores dado un vector. 

Estos valores predichos en un principio seran muy inexactos (seran muy distintos al valor esperado), para que estos valores predichos sean mas precisos a nuestra red la alimentaremos con casos de pruebas para que asi "aprenda" a predecir mejores valores, estos casos de prueba corresponderan a 1400 canciones tomadas al azar del dataset. 




---------------------------------------------------

 
# 🟩Neural network 

La red neural consiste en layers (capas) con neuronas dentro de estas, existen 3 tipos de layers , input , hidden y output layer. a las neuronas de la layer input le entregaremos valores los cuales serviran para calcular los valores de las demas neurondas en las otras layers , para al final generar un valor de output (valor predicho por la red) en la ultima layer 


Nuestra red neural contendra  1 layer de input , 2 layers hidden y 1 layer de output; Se inicializara con pesos aletorios.

La layer de input tendra 13 neuronas, cada neurona corresponde al valor de los atributos de la tabla 1 normalizada menos el valor de target 

 
atributos a normalizar tabla 1 |
---------------------|
*duration_ms/1004627 |
*loudness/33         |
*tempo/219.331       |
*time_signature/5    | 

la tabla se normaliza para solo tenga valores entre 0 y 1 , antes de ingresarlo a la layer de input.

la segunda layer contendra 10 neuronas , la tercera 7 neuronas y finalmente la layer de output 1 neurona

![red](https://user-images.githubusercontent.com/82010968/120174440-19338880-c1d3-11eb-81f2-7873b15a5233.png)


Para calcular los valores de la segunda layer en adelante dependera de los pesos y valores de la layer anterior junto a una funcion de activacion (sigmoide).

A continuacion se explicara como calcular el valor de 1 neurona:

---------
El valor de 1 neurona que no sea input viene dado por:

![forward_formula](https://user-images.githubusercontent.com/82010968/120178263-526df780-c1d7-11eb-8fc8-322a0d943165.png)

Donde wi=pesos y v1=valores de la neurondas anteriores

-------
Al valor obtenido de la sumatoria anterior se le aplica la funcion sigmoide :

![sigmoid](https://user-images.githubusercontent.com/82010968/120178269-5437bb00-c1d7-11eb-8726-b96be7d412f0.png)

-------
A continuacion se muestra un ejemplo :

![ej_forward](https://user-images.githubusercontent.com/82010968/120179510-aa592e00-c1d8-11eb-863c-7136cbaf9f06.png)


Se repetira el proceso para todas las neuronas de la red hasta obtener un valor de output, a este proceso se le denomina forward propagation.

El valor del output correspondera al valor predicho por la red,se calculara el error entre este valor predicho y el valor esperado ,para calcular el error de una prediccion se usa la formula:

![error](https://user-images.githubusercontent.com/82010968/120179710-ec826f80-c1d8-11eb-98f9-851fc2f52f6f.png)

donde 𝑦=valor predicho e 𝑦^=valor esperado 


Para que la red "aprenda" debe mimizar este error lo mas posible, para lograr esto tiene que ir ajustando todos los pesos de la red de manera que la prediccion sea mas "certera". Este proceso se demonia back propagation.

Back propagation va ajustando los pesos desde la layer de output hacia input, la cantidad que tiene que modificar cada peso depende de un delta,learningRate (valor constante) y los valores de la neurona de la capa actual con la anterior.

Primero se calculara el delta de la neurona.

Si la neurona es de la layer de output, su delta viene dado por la formula de :

!formula delta output

Si la neurona es de una layer hidden , su delta viene dado por la formula de:

!formual delta normal

La formula para cambiar los pesos es de :

!formula cambiar pesos

Notar que una vez calculados los pesos nuevos los guardamos en una variable , no actualizamos la red con estos nuevos pesos inmediatamente ya que los deltas de las neuronas de las layers hidden depende de los pesos no modificados de esta. 

Una vez calculados todos los pesos nuevos, updateamos la red con los nuevos valores .

Este proceso se repite con el training de datos (forward propagation,back propagation , update_pesos), (1400 veces ,70% de las canciones) 
y repetimos el proceso anterior una cantidad epoch=100.


Una vez entrenada nuestra red , simplemente calculamos su % de valores correctos con el 30% de las canciones con la que no entrenamos la red.















------------------------------------------



🟪


🔴Resultados


------


⬛VIDEO EXPLICATIVO LINK = https://youtu.be/3fYE5sh8Ijw


Coevaluacion 
Sebastian :+0

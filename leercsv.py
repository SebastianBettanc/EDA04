import numpy as np

def read_dataset(path): 

    cols=[]
    for k in range(1,15):
        cols.append(k)


    trainig_N= np.loadtxt(path,skiprows=1,delimiter=',',usecols=cols,encoding="utf8") 
        

    training=list()

    for row in trainig_N:
        
        aux=list()
        aux.append(row[0])
        aux.append(row[1])
        aux.append(row[2]/1004627) #/1004627
        aux.append(row[3])
        aux.append(row[4])
        aux.append(row[5]) 
        aux.append(row[6])
        aux.append(row[7]/33) #/33
        aux.append(row[8])
        aux.append(row[9])
        aux.append(row[10]/219.331) #/219.331  #
        aux.append(row[11]/5)  #/5
        aux.append(row[12])
   
        value=(row[-1],aux)
        training.append(value)



    return training

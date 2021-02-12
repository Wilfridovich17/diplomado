import random
import numpy as np


data_test = list(np.array(np.random.rand(50)*100).astype(int))

"""
Input: Un valor de comparación, lista de elementos

Output: Dos listas, una que tiene elementos menores o iguales al elemento de comparación 
        y otra con el resto de los elementos
"""
def compare(element, lista):
    x, y = [i for i in lista if i<=element],[i for i in lista if i>element]  
    return x,y

"""
Input: Una lista a ordenas

Output: Lista ordenada
"""
def sort(lista):
    #Donde se pondrá la lista ordenada
    lista_nueva = []
    #Caso general
    if len(lista) > 2:
        #Selecciona un elmento al azar de la lista por medio de su posición
        pos = random.randint(0,len(lista)-1)
        
        #Separa el elemento seleccionado
        selected_element = lista[pos]
        
        #Sacalo de la lista
        lista.pop(pos)
        
        # Genera dos grupos usando comparar
        s_1, s_2 = compare(selected_element, lista)
        
        #Si s_1 tiene elementos, se agregan de forma ordenada al a lista
        if len(s_1) > 0:
            lista_nueva.extend(sort(s_1))
            
        #Se agrega el elemento extraído
        lista_nueva.append(selected_element)
        
        #Si s_2 tiene elementos, se agregan de forma ordenada al a lista
        if len(s_2) > 0:
            lista_nueva.extend(sort(s_2))
        return lista_nueva
    
    #Casos base
    ##Si la lista es de longitud 2
    elif len(lista) == 2:
        #Si están en deseorden se regresa la lista ordenada
        if lista[0]>lista[1]:
            return [lista[1],lista[0]]
        #Si están en orden se regresa la lista ordenada
        else:
            return lista
    ##Si la lista de es longitud 1 o 0.
    else:
        return lista
        
#Se muestra un ejemplo de ordenamiento
print(sort(data_test))

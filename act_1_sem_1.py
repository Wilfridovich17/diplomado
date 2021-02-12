import numpy as np

lista = [34,478,233,13]
lista_random = list(np.array(np.random.rand(50)*100).astype(int))

def my_sort(data_test):      
    for i in range(len(data_test)):
        for j in range(i+1,len(data_test)):
            if data_test[i] > data_test[j]:
                data_test[i],data_test[j] = data_test[j], data_test[i]     
    return data_test

print(my_sort(lista))
print(my_sort(lista_random))

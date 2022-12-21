#Creación de matrices:

import pprint

mtx_abc = [[chr(65 + (x * 5) + i) for i in range(5)] for x in range(5)]


mtx_abc2 = []
for x in range(5):
    row = []
    for i in range(5):
        #row.append(chr(65 + (x * 5) + i))
        row.append("X")
    mtx_abc2.append(row)

pprint.pprint (mtx_abc)    
print ("_______________________________")
pprint.pprint (mtx_abc2)
print ("asdasd")

#se añade u  comentario a la matriz
print("daniela tiene un culazo")
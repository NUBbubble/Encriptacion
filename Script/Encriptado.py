import numpy as np
Diccionario = {
    "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, 
    "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, 
    "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25, " ":26
}

DiccionarioInvertido = {
    0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 
    10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 
    19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z", 26:" ",
}

MatrizA=[[],[],[]]
TextoNumerado=[]
print('     ENCRIPTACIÓN')
print()
texto=input('Dame tu nombre:')
texto=texto.upper()
Texto=''
for NoÑ in texto:
    if NoÑ=='Ñ':
        NoÑ='N'
    Texto+=NoÑ
#Añadir Espacios
while len(Texto)%3!=0:
    Texto=Texto+' '
#Creacion de MatrizA
Count=0
for Letra in Texto:
    if Count==3:
        Count=0
    MatrizA[Count].append((Diccionario[Letra]))
    Count+=1
#Matriz Llave
MatrizB=[
    [35,53,12],
    [12,21,5],
    [2,4,1]
]
#Matriz A'
MatrizA=np.array(MatrizA)
MatrizB=np.array(MatrizB)
MatrizAprima=MatrizB@MatrizA
#Matriz C
MatrizC=[]
columna = []
for Modulo28 in MatrizAprima:
    for elemento in Modulo28:
        columna.append(int(elemento % 27))
        if len(columna)==len(MatrizAprima[0]):
            MatrizC.append(columna)
            columna = [] 
print('     Encriptado')
Count=0
CountA=0
for Mantener in range(3):
    for Posicion in range(len(MatrizC[0])):
        if Count==3:
            CountA+=1
            Count=0
        print(DiccionarioInvertido[MatrizC[Count][CountA]],end='')
        Count+=1
print()

"Desencriptacion"
"Hacer Matriz Inversa de B"
MatrizInversaB=[
    [1,-5,13],
    [-2, 11, -31],
    [6,-34,99]
]
MatrizBInversa=[]
columna=[]
for Modulo28 in MatrizInversaB:
    for elemento in Modulo28:
        columna.append(int(elemento % 27))
        if len(columna)==3:
            MatrizBInversa.append(columna)
            columna = [] 
MatrizBInversa=np.array(MatrizBInversa)
MatrizC=np.array(MatrizC)
ProductoBmC=MatrizBInversa@MatrizC
columna=[]
BIMod28=[]
for Modulo28 in ProductoBmC:
    for elemento in Modulo28:
        columna.append(int(elemento % 27))
        if len(columna)==len(MatrizAprima[0]):
            BIMod28.append(columna)
            columna = [] 
BIMod28=np.array(BIMod28)
CountA=0
Count=0
print('     Desencriptado')
for Mantener in range(3):
    for Posicion in range(len(BIMod28[0])):
        if Count==3:
            CountA+=1
            Count=0
        print(DiccionarioInvertido[BIMod28[Count][CountA]],end='')
        Count+=1
import random
import math
from random import uniform
import os
import sys
from os import system
print("UIS-Curso de simulación-presentado por: Duban Oviedo Daza - Saida Gil Agudelo - Diego Quintero")
print("¡Hola!"," ingrese el tamaño de N")
print("Nota: el valor maximo de N para este codigo es de 1724 datos y el minimo es de 16")
x = int(input())
if x >= 1725:
    print("haga caso joven, hasta luego")
    sys.exit()
if x <= 15:
    print("haga caso joven, hasta luego")
    sys.exit()
p = x+1 #sumo uno para emparejar las listas X y X1
q=round(int(math.sqrt(math.sqrt(x))))
print("numero de clases")
print(q)
print("¿Desea limitar a un numero especifico la cifra de decimales?")
print("NOTA: a cualquier pregunta responda si o no, de lo contrario la consola se cerrará")
x1 = str(input())
X=[]
if x1=="si":
    print("¿cuantos decimales desea utilizar?")
    x2=int(input())
    for i in list(range(1,p+1)):
        X.append(round(uniform(0,1),x2))
    print("¿Desea ver el par de listas generadas?")
    x3=str(input())
    if x3=="si":
        X1=[]
        X1+=X#sumando las listas
        Z=[]
        Z1=[]
        X.pop(x)
        X1.pop(0)
        print("lx")
        print(X)
        system("pause")
        print("ly")
        print(X1)
        system("pause")
        system("cls")
        for i in range(q+1):
            Z.append(i/q)
        print(Z)
        for i1 in range(len(X)):
            if q==2:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(3)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(4)
            if q==3:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(4)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(5)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(7)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(8)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(9)
            if q==4:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(5)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(9)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(10)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(11)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(12)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(13)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(14)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(15)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(16)
            if q==5:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[4]<=X[i1]<=Z[5] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(5)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(9)
                if Z[4]<=X[i1]<=Z[5] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(10)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(11)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(12)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(13)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(14)
                if Z[4]<=X[i1]<=Z[5] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(15)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(16)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(17)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(18)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(19)
                if Z[4]<=X[i1]<=Z[5] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(20)
                if Z[0]<=X[i1]<=Z[1] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(21)
                if Z[1]<=X[i1]<=Z[2] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(22)
                if Z[2]<=X[i1]<=Z[3] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(23)
                if Z[3]<=X[i1]<=Z[4] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(24)
                if Z[4]<=X[i1]<=Z[5] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(25)
            if q==6:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[4]<=X[i1]<=Z[5] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(5)
                if Z[5]<=X[i1]<=Z[6] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(6)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(9)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(10)
                if Z[4]<=X[i1]<=Z[5] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(11)
                if Z[5]<=X[i1]<=Z[6] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(12)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(13)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(14)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(15)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(16)
                if Z[4]<=X[i1]<=Z[5] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(17)
                if Z[5]<=X[i1]<=Z[6] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(18)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(19)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(20)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(21)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(22)
                if Z[4]<=X[i1]<=Z[5] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(23)
                if Z[5]<=X[i1]<=Z[6] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(24)
                if Z[0]<=X[i1]<=Z[1] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(25)
                if Z[1]<=X[i1]<=Z[2] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(26)
                if Z[2]<=X[i1]<=Z[3] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(27)
                if Z[3]<=X[i1]<=Z[4] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(28)
                if Z[4]<=X[i1]<=Z[5] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(29)
                if Z[5]<=X[i1]<=Z[6] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(30)
                if Z[0]<=X[i1]<=Z[1] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(31)
                if Z[1]<=X[i1]<=Z[2] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(32)
                if Z[2]<=X[i1]<=Z[3] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(33)
                if Z[3]<=X[i1]<=Z[4] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(34)
                if Z[4]<=X[i1]<=Z[5] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(35)
                if Z[5]<=X[i1]<=Z[6] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(36)
        print(len(Z1))
        if q==2:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            print("los numeros se encuentran divididos de la siguiente manera")
            print(V1,V2,V3,V4)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append(((FE-i)**2)/FE)
            print(compararconchicuadrado)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 7.81472790325118
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==3:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            print("los numeros se encuentran divididos de la siguente manera")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append((FE-i)**2/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            chiexcel = 15.5073130558655
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==4:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            print("los numeros se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append((FE-i)**2/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 24.9957901397286
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==5:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            V17= len(list(filter(lambda numero: numero/17==1,Z1)))
            V18= len(list(filter(lambda numero: numero/18==1,Z1)))
            V19= len(list(filter(lambda numero: numero/19==1,Z1)))
            V20= len(list(filter(lambda numero: numero/20==1,Z1)))
            V21= len(list(filter(lambda numero: numero/21==1,Z1)))
            V22= len(list(filter(lambda numero: numero/22==1,Z1)))
            V23= len(list(filter(lambda numero: numero/23==1,Z1)))
            V24= len(list(filter(lambda numero: numero/24==1,Z1)))
            V25= len(list(filter(lambda numero: numero/25==1,Z1)))
            print("los datos se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25)
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append(((FE-i)**2)/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 36.4150285018073
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==6:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            V17= len(list(filter(lambda numero: numero/17==1,Z1)))
            V18= len(list(filter(lambda numero: numero/18==1,Z1)))
            V19= len(list(filter(lambda numero: numero/19==1,Z1)))
            V20= len(list(filter(lambda numero: numero/20==1,Z1)))
            V21= len(list(filter(lambda numero: numero/21==1,Z1)))
            V22= len(list(filter(lambda numero: numero/22==1,Z1)))
            V23= len(list(filter(lambda numero: numero/23==1,Z1)))
            V24= len(list(filter(lambda numero: numero/24==1,Z1)))
            V25= len(list(filter(lambda numero: numero/25==1,Z1)))
            V26= len(list(filter(lambda numero: numero/26==1,Z1)))
            V27= len(list(filter(lambda numero: numero/27==1,Z1)))
            V28= len(list(filter(lambda numero: numero/28==1,Z1)))
            V29= len(list(filter(lambda numero: numero/29==1,Z1)))
            V30= len(list(filter(lambda numero: numero/30==1,Z1)))
            V31= len(list(filter(lambda numero: numero/31==1,Z1)))
            V32= len(list(filter(lambda numero: numero/32==1,Z1)))
            V33= len(list(filter(lambda numero: numero/33==1,Z1)))
            V34= len(list(filter(lambda numero: numero/34==1,Z1)))
            V35= len(list(filter(lambda numero: numero/35==1,Z1)))
            V36= len(list(filter(lambda numero: numero/36==1,Z1)))
            print("los datos se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30,V31,V32,V33,V34,V35,V36)
            print("Frecuencia esperada")
            system("pause")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30,V31,V32,V33,V34,V35,V36]
            print(V1,V15)
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append(((FE-i)**2)/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 49.8018495682019
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
    if x3=="no":
        X1=[]
        X1+=X#sumando las listas
        Z=[]
        Z1=[]
        X.pop(x)
        X1.pop(0)
        print("lx")
        print(X)
        system("pause")
        print("ly")
        print(X1)
        system("pause")
        system("cls")
        for i in range(q+1):
            Z.append(i/q)
        print(Z)
        for i1 in range(len(X)):
            if q==2:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(3)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(4)
            if q==3:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(4)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(5)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(7)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(8)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(9)
            if q==4:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(5)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(9)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(10)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(11)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(12)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(13)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(14)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(15)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(16)
            if q==5:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[4]<=X[i1]<=Z[5] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(5)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(9)
                if Z[4]<=X[i1]<=Z[5] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(10)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(11)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(12)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(13)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(14)
                if Z[4]<=X[i1]<=Z[5] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(15)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(16)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(17)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(18)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(19)
                if Z[4]<=X[i1]<=Z[5] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(20)
                if Z[0]<=X[i1]<=Z[1] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(21)
                if Z[1]<=X[i1]<=Z[2] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(22)
                if Z[2]<=X[i1]<=Z[3] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(23)
                if Z[3]<=X[i1]<=Z[4] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(24)
                if Z[4]<=X[i1]<=Z[5] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(25)
            if q==6:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[4]<=X[i1]<=Z[5] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(5)
                if Z[5]<=X[i1]<=Z[6] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(6)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(9)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(10)
                if Z[4]<=X[i1]<=Z[5] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(11)
                if Z[5]<=X[i1]<=Z[6] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(12)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(13)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(14)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(15)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(16)
                if Z[4]<=X[i1]<=Z[5] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(17)
                if Z[5]<=X[i1]<=Z[6] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(18)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(19)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(20)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(21)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(22)
                if Z[4]<=X[i1]<=Z[5] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(23)
                if Z[5]<=X[i1]<=Z[6] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(24)
                if Z[0]<=X[i1]<=Z[1] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(25)
                if Z[1]<=X[i1]<=Z[2] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(26)
                if Z[2]<=X[i1]<=Z[3] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(27)
                if Z[3]<=X[i1]<=Z[4] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(28)
                if Z[4]<=X[i1]<=Z[5] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(29)
                if Z[5]<=X[i1]<=Z[6] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(30)
                if Z[0]<=X[i1]<=Z[1] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(31)
                if Z[1]<=X[i1]<=Z[2] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(32)
                if Z[2]<=X[i1]<=Z[3] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(33)
                if Z[3]<=X[i1]<=Z[4] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(34)
                if Z[4]<=X[i1]<=Z[5] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(35)
                if Z[5]<=X[i1]<=Z[6] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(36)
        print(len(Z1))
        if q==2:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            print("los numeros se encuentran divididos de la siguiente manera")
            print(V1,V2,V3,V4)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append(((FE-i)**2)/FE)
            print(compararconchicuadrado)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 7.81472790325118
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==3:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            print("los numeros se encuentran divididos de la siguente manera")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append((FE-i)**2/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            chiexcel = 15.5073130558655
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==4:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            print("los numeros se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append((FE-i)**2/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 24.9957901397286
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==5:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            V17= len(list(filter(lambda numero: numero/17==1,Z1)))
            V18= len(list(filter(lambda numero: numero/18==1,Z1)))
            V19= len(list(filter(lambda numero: numero/19==1,Z1)))
            V20= len(list(filter(lambda numero: numero/20==1,Z1)))
            V21= len(list(filter(lambda numero: numero/21==1,Z1)))
            V22= len(list(filter(lambda numero: numero/22==1,Z1)))
            V23= len(list(filter(lambda numero: numero/23==1,Z1)))
            V24= len(list(filter(lambda numero: numero/24==1,Z1)))
            V25= len(list(filter(lambda numero: numero/25==1,Z1)))
            print("los datos se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25)
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append((FE-i)**2/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 36.4150285018073
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==6:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            V17= len(list(filter(lambda numero: numero/17==1,Z1)))
            V18= len(list(filter(lambda numero: numero/18==1,Z1)))
            V19= len(list(filter(lambda numero: numero/19==1,Z1)))
            V20= len(list(filter(lambda numero: numero/20==1,Z1)))
            V21= len(list(filter(lambda numero: numero/21==1,Z1)))
            V22= len(list(filter(lambda numero: numero/22==1,Z1)))
            V23= len(list(filter(lambda numero: numero/23==1,Z1)))
            V24= len(list(filter(lambda numero: numero/24==1,Z1)))
            V25= len(list(filter(lambda numero: numero/25==1,Z1)))
            V26= len(list(filter(lambda numero: numero/26==1,Z1)))
            V27= len(list(filter(lambda numero: numero/27==1,Z1)))
            V28= len(list(filter(lambda numero: numero/28==1,Z1)))
            V29= len(list(filter(lambda numero: numero/29==1,Z1)))
            V30= len(list(filter(lambda numero: numero/30==1,Z1)))
            V31= len(list(filter(lambda numero: numero/31==1,Z1)))
            V32= len(list(filter(lambda numero: numero/32==1,Z1)))
            V33= len(list(filter(lambda numero: numero/33==1,Z1)))
            V34= len(list(filter(lambda numero: numero/34==1,Z1)))
            V35= len(list(filter(lambda numero: numero/35==1,Z1)))
            V36= len(list(filter(lambda numero: numero/36==1,Z1)))
            print("los datos se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30,V31,V32,V33,V34,V35,V36)
            print("Frecuencia esperada")
            system("pause")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30,V31,V32,V33,V34,V35,V36]
            print(V1,V15)
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append(((FE-i)**2)/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 49.8018495682019
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
if x1=="no":
    print("¿Desea ver el par de listas generadas?")
    x3=str(input())
    if x3=="si":
        X1=[]
        X1+=X#sumando las listas
        Z=[]
        Z1=[]
        X.pop(x)
        X1.pop(0)
        print("lx")
        print(X)
        system("pause")
        print("ly")
        print(X1)
        system("pause")
        system("cls")
        for i in range(q+1):
            Z.append(i/q)
        print(Z)
        for i1 in range(len(X)):
            if q==2:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(3)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(4)
            if q==3:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(4)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(5)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(7)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(8)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(9)
            if q==4:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(5)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(9)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(10)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(11)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(12)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(13)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(14)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(15)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(16)
            if q==5:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[4]<=X[i1]<=Z[5] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(5)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(9)
                if Z[4]<=X[i1]<=Z[5] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(10)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(11)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(12)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(13)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(14)
                if Z[4]<=X[i1]<=Z[5] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(15)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(16)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(17)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(18)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(19)
                if Z[4]<=X[i1]<=Z[5] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(20)
                if Z[0]<=X[i1]<=Z[1] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(21)
                if Z[1]<=X[i1]<=Z[2] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(22)
                if Z[2]<=X[i1]<=Z[3] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(23)
                if Z[3]<=X[i1]<=Z[4] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(24)
                if Z[4]<=X[i1]<=Z[5] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(25)
            if q==6:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[4]<=X[i1]<=Z[5] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(5)
                if Z[5]<=X[i1]<=Z[6] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(6)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(9)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(10)
                if Z[4]<=X[i1]<=Z[5] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(11)
                if Z[5]<=X[i1]<=Z[6] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(12)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(13)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(14)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(15)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(16)
                if Z[4]<=X[i1]<=Z[5] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(17)
                if Z[5]<=X[i1]<=Z[6] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(18)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(19)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(20)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(21)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(22)
                if Z[4]<=X[i1]<=Z[5] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(23)
                if Z[5]<=X[i1]<=Z[6] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(24)
                if Z[0]<=X[i1]<=Z[1] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(25)
                if Z[1]<=X[i1]<=Z[2] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(26)
                if Z[2]<=X[i1]<=Z[3] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(27)
                if Z[3]<=X[i1]<=Z[4] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(28)
                if Z[4]<=X[i1]<=Z[5] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(29)
                if Z[5]<=X[i1]<=Z[6] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(30)
                if Z[0]<=X[i1]<=Z[1] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(31)
                if Z[1]<=X[i1]<=Z[2] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(32)
                if Z[2]<=X[i1]<=Z[3] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(33)
                if Z[3]<=X[i1]<=Z[4] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(34)
                if Z[4]<=X[i1]<=Z[5] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(35)
                if Z[5]<=X[i1]<=Z[6] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(36)
        print(len(Z1))
        if q==2:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            print("los numeros se encuentran divididos de la siguiente manera")
            print(V1,V2,V3,V4)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append(((FE-i)**2)/FE)
            print(compararconchicuadrado)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 7.81472790325118
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==3:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            print("los numeros se encuentran divididos de la siguente manera")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append((FE-i)**2/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            chiexcel = 15.5073130558655
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==4:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            print("los numeros se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append((FE-i)**2/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 24.9957901397286
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==5:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            V17= len(list(filter(lambda numero: numero/17==1,Z1)))
            V18= len(list(filter(lambda numero: numero/18==1,Z1)))
            V19= len(list(filter(lambda numero: numero/19==1,Z1)))
            V20= len(list(filter(lambda numero: numero/20==1,Z1)))
            V21= len(list(filter(lambda numero: numero/21==1,Z1)))
            V22= len(list(filter(lambda numero: numero/22==1,Z1)))
            V23= len(list(filter(lambda numero: numero/23==1,Z1)))
            V24= len(list(filter(lambda numero: numero/24==1,Z1)))
            V25= len(list(filter(lambda numero: numero/25==1,Z1)))
            print("los datos se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25)
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append((FE-i)**2/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 36.4150285018073
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==6:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            V17= len(list(filter(lambda numero: numero/17==1,Z1)))
            V18= len(list(filter(lambda numero: numero/18==1,Z1)))
            V19= len(list(filter(lambda numero: numero/19==1,Z1)))
            V20= len(list(filter(lambda numero: numero/20==1,Z1)))
            V21= len(list(filter(lambda numero: numero/21==1,Z1)))
            V22= len(list(filter(lambda numero: numero/22==1,Z1)))
            V23= len(list(filter(lambda numero: numero/23==1,Z1)))
            V24= len(list(filter(lambda numero: numero/24==1,Z1)))
            V25= len(list(filter(lambda numero: numero/25==1,Z1)))
            V26= len(list(filter(lambda numero: numero/26==1,Z1)))
            V27= len(list(filter(lambda numero: numero/27==1,Z1)))
            V28= len(list(filter(lambda numero: numero/28==1,Z1)))
            V29= len(list(filter(lambda numero: numero/29==1,Z1)))
            V30= len(list(filter(lambda numero: numero/30==1,Z1)))
            V31= len(list(filter(lambda numero: numero/31==1,Z1)))
            V32= len(list(filter(lambda numero: numero/32==1,Z1)))
            V33= len(list(filter(lambda numero: numero/33==1,Z1)))
            V34= len(list(filter(lambda numero: numero/34==1,Z1)))
            V35= len(list(filter(lambda numero: numero/35==1,Z1)))
            V36= len(list(filter(lambda numero: numero/36==1,Z1)))
            print("los datos se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30,V31,V32,V33,V34,V35,V36)
            print("Frecuencia esperada")
            system("pause")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30,V31,V32,V33,V34,V35,V36]
            print(V1,V15)
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append(((FE-i)**2)/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 49.8018495682019
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
    if x3=="no":
        for i in list(range(1,p+1)):
            X.append(uniform(0,1))
        X1=[]
        X1+=X#sumando las listas
        Z=[]
        Z1=[]
        X.pop(x)
        X1.pop(0)
        for i in range(q+1):
            Z.append(i/q)
        print(Z)
        for i1 in range(len(X)):
            if q==2:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(3)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(4)
            if q==3:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(4)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(5)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(7)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(8)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(9)
            if q==4:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(5)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(9)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(10)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(11)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(12)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(13)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(14)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(15)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(16)
            if q==5:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[4]<=X[i1]<=Z[5] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(5)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(6)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(9)
                if Z[4]<=X[i1]<=Z[5] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(10)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(11)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(12)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(13)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(14)
                if Z[4]<=X[i1]<=Z[5] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(15)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(16)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(17)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(18)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(19)
                if Z[4]<=X[i1]<=Z[5] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(20)
                if Z[0]<=X[i1]<=Z[1] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(21)
                if Z[1]<=X[i1]<=Z[2] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(22)
                if Z[2]<=X[i1]<=Z[3] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(23)
                if Z[3]<=X[i1]<=Z[4] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(24)
                if Z[4]<=X[i1]<=Z[5] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(25)
            if q==6:
                if Z[0]<=X[i1]<=Z[1] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(1)
                if Z[1]<=X[i1]<=Z[2] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(2)
                if Z[2]<=X[i1]<=Z[3] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(3)
                if Z[3]<=X[i1]<=Z[4] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(4)
                if Z[4]<=X[i1]<=Z[5] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(5)
                if Z[5]<=X[i1]<=Z[6] and Z[0]<=X1[i1]<=Z[1]:
                    Z1.append(6)
                if Z[0]<=X[i1]<=Z[1] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(7)
                if Z[1]<=X[i1]<=Z[2] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(8)
                if Z[2]<=X[i1]<=Z[3] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(9)
                if Z[3]<=X[i1]<=Z[4] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(10)
                if Z[4]<=X[i1]<=Z[5] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(11)
                if Z[5]<=X[i1]<=Z[6] and Z[1]<=X1[i1]<=Z[2]:
                    Z1.append(12)
                if Z[0]<=X[i1]<=Z[1] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(13)
                if Z[1]<=X[i1]<=Z[2] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(14)
                if Z[2]<=X[i1]<=Z[3] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(15)
                if Z[3]<=X[i1]<=Z[4] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(16)
                if Z[4]<=X[i1]<=Z[5] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(17)
                if Z[5]<=X[i1]<=Z[6] and Z[2]<=X1[i1]<=Z[3]:
                    Z1.append(18)
                if Z[0]<=X[i1]<=Z[1] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(19)
                if Z[1]<=X[i1]<=Z[2] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(20)
                if Z[2]<=X[i1]<=Z[3] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(21)
                if Z[3]<=X[i1]<=Z[4] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(22)
                if Z[4]<=X[i1]<=Z[5] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(23)
                if Z[5]<=X[i1]<=Z[6] and Z[3]<=X1[i1]<=Z[4]:
                    Z1.append(24)
                if Z[0]<=X[i1]<=Z[1] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(25)
                if Z[1]<=X[i1]<=Z[2] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(26)
                if Z[2]<=X[i1]<=Z[3] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(27)
                if Z[3]<=X[i1]<=Z[4] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(28)
                if Z[4]<=X[i1]<=Z[5] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(29)
                if Z[5]<=X[i1]<=Z[6] and Z[4]<=X1[i1]<=Z[5]:
                    Z1.append(30)
                if Z[0]<=X[i1]<=Z[1] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(31)
                if Z[1]<=X[i1]<=Z[2] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(32)
                if Z[2]<=X[i1]<=Z[3] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(33)
                if Z[3]<=X[i1]<=Z[4] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(34)
                if Z[4]<=X[i1]<=Z[5] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(35)
                if Z[5]<=X[i1]<=Z[6] and Z[5]<=X1[i1]<=Z[6]:
                    Z1.append(36)
        print(len(Z1))
        if q==2:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            print("los numeros se encuentran divididos de la siguiente manera")
            print(V1,V2,V3,V4)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append(((FE-i)**2)/FE)
            print(compararconchicuadrado)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 7.81472790325118
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==3:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            print("los numeros se encuentran divididos de la siguente manera")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append((FE-i)**2/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            chiexcel = 15.5073130558655
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==4:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            print("los numeros se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16)
            system("pause")
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append((FE-i)**2/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 24.9957901397286
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==5:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            V17= len(list(filter(lambda numero: numero/17==1,Z1)))
            V18= len(list(filter(lambda numero: numero/18==1,Z1)))
            V19= len(list(filter(lambda numero: numero/19==1,Z1)))
            V20= len(list(filter(lambda numero: numero/20==1,Z1)))
            V21= len(list(filter(lambda numero: numero/21==1,Z1)))
            V22= len(list(filter(lambda numero: numero/22==1,Z1)))
            V23= len(list(filter(lambda numero: numero/23==1,Z1)))
            V24= len(list(filter(lambda numero: numero/24==1,Z1)))
            V25= len(list(filter(lambda numero: numero/25==1,Z1)))
            print("los datos se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25)
            print("Frecuencia esperada")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25]
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append((FE-i)**2/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 36.4150285018073
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
        if q==6:
            V1= len(list(filter(lambda numero: numero/1==1,Z1)))
            V2= len(list(filter(lambda numero: numero/2==1,Z1)))
            V3= len(list(filter(lambda numero: numero/3==1,Z1)))
            V4= len(list(filter(lambda numero: numero/4==1,Z1)))
            V5= len(list(filter(lambda numero: numero/5==1,Z1)))
            V6= len(list(filter(lambda numero: numero/6==1,Z1)))
            V7= len(list(filter(lambda numero: numero/7==1,Z1)))
            V8= len(list(filter(lambda numero: numero/8==1,Z1)))
            V9= len(list(filter(lambda numero: numero/9==1,Z1)))
            V10= len(list(filter(lambda numero: numero/10==1,Z1)))
            V11= len(list(filter(lambda numero: numero/11==1,Z1)))
            V12= len(list(filter(lambda numero: numero/12==1,Z1)))
            V13= len(list(filter(lambda numero: numero/13==1,Z1)))
            V14= len(list(filter(lambda numero: numero/14==1,Z1)))
            V15= len(list(filter(lambda numero: numero/15==1,Z1)))
            V16= len(list(filter(lambda numero: numero/16==1,Z1)))
            V17= len(list(filter(lambda numero: numero/17==1,Z1)))
            V18= len(list(filter(lambda numero: numero/18==1,Z1)))
            V19= len(list(filter(lambda numero: numero/19==1,Z1)))
            V20= len(list(filter(lambda numero: numero/20==1,Z1)))
            V21= len(list(filter(lambda numero: numero/21==1,Z1)))
            V22= len(list(filter(lambda numero: numero/22==1,Z1)))
            V23= len(list(filter(lambda numero: numero/23==1,Z1)))
            V24= len(list(filter(lambda numero: numero/24==1,Z1)))
            V25= len(list(filter(lambda numero: numero/25==1,Z1)))
            V26= len(list(filter(lambda numero: numero/26==1,Z1)))
            V27= len(list(filter(lambda numero: numero/27==1,Z1)))
            V28= len(list(filter(lambda numero: numero/28==1,Z1)))
            V29= len(list(filter(lambda numero: numero/29==1,Z1)))
            V30= len(list(filter(lambda numero: numero/30==1,Z1)))
            V31= len(list(filter(lambda numero: numero/31==1,Z1)))
            V32= len(list(filter(lambda numero: numero/32==1,Z1)))
            V33= len(list(filter(lambda numero: numero/33==1,Z1)))
            V34= len(list(filter(lambda numero: numero/34==1,Z1)))
            V35= len(list(filter(lambda numero: numero/35==1,Z1)))
            V36= len(list(filter(lambda numero: numero/36==1,Z1)))
            print("los datos se encuentran divididos de la siguiente manera:")
            print(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30,V31,V32,V33,V34,V35,V36)
            print("Frecuencia esperada")
            system("pause")
            FE = (x-1)/(q*q)
            print(FE)
            system("pause")
            VV = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30,V31,V32,V33,V34,V35,V36]
            print(V1,V15)
            compararconchicuadrado=[]
            for i in VV:
                compararconchicuadrado.append(((FE-i)**2)/FE)
            COMPARARCONCHICUADRADO = sum(compararconchicuadrado)
            print("ChiCuadradoCalculado")
            print(COMPARARCONCHICUADRADO)
            print("Grados de libertad")
            GL= (q*q)-1
            print(GL)
            system("pause")
            chiexcel = 49.8018495682019
            if COMPARARCONCHICUADRADO <= chiexcel:
                print("se acepta la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}<={chiexcel}.")
            if COMPARARCONCHICUADRADO >= chiexcel:
                print("se rechaza la hipotesis de que los datos tienen una distribucion uniforme bidimensional")
                print(F"debido a que {COMPARARCONCHICUADRADO}>={chiexcel}.")
            system("pause")
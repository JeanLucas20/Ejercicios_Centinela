


# Entrada Zzzzz....

import sre_compile


cod= float(input("Ingrese el código del estudiante: "))
cod= round(cod, )
name= input("Ingrese el nombre del estudiante: ")

if cod != 0:
    a1= float(input("Digite la nota del parcial #1: "))
    a2= float(input("Digite la nota del parcial #2: "))
    a3= float(input("Digite la nota del parcial #3: "))
else:
    print("Fin de los datos de emntrada :/")

# Proceso Zzzzz....
luk= 0

while cod !=0:
    b= (a1+a2+a3)/3
    print("El estudiante de codigo ", str(cod), str(name) + ", obtuvo una nota definitiva de: ",str(b)," :)")
    
    if b<3.0:
        luk= luk+1  
    
    cod= float(input("Ingrese el código del estudiante: "))
    cod= round(cod, )
    name= input("Ingrese el nombre del estudiante: ")

    if cod != 0:
        a1= float(input("Digite la nota del parcial #1: "))
        a2= float(input("Digite la nota del parcial #2: "))
        a3= float(input("Digite la nota del parcial #3: "))
    else:
        print("Se acabo :)")

# Salida Zzzzz....
print("La cantidad de estudiantes que reprovaron la materia son: "+ str(luk) + " :/")




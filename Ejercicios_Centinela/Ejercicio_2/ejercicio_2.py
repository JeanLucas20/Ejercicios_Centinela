

a= int(input("Ingrese un número: "))
par= 0
impar= 0



if a != 0:
    b= a%2

    while b == 0:
        par= par + 1
        impar= impar + 1

    a= int(input("Ingrese un número: "))

    if a != 0:
        b= a%2
    
    else:
        print("Fin del conte")

print("Hay " + str(impar) + " números impares y " + str(par) + " números pares" )    



# Salida Zzzzz....

class Ejercicios:
    def __init__(self):
        pass

#1. Diseñamos un pseudocódigo para encontrar la superficie de un círculo para un radio cualquiera.
def CalcularRadio(self):
    Rq = float(input("Ingrese el radio del circulo"))
    pc = 3.1416
    y = pc*Rq**2
    print("la superficie de su circulo es:{}".format(y))

#2. En una tienda se ofrece un descuento del %15 sobre el total de la compra y un cliente desea saber cuanto deberia pagar finalmente por su compra
def Descuento(self):
    Ti = float (input("Ingrese su total de su compra"))
    a = Ti*0.15
    Gh = Ti-a
    print("El total a cancelar es:{}".format(Gh))

#3. Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.
def Ventas(self):
    for x in range(4):
        Sa = float(input("Ingrese su salario"))
        t1 = float(input("Ingrese el valor de su primer venta: "))
        t2 = float(input("Ingrese el segundo valor de la venta: "))
        t3 = float(input("Ingrese el tercer valor de la venta: "))
        Rt = t1+t2+t3
        Xt = Rt*0.1
        Tv = round(Rt+Xt,2)
        print("El total a recibir por comision es:{} ".format(Tv))

#4. Construir un algoritmo tal, que dado como dato la calificacion de un alumno en un examen, escriba 
def Algoritmo(self):
    s = float(input("Ingrese su calificacion "))
    if s >= 7:
        print("Felicitaciones aprobaste")
    
#5. Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.
def Algoritmo2(self):
    s = float(input("Ingrese su calificacion "))
    if s >= 7:
        print("Felicitaciones has aprobado")
    else:
        print("Has reprovado :(")

#6. Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.
def Sueldo(self):
    u = float(input("Ingrese su sueldo: "))
    if u < 600:
        m = u+u*0.1
        print("Su nuevo sueldo es {}".format(m))
    else:
        print("Su sueldo sigue siendo de {}".format(u))

#7. Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo exceden de 40, el resto  se consideran horas extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8;  si las horas extras exceden de 8 se pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto al triple.
def Dinero(self):
    O = int(input("Ingrese el nuemro de horas trabajadas: "))
    V = float(input("Ingrese el valor a pagar por hora: "))
    if O > 48:
        t = O - 48
        d = 8
        s = 40*P + d*V*2 + t*V*3
        print("El total a pagar por las horas trabajadas es : {}".format(s))
    elif O < 40:
        d = O-40
        s = 40*V + d*V*2
        print("El total a pagar por las horas trabajadas es : {}".format(s))
    else:
        s = V*O
        print("El total a pagar por las horas trabajadas es : {}".format(s))

#8. Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.
def diff(self):
    l = []
    for i in range(3):
        num = float(input("Introduce el numero #{}: ".format(i +1)))
        l.append(num)
    m = l[0]
    for num in l:
        if num > m:
            m = num
    print("El numero mayor es : {}".format(m))


#9. Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función.
def Variables(self):
    v = int(input("Ingrese el valor de v: "))
    num = int(input("Ingrese el valor de num: "))
    if num == 1:
        r = 100*v
    elif num == 2:
        r = 100^v
    elif num == 3:
        r = 100/v
    else:
        r = 0
    print("El resultado es {}".format(r))


#10. Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.
def ExamAspirantes(self):
    S1=float(input("Ingrese la primera calificacion "))
    S2=float(input("Ingrese la segunda calificacion "))
    if S1>80 and S2>80:
        print("Usted a sido Aceptado")
    else:
        print("Usted a sido Rechazado")

#11. Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.
def cuadrad(self):
    F = 0
    i = 1
    for i in range(101):
        F = F + i
        i += 1
    print(F)
    
#12. Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100
def Numerosingr(self):
    x = 0
    while x<100:
        x += 1
    print(x) 
    
#13. Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por el usuario.
def sumayproducto(self):
    s = 0
    pr = 1
    n = "y"
    while n != "n"and n != "N":
        num = int(input("Ingrese N: "))
        s += num
        pr *= num
        n = input("Desea continuar(S/N)" )
    print("Total de la suma es :{}".format(pr))
    print("Total del producto es :{}".format(s))

#14. Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por centinela.
def calcu(self):
    su = 0
    p = 1
    n = int(input("Ingrese N: "))
    while n != -1:
        su += 1
        p = p*n
    print("Total de la suma es :{}".format(p))
    print("Total del producto es :{}".format(su))


#15. Determinar si un número entero proporcionado por el usuario es primo. Un número primo es un entero que no tiene más divisores que él mismo y la unidad. Elaborar Pseudocódigo:
def pro(self):
    pr = "True"
    di = 2
    r = int(input("Ingrese su numero"))
    while di < r and pr == "True":
        res = r % di
        if res == 0:
            pr = "False"
            di = di+1
    if pr == "True":
        print("Su numero {} es primo " .format(r))
    else:
        print("Su numero {} no es primo".format(r))
        

#16. Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N y calcular el resultado de la siguiente serie: 1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema utilizando bucle Repeat controlado por contador y usando banderas.
def metod(self):
        from fractions import Fraction
        sor = 0
        D = 1
        r = int(input("Ingrese un numero entero: "))
        n = "T"
        # while D>r:
        for x in range (r):
            if n == "T":
                sor = sor + Fraction(1,D)
                n ="F"               
            else:
                sor = sor - Fraction(1,D)
                n = "T"
            D += 1           
        print(sor) 

#17.Calcular el factorial de N números enteros leídos de teclado el problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número.
def fact(self):
    nu = int(input('Rango: '))
    for i in range(1,nu+1):
        m = int(input('Numero: '))
        fact = 1
    for j in range(1,m+1):
        fact = fact * j
        print(f'El factorial es: {fact}')


    
#18.Sea un vector “Calificaciones” de 100 componentes:
def vect(self):
        import random as rd
        pro = []
        cal = [[rd.randint(0,10)for e in range(6)]for e in range(30)]
        for i in range(30):
            su = 0
            for j in range(6):
                su = su + cal[i][j]
                p = round(su/6,2)
            pro.append(p)
            print(f'promedio del alumno: {i+1} : {round(su/6,2)}')

        pro.sort(reverse=True)
        print(f'La mayor nota es: {pro[0]}')



#19. Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos. Los datos sobre estos exámenes se proporcionan de la siguiente manera:
def Cal(self,prom,n):
    for i in range(1, 30):
        for j in range(1, 60):
            print("Escriba la calificacion del alumno",i,"en el examen",j)

    for j in range(1, 6):
        sum = 0
        for i in range(1, 30):
            sum = sum + cal[i,j]
            prom[j] = sum/30
            print("promedio examen",j,prom[j])
    for i in range(1, 30):
        sum = 0
        for j in range(1, 6):
            sum = sum + cal[i,j]
        print("Promedio del alumno" , i,sum/6)
    Examen = 1
    promayor = prom[1]
    for j in range(2, n+6):
        if promayor < prom[j]:
            promayor = prom[j]
            Examen = 0
    print("El examen",Examen,"obtuvo el mayor promedio=",promayor)







cal1=Ejercicios()
cal1.CalcularRadio()









 




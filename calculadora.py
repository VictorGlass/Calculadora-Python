#Creacion de una Calculadora usando Python.

'''
Programa que representa una Calculadora Básica creada con lenguaje de programacion Python.

Posee las operaciones mas básicas para realizar.
'''

class Calculador:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operacion = ''
    
    def sumar(self):
        print("-------------------------------------")
        self.num1 = int(input("Ingresa el primer numero: "))
        print("-------------------------------------")
        self.num2 = int(input("Ingresa el segundo numero: "))
        self.operacion = '+'
        self.calcular()
    
    def restar(self):
        print("-------------------------------------")
        self.num1 = int(input("Ingresa el primero numero: "))
        print("-------------------------------------")
        self.num2 = int(input("Ingresa el segundo numero: "))
        self.operacion = '-'
        self.calcular()
    
    def multiplicar(self):
        print("-------------------------------------")
        self.num1 = int(input("Ingresa el primer numero: "))
        print("-------------------------------------")
        self.num2 = int(input("Ingresa el segundo numero: "))
        self.operacion = '*'
        self.calcular()
    
    def dividir(self):
        print("-------------------------------------")
        self.num1 = int(input("Ingresa el primer numero: "))
        print("-------------------------------------")
        self.num2 = int(input("Ingresa el segundo numero: "))
        self.operacion = '/'
        self.calcular()
    
    def calcular(self):
        if self.operacion == '+':
            self.resultado = self.num1 + self.num2
        elif self.operacion == '-':
            self.operacion = self.num1 - self.num2
        elif self.operacion == '*':
            self.operacion = self.num1 * self.num2
        elif self.operacion == '/':
            self.operacion = self.num1 / self.num2
        else:
            self.resultado = 0
        print("-------------------------------------")
        print(f"El resultado de la operacion es: {self.resultado}")
        print("-------------------------------------")

calc = Calculador()

while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("===================")

    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        calc.sumar()
    elif opcion == 2:
        calc.restar()
    elif opcion == 3:
        calc.multiplicar()
    elif opcion == 4:
        calc.dividir()
    else:
        print("Opcion incorrecta.")

    
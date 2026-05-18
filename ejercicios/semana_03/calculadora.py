class Calculadora: 
    
    def __init__(self):
        pass

    def suma(self,numero1,numero2):
        resultado = numero1 + numero2
        print (f"Resultado: {resultado}")

    def sumaEnteros(self,numero1 : int , numero2 : int):
        resultado = numero1 + numero2
        print (f"Resultado: {resultado}")
        

casio_9850 = Calculadora()

casio_9850.suma(10,15.5)

casio_9850.sumaEnteros(10, 15.5)

casio_9850.suma("10","15.5")

casio_9850.sumaEnteros ("10", "15.5")

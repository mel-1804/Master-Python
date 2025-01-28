# Your code here
class InputOutString:
    def __init__(self):
        self.texto = ""

    def get_string(self):
        self.texto = input("Ingrese un texto: ")

    def print_string(self):
        print(self.texto.upper())


obj = InputOutString()  # Creamos una instancia de la clase
obj.get_string()  # Invocamos el método para obtener texto desde la consola
obj.print_string()  # Invocamos el método para imprimir el texto en mayúsculas
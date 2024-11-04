class FeedbackSystem:
    def __init__(self, filename="data.txt"):
        self.filename = filename

    def opciones(self):
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')

    def verificador(self, minima_puntuacion, mayor_puntuacion, prompt):
        while True:
            value = input(prompt)
            if value.isdecimal():
                nota = int(value)
                if minima_puntuacion <= nota <= mayor_puntuacion:
                    return nota
                print(f'Introduzca un número del {minima_puntuacion} al {mayor_puntuacion}')
            else:
                print(f'Introduzca un número del {minima_puntuacion} al {mayor_puntuacion}')

    def guardado(self, point, comment):
        post = f'puntuacion: {point} comentario dejado: {comment}'
        with open(self.filename, 'a') as file:
            file.write(f'{post}\n')

    def get_feedback(self):
        point = self.verificador(1, 5, 'Por favor, introduzca una puntuación en una escala de 1 a 5\n')
        print('Por favor, introduzca un comentario')
        comment = input()
        self.guardado(point, comment)

    def mostrar(self):
        print('Resultados hasta la fecha.')
        try:
            with open(self.filename, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("No hay resultados disponibles todavía.")

    def run(self):
        while True:
            self.opciones()
            option = self.verificador(1, 3, '')
            
            if option == 1:
                self.get_feedback()
            elif option == 2:
                self.mostrar()
            else:
                print('Finalizando')
                break

def main():
    feedback_system = FeedbackSystem()
    feedback_system.run()

if __name__ == "__main__":
    main()
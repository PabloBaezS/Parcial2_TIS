from flask import Flask, request, render_template
from models import Flight

app = Flask(__name__)

flights = []


@app.route('/')
def home():
    return render_template('home.html')


# Ruta para agregar un vuelo
@app.route('/add_flight', methods=['GET', 'POST'])
def add_flight():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        tipo = request.form.get('tipo')
        precio = request.form.get('precio')

        if tipo not in ["Nacional", "Internacional"]:
            return "Error: Tipo de vuelo no válido. Debe ser 'Nacional' o 'Internacional'."

        try:
            precio = float(precio)
        except ValueError:
            return "Error: Precio debe ser un número."

        flight = Flight(nombre, tipo, precio)
        flights.append(flight)
        return render_template('add_flight.html',
                               message="Vuelo añadido exitosamente.")

    return render_template('add_flight.html')


# Ruta para listar los vuelos
@app.route('/list_flights')
def list_flights():
    return render_template('list_flights.html', flights=flights)


# Ruta para calcular el factorial de un número
@app.route('/factorial_form', methods=['GET', 'POST'])
def factorial_form():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        result = 1
        for i in range(1, number + 1):
            result *= i
        return render_template('factorial.html', number=number, result=result)

    return render_template('factorial.html')



if __name__ == '__main__':
    app.run(debug=True)

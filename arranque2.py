#Importar la biblioteca de flask

#from flask import Flask
from flask import Flask, render_template, request


app = Flask(__name__)
inventario = []
@app.route('/')
def formulario():
    return render_template('index.html', inventario=inventario) # se pasa como argumento a la plantilla para que pueda mostrar la lista de productos actual

#DEFINIR LA RUTA DEL FORMULARIO QUE PROCESA EL ENVIO ATRAVES DEL METODO POST
@app.route('/index', methods=['post'])
def procesar_formulario():
    producto = request.form['producto']
    cantidad = int(request.form['cantidad'])
    precio = int(request.form['precio'])
    subtotal = cantidad * precio
    iva = subtotal * 0.16

#CREAR UNA LISTA PARA AGREGAR LOS PRODUCTOS DEL INVENTARIO
    inventario.append({
        'producto': producto,
        'cantidad': cantidad,
        'precio': precio,
        'subtotal': subtotal,
        'iva': iva
    })
    # Redirigir al usuario de vuelta a la página principal
    return render_template('index.html', inventario=inventario)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')


if __name__ == '__main__':
    app.run(debug=True)
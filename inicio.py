from flask import Flask, render_template
from rutas import configure_routes as configure_rutas
from ruta_peli import configure_routes as configure_ruta_peli
from ruta_escritores import configure_routes as configure_ruta_escritores

app = Flask(__name__) #instancia de un objeto Flask

configure_rutas(app)  # Integrar las rutas generales
configure_ruta_peli(app)  # Integrar las rutas específicas de Alicia
configure_ruta_escritores(app) 



@app.route('/escritores')
def escritores(): 
    return render_template('escritores.html')

@app.route('/conocenos')
def conocenos():
    return render_template('conocenos.html')

@app.route('/agregar')
def agregar():
    return render_template('agregar.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
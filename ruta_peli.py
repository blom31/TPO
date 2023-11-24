from flask import render_template

def configure_routes(app):
    @app.route('/alicia')
    def alicia():
        return render_template('pelicula_alicia.html')
    
    @app.route('/harry')
    def harry():
        return render_template('pelicula_harry.html')
    
    @app.route('/it')
    def it():
        return render_template('pelicula_it.html')
    
    @app.route('/juegos')
    def juegos():
        return render_template('pelicula_juegos_hambre.html')
    
    @app.route('/leyenda')
    def leyenda():
        return render_template('pelicula_leyenda.html')
    
    @app.route('/lord')
    def lord():
        return render_template('pelicula_señor_anillos.html')
    
    @app.route('/maze')
    def maze():
        return render_template('pelicula_maze_runner.html')
    
    @app.route('/matilda')
    def matilda():
        return render_template('pelicula_matilda.html')
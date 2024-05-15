from flask import Flask

app = Flask(__name__) 

@app.route("/") # Funcion para ruta predeterminada
def Hello():
    return "Hello, World! soy nano"

app.run(host="0.0.0.0") #Host para Docker

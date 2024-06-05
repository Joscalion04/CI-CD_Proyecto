from flask import Flask

app = Flask(__name__) 

@app.route("/") # Funcion para ruta predeterminada
def Hello():
    return "Hello, Mundo!"

app.run(host="0.0.0.0", port=5000) #Host para Docker

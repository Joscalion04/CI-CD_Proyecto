from flask import Flask

app = Flask(__name__) 

@app.route("/") # Funcion para ruta predeterminada
def Hello():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CI/CD PROJECT</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #2c2c2c;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                color: #e0e0e0;
            }
            .container {
                text-align: center;
                background-color: #3c3c3c;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            }
            h1 {
                color: #c0c0c0;
            }
            h2 {
                color: #c0c0c0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to CI/CD Project del Tigre!</h1>
            <h2>JAVI USAGA</h2>
            <h2>JEFFERSON SANDI</h2>
            <h2>JOHAN MORA</h2>
            <h2>JOSEPH LEON</h2>
        </div>
    </body>
    </html>
    """

app.run(host="0.0.0.0", port=5000) #Host para Docker

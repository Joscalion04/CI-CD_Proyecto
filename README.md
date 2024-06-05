# Pasos para Ejecutar el proyecto correctamente desde Windows con VS Code
 - Se necesita tener instalado Python Flask para el uso de Python Web, se puede instalar usando: " pip install -r requirements.txt "
 - Se necesita tener instalado Docker para poder cargar la aplicacion web dockerizada correctamente, se puede descargar en: https://hub.docker.com
 - Para los siguientes comandos de configuracion y ejecucion se necesita realizarlos desde la terminal del proyecto abierto en VS Code
 - La configuracion docker se instalara con el comando: " docker build -t app-flask . "
 - La instancia docker se ejecutara con el comando: " docker run -it -p 5000:5000 app-flask "
 - TODOS ESTOS PASOS ASEGURAN EL CORRECTO FUNCIONAMIENTO DE LA APP
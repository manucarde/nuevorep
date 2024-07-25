from datetime import datetime as dt
from django.http import HttpResponse

# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context


def saludo(request):
    return HttpResponse("Hola mundo!, hola Coder!" "Buenas noches Comi 57820")


def alejandro(request):
    texto = "Soy Alejandro Ramirez<br>Cursando Python"
    return HttpResponse(texto)


def dia_de_hoy(request):
    dia = dt.now()
    texto = f"Hoy es:<br>{dia}"
    return HttpResponse(texto)


def probando_template(request):

    # Abrimos el archivo html
    mi_html = open("./Clases_Coder/plantillas/index.html")

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

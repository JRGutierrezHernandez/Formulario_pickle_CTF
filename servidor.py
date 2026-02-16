from flask import Flask, render_template, request, jsonify, send_file
import pickle
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)

ARCHIVO = "datos.pkl"
PDF_FILE = "formulario.pdf"

# ===============================
# DATOS VACÍOS
# ===============================
def datos_vacios():
    return {
        "nombres": "",
        "apellido_paterno": "",
        "apellido_materno": "",
        "edad": "",
        "calle": "",
        "numero_exterior": "",
        "numero_interior": "",
        "telefono": "",
        "correo": "",
        "curp": "",
        "nss": "",
        "rfc": ""
    }

# ===============================
# CARGAR / GUARDAR PICKLE
# ===============================
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "rb") as f:
            return pickle.load(f)
    return datos_vacios()

def guardar_datos(datos):
    with open(ARCHIVO, "wb") as f:
        pickle.dump(datos, f)

# ===============================
# CREAR PDF
# ===============================
def crear_pdf(datos):
    c = canvas.Canvas(PDF_FILE, pagesize=letter)
    y = 750

    c.setFont("Helvetica", 12)
    c.drawString(200, y, "Formulario de Registro")
    y -= 40

    for campo, valor in datos.items():
        texto = f"{campo.replace('_',' ').title()}: {valor}"
        c.drawString(50, y, texto)
        y -= 20

    c.save()

# ===============================
# PÁGINA PRINCIPAL
# ===============================
@app.route("/", methods=["GET", "POST"])
def formulario():

    if request.method == "POST":
        datos = request.form.to_dict()
        guardar_datos(datos)
        crear_pdf(datos)
        return send_file(PDF_FILE, as_attachment=True)

    datos = cargar_datos()
    return render_template("formulario.html", datos=datos)

# ===============================
# GUARDADO AUTOMÁTICO
# ===============================
@app.route("/guardar_auto", methods=["POST"])
def guardar_auto():
    datos = request.json
    guardar_datos(datos)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)

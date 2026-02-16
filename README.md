
# Formulario Web con Restauración de Estado, Guardado en Tiempo Real y Exportación a PDF

Este proyecto es una aplicación web desarrollada con Python y Flask que permite capturar información de un formulario estructurado, guardar automáticamente los datos en tiempo real, restaurar el estado del sistema al volver a ejecutarlo y generar un archivo PDF con la información registrada.

El sistema implementa persistencia de datos mediante serialización de objetos usando el módulo `pickle` de Python.

---

## 🎯 Objetivo del proyecto

Demostrar la restauración del estado de ejecución de un sistema mediante:

- Persistencia de datos en archivo binario
- Serialización de objetos con Python
- Guardado automático en tiempo real
- Recuperación del estado del formulario
- Generación de documentos PDF como respaldo

---

## 🚀 Funcionalidades principales

✔ Formulario dividido en secciones  
✔ Guardado automático en tiempo real mientras se escribe  
✔ Persistencia de datos con pickle  
✔ Restauración automática del estado al abrir la aplicación  
✔ Guardado manual con botón  
✔ Generación automática de PDF del formulario  
✔ Descarga del documento PDF  
✔ Interfaz con Bootstrap y CSS personalizado  

---

## 🧩 Tecnologías utilizadas

- Python 3
- Flask
- Pickle (serialización de objetos)
- JavaScript (fetch API)
- Bootstrap 5
- CSS personalizado
- ReportLab (generación de PDF)

---

## ⚙️ Instalación

Instalar dependencias:

```bash
pip install flask
pip install reportlab

### ▶️ Ejecución del sistema

Ejecutar el servidor:

python servidor.py


Abrir navegador:

http://127.0.0.1:5000

💾 Persistencia de datos con pickle

El sistema utiliza el módulo pickle para serializar los datos del formulario y almacenarlos en un archivo binario (datos.pkl).

Esto permite:

Guardar el estado del sistema

Restaurar datos al reiniciar el servidor

Mantener la información entre ejecuciones

🔹 Guardar datos
def guardar_datos(datos):
    with open(ARCHIVO, "wb") as f:
        pickle.dump(datos, f)


pickle.dump() convierte el objeto Python en una secuencia de bytes y lo guarda en un archivo.

🔹 Cargar datos
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "rb") as f:
            return pickle.load(f)


pickle.load() reconstruye el objeto original desde el archivo.

Esto permite restaurar el estado del formulario automáticamente.

⚡ Guardado automático en tiempo real

El sistema guarda los datos continuamente mientras el usuario escribe.

🔹 Funcionamiento

JavaScript detecta cambios en los campos del formulario

Se envían datos al servidor mediante fetch()

Flask recibe los datos

Se guardan con pickle inmediatamente

🔹 Código JavaScript
const campos = document.querySelectorAll("input, textarea");

campos.forEach(campo => {
    campo.addEventListener("input", guardarAutomatico);
});

function guardarAutomatico() {
    const datos = {};

    campos.forEach(campo => {
        datos[campo.name] = campo.value;
    });

    fetch("/guardar_auto", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(datos)
    });
}

🔹 Ruta Flask para auto-guardado
@app.route("/guardar_auto", methods=["POST"])
def guardar_auto():
    datos = request.json
    guardar_datos(datos)
    return jsonify({"status": "ok"})


Esto permite sincronización continua entre cliente y servidor.

🧾 Generación automática de PDF

Cuando el usuario presiona el botón Guardar:

Se guardan los datos en pickle

Se genera un PDF con ReportLab

Se envía el archivo al navegador para descarga

🔹 Crear PDF
def crear_pdf(datos):
    c = canvas.Canvas(PDF_FILE, pagesize=letter)
    y = 750

    for campo, valor in datos.items():
        c.drawString(50, y, f"{campo}: {valor}")
        y -= 20

    c.save()

🔹 Enviar PDF al usuario
return send_file(PDF_FILE, as_attachment=True)

🔄 Restauración del estado del sistema

Cuando se abre la aplicación:

Flask revisa si existe datos.pkl

Si existe → carga datos guardados

Se rellenan automáticamente los campos del formulario

Esto permite continuar exactamente donde se dejó el sistema.

🧠 Flujo general del sistema
Usuario escribe datos
        ↓
JavaScript detecta cambios
        ↓
Datos enviados al servidor
        ↓
Servidor guarda con pickle
        ↓
Archivo datos.pkl actualizado
        ↓
Al reiniciar → datos restaurados

📚 Conceptos implementados

Persistencia de datos

Serialización de objetos

Arquitectura cliente-servidor

Comunicación asíncrona

Restauración del estado de ejecución

Generación de documentos dinámicos

⚠️ Notas importantes

pickle no debe usarse con datos no confiables

el archivo PDF se sobrescribe en cada guardado

el servidor debe estar activo para funcionar

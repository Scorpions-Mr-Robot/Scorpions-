from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = Flask(__name__)

# 🔹 Conectar a MongoDB Atlas
URI = "mongodb+srv://rluisabad:ksRcInFjwjtJMcyC@cluster0.gpkrs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(URI)
    db = client["Registro"]  # Base de datos
    collection = db["usuarios"]  # Colección
    client.admin.command('ping')  # Prueba de conexión
    print("✅ Conectado a MongoDB correctamente")
except ConnectionFailure as e:
    print(f"❌ Error de conexión a MongoDB: {e}")

# 🔹 Ruta principal (Carga el formulario HTML)
@app.route('/')
def index():
    return render_template('index.html')

# 🔹 Ruta de registro
@app.route('/registro', methods=['POST'])
def registrar_usuario():
    try:
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")

        if not nombre or not correo:
            return jsonify({"error": "Todos los campos son obligatorios"}), 400

        if collection.find_one({"correo": correo}):
            return jsonify({"error": "Este correo ya está registrado"}), 409

        usuario = {"nombre": nombre, "correo": correo}
        resultado = collection.insert_one(usuario)

        if resultado.inserted_id:
            return jsonify({"mensaje": "✅ Registro exitoso"}), 201
        else:
            return jsonify({"error": "No se pudo registrar el usuario"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)

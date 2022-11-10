from flask import Flask, request, render_template, redirect
from helper.crudTareas import database

app = Flask(__name__)

db = database()

#Comentario prueba

@app.route("/")
@app.route("/listaTareas", methods=["GET"])
def listaTareas():
    tareas = db.leerTareas()
    print(tareas)
    return render_template("lista_tareas.html", template_tareas = tareas)

@app.route("/formulario", methods=["GET"])
def crearTarea():
    return render_template("formulario.html")

@app.route("/formulario", methods=["POST"])
def guardarTarea():
    tarea = request.form["tarea"]
    db.agregarTarea(tarea)
    return redirect("/listaTareas")

@app.route("/eliminarTarea/<id>", methods=["GET"])
def eliminarTarea(id):
    db.eliminarTarea(id)
    tareas = db.leerTareas()
    return render_template("lista_tareas.html", template_tareas = tareas)

@app.route("/editarTarea/<id>", methods=["GET"])
def editarTarea(id):
    tarea = db.leerTareaId(id)
    print(tarea)
    return render_template("formularioEditarTarea.html", tarea_por_defecto = tarea[0][1], id=id)

@app.route("/editarTarea/<id>", methods=["POST"])
def cambiarTarea(id):
    nuevaTarea = request.form["tarea"]
    db.editarTarea(id, nuevaTarea)
    return redirect("/listaTareas")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 3000)
    app.debug()

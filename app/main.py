from fastapi import FastAPI

app = FastAPI()

@app.post("/api/empleados")
def crear_empleado(empleado: dict):
    return {
        "mensaje": "Empleado creado correctamente",
        "empleado": empleado
    }

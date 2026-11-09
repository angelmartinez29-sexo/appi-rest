class Empleado:
    def __init__(self, idEmp: int, nombreEmp: str, fechaNac: str, sueldo: float = 0.0):
        self.idEmp = idEmp
        self.nombreEmp = nombreEmp
        self.fechaNac = fechaNac
        self.sueldo = sueldo

    def createPOST(self, nombrePOST, sueldoPOST):
        self.nombreEmp = nombrePOST
        self.sueldo = sueldoPOST
        print(f"Registrando empleado en la BD con sueldo inicial: ${self.sueldo}")

    def readGET(self):
        return f"Nombre: {self.nombreEmp} | Sueldo: ${self.sueldo}"

    def getSueldo(self):
        return self.sueldo

    def updatePUT(self, nuevoNombre, aumentoSueldo):
        self.nombreEmp = nuevoNombre
        self.sueldo += aumentoSueldo
        print(f"Actualizando empleado en la BD. Nuevo sueldo: ${self.sueldo}")
    def deleteDEL(self):
        print("Eliminando el empleado de la BD")


# --- Pruebas ---
app = Empleado(1, "", "")

app.createPOST("Roberto", 7000)

# Recuperar solo el valor del sueldo en una variable
sueldo_actual = app.getSueldo()
print(f"El sueldo recuperado es: ${sueldo_actual}")

app.updatePUT("williams", 500)

sueldo_actualizado = app.getSueldo()
print(f"El nuevo sueldo recuperado es: ${sueldo_actualizado}")
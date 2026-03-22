
---

## Funcionamiento del Sistema

###  1. Modelo (`modelos/visitante.py`)
Define la clase `Visitante`, que representa los datos de cada persona:
- Cédula 
- Nombre
- Motivo de la visita

---

###  2. Servicio (`servicios/visita_servicio.py`)
Contiene la lógica del sistema (CRUD):
- `registrar()` → Agrega un visitante si no existe
- `listar()` → Devuelve la lista de visitantes
- `eliminar()` → Elimina un visitante por cédula

La lista de visitantes está encapsulada (no accesible directamente).

---

### 3. Interfaz (`ui/app_tkinter.py`)
Construida con Tkinter:
- Formulario de entrada de datos
- Botones de acción (Registrar, Eliminar, Limpiar)
- Tabla dinámica (`Treeview`) para visualizar registros
- Validaciones con mensajes emergentes

---

### 4. Main (`main.py`)
Punto de entrada del programa:
- Crea el servicio
- Inyecta el servicio en la interfaz
- Ejecuta la aplicación

---


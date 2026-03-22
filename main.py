from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import App

if __name__ == "__main__":
    servicio = VisitaServicio()
    app = App(servicio)
    app.mainloop()
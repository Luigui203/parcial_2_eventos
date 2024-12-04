import tkinter as tk
from tkinter import messagebox
import random

class JuegoAdivinarNumero:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Juego de Adivinar el Número")
        
        # Variables para el juego
        self.rango_maximo = None
        self.numero_adivinar = None
        self.max_intentos = None
        self.intentos_realizados = 0
        self.vector_resultados = []
        self.juego_terminado = False  # Nueva bandera para controlar el estado del juego
        
        # Inicializar la interfaz
        self.inicializar_interfaz()
    
    def inicializar_interfaz(self):
        """Configura la interfaz inicial para seleccionar el rango."""
        self.limpiar_interfaz()
        
        tk.Label(self.ventana, text="Introduce el rango máximo:").pack(pady=10)
        self.entrada_rango = tk.Entry(self.ventana)
        self.entrada_rango.pack(pady=5)
        
        tk.Button(self.ventana, text="Iniciar Juego", command=self.iniciar_juego).pack(pady=10)
    
    def limpiar_interfaz(self):
        """Elimina todos los widgets de la ventana."""
        for widget in self.ventana.winfo_children():
            widget.destroy()
    
    def iniciar_juego(self):
        """Inicia el juego generando el número y configurando los intentos."""
        try:
            self.rango_maximo = int(self.entrada_rango.get())
            if self.rango_maximo <= 1:
                messagebox.showerror("Error", "El rango máximo debe ser mayor a 1.")
                return
            
            # Configurar el número aleatorio y el vector
            self.max_intentos = self.rango_maximo // 20 or 1  # Al menos 1 intento
            self.numero_adivinar = random.randint(1, self.rango_maximo)
            self.vector_resultados = ["falló"] * self.rango_maximo
            self.vector_resultados[self.numero_adivinar - 1] = "acertó"
            self.intentos_realizados = 0
            self.juego_terminado = False  # Reiniciar bandera
            
            # Mostrar la interfaz de juego
            self.mostrar_interfaz_juego()
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número entero válido.")
    
    def mostrar_interfaz_juego(self):
        """Configura la interfaz para que el usuario realice sus intentos."""
        self.limpiar_interfaz()
        
        tk.Label(self.ventana, text=f"Adivina un número entre 1 y {self.rango_maximo}").pack(pady=10)
        tk.Label(self.ventana, text=f"Tienes {self.max_intentos} intentos.").pack(pady=5)
        
        self.entrada_intento = tk.Entry(self.ventana)
        self.entrada_intento.pack(pady=5)
        
        tk.Button(self.ventana, text="Intentar", command=self.realizar_intento).pack(pady=10)
        self.resultado_label = tk.Label(self.ventana, text="", wraplength=300)
        self.resultado_label.pack(pady=10)
    
    def realizar_intento(self):
        """Evalúa el intento del usuario."""
        if self.juego_terminado:
            return  # Si el juego ya terminó, no se realizan más acciones
        
        try:
            intento = int(self.entrada_intento.get())
            self.intentos_realizados += 1
            
            if intento < 1 or intento > self.rango_maximo:
                self.resultado_label.config(text=f"El número debe estar entre 1 y {self.rango_maximo}.")
                return
            
            if intento == self.numero_adivinar:
                self.juego_terminado = True
                messagebox.showinfo("¡Ganaste!", f"¡Felicidades! Adivinaste el número {self.numero_adivinar} "
                                                 f"en {self.intentos_realizados} intento(s).")
                self.mostrar_resultado_final(True)
            elif intento < self.numero_adivinar:
                self.resultado_label.config(text="El número a adivinar es mayor.")
            else:
                self.resultado_label.config(text="El número a adivinar es menor.")
            
            if self.intentos_realizados >= self.max_intentos and not self.juego_terminado:
                self.juego_terminado = True
                self.mostrar_resultado_final(False)
        
        except ValueError:
            self.intentos_realizados += 1
            self.resultado_label.config(text="Entrada no válida. Por favor, introduce un número entero.")
    
    def mostrar_resultado_final(self, ganador):
        """Muestra un mensaje final y reinicia el juego."""
        if ganador:
            resultado = f"Estado del vector: {self.vector_resultados}"
        else:
            resultado = f"¡Lo siento! No lograste adivinar el número. Era {self.numero_adivinar}.\n" \
                        f"Estado del vector: {self.vector_resultados}"
        messagebox.showinfo("Fin del juego", resultado)
        self.inicializar_interfaz()


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoAdivinarNumero(root)
    root.mainloop()

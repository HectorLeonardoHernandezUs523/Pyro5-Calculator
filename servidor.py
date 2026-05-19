import Pyro5.api


@Pyro5.api.expose
class Calculadora:
    """Servicio remoto simple de calculadora"""
    
    def __init__(self):
        self.historial = []
    
    def suma(self, a, b):
        """Suma dos números"""
        resultado = a + b
        self.historial.append(f"suma({a}, {b}) = {resultado}")
        return resultado
    
    def resta(self, a, b):
        """Resta dos números"""
        resultado = a - b
        self.historial.append(f"resta({a}, {b}) = {resultado}")
        return resultado
    
    def multiplicacion(self, a, b):
        """Multiplica dos números"""
        resultado = a * b
        self.historial.append(f"multiplicacion({a}, {b}) = {resultado}")
        return resultado
    
    def division(self, a, b):
        """Divide dos números"""
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        resultado = a / b
        self.historial.append(f"division({a}, {b}) = {resultado}")
        return resultado
    
    def obtener_historial(self):
        """Obtiene el historial de operaciones"""
        return self.historial
    
    def limpiar_historial(self):
        """Limpia el historial de operaciones"""
        self.historial = []
        return "Historial limpiado"
    
    def obtener_info(self):
        """Obtiene información del servidor"""
        return f"Servidor Calculadora - {len(self.historial)} operaciones realizadas"


def main():
    servidor = Calculadora()
    with Pyro5.api.Daemon(host="localhost", port=9090) as daemon:
        uri = daemon.register(servidor, "calculadora")
        print(f"Servidor iniciado en: {uri}")
        print("Esperando conexiones de clientes...")
        print("Presiona Ctrl+C para detener el servidor\n")
        
        try:
            daemon.requestLoop()
        except KeyboardInterrupt:
            print("\nServidor detenido.")


if __name__ == "__main__":
    main()

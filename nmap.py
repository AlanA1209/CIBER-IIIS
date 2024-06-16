import socket

# Configuración del servidor de destino
hostname = '192.168.1.4'
port = 22  # Puerto de destino

def simulate_nmap_scan(hostname, port):
    try:
        # Crear un socket TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((hostname, port))
        s.send(b'')  # Enviar un paquete con tamaño de datos 0
        print(f"Sent TCP packet with size 0 to {hostname}:{port}")
        s.close()
    except Exception as e:
        print(f"Connection failed: {e}")

for _ in range(10):  # Simular múltiples intentos
    simulate_nmap_scan(hostname, port)

print("Nmap scan simulation completed.")

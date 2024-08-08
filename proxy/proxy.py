import socket
import threading

class FirewallProxy:
    # Inicializa o proxy com o endereço do servidor e a porta
    def __init__(self, host='localhost', port=8888):
        self.server_address = (host, port)
        self.allowed_domains = ['www.example.com']  # Domínios permitidos

    # Inicia o proxy
    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket TCP
        server.bind(self.server_address) # Associa o socket ao endereço do servidor
        server.listen(5) # Habilita o servidor para aceitar conexões
        print(f"Proxy listening on {self.server_address}") # Imprime o endereço do servidor

        # Aceita conexões de clientes
        while True:
            client_socket, _ = server.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    # Manipula a solicitação do cliente
    def handle_client(self, client_socket):
        request = client_socket.recv(4096).decode() # Recebe a solicitação do cliente
        print(f"Received request:\n{request}") 

        # Extrair o domínio da solicitação
        lines = request.split('\n') 
        host = None 
        for line in lines: 
            if line.startswith('Host:'): 
                host = line.split(' ')[1].strip() 
                break

        if host is None:
            print("No host found in request.")
            client_socket.sendall(b"HTTP/1.1 400 Bad Request\r\n\r\nNo Host header found.") 
            client_socket.close()
            return

        # Verificar se o domínio está permitido
        if host not in self.allowed_domains:
            print(f"Access denied to domain: {host}")
            client_socket.sendall(b"HTTP/1.1 403 Forbidden\r\n\r\nAccess Denied")
            client_socket.close()
            return

        # Encaminhar solicitação ao servidor real
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: 
            server_socket.connect((host, 80))  # Conectar ao servidor real
            server_socket.sendall(request.encode())

            while True:
                response = server_socket.recv(4096)
                if len(response) == 0:
                    break
                client_socket.sendall(response)

        client_socket.close()

if __name__ == "__main__":
    proxy = FirewallProxy()
    proxy.start()

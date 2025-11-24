class RoundRobinLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def get_next_server(self):
        if not self.servers:
            return "No servers available"
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

    def add_server(self, server):
        self.servers.append(server)
        print(f"Server '{server}' added.")

    def remove_server(self, server):
        if server in self.servers:
            self.servers.remove(server)
            print(f"Server '{server}' removed.")
            if self.current_index >= len(self.servers):
                self.current_index = 0
        else:
            print(f"Server '{server}' not found.")


if __name__ == "__main__":
    lb = RoundRobinLoadBalancer(["Server1", "Server2", "Server3"])

    for i in range(1, 11):
        server = lb.get_next_server()
        print(f"Request {i} handled by {server}")

    lb.add_server("Server4")

    for i in range(11, 16):
        server = lb.get_next_server()
        print(f"Request {i} handled by {server}")

    lb.remove_server("Server2")

    for i in range(16, 21):
        server = lb.get_next_server()
        print(f"Request {i} handled by {server}")

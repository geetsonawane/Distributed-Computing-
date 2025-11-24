class Resource:
    def __init__(self, name):
        self.name = name
        self.holder = None

class Process:
    def __init__(self, name):
        self.name = name
        self.held_resources = []
        
    def request_resource(self, resource):
        if resource.holder is None:
            resource.holder = self
            self.held_resources.append(resource)
            print(f"{self.name} acquired {resource.name}.")  # Fixed formatting
        else:
            print(f"{self.name} is waiting for {resource.name} held by {resource.holder.name}.")  # Fixed formatting

def detect_deadlock(processes):
    for process in processes:
        if len(process.held_resources) == 2:
            print(f"Potential deadlock detected with {process.name} holding 2 resources")  # Fixed formatting

def main():
    # Create resources and processes
    r1, r2 = Resource("R1"), Resource("R2")
    p1, p2 = Process("P1"), Process("P2")
    
    # Simulate resource allocation
    p1.request_resource(r1)
    p1.request_resource(r2)
    p2.request_resource(r1)  # Changed from p1 to p2 to simulate a proper wait
    
    # Check for deadlocks
    detect_deadlock([p1, p2])

if __name__ == "__main__":
    main()


class ServiceManager:
    def __init__(self):
        self.services = []

    def add_service(self, service):
        self.services.append(service)

    def get_services(self):
        return self.services

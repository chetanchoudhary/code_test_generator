class DIContainer:
    def __init__(self):
        self._services = {}

    def register(self, service_name, service_factory):
        self._services[service_name] = service_factory

    def get(self, service_name):
        if service_name not in self._services:
            raise KeyError(f"Service '{service_name}' not registered.")
        return self._services[service_name]()

container = DIContainer()
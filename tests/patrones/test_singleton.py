from python_smarthome.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry

def test_singleton_instance():
    registry1 = DispositivoServiceRegistry.get_instance()
    registry2 = DispositivoServiceRegistry.get_instance()
    assert registry1 is registry2

def test_singleton_new():
    registry1 = DispositivoServiceRegistry()
    registry2 = DispositivoServiceRegistry()
    assert registry1 is registry2

def test_singleton_mixed():
    registry1 = DispositivoServiceRegistry()
    registry2 = DispositivoServiceRegistry.get_instance()
    assert registry1 is registry2

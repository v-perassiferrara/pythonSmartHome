from python_smarthome.entidades.usuarios.usuario import Usuario
from python_smarthome.entidades.usuarios.escena import Escena
from python_smarthome.entidades.usuarios.nivel_acceso import NivelAcceso

def test_usuario():
    escena = Escena(id_escena=1, nombre="Modo Noche", descripcion="Luces tenues")
    usuario = Usuario(id_usuario=1, nombre="Juan Perez", nivel_acceso=NivelAcceso.PROPIETARIO, escenas=[escena])

    assert usuario.get_id_usuario() == 1
    assert usuario.get_nombre() == "Juan Perez"
    assert usuario.get_nivel_acceso() == NivelAcceso.PROPIETARIO
    assert len(usuario.get_escenas()) == 1

def test_escena():
    escena = Escena(id_escena=2, nombre="Modo Cine", descripcion="Luces apagadas")
    assert escena.get_id_escena() == 2
    assert escena.get_nombre() == "Modo Cine"
    assert escena.get_descripcion() == "Luces apagadas"

def test_nivel_acceso():
    assert NivelAcceso.INVITADO.value == 1
    assert NivelAcceso.FAMILIAR.value == 2
    assert NivelAcceso.PROPIETARIO.value == 3
    assert NivelAcceso.ADMIN.value == 4
    assert NivelAcceso.SUPER.value == 5

from libpythonpro.spam.model import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Arthur', email='tavares.arthur@ymail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Arthur', email='tavares.arthur@ymail.com'),
        Usuario(nome='Bernardo', email='tavares.arthur@ymail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

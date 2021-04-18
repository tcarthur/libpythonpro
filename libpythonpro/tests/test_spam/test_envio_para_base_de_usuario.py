import pytest as pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.model import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Arthur', email='tavares.arthur@ymail.com'),
            Usuario(nome='Bernardo', email='tavares.arthur@ymail.com')

        ],
        [
            Usuario(nome='Arthur', email='tavares.arthur@ymail.com'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'tavares.arthur@ymail.com',
        'Módulo PyTools',
        'Teste do código'
    )
    assert len(usuarios) == enviador.qtd_email_enviados

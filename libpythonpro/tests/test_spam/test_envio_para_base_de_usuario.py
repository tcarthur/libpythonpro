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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'tavares.arthur@ymail.com',
        'Módulo PyTools',
        'Teste do código'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):

    usuario = Usuario(nome='Arthur', email='tavares.arthur@ymail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'tavares.bernardo@ymail.com',
        'Módulo PyTools',
        'Teste do código'
    )
    assert enviador.parametros_de_envio == (
        'tavares.bernardo@ymail.com',
        'tavares.arthur@ymail.com',
        'Módulo PyTools',
        'Teste do código'
    )

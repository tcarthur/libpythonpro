import pytest as pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['tavares.arthur@ymail.com','contato.arthurpig@gmail.com']
)
def test_remetente(destinatario):
    enviador=Enviador()

    resultado = enviador.enviar(
        destinatario,
        'contato.arthurpig@gmail.com',
        'Curso Python Pro',
        'Aula do módulo PyTools.'
    )
    assert destinatario in resultado
import pytest as pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['tavares.arthur@ymail.com', 'contato.arthurpig@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'contato.arthurpig@gmail.com',
        'Curso Python Pro',
        'Aula do módulo PyTools.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'arthurpigcom']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'contato.arthurpig@gmail.com',
            'Curso Python Pro',
            'Aula do módulo PyTools.'
        )

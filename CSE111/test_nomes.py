from nomes import criar_nome_completo, extrair_primeiro_nome, extrair_sobrenome
import pytest

def test_criar_nome_completo():
    primeiro_nome = "Eliane"
    sobrenome = "Oliveira"
    resultado = "Oliveira; Eliane"

    saida = criar_nome_completo(primeiro_nome, sobrenome)
    
    assert saida == resultado


def test_extrair_sobrenome():
    nome_completo = "Oliveira; Eliane"
    saida_esperada = "Oliveira"

    saida = extrair_sobrenome(nome_completo)
    
    assert saida == saida_esperada


def test_extrair_primeiro_nome():
    nome_completo = "Oliveira; Eliane"
    saida_esperada = "Eliane"

    saida = extrair_primeiro_nome(nome_completo)
    
    assert saida == saida_esperada


pytest.main(["-v", "--tb=line", "-rN", __file__])
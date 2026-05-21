from endereco import extrair_cidade, extrair_estado, extrair_cep
import pytest

def test_extrair_cidade():
    endereco_completo = "Rua das Flores, 123, Centro, Belo Horizonte - MG, 30123-456"
    saida_esperada = "Belo Horizonte"
    assert extrair_cidade(endereco_completo) == saida_esperada

def test_extrair_estado():
    endereco_completo = "Rua das Flores, 123, Centro, Belo Horizonte - MG, 30123-456"
    saida_esperada = "MG"
    assert extrair_estado(endereco_completo) == saida_esperada

def test_extrair_cep():
    endereco_completo = "Rua das Flores, 123, Centro, Belo Horizonte - MG, 30123-456"
    saida_esperada = "30123-456"
    assert extrair_cep(endereco_completo) == saida_esperada

pytest.main(["-v", "--tb=line", "-rN", __file__])
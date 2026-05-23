from pytest import approx
import pytest
from fluxo_de_agua import calc_altura_coluna_agua, calc_pressao_pela_altura, calc_perda_pressao_tubo, calc_perda_pressao_conexoes, calc_num_reynolds, calc_perda_pressao_reducao_tubo, kpa_para_mca

def test_cal_altura_coluna_agua():
    assert calc_altura_coluna_agua(0, 0) == approx(0.0  )
    assert calc_altura_coluna_agua(0, 10) == approx(7.5)
    assert calc_altura_coluna_agua(25, 0) == approx(25.0)
    assert calc_altura_coluna_agua(48.3, 12.8) == approx(57.9)

def test_calc_pressao_pela_altura():
    assert calc_pressao_pela_altura(0.0) == approx(0.0, abs=0.001)
    assert calc_pressao_pela_altura(30.2) == approx(295.628, abs=0.001)
    assert calc_pressao_pela_altura(50.0) == approx(489.450, abs=0.001)

def test_calc_perda_pressao_tubo():
    assert calc_perda_pressao_tubo(0.048692, 0.0, 0.018, 1.75) == approx(0.0, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.0, 0.0, 1.75) == approx(0.0, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.0, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.0, 0.018, 1.65) == approx(-100.462, abs=0.001)

def test_calc_perda_pressao_conexoes():
    assert calc_perda_pressao_conexoes(0.00, 3) == approx(0.0, abs=0.001)
    assert calc_perda_pressao_conexoes(1.65, 0) == approx(0.0, abs=0.001)
    assert calc_perda_pressao_conexoes(1.65, 2) == approx(-0.109, abs=0.001)
    assert calc_perda_pressao_conexoes(1.75, 2) == approx(-0.122, abs=0.001)
    assert calc_perda_pressao_conexoes(1.75, 5) == approx(-0.306, abs=0.001)
    
def test_calc_num_reynolds():
    assert calc_num_reynolds(0.048692, 0.0) == approx(0.0, abs=1)
    assert calc_num_reynolds(0.048692, 1.65) == approx(80069, abs=1)
    assert calc_num_reynolds(0.048692, 1.75) == approx(84922, abs=1)
    assert calc_num_reynolds(0.286870, 1.65) == approx(471729, abs=1)
    assert calc_num_reynolds(0.286870, 1.75) == approx(500318, abs=1)

def test_calc_perda_pressao_reducao_tubo():
    assert calc_perda_pressao_reducao_tubo(0.28687, 0.00, 1, 0.048692) == approx(0.0, abs=0.001)
    assert calc_perda_pressao_reducao_tubo(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert calc_perda_pressao_reducao_tubo(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)


# Melhoria adicionada para converter KPa para MCA, para facilitar a compreensão do usuário, pois é mais comum falar em metros de coluna d'água do que em KPa no Brasil.
def test_kpa_para_mca():
    assert kpa_para_mca(0.0) == approx(0.0, abs=0.1)
    assert kpa_para_mca(158.7) == approx(16.2, abs=0.1)


# Chama a função main que faz parte do pytest para que o
# o computador execute as funções de teste neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])
import math
import pytest

class Circulo:
    def __init__(self, raio):
        if raio < 0:
            raise ValueError("O raio não pode ser negativo!")
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

# Testes
def test_area_circulo():
    circulo = Circulo(1)
    assert circulo.area() == pytest.approx(math.pi, rel=1e-5)
    
    circulo = Circulo(0)
    assert circulo.area() == 0
    
    circulo = Circulo(2)
    assert circulo.area() == pytest.approx(4 * math.pi, rel=1e-5)
    
    with pytest.raises(ValueError):
        Circulo(-1)

# Código de execução principal
if __name__ == "__main__":
    raio = float(input("Digite o raio do círculo: "))
    circulo = Circulo(raio)
    print(f"O valor da área do círculo de raio {raio} equivale a {circulo.area()}")
import math

class GeometriaPlana:
    '''Classe para cálculos de geometria plana.'''

    @staticmethod
    def area_triangulo(base: float, altura: float) -> float:
        """Calcula a área de um triângulo."""

        return (base * altura) / 2

    @staticmethod
    def area_quadrado(lado: float) -> float:
        """Calcula a área de um quadrado."""

        return lado ** 2

    @staticmethod
    def area_retangulo(base: float, altura: float) -> float:
        """Calcula a área de um retângulo."""

        return base * altura

    @staticmethod
    def area_paralelogramo(base: float, altura: float) -> float:
        """Calcula a área de um paralelogramo."""

        return base * altura
    
    @staticmethod
    def area_losango(diagonal_maior: float, diagonal_menor: float) -> float:
        """Calcula a área de um losango."""

        return (diagonal_maior * diagonal_menor) / 2
    
    @staticmethod
    def area_trapezio(base_maior: float, base_menor: float, altura: float) -> float:
        """Calcula a área de um trapézio."""

        return ((base_maior + base_menor) * altura) / 2
    
    @staticmethod
    def area_circulo(raio: float) -> float:
        """Calcula a área de um círculo."""

        return math.pi * (raio ** 2)
    
    @staticmethod
    def area_coroa_circular(raio_externo: float, raio_interno: float) -> float:
        """Calcula a área de uma coroa circular."""

        return math.pi * (raio_externo ** 2 - raio_interno ** 2)
    
    @staticmethod
    def area_setor_circular(raio: float, angulo_graus: float) -> float:
        """Calcula a área de um setor circular."""

        return (angulo_graus / 360) * math.pi * (raio ** 2)

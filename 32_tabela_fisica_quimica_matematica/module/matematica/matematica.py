from geometria_plana import *

class CalculoMatematica:
    '''Classe para cálculos matemáticos.'''


    def service(formula: str, funcao: str):


        match funcao:
            case "area_quadrado":
                value = GeometriaPlana.area_quadrado(5)

        return value

### gerar dados json

import json

class Payload:
    def __init__(self):

        self.dados = {
            'nome': 'João',
            'sobrenome': 'Pedro Sousa Silva',
            'idade': 30,
            'cidade': 'São Paulo',
            'estado': 'SP',
            'nacionalidade': 'Brasileiro',
            'solteiro': True,
            'filhos': None,
            'altura': 1.80,
            'peso': 80.5,
            'sexo': 'M',
            'profissao': 'Professor',
            'salario': 2500.00,
            'email': 'jp-s-s@teste.com',
            'titulos': ['Graduação', 'Mestrado', 'Doutorado'],
            'idiomas': {
                'ingles': 'fluente',
                'espanhol': 'básico',
                'frances': 'básico'
            },
            'notas': [
                55,
                70,
                30,
                40,
                85
            ],
            'carro': {
                'marca': 'Ford',
                'modelo': 'Fiesta',
                'ano': 2010,
                'cor': 'branco',
                'placa': 'ABC-1234',
                'km': 50000,
                'vistorias': [
                    {
                        'data': '20200522',
                        'local': 'DETRAN',
                        'resultado': 'Aprovado'
                    },
                    {
                        'data': '20210215',
                        'local': 'Autorizada',
                        'resultado': 'Reprovado'
                    },
                    {
                        'data': '20230311',
                        'local': 'DETRAN',
                        'resultado': 'Aprovado'
                    }
                ]
            }
        }


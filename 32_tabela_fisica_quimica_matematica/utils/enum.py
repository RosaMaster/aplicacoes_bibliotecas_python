import enum

class Categoria(enum.IntEnum):
    '''Categorias de disciplinas'''

    fisica = 1
    quimica = 2
    matematica = 3


class Matematica(enum.IntEnum):
    '''Subcategorias de Matemática'''

    simbolos_usuais = 1
    identidades_notaveis = 2
    radicais_racionalizacao = 3
    sistema_lineares = 4
    potencias = 5
    equacao_do_1o_grau = 6
    equacao_do_2o_grau = 7
    funcao_polinominal_do_1o_grau = 8
    funcao_polinominal_do_2o_grau = 9
    funcao_modular = 10
    funcao_exponencial = 11
    funcao_logaritmica = 12
    progressao_geometrica = 13
    progressao_aritmetica = 14
    analise_combinatoria = 15
    trigonometria = 16
    numeros_complexos = 17
    geometria_analitica = 18
    GeometriaPlana = 19
    geometria_espacial = 20
    # estatistica = 21
    # probabilidade = 22
    # conjuntos = 23


class Fisica(enum.IntEnum):
    '''Subcategorias de Física'''

    optica = 1
    termologia = 2
    hidrostatica = 3
    cinematica_e_dinamica = 4
    eletromagnetismo = 5
    ondulatoria = 6
    eletrodinamica = 7
    eletrostatica = 8
    # eletricidade = 9
    # magnetismo = 10
    # mecanica = 11
    # termodinamica = 12
    # fluidos = 13
    # metrologia = 14


class Quimica(enum.IntEnum):
    '''Subcategorias de Química'''

    tabela_periodica_dos_elementos = 1
    tabela_de_cations_e_anions = 2
    forca_das_bases_e_dos_acidos = 3
    atividade_reatividade_dos_elementos = 4
    unidades_de_concentracao_das_solucoes = 5
    propriedades_coligativas = 6
    equilibrio_quimico = 7
    ph_e_poh = 8
    solubilidade = 9
    # ligacoes_quimicas = 10
    # eletroquimica = 11
    # estequiometria = 12
    # nomenclatura_quimica = 13
    # propriedades_periodicas_dos_elementos = 14
    # gases = 15
    # termodinamica = 16
    # cinetica_quimica = 17
    # estados_fisicos_da_materia = 18
    # atomistica = 19
    # tabela_de_cores_para_indicadores_acido_base = 20
    # tabela_de_constantes_quimicas = 21
    # tabela_de_calores_especificos = 22

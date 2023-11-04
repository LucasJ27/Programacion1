import pytest
from FuncionesParcial2 import is_mutant


test_data = [
    (  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en las FILAS del ADN
        [
            "AAAATT",
            "CGATAC",
            "GGGGAT",  
            "CCGATT",
            "GGGTTA",
            "AACAGC"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en las FILAS del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TAGCAT",
            "CCGATT",
            "GGGTTA",
            "AATAGC"
        ],
        False
    ),
    (  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en las COLUMNAS del ADN
        [
            "AAAGTT",
            "AGAGAC",
            "AGGGAT",
            "ACTGTT",
            "GTCGTA",
            "AATCTC"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en las COLUMNAS del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TAGCAT",
            "CCGATT",
            "GGGTTA",
            "AATAGC"
        ],
        False
    ),(  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en la DIAGONAL PRINCIPAL del ADN
        [
            "TAAGTT",
            "CTACAC",
            "GCTGAT",
            "CAGTTT",
            "GCGCTA",
            "AATAGC"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en la DIAGONAL PRINCIPAL del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TAGCAT",
            "CCGATT",
            "GGGTTA",
            "AATAGC"
        ],
        False
    ),(  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en la DIAGONAL SUPERIOR del ADN
        [
            "ATAATT",
            "CGTTAC",
            "GGGTAT",
            "CCGATT",
            "GGGTTA",
            "AATAGC"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en la DIAGONAL SUPERIOR del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TAGCAT",
            "CCGATT",
            "GGGTTA",
            "AATAGC"
        ],
        False
    ),(  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en la DIAGONAL SUPERIOR POSTERIOR del ADN
        [
            "AATATT",
            "CGATAC",
            "GGCGTT",  
            "CCGATT",
            "GCGTTA",
            "AATAGC"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en la DIAGONAL SUPERIOR POSTERIOR del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TAGCAT",
            "CCGATT",
            "GGGTTA",
            "AATAGC"
        ],
        False
    ),(  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en la DIAGONAL INFERIOR del ADN
        [
            "AAGATT",
            "CGATAC",
            "GCGGAT",
            "AGCATT",
            "GGGCTA",
            "AATACG"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en la DIAGONAL INFERIOR del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TAGCAT",
            "CCGAGT",
            "GGGTTA",
            "AATAGC"
        ],
        False
    ),(  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en la DIAGONAL INFERIOR POSTERIOR del ADN
        [
            "AATATT",
            "CGATAC",
            "GCTTAT",
            "CGCATT",
            "ATGTTA",
            "AAAGAC"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en la DIAGONAL INFERIOR POSTERIOR del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TAGCAT",
            "CCGATT",
            "GTGCTA",
            "AATAGC"
        ],
        False
    ),(  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en la DIAGONAL INVERSA del ADN
        [
            "AGAAGT",
            "CGACTC",
            "GGGTAT",  
            "CCTATG",
            "GTGCTA",
            "AATAGC"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en la DIAGONAL INVERSA del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TAGCAT",
            "CCGATT",
            "GGGTTA",
            "AATAGC"
        ],
        False
    ),(  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en la DIAGONAL INVERSA SUPERIOR del ADN
        [
            "AGAATT",
            "CGATAC",
            "GGTGAT",
            "CTGAGT",
            "CGGTTA",
            "AACAGC"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en la DIAGONAL INVERSA SUPERIOR del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TCGCAT",
            "CCAATT",
            "GTGCTA",
            "AATAGC"
        ],
        False
    ),(  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en la DIAGONAL INVERSA SUPERIOR POSTERIOR del ADN
        [
            "AGAATT",
            "CGATAC",
            "GAGGAT",
            "ACGACT",
            "GGGTTA",
            "ACTAGC"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en la DIAGONAL INVERSA SUPERIOR POSTERIOR del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TAGCAT",
            "CCGATT",
            "CGGCTA",
            "AATAGC"
        ],
        False
    ),(  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en la DIAGONAL INVERSA INFERIOR del ADN
        [
            "AGAATT",
            "CGATAC",
            "GAGGCT",
            "TCGCTT",
            "GGCTTA",
            "ACTAGC"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en la DIAGONAL INVERSA INFERIOR del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TAGTAT",
            "CCTATT",
            "GCGGTA",
            "AATAGC"
        ],
        False
    ),(  # Probamos la EXISTENCIA de secuencias de 4 letras iguales en la DIAGONAL INVERSA INFERIOR POSTERIOR del ADN
        [
            "AACATT",
            "CGATAC",
            "GTGGAT",  # Contiene una secuencia repetida "GGAT"
            "CCGATT",
            "GGGTAA",
            "AATAGC"
        ],
        True
    ),
    (  # Probamos la AUSENCIA de secuencias de 4 letras iguales en la DIAGONAL INVERSA INFERIOR POSTERIOR del ADN
        [
            "ATCGAT",
            "CGATAC",
            "TAGCAT",
            "CCGAGT",
            "GGGTTA",
            "AACAGC"
        ],
        False
    ),
]

@pytest.mark.parametrize("dna, res", test_data)
def test_is_mutant(dna, res):
    assert is_mutant(dna) == res
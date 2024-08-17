from .. import efeitos
from . import equalizador
from audio.efeitos import eco
from ..formatos import wav_leitura


def codificador_feminino(entrada, saida, p3, p4):
    print("filtros/codificador_voz/")
    print("Codificador feminino")
    equalizador.modo_rock(1,2,3,4)

def codificador_masculino(entrada, saida, p3, p4):
    print("filtros/codificador_voz/")
    print("Codificador masculino")
    efeitos.eco.eco_filtro(1,2,3,4)
    eco.eco_filtro(1,2,3,4)

def codificador_adulto(entrada, saida, p3, p4):
    print("filtros/codificador_voz/")
    print("Codificador adulto")
    wav_leitura.entrada(1,2)


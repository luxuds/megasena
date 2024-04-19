from megasena import MegasenaClass

if __name__ == "__main__":
    megasena = MegasenaClass()
    jogo = [9, 21, 31, 39, 47, 59, 1, 15, 17]
    print('\n>>>>>>>>>OCORRÊNCIAS<<<<<<<<')
    ocorrencias = megasena.getOcorrencias()
    for ocorrencia in ocorrencias:
        print(ocorrencia)
    print('>>>>>>>>>FIM DE OCORRÊNCIAS<<<<<<<<')
    print('\n>>>>>>>>>CONFERIR<<<<<<<<')
    conferir = megasena.conferir(jogo)
    print(jogo)
    for con in conferir:
        print(con)
    print('>>>>>>>>>FIM DE CONFERIR<<<<<<<<')
    print('\n>>>>>>>>>SUGERIR<<<<<<<<')
    sugerir = megasena.numerosMaisSorteados()
    sugerir = megasena.sugerirJogo()
    print(sugerir)
    print('>>>>>>>>>FIM DE SUGERIR<<<<<<<<\n')

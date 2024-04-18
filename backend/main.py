from megasena import MegasenaClass

if __name__ == "__main__":
    megasena = MegasenaClass(linha_de_comando=True)
    # megasena.carregar(filename)
    # 2708 jogos
    ocorrencias = megasena.getOcorrencias()
    # jogo = ['9', '21', '31', '39', '47', '59']
    jogo = [9, 21, 31, 39, 47, 59, 1, 15, 17]
    jogo_e_data_do_acerto = megasena.conferir(jogo)
    print(jogo_e_data_do_acerto)
    # if not flag:
    #     print("Jogo invalido...veio com..: ", erro)
    # megasena.numerosMaisSorteados()
    # for numero in megasena.listaDos30NumerosMaisSorteados[:30]:
    #     print(numero)
    # megasena.sugerirJogo()
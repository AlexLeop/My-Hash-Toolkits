""" Importando as bibliotecas necessárias """
import hashlib


def compare_hashes(arquivo1, arquivo2):
    """ Função responsável por compara dois Hashes"""

    if (arquivo1 != '') and (arquivo2 != ''):

        hash1 = hashlib.new('ripemd160')  # Definindo o algoritmo de hash que será usado
        hash1.update(open(arquivo1, 'rb').read())  # Realizando a comparação de hash

        hash2 = hashlib.new('ripemd160')  # Definindo o algoritmo de hash que será usado
        hash2.update(open(arquivo2, 'rb').read())  # Realizando a comparação de hash

        if hash1.digest() != hash2.digest():
            print('\033[32m             OS ARQUIVOS {} E {} SÃO:\n'
                  '                      DIFERENTES!'.format(arquivo1, arquivo2))
            print('\033[38m-' * 67)
            print('\033[38mO hash do arquivo {} é: \033[36m{}'.format(arquivo1, hash1.hexdigest()))
            print('\033[38mO hash do arquivo {} é: \033[36m{}'.format(arquivo2, hash2.hexdigest()))

        else:
            print('\033[32m             OS ARQUIVOS {} E {} SÃO:\n'
                  '                          IGUAIS!'.format(arquivo1, arquivo2))
            print('\033[38m-' * 67)
            print('\033[38mO hash do arquivo {} é: \033[36m{}'.format(arquivo1, hash1.hexdigest()))
            print('\033[38mO hash do arquivo {} é: \033[36m{}'.format(arquivo2, hash2.hexdigest()))

    else:
        if arquivo1 == '':
            return print('O 1º argumento não foi informado')

        else:
            return print('O 2º argumento não foi informado')


if __name__ == '__main__':
    compare_hashes('', 'a.txt')

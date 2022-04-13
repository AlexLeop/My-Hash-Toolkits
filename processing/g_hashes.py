""" Importando as bibliotecas necessárias """
import hashlib


class GenerateHash:
    """ Função responsável por gerar hash a partir do texto informado """
    try:
        @staticmethod
        def hash_md5(string):
            """ Gera da palavra ou texto informado um Hash md5"""
            resultado = hashlib.md5(string.encode('utf-8'))
            print('O hash MD5 de {} é: \033[35m{}'.format(string, resultado.hexdigest()))

        @staticmethod
        def sha_1(string):
            """ Gera da palavra ou texto informado um Hash1"""
            resultado = hashlib.sha1(string.encode('utf-8'))
            print('O hash SHA1 de {} é: \033[35m{}'.format(string, resultado.hexdigest()))

        @staticmethod
        def sha_256(string):
            """ Gera da palavra ou texto informado um Hash256"""
            resultado = hashlib.sha256(string.encode('utf-8'))
            print('O hash SHA256 de {} é: \033[35m{}'.format(string, resultado.hexdigest()))

        @staticmethod
        def sha_512(string):
            """ Gera da palavra ou texto informado um Hash512"""
            resultado = hashlib.sha512(string.encode('utf-8'))
            print('O hash SHA512 de {} é: \033[35m{}'.format(string, resultado.hexdigest()))

    except ValueError as error:
        print('Algo deu Errado, tente novamente.\n {}'.format(error))


if __name__ == '__main__':
    try:
        g = GenerateHash()
        g.sha_1('python e segurança da informação')
    except AttributeError as error:
        print('Hash incorreto!\n Error: {}'.format(error))

# -*- coding: utf-8 -*-

import sys, os.path, time

# Funcao que cria o txt do relatorio
def incluir_log(relat, relat_path, linha, data):
    nome = "{}_{}.txt".format(data, relat)
    try:
        arquivo = open(os.path.join(relat_path, nome),'a')
        arquivo.write(linha)
    except:
        try:
            arquivo = open(os.path.join(relat_path, nome),'w')
            arquivo.write(linha)
        except Exception as ex:
            print ex

print 'Inicio'

relat = 'TESTE_CRIACAO'
relat_path = r"C:\\Teste\\geotag\\"
data = time.strftime('%Y-%m-%d')
horario = time.strftime("%x %X")

linha = 'Teste de criacao de txt'

try:
    incluir_log(relat, relat_path, linha, data)
except Exception as e:
    print 'Erro ao gravar relatorio: ' + str(e)

print 'Fim'

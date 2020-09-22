# coding: utf-8
import time
import threading
import sys
import os
from glob import glob

#Import scripts
import deter
import descompactar
from descompactar import unzipefile_raiz
from deter import import_deter
import temporizador
from temporizador import IntervalRunner
import log
from log import log
import tratamento_data
from tratamento_data import create_publish,datai,datanomei
#import filter_data
from filter_data import filter_data
from deleta_vazio import deleta_vazio


#Importando dados de dadas
datai = datai()
datanomei = datanomei()


def main():
    #chamando a função que baixar os dados do deter
    import_deter()
    #chamando a função que descompacta e move o arquivo deter_amz para a pasta raiz
    unzipefile_raiz()

    #Testando para ver se o dado de datas foi criado
    #print("Vai printar o datai",datai)
    #print(datanomei)

    #Filtrando dado
    for i in range(len(datai)):
        print(i)
        filter_data(datai[i],datanomei[i])
    
    for shp in range(len(glob('*.shp'))-1):
        print(shp)   
        deleta_vazio(datanomei[shp])
        
#Rodando de tempo e tempo
interval_monitor = IntervalRunner(86400.0,main)
interval_monitor.start()
threading.Event().wait()


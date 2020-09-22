# coding: utf-8
#Importando bibliotecas
import sys
import os
from osgeo import ogr
#Biblioteca que realiza operações com datas
from datetime import date
import datetime
import chardet


#Deletando arquivos nulos

def deleta_vazio(datanome):
    os.environ['PROJ_LIB'] = os.path.dirname(sys.argv[0]) 

    #criando diretório
    dir_name = os.path.dirname(os.path.realpath(__file__))

    ds1 = ogr.Open(dir_name,1)

    if ds1 is None:
        sys.exit("Não pode carregar o shp")

    #Modelo de parâmetro
    #datanome = 'Deter_2020_09_31'
    datafilter = str(dir_name+'/'+datanome+'.shp')

    #Criando arquivo que verifica o tamanho do arquivo, se tiver vazio ele vai deletar.
    try:
        datavazio = (os.stat(datafilter).st_size)/1024
        if ds1.GetLayer(datanome) and datavazio<1:
            ds1.DeleteLayer(datanome)
        else:
            print("O arquivo está correto")
            return
    except:
        print("Não tem arquivo")
        return
    

#Modelo de parâmetro
#datanome = 'Deter_2020_09_28'
#deleta_vazio(datanome)


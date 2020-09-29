# coding: utf-8
#Importando bibliotecas
import sys
import os
from osgeo import ogr
#Biblioteca que realiza operações com datas
from datetime import date
import datetime
import chardet

#os.environ['PROJ_LIB'] = os.path.dirname(sys.argv[0])

def filter_data(data,datanome):
    #importando data
    #Leitura da biblioteca
    os.environ['PROJ_LIB'] = os.path.dirname(sys.argv[0])  

    #criando diretório
    dir_name = os.path.dirname(os.path.realpath(__file__))
    #Abrindo shapefile
    ds = ogr.Open(dir_name,1)
    if ds is None:
        sys.exit("Não pode carregar o shp")
    
    shape = ds.GetLayer('deter_amz')
    #count = shape.GetFeatureCount()
    
    #Formato do dado
    #data='2020/09/12'
    #datanome = "Deter_2020_07_12"

    #datafilter = str(dir_name+'/'+datanome+'.shp')

    if ds.GetLayer(datanome): 
        #ds.DeleteLayer(data)
        #print(datanome)
        print("Não entrou, já existe!")
        #print(datafilter)
        return
    else:  
        #Criando layer de saída
        print("Vai criar o arquivo")
        #Criando a layers e construindo do shapefile
        out_lyr=ds.CreateLayer(datanome,shape.GetSpatialRef(),ogr.wkbPolygon)
        #Dandando permissão aos arquivos geradods
        permissao = 755
        os.chmod(out_lyr,permissao)
        #Construindo as colunas
        out_lyr.CreateFields(shape.schema)

        out_defn=shape.GetLayerDefn()
        out_feat=ogr.Feature(out_defn)
        
        
        for feat in shape:
            if feat.GetField('date') == data:
                geom = feat.geometry()
                out_feat.SetGeometry(geom)
                
                for i in range(feat.GetFieldCount()):
                    value = feat.GetField(i)
                    #print(value)
                    #print(type(value))
                    #print(i)
                    try:
                        out_feat.SetField(i,value)
                        
                    except:
                        if type(value) is str:
                            out_feat.SetField(i,str(value.encode('ascii','ignore')))
                            #print(chardet.detect(feat.GetFieldAsString(i)))
                            #print(str(value.encode('ISO-8859-1','ignore').decode()))
                            #print(type(value.encode('ascii','ignore')))
                        else:
                            out_feat.SetField(i,'null')

                out_lyr.CreateFeature(out_feat) 
        del ds 


#Testes
#data='2020/09/31'
#datanome = "Deter_2020_09_31"
#filter_data(data,datanome)


#https://gis.stackexchange.com/questions/246655/how-to-create-line-polygon-shapefiles-from-geojson-using-gdal-in-python
#https://livebook.manning.com/book/geoprocessing-with-python/chapter-3/137
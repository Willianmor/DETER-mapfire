import glob
import os
import re
import zipfile
from zipfile import ZipFile
 
file_types = ('.dbf', '.shx', '.cpg', '.fix' , '.prj', '.qix', '.sbn', '.shp', '.shp.xml')

inpath = os.path.dirname(os.path.realpath(__file__))
#inpath = 'D:/input/'
 
def zip_shapes(inpath, outpath):

    #Fazer um script para armazenar todos os nomes de zips
 
    files = [re.split('|'.join(file_types), f)[0] for f in os.listdir(inpath) if os.path.isfile(os.path.join(inpath, f)) and any(substring in f for substring in list(file_types))]
    files = list(set(files))
    os.chdir(inpath)
    for name in files:
        _file = name
        files_ = [f for name in [glob.glob(name + e) for e in file_types] for f in name]
        zip_path = os.path.join(outpath, _file + '.zip')
        print('vai printar o zippath:',zip_path)
        if os.path.isfile(zip_path):
            print("O Arquivo já existe na pasta")
            continue

        else: 
            zip = zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED)
            [zip.write(x) for x in files_]
            zip.close()
            permissao = 755
            os.chmod(zip_path,permissao)
            print('completed file: {}'.format(_file))
    
    for name in files:
        _file = name
        files_ = [f for name in [glob.glob(name + e) for e in file_types] for f in name]
        zip_path = os.path.join(outpath, _file + '.zip')
        tamanho = os.stat(zip_path).st_size/1024
        #print(tamanho)
        if tamanho< 1:
            os.remove(zip_path)
            continue
        else:
            print("Tá tudo certo!")
            continue
        
 
    print('*****************')
    print('all done')
 
if __name__ == '__main__':

    inpath = os.path.dirname(os.path.realpath(__file__))
    outpath = str(inpath)
 
    zip_shapes(inpath, outpath)

#https://thegeoict.com/blog/2019/08/13/batch-zipping-your-shapefiles-with-python/
#https://desktop.arcgis.com/en/arcmap/latest/analyze/sharing-workflows/h-zip-python-script.htm
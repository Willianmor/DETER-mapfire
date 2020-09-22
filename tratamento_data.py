from datetime import date
import datetime


def create_publish():
    #obtendo informações de mês e ano do dia recorrente
    mes = datetime.datetime.now().strftime('%m')
    ano = datetime.datetime.now().strftime('%Y')
    #Gerando a data padrão de publicação - publish_mo
    data_publish = str(ano+"-"+mes+"-01" )
    return(data_publish)
    #print (data_publish)


def datai():
    #obtendo informações de mês e ano do dia recorrente 
    mes = datetime.datetime.now().strftime('%m')
    ano = datetime.datetime.now().strftime('%Y')

    #Filtrando informações para mês anterior
    today = datetime.date.today()
    first = today.replace(day=1)
    guardando = (first - datetime.timedelta(days=1))
    mes_anterior = guardando.strftime("%m")
    ano_anterior = guardando.strftime("%Y")
    #print("mes anterior: ",mes_anterior)
    #print("ano atual até o mês 12 ou ano anterior ao mês 1: ",ano_anterior)
                                                
    #Criar lista do mes
    datai = []
    
    for i in range(9):
        v = i + 1 
        t = str(str(ano_anterior+"/"+mes_anterior+"/0") + str(v))
        datai.append(t) 

    for i in range(22):
        v = i + 10 
        t = str(str(ano_anterior+"/"+mes_anterior+"/") + str(v))
        datai.append(t)  

    for i in range(9):
        v = i + 1 
        t = str(str(ano+"/"+mes+"/0") + str(v))
        datai.append(t) 

    for i in range(22):
        v = i + 10 
        t = str(str(ano+"/"+mes+"/") + str(v))
        datai.append(t) 
        
    return(datai)

def datanomei():
    #obtendo informações de mês e ano do dia recorrente 
    mes = datetime.datetime.now().strftime('%m')
    ano = datetime.datetime.now().strftime('%Y')
    
    #Filtrando informações para mês anterior
    today = datetime.date.today()
    first = today.replace(day=1)
    guardando = (first - datetime.timedelta(days=1))
    mes_anterior = guardando.strftime("%m")
    ano_anterior = guardando.strftime("%Y")
    #print("mes anterior: ",mes_anterior)
    #print("ano atual até o mês 12 ou ano anterior ao mês 1: ",ano_anterior)
    

    #Criar lista do mes
    datai = [] 

    for i in range(9):
        v = i + 1 
        t = str(str("Deter_"+ano_anterior+"_"+mes_anterior+"_0") + str(v))
        datai.append(t) 

    for i in range(22):
        v = i + 10 
        t = str(str("Deter_"+ano_anterior+"_"+mes_anterior+"_") + str(v))
        datai.append(t) 

    for i in range(9):
        v = i + 1 
        t = str(str("Deter_"+ano+"_"+mes+"_0") + str(v))
        datai.append(t) 

    for i in range(22):
        v = i + 10 
        t = str(str("Deter_"+ano+"_"+mes+"_") + str(v))
        datai.append(t) 
        
    return(datai)







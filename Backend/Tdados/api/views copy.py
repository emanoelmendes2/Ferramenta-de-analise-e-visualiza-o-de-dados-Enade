from django.http.response import JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from django.template import loader
from .serializers import *
from ..models import *
import pandas as pd
import csv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn.multioutput import MultiOutputClassifier

# definir colunas para exibição de seleção no frontend    
# api get passando a coluna para realizar o processamento
# comunicacao com a api



# fazer uma função de catalogação de eventos a partir de uma coluna passada ex: função recebe coluna exercicio_1, a função deve catalogar a quantidade desses dados 
# o retorno da função deve armazenar em um array o dado deve ser do tipo dicionario/obj Json  para apresentação dos dados no front
#  [{a:65}, {b:59}, 80, 81, 56, 55, 40] (respostas), label: 'coluna' }


def PreProcessamento(dados):
    # CO_UF_CURSO
    # dados=dados.drop(['NU_ANO','CO_CATEGAD','CO_UF_CURSO','CO_REGIAO_CURSO','TP_INSCRICAO_ADM','TP_INSCRICAO','NU_ITEM_OFG','NU_ITEM_OFG_Z','NU_ITEM_OFG_X','NU_ITEM_OFG_N','NU_ITEM_OCE','NU_ITEM_OCE_Z','NU_ITEM_OCE_X','NU_ITEM_OCE_N','DS_VT_GAB_OFG_ORIG','DS_VT_GAB_OFG_FIN','DS_VT_GAB_OCE_ORIG','DS_VT_GAB_OCE_FIN','DS_VT_ESC_OFG','DS_VT_ACE_OFG','DS_VT_ESC_OCE','DS_VT_ACE_OCE','TP_PR_OB_FG','TP_PR_DI_FG','TP_PR_OB_CE','TP_PR_DI_CE','TP_SFG_D1','TP_SFG_D2','TP_SCE_D2','TP_SCE_D3','NT_GER','NT_FG','NT_OBJ_FG','NT_DIS_FG','NT_FG_D1','NT_FG_D1_PT','NT_FG_D1_CT','NT_FG_D2','NT_FG_D2_PT','NT_FG_D2_CT','NT_CE','NT_OBJ_CE','NT_DIS_CE','NT_CE_D1','NT_CE_D2','NT_CE_D3','CO_RS_I1','CO_RS_I2','CO_RS_I3','CO_RS_I4', 'CO_RS_I5','CO_RS_I6',    'CO_RS_I7','CO_RS_I8','CO_RS_I9','QE_I03','QE_I06','QE_I10','QE_I14','QE_I18','QE_I19','QE_I20','QE_I24','QE_I25','QE_I26','QE_I69','QE_I70','QE_I71','QE_I72','QE_I73','QE_I74','QE_I75','QE_I76','QE_I77','QE_I78','QE_I79','QE_I80','QE_I81'], axis=1) # excluir as colunas que não serão utilizadas no modelo

    dados.fillna("",  inplace=True) #Os campos nulos estão sendo substituidos por strig vazia  
    
    #dados.drop(['NU_ANO','CO_CATEGAD','CO_REGIAO_CURSO','TP_INSCRICAO_ADM','TP_INSCRICAO','NU_ITEM_OFG','NU_ITEM_OFG_Z','NU_ITEM_OFG_X','NU_ITEM_OFG_N','NU_ITEM_OCE','NU_ITEM_OCE_Z','NU_ITEM_OCE_X','NU_ITEM_OCE_N','DS_VT_GAB_OFG_ORIG','DS_VT_GAB_OFG_FIN','DS_VT_GAB_OCE_ORIG','DS_VT_GAB_OCE_FIN','DS_VT_ESC_OFG','DS_VT_ACE_OFG','DS_VT_ESC_OCE','DS_VT_ACE_OCE','TP_PR_OB_FG','TP_PR_DI_FG','TP_PR_OB_CE','TP_PR_DI_CE','TP_SFG_D1','TP_SFG_D2','TP_SCE_D2','TP_SCE_D3','NT_GER','NT_FG','NT_OBJ_FG','NT_DIS_FG','NT_FG_D1','NT_FG_D1_PT','NT_FG_D1_CT','NT_FG_D2','NT_FG_D2_PT','NT_FG_D2_CT','NT_CE','NT_OBJ_CE','NT_DIS_CE','NT_CE_D1','NT_CE_D2','NT_CE_D3','CO_RS_I1','CO_RS_I2','CO_RS_I3','CO_RS_I4','CO_RS_I7','CO_RS_I8','CO_RS_I9','QE_I03','QE_I06','QE_I10','QE_I14','QE_I18','QE_I19','QE_I20','QE_I24','QE_I25','QE_I26','QE_I69','QE_I70','QE_I71','QE_I72','QE_I73','QE_I74','QE_I75','QE_I76','QE_I77','QE_I78','QE_I79','QE_I80','QE_I81'], axis=1) # excluir as colunas que não serão utilizadas no modelo
    #non_numerical = ['TP_SEXO','QE_I01','QE_I02','QE_I04','QE_I05','QE_I07','QE_I08','QE_I09','QE_I11','QE_I12','QE_I13','QE_I15','QE_I17','QE_I21','QE_I22','QE_I23']
    #dados 
    # 'CO_IES','CO_ORGACAD','CO_GRUPO','CO_CURSO','CO_MODALIDADE','CO_MUNIC_CURSO','NU_IDADE','TP_SEXO','ANO_FIM_EM','ANO_IN_GRAD','CO_TURNO_GRADUACAO','TP_PRES','QE_I01','QE_I02','QE_I04','QE_I05','QE_I07','QE_I08','QE_I09','QE_I11','QE_I12','QE_I13','QE_I15','QE_I16','QE_I17','QE_I21','QE_I22','QE_I23','QE_I27','QE_I28','QE_I29','QE_I30','QE_I31','QE_I32','QE_I33','QE_I34','QE_I35','QE_I36','QE_I37','QE_I38','QE_I39','QE_I40','QE_I41','QE_I42','QE_I43','QE_I44','QE_I45','QE_I46','QE_I47','QE_I48','QE_I49','QE_I50','QE_I51','QE_I52','QE_I53','QE_I54','QE_I55','QE_I56','QE_I57','QE_I58','QE_I59','QE_I60','QE_I61','QE_I62','QE_I63','QE_I64','QE_I65','QE_I66','QE_I67','QE_I68'
    
    # id - Estado 

    non_numerical = ['TP_SEXO','QE_I01','QE_I02','QE_I04','QE_I05','QE_I07','QE_I08','QE_I09','QE_I11','QE_I12','QE_I13','QE_I15','QE_I17','QE_I21','QE_I22','QE_I23']
    le = preprocessing.LabelEncoder()
    for x in non_numerical:
        le.fit(dados[x])
        # converte string em numero
        dados[x] = le.transform(dados[x].astype(str))

    Dados=dados.replace([""],0)
    Dados=Dados.astype(int)
    return Dados
    


def tratamento(dados):
    Dados=dados.rename(columns={'CO_IES':'Codigo_instituicao','CO_ORGACAD':'org_academica','CO_GRUPO':'area_curso','CO_CURSO':'Codigo_curso','CO_MODALIDADE':'Modalidade_Ensino','CO_MUNIC_CURSO':'municipio_curso','NU_IDADE':'Idade','TP_SEXO':'Sexo','ANO_FIM_EM':'Ano_Final_EM','ANO_IN_GRAD':'Inicio_Grad.','CO_TURNO_GRADUACAO':'Turno_Grad.','TP_PRES':'Presenca_Enade','QE_I01':'Questao_01','QE_I02':'Questao_02','QE_I04':'Questao_04','QE_I05':'Questao_05','QE_I07':'Questao_07','QE_I08':'Questao_08','QE_I09':'Questao_09','QE_I11':'Questao_11','QE_I12':'Questao_12','QE_I13':'Questao_13','QE_I15':'Questao_15','QE_I16':'Questao_16','QE_I17':'Questao_17','QE_I21':'Questao_21','QE_I22':'Questao_22','QE_I23':'Questao_23','QE_I27':'Questao_27','QE_I28':'Questao_28','QE_I29':'Questao_29','QE_I30':'Questao_30','QE_I31':'Questao_31','QE_I32':'Questao_32','QE_I33':'Questao_33','QE_I34':'Questao_34','QE_I35':'Questao_35','QE_I36':'Questao_36','QE_I37':'Questao_37','QE_I38':'Questao_38','QE_I39':'Questao_39','QE_I40':'Questao_40','QE_I41':'Questao_41','QE_I42':'Questao_42','QE_I43':'Questao_43','QE_I44':'Questao_44','QE_I45':'Questao_45','QE_I46':'Questao_46','QE_I47':'Questao_47','QE_I48':'Questao_48','QE_I49':'Questao_49','QE_I50':'Questao_50','QE_I51':'Questao_51','QE_I52':'Questao_52','QE_I53':'Questao_53','QE_I54':'Questao_54','QE_I55':'Questao_55','QE_I56':'Questao_56','QE_I57':'Questao_57','QE_I58':'Questao_58','QE_I59':'Questao_59','QE_I60':'Questao_60','QE_I61':'Questao_61','QE_I62':'Questao_62','QE_I63':'Questao_63','QE_I64':'Questao_64','QE_I65':'Questao_65','QE_I66':'Questao_66','QE_I67':'Questao_67','QE_I68':'Questao_68'})
    
    return Dados

    #f = open('testes1.csv', 'w', newline='')
    #Dados.to_csv(f, encoding='utf-8', index=False)   

def mineracao(dados):
    
    for i in dados.columns:
        # criar uma matriz X e o vetor y
        x = np.array(dados.iloc[:, 0:12]) 	
        y = np.array(dados[i])    


    # criação de intervalo de números ímpares de K para KNN
    neighbors = list(range(1,100,2))

    # criação de intervalo de f para k-fold
    cv_list = list(range(10,40))


    # criação da estrutura de listas para armazenar valores
    k_list = []
    fold_list = []
    cv_scores = []
    

    # executar KNN e k-fold cross validation
    for k in neighbors:
        for f in cv_list:
            knn = KNeighborsClassifier(n_neighbors=k)
            scores = cross_val_score(knn, x, y, cv=f, scoring='accuracy')
            cv_scores.append(scores.mean())  #popular listas
            k_list.append(k)                 
            fold_list.append(f)
    
    # calcular o erro 
    MSE = [1 - x for x in cv_scores]
   
    

    # contrução do dataframe
    df_1 = pd.DataFrame (k_list, columns=['k_list'])
    df_2 = pd.DataFrame (fold_list, columns=['fold_list'])
    df_3 = pd.DataFrame (MSE, columns=['MSE'])
    df_knn = pd.concat([df_1, df_2, df_3], axis=1)

    # retorna o menor erro obtido
    optimal_k = min(df_knn['MSE'])

    # retorna os valores de k e f do menor erro obtido
    index_opt = df_knn[df_knn['MSE'] == optimal_k].index.item()
    

    print(df_knn[df_knn['MSE'] == optimal_k].index)


    # printar os resultados
    print ("O número ótimo de vizinhos k é %d" % df_knn.loc[index_opt, 'k_list'] )
    print ("O número ideal de dobras f é %d" % df_knn.loc[index_opt, 'fold_list'] )
    print ("Erro de classificação incorreta é %f" % optimal_k )

  
 
class Dados_adicionar(APIView):
    
    permission_classes = [permissions.AllowAny, ]
    def get(self, request, format=None):
        dados = Dados.objects.all()
  
        serializer = DadosSerializer(dados, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # estado = Estado.objects.get(estado=request.data["estado"])

        
        enade = Enade()
        enade.ano = request.data["ano"]
        enade.save()
        arq = request.data["arquivo"]

        dados = pd.read_csv(arq, encoding = "UTF-8-sig", sep=";")

        dados=dados.loc[dados['CO_UF_CURSO'] == (estado.id)]

        dados = PreProcessamento(dados)
        dados = tratamento(dados)
        # dados1 = mineracao(dados)
         
        objetos = []
        for i in range(dados.shape[0]):
            obj_dados = Dados()
            print(dados.loc[i, 'Codigo_instituicao'])
            obj_dados.codigoInstituicao  'Codigo_instituicao']
            obj_dados.orgAcademica  'org_academica']
            obj_dados.areaCurso  'area_curso']
            obj_dados.codigoCurso  'Codigo_curso']
            obj_dados.modalidadeEnsino  'Modalidade_Ensino']
            obj_dados.municipioCurso  'municipio_curso']
            obj_dados.idade  'Idade']
            obj_dados.sexo  'Sexo']
            obj_dados.anoFinalEM  'Ano_Final_EM']
            obj_dados.iniciograd  'Inicio_Grad.']
            obj_dados.turnoGrad  'Turno_Grad.']
            obj_dados.presencaenade  'Presenca_Enade']
            obj_dados.questao01  'Questao_01']
            obj_dados.questao02  'Questao_02']
            obj_dados.questao04  'Questao_04']
            obj_dados.questao05  'Questao_05']
            obj_dados.questao07  'Questao_07']
            obj_dados.questao08  'Questao_08']
            obj_dados.questao09  'Questao_09']
            obj_dados.questao11  'Questao_11']
            obj_dados.questao12  'Questao_12']
            obj_dados.questao13  'Questao_13']
            obj_dados.questao15  'Questao_15']
            obj_dados.questao16  'Questao_16']
            obj_dados.questao17  'Questao_17']
            obj_dados.questao21  'Questao_21']
            obj_dados.questao22  'Questao_22']
            obj_dados.questao23  'Questao_23']
            obj_dados.questao27  'Questao_27']
            obj_dados.questao28  'Questao_28']
            obj_dados.questao29  'Questao_29']
            obj_dados.questao30  'Questao_30']
            obj_dados.questao31  'Questao_31']
            obj_dados.questao32  'Questao_32']
            obj_dados.questao33  'Questao_33']
            obj_dados.questao34  'Questao_34']
            obj_dados.questao35  'Questao_35']
            obj_dados.questao36  'Questao_36']
            obj_dados.questao37  'Questao_37']
            obj_dados.questao38  'Questao_38']
            obj_dados.questao39  'Questao_39']
            obj_dados.questao40  'Questao_40']
            obj_dados.questao41  'Questao_41']
            obj_dados.questao42  'Questao_42']
            obj_dados.questao43  'Questao_43']
            obj_dados.questao44  'Questao_44']
            obj_dados.questao45  'Questao_45']
            obj_dados.questao46  'Questao_46']
            obj_dados.questao47  'Questao_47']
            obj_dados.questao48  'Questao_48']
            obj_dados.questao49  'Questao_49']
            obj_dados.questao50  'Questao_50']
            obj_dados.questao51  'Questao_51']
            obj_dados.questao52  'Questao_52']
            obj_dados.questao53  'Questao_53']
            obj_dados.questao54  'Questao_54']
            obj_dados.questao55  'Questao_55']
            obj_dados.questao56  'Questao_56']
            obj_dados.questao57  'Questao_57']
            obj_dados.questao58  'Questao_58']
            obj_dados.questao59  'Questao_59']
            obj_dados.questao60  'Questao_60']
            obj_dados.questao61  'Questao_61']
            obj_dados.questao62  'Questao_62']
            obj_dados.questao63  'Questao_63']
            obj_dados.questao64  'Questao_64']
            obj_dados.questao65  'Questao_65']
            obj_dados.questao66  'Questao_66']
            obj_dados.questao67  'Questao_67']
            obj_dados.questao68  'Questao_68']
            obj_dados.enade = enade
            # obj_dados.estado = estado
            objetos.append(obj_dados)
        Dados.objects.bulk_create(objetos) #bulk_create insere obj contidos em um array no banco de dados
        
        dados = Dados.objects.filter(enade=enade)
        serializer = DadosSerializer(dados, many=True).data
        
        if serializer:
            return Response(serializer, status=201)
        return Response({"erro":""}, status=400)


class ano_get(APIView):
    
    permission_classes = [permissions.AllowAny, ]
    def get(self, request, format=None):
        enade = Enade.objects.all().values('ano')
        return  Response(enade, status=200)

class processar_api(APIView):
    
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, format=None):
        enade = Enade.objects.get(ano=request.data["ano"])
        if(enade):
            dados = Dados.objects.filter(enade=enade)
            colums = request.data["colums"]

            colum_converter = {
            'Codigo_instituicao': codigoInstituicao ,
            'org_academica': orgAcademica ,
            'area_curso': areaCurso ,
            'Codigo_curso': codigoCurso ,
            'Modalidade_Ensino': modalidadeEnsino ,
            'municipio_curso': municipioCurso ,
            'Idade': idade ,
            'Sexo': sexo ,
            'Ano_Final_EM': anoFinalEM ,
            'Inicio_Grad.': iniciograd,
            'Turno_Grad.': turnoGrad,
            'Presenca_Enade': presencaenad,
            'Questao_01':questao01,
            'Questao_02':questao02,
            'Questao_04':questao04,
            'Questao_05':questao05,
            'Questao_07':questao07,
            'Questao_08':questao08,
            'Questao_09':questao09,
            'Questao_11':questao11,
            'Questao_12':questao12,
            'Questao_13':questao13,
            'Questao_15':questao15,
            'Questao_16':questao16,
            'Questao_17':questao17,
            'Questao_21':questao21,
            'Questao_22':questao22,
            'Questao_23':questao23,
            'Questao_27':questao27,
            'Questao_28':questao28,
            'Questao_29':questao29,
            'Questao_30':questao30,
            'Questao_31':questao31,
            'Questao_32':questao32,
            'Questao_33':questao33,
            'Questao_34':questao34,
            'Questao_35':questao35,
            'Questao_36':questao36,
            'Questao_37':questao37,
            'Questao_38':questao38,
            'Questao_39':questao39,
            'Questao_40':questao40,
            'Questao_41':questao41,
            'Questao_42':questao42,
            'Questao_43':questao43,
            'Questao_44':questao44,
            'Questao_45':questao45,
            'Questao_46':questao46,
            'Questao_47':questao47,
            'Questao_48':questao48,
            'Questao_49':questao49,
            'Questao_50':questao50,
            'Questao_51':questao51,
            'Questao_52':questao52,
            'Questao_53':questao53,
            'Questao_54':questao54,
            'Questao_55':questao55,
            'Questao_56':questao56,
            'Questao_57':questao57,
            'Questao_58':questao58,
            'Questao_59':questao59,
            'Questao_60':questao60,
            'Questao_61':questao61,
            'Questao_62':questao62,
            'Questao_63':questao63,
            'Questao_64':questao64,
            'Questao_65':questao65,
            'Questao_66':questao66,
            'Questao_67':questao67,
            'Questao_68':questao68}

            teste_colum = []
            for colum in request.data["colums"]:
                for line in dados:
                    teste_colum.append(line.colum_converter[colum])

            
            print(teste_colum)
        return  Response({'deucerto':teste_colum}, status=200)
        # estado = Estado.objects.get(estado=request.data["estado"])
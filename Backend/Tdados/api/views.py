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
from django.core import serializers

    
    
def PreProcessamento(dados):

    # 'CO_IES','CO_ORGACAD','CO_GRUPO','CO_CURSO','CO_MODALIDADE','CO_MUNIC_CURSO','NU_IDADE','TP_SEXO','ANO_FIM_EM','ANO_IN_GRAD','CO_TURNO_GRADUACAO','TP_PRES','QE_I01','QE_I02','QE_I04','QE_I05','QE_I07','QE_I08','QE_I09','QE_I11','QE_I12','QE_I13','QE_I15','QE_I16','QE_I17','QE_I21','QE_I22','QE_I23','QE_I27','QE_I28','QE_I29','QE_I30','QE_I31','QE_I32','QE_I33','QE_I34','QE_I35','QE_I36','QE_I37','QE_I38','QE_I39','QE_I40','QE_I41','QE_I42','QE_I43','QE_I44','QE_I45','QE_I46','QE_I47','QE_I48','QE_I49','QE_I50','QE_I51','QE_I52','QE_I53','QE_I54','QE_I55','QE_I56','QE_I57','QE_I58','QE_I59','QE_I60','QE_I61','QE_I62','QE_I63','QE_I64','QE_I65','QE_I66','QE_I67','QE_I68'

    # Inserção dos dados por estado/ etapa de exclusão dos dados não necessarios
    # dados=dados.drop(['NU_ANO','CO_CATEGAD','CO_UF_CURSO','CO_REGIAO_CURSO','TP_INSCRICAO_ADM','TP_INSCRICAO','NU_ITEM_OFG','NU_ITEM_OFG_Z','NU_ITEM_OFG_X','NU_ITEM_OFG_N','NU_ITEM_OCE','NU_ITEM_OCE_Z','NU_ITEM_OCE_X','NU_ITEM_OCE_N','DS_VT_GAB_OFG_ORIG','DS_VT_GAB_OFG_FIN','DS_VT_GAB_OCE_ORIG','DS_VT_GAB_OCE_FIN','DS_VT_ESC_OFG','DS_VT_ACE_OFG','DS_VT_ESC_OCE','DS_VT_ACE_OCE','TP_PR_GER','TP_PR_OB_FG','TP_PR_DI_FG','TP_PR_OB_CE','TP_PR_DI_CE','TP_SFG_D1','TP_SFG_D2','TP_SCE_D1','TP_SCE_D2','TP_SCE_D3','NT_GER','NT_FG','NT_OBJ_FG','NT_DIS_FG','NT_FG_D1','NT_FG_D1_PT','NT_FG_D1_CT','NT_FG_D2','NT_FG_D2_PT','NT_FG_D2_CT','NT_CE','NT_OBJ_CE','NT_DIS_CE','NT_CE_D1','NT_CE_D2','NT_CE_D3','CO_RS_I1','CO_RS_I2','CO_RS_I3','CO_RS_I4', 'CO_RS_I5','CO_RS_I6', 'CO_RS_I7','CO_RS_I8','CO_RS_I9','QE_I03','QE_I06','QE_I10','QE_I14','QE_I18','QE_I19','QE_I20','QE_I24','QE_I25','QE_I26','QE_I69','QE_I70','QE_I71','QE_I72','QE_I73','QE_I74','QE_I75','QE_I76','QE_I77','QE_I78','QE_I79','QE_I80','QE_I81'], axis=1) # excluir as colunas que não serão utilizadas no modelo

    # Colunas selecionadas para utilização deste trabalho
    # 'CO_IES','CO_ORGACAD','CO_GRUPO','CO_CURSO','CO_MODALIDADE','CO_MUNIC_CURSO','NU_IDADE','TP_SEXO','ANO_FIM_EM','ANO_IN_GRAD','CO_TURNO_GRADUACAO','TP_PRES','QE_I01','QE_I02','QE_I04','QE_I05','QE_I07','QE_I08','QE_I09','QE_I11','QE_I12','QE_I13','QE_I15','QE_I16','QE_I17','QE_I21','QE_I22','QE_I23','QE_I27','QE_I28','QE_I29','QE_I30','QE_I31','QE_I32','QE_I33','QE_I34','QE_I35','QE_I36','QE_I37','QE_I38','QE_I39','QE_I40','QE_I41','QE_I42','QE_I43','QE_I44','QE_I45','QE_I46','QE_I47','QE_I48','QE_I49','QE_I50','QE_I51','QE_I52','QE_I53','QE_I54','QE_I55','QE_I56','QE_I57','QE_I58','QE_I59','QE_I60','QE_I61','QE_I62','QE_I63','QE_I64','QE_I65','QE_I66','QE_I67','QE_I68'

    dados.fillna("",  inplace=True) #Os campos nulos estão sendo substituidos por strig vazia

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

def mineracao(dados):
    
    for i in dados.columns:
        # criar uma matriz X e o vetor y
        x = np.array(dados.iloc[:, 0:12]) 	
        y = np.array(dados[i])

    #listas para armazenar valores
    k_list = []
    fold_list = []
    cv_scores = []

    #intervalo de números ímpares de K para KNN
    neighbors = list(range(1,100,2))

    #intervalo de f para k-fold
    cv_list = list(range(10,40))

    # executar KNN e k-fold cross validation
    for k in neighbors:
        for f in cv_list:
            knn = KNeighborsClassifier(n_neighbors=k)
            scores = cross_val_score(knn, x, y, cv=f, scoring='accuracy')
            cv_scores.append(scores.mean())  #popular listas
            k_list.append(k)                 
            fold_list.append(f)

    MSE = [1 - x for x in cv_scores]
   
    df_1 = pd.DataFrame (k_list, columns=['k_list'])
    df_2 = pd.DataFrame (fold_list, columns=['fold_list'])
    df_3 = pd.DataFrame (MSE, columns=['MSE'])
    df_knn = pd.concat([df_1, df_2, df_3], axis=1)

    optimal_k = min(df_knn['MSE'])
    index_opt = df_knn[df_knn['MSE'] == optimal_k].index.item()

    # resultados
    print("Erro de classificação incorreta é %f" % optimal_k)
    print ("O número ótimo de k vizinhos é %d" % df_knn.loc[index_opt, 'k_list'] )
    print ("O número ideal de dobras f é %d" % df_knn.loc[index_opt, 'fold_list'] )
    return {'kVizinhos':df_knn.loc[index_opt, 'k_list'], 'dobrasF':df_knn.loc[index_opt, 'fold_list'], 'erro':optimal_k}
    

class Dados_adicionar(APIView):
    
    permission_classes = [permissions.AllowAny, ]
    def get(self, request, format=None):
        dados = Dados.objects.all()
  
        serializer = DadosSerializer(dados, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Inserção dos dados por estado
        # estado = Estado.objects.get(estado=request.data["estado"])

        enade = Enade()
        enade.ano = request.data["ano"]
        arq = request.data["arquivo"]
        dados = pd.read_csv(arq, encoding = "UTF-8-sig", sep=";")

        # Inserção dos dados por estado
        # dados=dados.loc[dados['CO_UF_CURSO'] == (estado.id)]


        dados = PreProcessamento(dados)
        dados = tratamento(dados)
        dados1 = mineracao(dados)
        resultado = Resultado()
        resultado.kVizinhos = dados1['kVizinhos']
        resultado.dobrasF = dados1['dobrasF']
        resultado.erro = dados1['erro']
        resultado.save()
        enade.resultado = resultado
        enade.save()

        objetos = []
        for i in range(dados.shape[0]):
            obj_dados = Dados()
            obj_dados.codigoInstituicao = dados.loc[i, 'Codigo_instituicao']
            obj_dados.orgAcademica = dados.loc[i, 'org_academica']
            obj_dados.areaCurso = dados.loc[i, 'area_curso']
            obj_dados.codigoCurso = dados.loc[i, 'Codigo_curso']
            obj_dados.modalidadeEnsino = dados.loc[i, 'Modalidade_Ensino']
            obj_dados.municipioCurso = dados.loc[i, 'municipio_curso']
            obj_dados.idade = dados.loc[i, 'Idade']
            obj_dados.sexo = dados.loc[i, 'Sexo']
            obj_dados.anoFinalEM = dados.loc[i, 'Ano_Final_EM']
            obj_dados.iniciograd = dados.loc[i, 'Inicio_Grad.']
            obj_dados.turnoGrad = dados.loc[i, 'Turno_Grad.']
            obj_dados.presencaenade = dados.loc[i, 'Presenca_Enade']
            obj_dados.questao01 = dados.loc[i, 'Questao_01']
            obj_dados.questao02 = dados.loc[i, 'Questao_02']
            obj_dados.questao04 = dados.loc[i, 'Questao_04']
            obj_dados.questao05 = dados.loc[i, 'Questao_05']
            obj_dados.questao07 = dados.loc[i, 'Questao_07']
            obj_dados.questao08 = dados.loc[i, 'Questao_08']
            obj_dados.questao09 = dados.loc[i, 'Questao_09']
            obj_dados.questao11 = dados.loc[i, 'Questao_11']
            obj_dados.questao12 = dados.loc[i, 'Questao_12']
            obj_dados.questao13 = dados.loc[i, 'Questao_13']
            obj_dados.questao15 = dados.loc[i, 'Questao_15']
            obj_dados.questao16 = dados.loc[i, 'Questao_16']
            obj_dados.questao17 = dados.loc[i, 'Questao_17']
            obj_dados.questao21 = dados.loc[i, 'Questao_21']
            obj_dados.questao22 = dados.loc[i, 'Questao_22']
            obj_dados.questao23 = dados.loc[i, 'Questao_23']
            obj_dados.questao27 = dados.loc[i, 'Questao_27']
            obj_dados.questao28 = dados.loc[i, 'Questao_28']
            obj_dados.questao29 = dados.loc[i, 'Questao_29']
            obj_dados.questao30 = dados.loc[i, 'Questao_30']
            obj_dados.questao31 = dados.loc[i, 'Questao_31']
            obj_dados.questao32 = dados.loc[i, 'Questao_32']
            obj_dados.questao33 = dados.loc[i, 'Questao_33']
            obj_dados.questao34 = dados.loc[i, 'Questao_34']
            obj_dados.questao35 = dados.loc[i, 'Questao_35']
            obj_dados.questao36 = dados.loc[i, 'Questao_36']
            obj_dados.questao37 = dados.loc[i, 'Questao_37']
            obj_dados.questao38 = dados.loc[i, 'Questao_38']
            obj_dados.questao39 = dados.loc[i, 'Questao_39']
            obj_dados.questao40 = dados.loc[i, 'Questao_40']
            obj_dados.questao41 = dados.loc[i, 'Questao_41']
            obj_dados.questao42 = dados.loc[i, 'Questao_42']
            obj_dados.questao43 = dados.loc[i, 'Questao_43']
            obj_dados.questao44 = dados.loc[i, 'Questao_44']
            obj_dados.questao45 = dados.loc[i, 'Questao_45']
            obj_dados.questao46 = dados.loc[i, 'Questao_46']
            obj_dados.questao47 = dados.loc[i, 'Questao_47']
            obj_dados.questao48 = dados.loc[i, 'Questao_48']
            obj_dados.questao49 = dados.loc[i, 'Questao_49']
            obj_dados.questao50 = dados.loc[i, 'Questao_50']
            obj_dados.questao51 = dados.loc[i, 'Questao_51']
            obj_dados.questao52 = dados.loc[i, 'Questao_52']
            obj_dados.questao53 = dados.loc[i, 'Questao_53']
            obj_dados.questao54 = dados.loc[i, 'Questao_54']
            obj_dados.questao55 = dados.loc[i, 'Questao_55']
            obj_dados.questao56 = dados.loc[i, 'Questao_56']
            obj_dados.questao57 = dados.loc[i, 'Questao_57']
            obj_dados.questao58 = dados.loc[i, 'Questao_58']
            obj_dados.questao59 = dados.loc[i, 'Questao_59']
            obj_dados.questao60 = dados.loc[i, 'Questao_60']
            obj_dados.questao61 = dados.loc[i, 'Questao_61']
            obj_dados.questao62 = dados.loc[i, 'Questao_62']
            obj_dados.questao63 = dados.loc[i, 'Questao_63']
            obj_dados.questao64 = dados.loc[i, 'Questao_64']
            obj_dados.questao65 = dados.loc[i, 'Questao_65']
            obj_dados.questao66 = dados.loc[i, 'Questao_66']
            obj_dados.questao67 = dados.loc[i, 'Questao_67']
            obj_dados.questao68 = dados.loc[i, 'Questao_68']
            obj_dados.enade = enade
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

        return Response(enade, status=200)

class get_knn(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, format=None):

        enade = Enade.objects.get(ano = request.data['ano'])

        return Response({"kVizinhos":enade.resultado.kVizinhos, "dobrasF":enade.resultado.dobrasF, "erro":enade.resultado.erro}, status=200)

class processar_api(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, format=None):
        enade = Enade.objects.get(ano=request.data["ano"])
        if(enade):
            dados = Dados.objects.filter(enade=enade)

            data_values = {}
            for colum in request.data["colums"]:
                for line in dados:
                    if colum not in data_values:
                        data_values[colum] = {}

                    if colum == 'Codigo_instituicao':
                        if line.codigoInstituicao not in data_values[colum]:
                            data_values[colum][line.codigoInstituicao] = 1
                        else:
                            data_values[colum][line.codigoInstituicao] += 1

                    if colum == 'org_academica':
                        if line.orgAcademica not in data_values[colum]:
                            data_values[colum][line.orgAcademica] = 1
                        else:
                            data_values[colum][line.orgAcademica] += 1

                    if colum == 'area_curso':
                        if line.areaCurso not in data_values[colum]:
                            data_values[colum][line.areaCurso] = 1
                        else:
                            data_values[colum][line.areaCurso] += 1

                    if colum == 'Codigo_curso':
                        if line.codigoCurso not in data_values[colum]:
                            data_values[colum][line.codigoCurso] = 1
                        else:
                            data_values[colum][line.codigoCurso] += 1

                    if colum == 'Modalidade_Ensino':
                        if line.modalidadeEnsino not in data_values[colum]:
                            data_values[colum][line.modalidadeEnsino] = 1
                        else:
                            data_values[colum][line.modalidadeEnsino] += 1

                    if colum == 'municipio_curso':
                        if line.municipioCurso not in data_values[colum]:
                            data_values[colum][line.municipioCurso] = 1
                        else:
                            data_values[colum][line.municipioCurso] += 1

                    if colum == 'Idade':
                        if line.idade not in data_values[colum]:
                            data_values[colum][line.idade] = 1
                        else:
                            data_values[colum][line.idade] += 1

                    if colum == 'Sexo':
                        if line.sexo not in data_values[colum]:
                            data_values[colum][line.sexo] = 1
                        else:
                            data_values[colum][line.sexo] += 1

                    if colum == 'Ano_Final_EM':
                        if line.anoFinalEM not in data_values[colum]:
                            data_values[colum][line.anoFinalEM] = 1
                        else:
                            data_values[colum][line.anoFinalEM] += 1

                    if colum == 'Inicio_Grad.':
                        if line.iniciograd not in data_values[colum]:
                            data_values[colum][line.iniciograd] = 1
                        else:
                            data_values[colum][line.iniciograd] += 1

                    if colum == 'Turno_Grad.':
                        if line.turnoGrad not in data_values[colum]:
                            data_values[colum][line.turnoGrad] = 1
                        else:
                            data_values[colum][line.turnoGrad] += 1

                    if colum == 'Presenca_Enade':
                        if line.presencaenade not in data_values[colum]:
                            data_values[colum][line.presencaenade] = 1
                        else:
                            data_values[colum][line.presencaenade] += 1

                    if colum == 'Questao_01':
                        if line.questao01 not in data_values[colum]:
                            data_values[colum][line.questao01] = 1
                        else:
                            data_values[colum][line.questao01] += 1

                    if colum == 'Questao_02':
                        if line.questao02 not in data_values[colum]:
                            data_values[colum][line.questao02] = 1
                        else:
                            data_values[colum][line.questao02] += 1

                    if colum == 'Questao_04':
                        if line.questao04 not in data_values[colum]:
                            data_values[colum][line.questao04] = 1
                        else:
                            data_values[colum][line.questao04] += 1

                    if colum == 'Questao_07':
                        if line.questao07 not in data_values[colum]:
                            data_values[colum][line.questao07] = 1
                        else:
                            data_values[colum][line.questao07] += 1

                    if colum == 'Questao_08':
                        if line.questao08 not in data_values[colum]:
                            data_values[colum][line.questao08] = 1
                        else:
                            data_values[colum][line.questao08] += 1

                    if colum == 'Questao_09':
                        if line.questao09 not in data_values[colum]:
                            data_values[colum][line.questao09] = 1
                        else:
                            data_values[colum][line.questao09] += 1

                    if colum == 'Questao_11':
                        if line.questao11 not in data_values[colum]:
                            data_values[colum][line.questao11] = 1
                        else:
                            data_values[colum][line.questao11] += 1

                    if colum == 'Questao_12':
                        if line.questao12 not in data_values[colum]:
                            data_values[colum][line.questao12] = 1
                        else:
                            data_values[colum][line.questao12] += 1

                    if colum == 'Questao_13':
                        if line.questao13 not in data_values[colum]:
                            data_values[colum][line.questao13] = 1
                        else:
                            data_values[colum][line.questao13] += 1

                    if colum == 'Questao_15':
                        if line.questao15 not in data_values[colum]:
                            data_values[colum][line.questao15] = 1
                        else:
                            data_values[colum][line.questao15] += 1

                    if colum == 'Questao_16':
                        if line.questao16 not in data_values[colum]:
                            data_values[colum][line.questao16] = 1
                        else:
                            data_values[colum][line.questao16] += 1

                    if colum == 'Questao_17':
                        if line.questao17 not in data_values[colum]:
                            data_values[colum][line.questao17] = 1
                        else:
                            data_values[colum][line.questao0118] += 1

                    if colum == 'Questao_21':
                        if line.questao21 not in data_values[colum]:
                            data_values[colum][line.questao21] = 1
                        else:
                            data_values[colum][line.questao21] += 1

                    if colum == 'Questao_22':
                        if line.questao22 not in data_values[colum]:
                            data_values[colum][line.questao22] = 1
                        else:
                            data_values[colum][line.questao22] += 1

                    if colum == 'Questao_23':
                        if line.questao23 not in data_values[colum]:
                            data_values[colum][line.questao23] = 1
                        else:
                            data_values[colum][line.questao23] += 1

                    if colum == 'Questao_27':
                        if line.questao27 not in data_values[colum]:
                            data_values[colum][line.questao27] = 1
                        else:
                            data_values[colum][line.questao27] += 1

                    if colum == 'Questao_28':
                        if line.questao28 not in data_values[colum]:
                            data_values[colum][line.questao28] = 1
                        else:
                            data_values[colum][line.questao28] += 1

                    if colum == 'Questao_29':
                        if line.questao29 not in data_values[colum]:
                            data_values[colum][line.questao29] = 1
                        else:
                            data_values[colum][line.questao29] += 1

                    if colum == 'Questao_30':
                        if line.questao30 not in data_values[colum]:
                            data_values[colum][line.questao30] = 1
                        else:
                            data_values[colum][line.questao30] += 1

                    if colum == 'Questao_31':
                        if line.questao31 not in data_values[colum]:
                            data_values[colum][line.questao31] = 1
                        else:
                            data_values[colum][line.questao31] += 1

                    if colum == 'Questao_32':
                        if line.questao32 not in data_values[colum]:
                            data_values[colum][line.questao32] = 1
                        else:
                            data_values[colum][line.questao32] += 1

                    if colum == 'Questao_33':
                        if line.questao33 not in data_values[colum]:
                            data_values[colum][line.questao33] = 1
                        else:
                            data_values[colum][line.questao33] += 1

                    if colum == 'Questao_34':
                        if line.questao34 not in data_values[colum]:
                            data_values[colum][line.questao34] = 1
                        else:
                            data_values[colum][line.questao34] += 1

                    if colum == 'Questao_35':
                        if line.questao35 not in data_values[colum]:
                            data_values[colum][line.questao35] = 1
                        else:
                            data_values[colum][line.questao35] += 1

                    if colum == 'Questao_36':
                        if line.questao36 not in data_values[colum]:
                            data_values[colum][line.questao36] = 1
                        else:
                            data_values[colum][line.questao36] += 1

                    if colum == 'Questao_37':
                        if line.questao37 not in data_values[colum]:
                            data_values[colum][line.questao37] = 1
                        else:
                            data_values[colum][line.questao37] += 1

                    if colum == 'Questao_38':
                        if line.questao38 not in data_values[colum]:
                            data_values[colum][line.questao38] = 1
                        else:
                            data_values[colum][line.questao38] += 1

                    if colum == 'Questao_39':
                        if line.questao39 not in data_values[colum]:
                            data_values[colum][line.questao39] = 1
                        else:
                            data_values[colum][line.questao39] += 1

                    if colum == 'Questao_40':
                        if line.questao40 not in data_values[colum]:
                            data_values[colum][line.questao40] = 1
                        else:
                            data_values[colum][line.questao40] += 1

                    if colum == 'Questao_41':
                        if line.questao41 not in data_values[colum]:
                            data_values[colum][line.questao41] = 1
                        else:
                            data_values[colum][line.questao41] += 1

                    if colum == 'Questao_42':
                        if line.questao42 not in data_values[colum]:
                            data_values[colum][line.questao42] = 1
                        else:
                            data_values[colum][line.questao42] += 1

                    if colum == 'Questao_43':
                        if line.questao43 not in data_values[colum]:
                            data_values[colum][line.questao43] = 1
                        else:
                            data_values[colum][line.questao43] += 1

                    if colum == 'Questao_44':
                        if line.questao44 not in data_values[colum]:
                            data_values[colum][line.questao44] = 1
                        else:
                            data_values[colum][line.questao44] += 1

                    if colum == 'Questao_45':
                        if line.questao45 not in data_values[colum]:
                            data_values[colum][line.questao45] = 1
                        else:
                            data_values[colum][line.questao45] += 1

                    if colum == 'Questao_46':
                        if line.questao46 not in data_values[colum]:
                            data_values[colum][line.questao46] = 1
                        else:
                            data_values[colum][line.questao46] += 1

                    if colum == 'Questao_47':
                        if line.questao47 not in data_values[colum]:
                            data_values[colum][line.questao47] = 1
                        else:
                            data_values[colum][line.questao47] += 1

                    if colum == 'Questao_48':
                        if line.questao47 not in data_values[colum]:
                            data_values[colum][line.questao47] = 1
                        else:
                            data_values[colum][line.questao47] += 1

                    if colum == 'Questao_49':
                        if line.questao49 not in data_values[colum]:
                            data_values[colum][line.questao49] = 1
                        else:
                            data_values[colum][line.questao49] += 1

                    if colum == 'Questao_50':
                        if line.questao50 not in data_values[colum]:
                            data_values[colum][line.questao50] = 1
                        else:
                            data_values[colum][line.questao50] += 1

                    if colum == 'Questao_51':
                        if line.questao51 not in data_values[colum]:
                            data_values[colum][line.questao51] = 1
                        else:
                            data_values[colum][line.questao51] += 1

                    if colum == 'Questao_52':
                        if line.questao52 not in data_values[colum]:
                            data_values[colum][line.questao52] = 1
                        else:
                            data_values[colum][line.questao52] += 1

                    if colum == 'Questao_53':
                        if line.questao53 not in data_values[colum]:
                            data_values[colum][line.questao53] = 1
                        else:
                            data_values[colum][line.questao53] += 1

                    if colum == 'Questao_54':
                        if line.questao54 not in data_values[colum]:
                            data_values[colum][line.questao54] = 1
                        else:
                            data_values[colum][line.questao54] += 1

                    if colum == 'Questao_55':
                        if line.questao55 not in data_values[colum]:
                            data_values[colum][line.questao55] = 1
                        else:
                            data_values[colum][line.questao55] += 1

                    if colum == 'Questao_56':
                        if line.questao56 not in data_values[colum]:
                            data_values[colum][line.questao56] = 1
                        else:
                            data_values[colum][line.questao56] += 1

                    if colum == 'Questao_57':
                        if line.questao57 not in data_values[colum]:
                            data_values[colum][line.questao57] = 1
                        else:
                            data_values[colum][line.questao57] += 1

                    if colum == 'Questao_58':
                        if line.questao58 not in data_values[colum]:
                            data_values[colum][line.questao58] = 1
                        else:
                            data_values[colum][line.questao58] += 1

                    if colum == 'Questao_59':
                        if line.questao59 not in data_values[colum]:
                            data_values[colum][line.questao59] = 1
                        else:
                            data_values[colum][line.questao59] += 1

                    if colum == 'Questao_60':
                        if line.questao60 not in data_values[colum]:
                            data_values[colum][line.questao60] = 1
                        else:
                            data_values[colum][line.questao60] += 1

                    if colum == 'Questao_61':
                        if line.questao60 not in data_values[colum]:
                            data_values[colum][line.questao60] = 1
                        else:
                            data_values[colum][line.questao60] += 1

                    if colum == 'Questao_62':
                        if line.questao62 not in data_values[colum]:
                            data_values[colum][line.questao62] = 1
                        else:
                            data_values[colum][line.questao62] += 1

                    if colum == 'Questao_63':
                        if line.questao63 not in data_values[colum]:
                            data_values[colum][line.questao63] = 1
                        else:
                            data_values[colum][line.questao63] += 1

                    if colum == 'Questao_64':
                        if line.questao64 not in data_values[colum]:
                            data_values[colum][line.questao64] = 1
                        else:
                            data_values[colum][line.questao64] += 1

                    if colum == 'Questao_65':
                        if line.questao65 not in data_values[colum]:
                            data_values[colum][line.questao65] = 1
                        else:
                            data_values[colum][line.questao65] += 1

                    if colum == 'Questao_66':
                        if line.questao66 not in data_values[colum]:
                            data_values[colum][line.questao66] = 1
                        else:
                            data_values[colum][line.questao66] += 1

                    if colum == 'Questao_67':
                        if line.questao67 not in data_values[colum]:
                            data_values[colum][line.questao68] = 1
                        else:
                            data_values[colum][line.questao67] += 1

                    if colum == 'Questao_68':
                        if line.questao68 not in data_values[colum]:
                            data_values[colum][line.questao68] = 1
                        else:
                            data_values[colum][line.questao68] += 1



        return  Response(data_values, status=200)



from rest_framework import viewsets, permissions, status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from django.template import loader
from .serializers import *
from ..models import *
import csv
import pandas as pd
    
def PreProcessamento(dados):
    dados.fillna(0,  inplace=True) #Os campos vazios estão sendo substituidos por 0
    Dados=dados.astype(int, errors='ignore') #Realiza a conversão dos dados de Float para int
    return Dados
    
                                            
def tratamento(dados):
    Dados=dados.rename(columns={'CO_IES':'Codigo instituicao','CO_ORGACAD':'org. academica','CO_GRUPO':'area do curso','CO_CURSO':'Codigo do curso','CO_MODALIDADE':'Modalidade de Ensino','CO_MUNIC_CURSO':'municipio do curso','NU_IDADE':'Idade','TP_SEXO':'Sexo','ANO_FIM_EM':'Ano Final do EM','ANO_IN_GRAD':'Inicio da Grad.','CO_TURNO_GRADUACAO':'Turno da Grad.','TP_PRES':'Presenca no Enade','QE_I01':'Questao 01','QE_I02':'Questao 02','QE_I04':'Questao 04','QE_I05':'Questao 05','QE_I07':'Questao 07','QE_I08':'Questao 08','QE_I09':'Questao 09','QE_I11':'Questao 11','QE_I12':'Questao 12','QE_I13':'Questao 13','QE_I15':'Questao 15','QE_I16':'Questao 16','QE_I17':'Questao 17','QE_I21':'Questao 21','QE_I22':'Questao 22','QE_I23':'Questao 23','QE_I27':'Questao 27','QE_I28':'Questao 28','QE_I29':'Questao 29','QE_I30':'Questao 30','QE_I31':'Questao 31','QE_I32':'Questao 32','QE_I33':'Questao 33','QE_I34':'Questao 34','QE_I35':'Questao 35','QE_I36':'Questao 36','QE_I37':'Questao 37','QE_I38':'Questao 38','QE_I39':'Questao 39','QE_I40':'Questao 40','QE_I41':'Questao 41','QE_I42':'Questao 42','QE_I43':'Questao 43','QE_I44':'Questao 44','QE_I45':'Questao 45','QE_I46':'Questao 46','QE_I47':'Questao 47','QE_I48':'Questao 48','QE_I49':'Questao 49','QE_I50':'Questao 50','QE_I51':'Questao 51','QE_I52':'Questao 52','QE_I53':'Questao 53','QE_I54':'Questao 54','QE_I55':'Questao 55','QE_I56':'Questao 56','QE_I57':'Questao 57','QE_I58':'Questao 58','QE_I59':'Questao 59','QE_I60':'Questao 60','QE_I61':'Questao 61','QE_I62':'Questao 62','QE_I63':'Questao 63','QE_I64':'Questao 64','QE_I65':'Questao 65','QE_I66':'Questao 66','QE_I67':'Questao 67','QE_I68':'Questao 68'})
    return Dados


class Dados_adicionar(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.AllowAny, ]
    def get(self, request, format=None):
        dados = Dados.objects.all()
        serializer = DadosSerializer(dados, many=True)
        return Response(serializer.data)





    def post(self, request, format=None):
        enade = Enade()
        enade.ano = request.data["ano"]
        enade.save()

        arq = request.data["arquivo"]
        dados = pd.read_csv(arq, encoding = "UTF-8-sig", sep=";")
        dados = PreProcessamento(dados)

        dados = tratamento(dados)

        objetos = []
        for i in range(dados.shape[0]):
            print(i)
            obj_dados = Dados()
            obj_dados.codigoInstituicao = dados.loc[i, 'Codigo instituicao']
            obj_dados.orgAcademica = dados.loc[i, 'org. academica']
            obj_dados.areaCurso = dados.loc[i, 'area do curso']
            obj_dados.codigoCurso = dados.loc[i, 'Codigo do curso']
            obj_dados.modalidadeEnsino = dados.loc[i, 'Modalidade de Ensino']
            obj_dados.municipioCurso = dados.loc[i, 'municipio do curso']
            obj_dados.idade = dados.loc[i, 'Idade']
            obj_dados.sexo = dados.loc[i, 'Sexo'] 
            obj_dados.anoFinalEM = dados.loc[i, 'Ano Final do EM']
            obj_dados.iniciograd = dados.loc[i, 'Inicio da Grad.']
            obj_dados.turnoGrad = dados.loc[i, 'Turno da Grad.']
            obj_dados.presencaenade = dados.loc[i, 'Presenca no Enade']
            obj_dados.questao01 = dados.loc[i, 'Questao 01']
            obj_dados.questao02 = dados.loc[i, 'Questao 02']
            obj_dados.questao04 = dados.loc[i, 'Questao 04']
            obj_dados.questao05 = dados.loc[i, 'Questao 05']
            obj_dados.questao07 = dados.loc[i, 'Questao 07']
            obj_dados.questao08 = dados.loc[i, 'Questao 08']
            obj_dados.questao09 = dados.loc[i, 'Questao 09']
            obj_dados.questao11 = dados.loc[i, 'Questao 11']
            obj_dados.questao12 = dados.loc[i, 'Questao 12']
            obj_dados.questao13 = dados.loc[i, 'Questao 13']
            obj_dados.questao15 = dados.loc[i, 'Questao 15']
            obj_dados.questao16 = dados.loc[i, 'Questao 16']
            obj_dados.questao17 = dados.loc[i, 'Questao 17']
            obj_dados.questao21 = dados.loc[i, 'Questao 21']
            obj_dados.questao22 = dados.loc[i, 'Questao 22']
            obj_dados.questao23 = dados.loc[i, 'Questao 23']
            obj_dados.questao27 = dados.loc[i, 'Questao 27']
            obj_dados.questao28 = dados.loc[i, 'Questao 28']
            obj_dados.questao29 = dados.loc[i, 'Questao 29']
            obj_dados.questao30 = dados.loc[i, 'Questao 30']
            obj_dados.questao31 = dados.loc[i, 'Questao 31']
            obj_dados.questao32 = dados.loc[i, 'Questao 32']
            obj_dados.questao33 = dados.loc[i, 'Questao 33']
            obj_dados.questao34 = dados.loc[i, 'Questao 34']
            obj_dados.questao35 = dados.loc[i, 'Questao 35']
            obj_dados.questao36 = dados.loc[i, 'Questao 36']
            obj_dados.questao37 = dados.loc[i, 'Questao 37']
            obj_dados.questao38 = dados.loc[i, 'Questao 38']
            obj_dados.questao39 = dados.loc[i, 'Questao 39']
            obj_dados.questao40 = dados.loc[i, 'Questao 40']
            obj_dados.questao41 = dados.loc[i, 'Questao 41']
            obj_dados.questao42 = dados.loc[i, 'Questao 42']
            obj_dados.questao43 = dados.loc[i, 'Questao 43']
            obj_dados.questao44 = dados.loc[i, 'Questao 44']
            obj_dados.questao45 = dados.loc[i, 'Questao 45']
            obj_dados.questao46 = dados.loc[i, 'Questao 46']
            obj_dados.questao47 = dados.loc[i, 'Questao 47']
            obj_dados.questao48 = dados.loc[i, 'Questao 48']
            obj_dados.questao49 = dados.loc[i, 'Questao 49']
            obj_dados.questao50 = dados.loc[i, 'Questao 50']
            obj_dados.questao51 = dados.loc[i, 'Questao 51']
            obj_dados.questao52 = dados.loc[i, 'Questao 52']
            obj_dados.questao53 = dados.loc[i, 'Questao 53']
            obj_dados.questao54 = dados.loc[i, 'Questao 54']
            obj_dados.questao55 = dados.loc[i, 'Questao 55']
            obj_dados.questao56 = dados.loc[i, 'Questao 56']
            obj_dados.questao57 = dados.loc[i, 'Questao 57']
            obj_dados.questao58 = dados.loc[i, 'Questao 58']
            obj_dados.questao59 = dados.loc[i, 'Questao 59']
            obj_dados.questao60 = dados.loc[i, 'Questao 60']
            obj_dados.questao61 = dados.loc[i, 'Questao 61']
            obj_dados.questao62 = dados.loc[i, 'Questao 62']
            obj_dados.questao63 = dados.loc[i, 'Questao 63']
            obj_dados.questao64 = dados.loc[i, 'Questao 64']
            obj_dados.questao65 = dados.loc[i, 'Questao 65']
            obj_dados.questao66 = dados.loc[i, 'Questao 66']
            obj_dados.questao67 = dados.loc[i, 'Questao 67']
            obj_dados.questao68 = dados.loc[i, 'Questao 68']
            obj_dados.enade = enade
            objetos.append(obj_dados)
        Dados.objects.bulk_create(objetos) #bulk_create insere obj contidos em um array no banco de dados


       #utilizar thread pra inserir no banco de 1000 em 1000

        # for i in range(dados.shape[0]):
        #     print(i)
        #     obj_dados = Dados()
        #     obj_dados.codigoInstituicao = dados.loc[i, 'Codigo instituição']
        #     obj_dados.orgAcademica = dados.loc[i, 'org. acadêmica']
        #     obj_dados.areaCurso = dados.loc[i, 'área do curso']
        #     obj_dados.codigoCurso = dados.loc[i, 'Código do curso']
        #     obj_dados.modalidadeEnsino = dados.loc[i, 'Modalidade de Ensino']
        #     obj_dados.municipioCurso = dados.loc[i, 'município do curso']
        #     obj_dados.idade = dados.loc[i, 'Idade']
        #     obj_dados.sexo = dados.loc[i, 'Sexo'] 
        #     obj_dados.anoFinalEM = dados.loc[i, 'Ano Final do E.M.']
        #     obj_dados.iniciograd = dados.loc[i, 'Inicio da Grad.']
        #     obj_dados.turnoGrad = dados.loc[i, 'Turno da Grad.']
        #     obj_dados.presencaenade = dados.loc[i, 'Presença no Enade']
        #     obj_dados.questao01 = dados.loc[i, 'Questao 01']
        #     obj_dados.questao02 = dados.loc[i, 'Questao 02']
        #     obj_dados.questao04 = dados.loc[i, 'Questao 04']
        #     obj_dados.questao05 = dados.loc[i, 'Questao 05']
        #     obj_dados.questao07 = dados.loc[i, 'Questao 07']
        #     obj_dados.questao08 = dados.loc[i, 'Questao 08']
        #     obj_dados.questao09 = dados.loc[i, 'Questao 09']
        #     obj_dados.questao11 = dados.loc[i, 'Questao 11']
        #     obj_dados.questao12 = dados.loc[i, 'Questao 12']
        #     obj_dados.questao13 = dados.loc[i, 'Questao 13']
        #     obj_dados.questao15 = dados.loc[i, 'Questao 15']
        #     obj_dados.questao16 = dados.loc[i, 'Questao 16']
        #     obj_dados.questao17 = dados.loc[i, 'Questao 17']
        #     obj_dados.questao21 = dados.loc[i, 'Questao 21']
        #     obj_dados.questao22 = dados.loc[i, 'Questao 22']
        #     obj_dados.questao23 = dados.loc[i, 'Questao 23']
        #     obj_dados.questao27 = dados.loc[i, 'Questao 27']
        #     obj_dados.questao28 = dados.loc[i, 'Questao 28']
        #     obj_dados.questao29 = dados.loc[i, 'Questao 30']
        #     obj_dados.questao30 = dados.loc[i, 'Questao 30']
        #     obj_dados.questao31 = dados.loc[i, 'Questao 31']
        #     obj_dados.questao32 = dados.loc[i, 'Questao 32']
        #     obj_dados.questao33 = dados.loc[i, 'Questao 33']
        #     obj_dados.questao34 = dados.loc[i, 'Questao 34']
        #     obj_dados.questao35 = dados.loc[i, 'Questao 35']
        #     obj_dados.questao36 = dados.loc[i, 'Questao 36']
        #     obj_dados.questao37 = dados.loc[i, 'Questao 37']
        #     obj_dados.questao38 = dados.loc[i, 'Questao 38']
        #     obj_dados.questao39 = dados.loc[i, 'Questao 39']
        #     obj_dados.questao40 = dados.loc[i, 'Questao 40']
        #     obj_dados.questao41 = dados.loc[i, 'Questao 41']
        #     obj_dados.questao42 = dados.loc[i, 'Questao 42']
        #     obj_dados.questao43 = dados.loc[i, 'Questao 43']
        #     obj_dados.questao44 = dados.loc[i, 'Questao 44']
        #     obj_dados.questao45 = dados.loc[i, 'Questao 45']
        #     obj_dados.questao46 = dados.loc[i, 'Questao 46']
        #     obj_dados.questao47 = dados.loc[i, 'Questao 47']
        #     obj_dados.questao48 = dados.loc[i, 'Questao 48']
        #     obj_dados.questao49 = dados.loc[i, 'Questao 49']
        #     obj_dados.questao50 = dados.loc[i, 'Questao 50']
        #     obj_dados.questao51 = dados.loc[i, 'Questao 51']
        #     obj_dados.questao52 = dados.loc[i, 'Questao 52']
        #     obj_dados.questao53 = dados.loc[i, 'Questao 53']
        #     obj_dados.questao54 = dados.loc[i, 'Questao 54']
        #     obj_dados.questao55 = dados.loc[i, 'Questao 55']
        #     obj_dados.questao56 = dados.loc[i, 'Questao 56']
        #     obj_dados.questao57 = dados.loc[i, 'Questao 57']
        #     obj_dados.questao58 = dados.loc[i, 'Questao 58']
        #     obj_dados.questao59 = dados.loc[i, 'Questao 59']
        #     obj_dados.questao60 = dados.loc[i, 'Questao 60']
        #     obj_dados.questao61 = dados.loc[i, 'Questao 61']
        #     obj_dados.questao62 = dados.loc[i, 'Questao 62']
        #     obj_dados.questao63 = dados.loc[i, 'Questao 63']
        #     obj_dados.questao64 = dados.loc[i, 'Questao 64']
        #     obj_dados.questao65 = dados.loc[i, 'Questao 65']
        #     obj_dados.questao66 = dados.loc[i, 'Questao 66']
        #     obj_dados.questao67 = dados.loc[i, 'Questao 67']
        #     obj_dados.questao68 = dados.loc[i, 'Questao 68']
        #     obj_dados.enade = enade
        #     obj_dados.save()
        dados = Dados.objects.filter(enade=enade)
        serializer = DadosSerializer(dados, many=True).data

        if serializer:
            return Response(serializer, status=201)
        return Response({"erro":""}, status=400)




        # busca por ano
        # enade = Enade.objects.get(ano="2019")
        # dados = Dados.objects.filter(enade=enade)




# class DadosList(APIView):

#     """
#     List all snippets, or create a new snippet.
#     """

#     def get(self, request, format=None):
#         dados = Dados.objects.all()
#         serializer = DadosSerializer(dados, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         dados = dados()
#         group = Group.objects.get(name=request.data["tipo"])

#         login = request.data["login"]
#         senha = request.data["senha"]
#         if User.objects.filter(username=login).exists():
#             return Response({"message":"Usuário já existe!",'sucesso':False}, status=400)
#         user = User.objects.create_user(login, request.data["email"], senha)
        
#         funcionario.tipo = request.data["tipo"]
#         funcionario.nome = request.data["nome"]
#         funcionario.cpf = request.data["cpf"]
#         funcionario.email = request.data["email"]
#         funcionario.cargo = request.data["cargo"]
#         funcionario.usuario = user
#         funcionario.save()
#         if funcionario:
#             if group:
#                 funcionario.usuario.groups.add(group)
        
#         funcionario_data = FuncionarioSerializer([funcionario], many=True).data
        
#         if funcionario:
#             return Response({"funcionario":funcionario_data}, status=201)
#         return Response({"funcionario":None}, status=400)
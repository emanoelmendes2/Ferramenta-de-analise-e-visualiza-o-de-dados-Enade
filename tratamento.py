import csv
import pandas as pd
from matplotlib import pyplot as plt


import tkinter as tk
from tkinter import filedialog as dlg

def Selecao():
    root=tk.Tk()
    root.withdraw()
    arq = dlg.askopenfilename(filetypes=[("Arquivo de texto", "*.csv")])
    
    dados = pd.read_csv(arq, encoding = "UTF-8-sig", sep=";")
    return dados
    

def PreProcessamento(dados):
    dados.fillna(0,  inplace=True) #Os campos vazios estão sendo substituidos por 0
    Dados=dados.astype(int, errors='ignore') #Realiza a conversão dos dados de Float para int
    return Dados
    
                                            
def tratamento(dados):
    Df=dados.rename(columns={'CO_IES':'Codigo instituicao','CO_ORGACAD':'org. academica','CO_GRUPO':'area do curso','CO_CURSO':'Codigo do curso','CO_MODALIDADE':'Modalidade de Ensino','CO_MUNIC_CURSO':'municipio do curso','NU_IDADE':'Idade','TP_SEXO':'Sexo','ANO_FIM_EM':'Ano Final do EM','ANO_IN_GRAD':'Inicio da Grad.','CO_TURNO_GRADUACAO':'Turno da Grad.','TP_PRES':'Presença no Enade','QE_I01':'Questao 01','QE_I02':'Questao 02','QE_I04':'Questao 04','QE_I05':'Questao 05','QE_I07':'Questao 07','QE_I08':'Questao 08','QE_I09':'Questao 09','QE_I11':'Questao 11','QE_I12':'Questao 12','QE_I13':'Questao 13','QE_I15':'Questao 15','QE_I16':'Questao 16','QE_I17':'Questao 17','QE_I21':'Questao 21','QE_I22':'Questao 22','QE_I23':'Questao 23','QE_I27':'Questao 27','QE_I28':'Questao 28','QE_I29':'Questao 29','QE_I30':'Questao 30','QE_I31':'Questao 31','QE_I32':'Questao 32','QE_I33':'Questao 33','QE_I34':'Questao 34','QE_I35':'Questao 35','QE_I36':'Questao 36','QE_I37':'Questao 37','QE_I38':'Questao 38','QE_I39':'Questao 39','QE_I40':'Questao 40','QE_I41':'Questao 41','QE_I42':'Questao 42','QE_I43':'Questao 43','QE_I44':'Questao 44','QE_I45':'Questao 45','QE_I46':'Questao 46','QE_I47':'Questao 47','QE_I48':'Questao 48','QE_I49':'Questao 49','QE_I50':'Questao 50','QE_I51':'Questao 51','QE_I52':'Questao 52','QE_I53':'Questao 53','QE_I54':'Questao 54','QE_I55':'Questao 55','QE_I56':'Questao 56','QE_I57':'Questao 57','QE_I58':'Questao 58','QE_I59':'Questao 59','QE_I60':'Questao 60','QE_I61':'Questao 61','QE_I62':'Questao 62','QE_I63':'Questao 63','QE_I64':'Questao 64','QE_I65':'Questao 65','QE_I66':'Questao 66','QE_I67':'Questao 67','QE_I68':'Questao 68'})
    print(Df.shape)


# def mineracao(dados):
#     selecionarAno = input("Ano")
#     if selecionarAno == "2017":
#         selecionarGrafico = input("Grafico")
#         if selecionarGrafico == "histograma":
#             var= input("Variavel")
#             var1 = dados[var]

#             plt.figure(figsize=(8, 6))
#             plt.hist(var1)
#             plt.title(var1)
            
            

Dados = Selecao()
PreProcessamento(Dados)
tratamento(PreProcessamento(Dados))
#mineracao(tratamento)
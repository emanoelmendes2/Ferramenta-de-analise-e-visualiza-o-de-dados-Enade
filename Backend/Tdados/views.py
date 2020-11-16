from django.shortcuts import render, HttpResponse
import csv
import tkinter as tk
from tkinter import filedialog as dlg

# Create your views here.

def Selecao(request):
    root=tk.Tk()
    root.withdraw()
    arq = dlg.askopenfilename(filetypes=[("Arquivo de texto", "*.csv")])
    with open(arq) as csv_file:
    
        csv_reader = csv.DictReader(csv_file, delimiter=(';'))

        csv_reader.__next__()

        for row in csv_reader:
            print( row)


def PreProcessamento(request):
    return HttpResponse("Processamento")
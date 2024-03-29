from django.db import models

class Resultado(models.Model):
    kVizinhos = models.CharField(max_length= 16,blank= True, null=True, unique=True)
    dobrasF = models.CharField(max_length= 16,blank= True, null=True, unique=True)
    erro = models.CharField(max_length= 16,blank= True, null=True, unique=True)

class Enade(models.Model):
    ano = models.CharField(max_length= 16,blank= True, null=True, unique=True)
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE, blank= True, null=True )

class Estado(models.Model):
    id = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length= 20,blank= True, null=True, unique=True)

class Dados(models.Model):
    codigoInstituicao = models.IntegerField(blank= True, null=True)
    orgAcademica = models.IntegerField(blank= True, null=True)
    areaCurso = models.IntegerField(blank= True, null=True)
    codigoCurso = models.IntegerField(blank= True, null=True)
    modalidadeEnsino = models.IntegerField(blank= True, null=True)
    municipioCurso = models.IntegerField(blank= True, null=True)
    idade = models.IntegerField(blank= True, null=True)
    sexo = models.CharField(max_length= 16,blank= True, null=True)
    anoFinalEM = models.IntegerField(blank= True, null=True)
    iniciograd = models.IntegerField(blank= True, null=True)
    turnoGrad = models.IntegerField(blank= True, null=True)
    presencaenade = models.IntegerField(blank= True, null=True)
    questao01 = models.CharField(max_length= 16,blank= True, null=True)
    questao02 = models.CharField(max_length= 16,blank= True, null=True)
    questao04 = models.CharField(max_length= 16,blank= True, null=True)
    questao05 = models.CharField(max_length= 16,blank= True, null=True)
    questao07 = models.CharField(max_length= 16,blank= True, null=True)
    questao08 = models.CharField(max_length= 16,blank= True, null=True)
    questao09 = models.CharField(max_length= 16,blank= True, null=True)
    questao11 = models.CharField(max_length= 16,blank= True, null=True)
    questao12 = models.CharField(max_length= 16,blank= True, null=True)
    questao13 = models.CharField(max_length= 16,blank= True, null=True)
    questao15 = models.CharField(max_length= 16,blank= True, null=True)
    questao16 = models.CharField(max_length= 16,blank= True, null=True)
    questao17 = models.CharField(max_length= 16,blank= True, null=True)
    questao21 = models.CharField(max_length= 16,blank= True, null=True)
    questao22 = models.CharField(max_length= 16,blank= True, null=True)
    questao23 = models.CharField(max_length= 16,blank= True, null=True)
    questao27 = models.CharField(max_length= 16,blank= True, null=True)
    questao28 = models.CharField(max_length= 16,blank= True, null=True)
    questao29 = models.CharField(max_length= 16,blank= True, null=True)
    questao30 = models.CharField(max_length= 16,blank= True, null=True)
    questao31 = models.CharField(max_length= 16,blank= True, null=True)
    questao32 = models.CharField(max_length= 16,blank= True, null=True)
    questao33 = models.CharField(max_length= 16,blank= True, null=True)
    questao34 = models.CharField(max_length= 16,blank= True, null=True)
    questao35 = models.CharField(max_length= 16,blank= True, null=True)
    questao36 = models.CharField(max_length= 16,blank= True, null=True)
    questao37 = models.CharField(max_length= 16,blank= True, null=True)
    questao38 = models.CharField(max_length= 16,blank= True, null=True)
    questao39 = models.CharField(max_length= 16,blank= True, null=True)
    questao40 = models.CharField(max_length= 16,blank= True, null=True)
    questao41 = models.CharField(max_length= 16,blank= True, null=True)
    questao42 = models.CharField(max_length= 16,blank= True, null=True)
    questao43 = models.CharField(max_length= 16,blank= True, null=True)
    questao44 = models.CharField(max_length= 16,blank= True, null=True)
    questao45 = models.CharField(max_length= 16,blank= True, null=True)
    questao46 = models.CharField(max_length= 16,blank= True, null=True)
    questao47 = models.CharField(max_length= 16,blank= True, null=True)
    questao48 = models.CharField(max_length= 16,blank= True, null=True)
    questao49 = models.CharField(max_length= 16,blank= True, null=True)
    questao50 = models.CharField(max_length= 16,blank= True, null=True)
    questao51 = models.CharField(max_length= 16,blank= True, null=True)
    questao52 = models.CharField(max_length= 16,blank= True, null=True)
    questao53 = models.CharField(max_length= 16,blank= True, null=True)
    questao54 = models.CharField(max_length= 16,blank= True, null=True)
    questao55 = models.CharField(max_length= 16,blank= True, null=True)
    questao56 = models.CharField(max_length= 16,blank= True, null=True)
    questao57 = models.CharField(max_length= 16,blank= True, null=True)
    questao58 = models.CharField(max_length= 16,blank= True, null=True)
    questao59 = models.CharField(max_length= 16,blank= True, null=True)
    questao60 = models.CharField(max_length= 16,blank= True, null=True)
    questao61 = models.CharField(max_length= 16,blank= True, null=True)
    questao62 = models.CharField(max_length= 16,blank= True, null=True)
    questao63 = models.CharField(max_length= 16,blank= True, null=True)
    questao64 = models.CharField(max_length= 16,blank= True, null=True)
    questao65 = models.CharField(max_length= 16,blank= True, null=True)
    questao66 = models.CharField(max_length= 16,blank= True, null=True)
    questao67 = models.CharField(max_length= 16,blank= True, null=True)
    questao68 = models.CharField(max_length= 16,blank= True, null=True)
    enade = models.ForeignKey(Enade, on_delete=models.CASCADE, blank= True, null=True )




def decode(encodedString):
    # Write your code here
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        encodedString = raw_input()

        result = decode(encodedString)

        fptr.write(result + '\n')

        fptr.close()
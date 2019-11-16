import os
#mostrar valores
nota1, nota2, nota3, nota4, alumno=0.0, 0.0, 0.0, 0.0, ""

#input
nota1=float(os.sys.argv[1])
nota2=float(os.sys.argv[2])
nota3=float(os.sys.argv[3])
nota4=float(os.sys.argv[4])
alumno=os.sys.argv[5]
#processing
promedio_final=(nota1+nota2+nota3+nota4)/4

#verificador
buen_alumno=(promedio_final>17)

#output
print("##################################")
print("voleta electronica de notas")
print("###############################")
print("alumno:",alumno)
print("#####################################")
print("nota1:",nota1)
print("nota2:",nota2)
print("nota3=",nota3)
print("nota4:",nota4)
print("####################")
print("promedio final es=",promedio_final)

#condicion simple
#si el alumno es buen alumno entonces sera becado
if (buen_alumno==False):
    print("entoces sera no sera becado")

#fin_if

#condicional doble
else :
    pritn("el alumno debera esforsarse un poca mas")




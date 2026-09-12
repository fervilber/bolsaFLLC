---
title: "Software para calcular la rentabilidad financiero fiscal"
date: 2008-05-12
source: https://www.rankia.com/blog/llinares/365043-software-para-calcular-rentabilidad-financiero-fiscal
author: Francisco Llinares Coloma
blog: Rankia
---

# Software para calcular la rentabilidad financiero fiscal

Desde que hemos empezado con la cartera de renta fija especulativa muchos lectores me han preguntado la manera de calcular la rentabilidad de una emisión concreta de renta fija.

Después de varios intentos fallidos míos y de algunos lectores de buscar en la red algún programa que pudiera calcular la rentabilidad, he decidido desempolvar mi curso de programación en BASIC jurásico y hacer este rudimentario programa.

Esta aplicación es capaz de sacar la rentabilidad en cualquier circunstancia, pero para que no fuera demasiado engorroso me he limitado a calcular la vida restante de la emisión en meses. Debido a este detalle y a la sencillez del programa, la rentabilidad puede tener un error anual de un 0.05% más o menos. Pienso que a pesar de no ser muy exacto puede servir para que los lectores tengan una idea muy aproximada de la rentabilidad de cualquier emisión.

Pongo el código del programa abierto por dos motivos:

1 - Estando a la vista nadie me podrá acusar de haberle introducido un virus o un programa espía en su ordenador.

2 - Quizá alguno de los programadores voluntarios del laboratorio de inversión use estas fórmulas y haga un programita decente para Windows.

Copiar y pegar el texto siguiente y guardarlo en una carpeta con el nombre de TIR.BAS

20 CLS:INPUT "PRECIO DE COMPRA EN PORCENTAJE ",PC
30 INPUT "PRECIO DE VENTA O AMORTIZACION ",PV
40 INPUT "CANTIDAD DE MESES DE VIDA HASTA LA VENTA O EL VENCIMIENTO ",MV
50 INPUT "INTERES NOMINAL ANUAL ",IN
60 INM=IN/12
70 FOR I=.1 TO 2 STEP .001
80 C#=PC
90 FOR X=1 TO MV
100 IM=C#*I/100
110 C#=C#+IM
120 C#=C#-INM
130 NEXT X
140 IF C#=>PV THEN 160
150 NEXT I
160 PRINT:PRINT
170 RA=I*12:PRINT "RENTABILIDAD ANUAL ";RA
180 :
190 PRINT:PRINT
200 RFF=(IN*((100-18+(24-1.2))/100))/((100-18)/100):RFA=(RFF-IN)/PC*PV
210 PRINT "RENTABILIDAD FINANCIERO FISCAL SI SON AUTOPISTAS BONIFICADAS ";RFA+RA

Para poder ejecutar este software se debe de descargar en la red un programa llamado GWBASIC.EXE que se pondrá en la misma carpeta que el TIR.BAS.

EJECUCION DEL PROGRAMA

Se arranca el GWBASIC.EXE

Se escribe LOAD"TIR y se pulsa intro.

Se escribe RUN e intro.

Llegado a este punto se deben contestar las preguntas siguientes:

PRECIO DE COMPRA EN PORCENTAJE

A esta pregunta se contestará con el precio de compra en porcentaje sobre su nominal, no en euros. Después de cada pregunta se pulsa intro.

Como ejemplo voy a poner la última recomendación sobre las OBLIGACIONES DE AUTOPISTAS AUCALSA AL 4%

En este caso escribiremos el precio de compra recomendado, o sea, 91

PRECIO DE VENTA O AMORTIZACION

Se supone que si mantenemos hasta el vencimiento nos lo reembolsarán a 100. Por lo tanto escribo 100

CANTIDAD DE MESES DE VIDA HASTA LA VENTA O EL VENCIMIENTO

Como su VENCIMIENTO es el 8/06/2014, le faltan aproximadamente 73 meses, pues pongo 73

INTERES NOMINAL ANUAL

Aquí escribo el interés, o sea, 4

El programa ofrecerá dos respuestas:

1 - RENTABILIDAD ANUAL

Que en el ejemplo que nos ocupa será del 5.76%

2 - RENTABILIDAD FINANCIERO FISCAL SI SON AUTOPISTAS BONIFICADAS

Como el ejemplo precisamente es una autopista, en esta respuesta está incluida la rentabilidad repercutida debida a la deducción fiscal del 95% de la retención. Nos dará una rentabilidad del 6.98%.
----------------------------------------------------------------------------
Con posterioridad a este artículo, Paco ha tenido la amabilidad de pasar este código a Visual Basic, de esta manera se puede ejecutar en windows directamente. Gracias Paco.

Aquí se puede descargar el programa comprimido.

RFF.zip

Articulos relacionados

F2LL Para la cartera de renta fija
Cuenta para operar en renta fija
Estrategia especial para renta fija
Enfoque profesional sobre Renta fija y futuros
Carta abierta a la C.N.M.V
---
title: "ETCHART: Los spreads históricos más completos de la galaxia."
date: 2012-05-10
source: https://www.rankia.com/blog/llinares/1251153-etchart-spreads-historicos-mas-completos-galaxia
author: Francisco Llinares Coloma
blog: Rankia
---

# ETCHART: Los spreads históricos más completos de la galaxia.

Se ha acoplado la base de datos descargada por los exprimidores de los estupendos colaboradores del proyecto Egregore para que la pueda manejar el ETCHART de una manera automatizada.


Para evitar el tener que actualizar esa base de datos a menudo, se descargará una vez al año. Para continuar con los últimos meses no incluidos en la base de datos, se podrán usar los archivos normales de ETCHART, que se actualizan cada día.


Esta base de datos quedará ubicada en \ETCHART\EGREGORE\BDD y desde allí la leerá el programa. Como hay modificaciones del software, carpetas, etc. y, además, se han actualizado las tablas que estaban con vencimientos anticuados, quizá lo más cómodo es que esta vez se descargue todo completo. Los que quieran guardar cualquier configuración de usuario ya saben que luego la pueden copiar encima.




Aquí se pueden consultar las instrucciones de manejo




Y aquí se puede descargar todo completo.




VENTAJAS SOBRE OTROS PROGRAMAS DISPONIBLES EN LA RED




1 –  Con esta base de datos se podrá ver cualquier combinación con mucho mayor histórico. En algunos productos, más de 50 años. En casi todos los sitios no pasan de 20 años.


2 – Se podrán ver los resultados día a día. En otros sitios, para ver 20 años sólo dispones de un dato al mes.


3 – El número de productos implicados en un spread es ilimitado. En el resto suele estar limitado a tres productos.


4 – Se podrán ver spreads estacionales sin que el programa los saque al revés como suele ocurrir. Por ejemplo: si quiero ver la diferencia entre el gasóleo de diciembre menos el de junio, los otros programas, cuando termina junio pasan al junio siguiente pero mantienen la pata de diciembre del año anterior. Eso desvirtúa todos los datos.


Con el spredador más completo de la galaxia se podrá elegir tanto el mes del vencimiento como si ese vencimiento tiene que ser del mismo año, del año anterior o del año siguiente. Gracias a esta posibilidad puedo hacer cualquier mariposa, sean todos los vencimientos implicados del mismo año o del siguiente, y ver los resultados de varias décadas en un sólo gráfico.


Otra cosa que me permite hacer y que no se podía hacer con otros programas, es hacer, por ejemplo, una mariposa toda con diciembres, indicando la distancia entre cada pata en años ( uno, dos años, etc.). Y luego ver el resultado de esa mariposa de todo el histórico. En otros programas sólo podía ver un vencimiento exacto y para ver otro vencimiento tenía que volver a cambiarlo.


5  - Como con el resto de funciones de ETCHART, se podrá configurar cualquier spread o cálculo en una lista para poder verlos uno a uno pulsando enter.


6 – Los resultados de cualquier cálculo quedarán en un archivo de la carpeta “EGR” de la BDD del ETCHART, con el mismo formato que el resto y con el nombre elegido. Esto permitirá un posterior procesamiento de los datos de salida para ser tratados con cualquier otra herramienta de ETCHART o para usarlos para nuevos cálculos.




EJEMPLOS EXPLICADOS


Teniendo en cuenta que los vencimientos de las vaquicerdas a precio barato suelen ser junio y agosto, quiero saber cuánto me suele costar hacer el roll over del spread completo de junio a agosto. Con este gráfico puedo ver cuál es el precio habitual del roll over del spread y en qué meses sube o baja.


El archivo de configuración de este spread a 4 bandas:


+, 4,, CON, 0, LEHE_MM_QQ, 3, #1-#2-#3+#4

LE,6,,L,,

HE,6,,L,,

LE,8,,L,,

HE,8,,L,,




Un spread hecho con los vencimientos más cercanos del contrato de cacao de Londres traducido a dólares menos el cacao de Nueva York:


+, 3,, CER, 0, INTERCACAO, 0, (#1*#2)-#3

CA,,,L,,CCNPAR.CCL

B6,,,L,,GBPUSD.DIV

CC,,,L,,CCNPAR.ICE








Lo mismo pero del azúcar:


+, 2,, CER, 0, INTERAZUCAR, 0, #1*50 - ((#2/100)*112000)

SW,,,L,,WSVPAR.CCL

SB,,,L,,SBVPAR.ICE





Es curioso que la Nocilla ( azúcar, cacao y posiblemente también las avellanas) en Londres siempre sea más cara que en Nueva York. Es algo que escapa a la lógica, pero, como se puede ver,  la diferencia es importante.





ASÍ QUEDA UN ARCHIVO DE EJEMPLO CON VARIOS SPREADS  (este archivo se puede copiar con el nombre que se quiera en  "\ETCHART\EGREGORE" )





Spread del vencimiento más cercano de 100 onzas de plata menos 2 de oro:


+, 2,, CER, 0, GCSI_CER, 0, #1-#2

SI,,,L,100,SIZPAR.CMX

GC,,,L,2,GCZ2.CMX




Un contrato de harina de soja + uno de aceite de soja - uno de habas de soja:


+, 3,, CER, 0, SOJA_COMPLEJO, 0, #1+#2-#3

ZM,,,L,100,SMPERP.CBT

ZL,,,L,600,BOPERP.CBT

ZS,,,L,50,SPERP.CBT




Roll over entre el spread vaca-cerdo de junio y vaca-cerdo de agosto:


+, 4,, CON, 0, LEHE_MM_QQ, 3, #1-#2-#3+#4

LE,6,,L,,

HE,6,,L,,

LE,8,,L,,

HE,8,,L,,


Un contrato de azúcar de Londres menos uno de azúcar de Nueva York:


+, 2,, CER, 0, INTERAZUCAR, 0, #1*50 - ((#2/100)*112000)

SW,,,L,,WSVPAR.CCL

SB,,,L,,SBVPAR.ICE


Un contrato de cacao de Londres menos uno de cacao de Nueva York:


+, 3,, CER, 0, INTERCACAO, 0, (#1*#2)-#3

CA,,,L,,CCNPAR.CCL

B6,,,L,,GBPUSD.DIV

CC,,,L,,CCNPAR.ICE


Una mariposa con diciembres del eurodolar con dos años de distancia entre cada pata:


+, 3,, CON, 0, GE_MARIPGRANDE, 4, #1-2*#2+#3

GE,12,-2,L,,

GE,12,0,L,,

GE,12,+2,L,,
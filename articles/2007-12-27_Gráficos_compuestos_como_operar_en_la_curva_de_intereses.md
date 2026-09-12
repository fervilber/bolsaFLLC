---
title: "Gráficos compuestos: como operar en la curva de intereses"
date: 2007-12-27
source: https://www.rankia.com/blog/llinares/364952-graficos-compuestos-como-operar-curva-intereses
author: Francisco Llinares Coloma
blog: Rankia
---

# Gráficos compuestos: como operar en la curva de intereses

Los intereses siempre conforman una estructura temporal llamada "curva de intereses". Cada plazo tiene su tipo de interés de mercado. No es lo mismo poner dinero en un plazo fijo a un mes que comprar un bono a 30 años.

Lo más habitual es que los plazos más largos paguen un interés mayor que los plazos cortos, pero ese diferencial va cambiando en arreglo a las expectativas.

Cuando el diferencial entre dos plazos inicia una tendencia convergente o divergente, podemos aprovecharla operando con un gráfico compuesto. En el artículo Análisis técnico avanzado: gráficos compuestos está explicado el mecanismo de estos gráficos, sus ventajas operativas, como construirlos con el VISUAL CHART, y como descargar e instalar la herramienta para su utilización.

Hoy vamos a hacer un spread entre el futuro del bono alemán a cinco años (BOBL) y el futuro sobre el de diez años (BUND). A continuación voy a poner una tabla comparativa entre el precio de cotización del futuro y su rentabilidad anual.

Esta tabla es muy aproximada pero no exacta, pues la exactitud depende del bono físico entregable más barato que se asigna para cada vencimiento y que cambia con el tiempo. De todas formas servirá como orientación para lo que se quiere explicar.

Precios del futuro sobre cinco años y rentabilidad anual a ese precio

92 --- 8
93 --- 7.74
94 --- 7.48
95 --- 7.22
96 --- 6.97
97 --- 6.72
98 --- 6.48
99 --- 6.24
100 --- 6
101 --- 5.76
102 --- 5.53
103 --- 5.30
104 --- 5.07
105 --- 4.85
106 --- 4.62
107 --- 4.41
108 --- 4.19
109 --- 3.98
110 --- 3.76
111 --- 3.56
112 --- 3.35
113 --- 3.15
114 --- 2.94
115 --- 2.74
116 --- 2.55
117 --- 2.35
118 --- 2.16

Precios del futuro sobre diez años y rentabilidad anual a ese precio

90 --- 7.45
91 --- 7.30
92 --- 7.15
93 --- 7
94 --- 6.85
95 --- 6.70
96 --- 6.56
97 --- 6.42
98 --- 6.28
99 --- 6.14
100 --- 6
101 --- 5.87
102 --- 5.73
103 --- 5.60
104 --- 5.47
105 --- 5.34
106 --- 5.22
107 --- 5.09
108 --- 4.97
109 --- 4.84
110 --- 4.72
111 --- 4.60
112 --- 4.49
113 --- 4.37
114 --- 4.25
115 --- 4.14
116 --- 4.03
117 --- 3.91
118 --- 3.80
119 --- 3.69
120 --- 3.59
121 --- 3.48
122 --- 3.37
123 --- 3.27
124 --- 3.16
125 --- 3.06

Como se puede observar, un movimiento de un punto de rentabilidad anual produce un movimiento en el precio de los futuros diferente para el de cinco años o para el de diez. Con mucha aproximación se puede decir que se mueve el doble de puntos el de diez años que el de cinco para el mismo movimiento de intereses. Esto se debe al hecho de que, a mayor vida restante de cada bono, mayor es el impacto sobre el precio del futuro cuando hay un movimiento del tipo de interés.

Para neutralizar esta diferencia en los movimientos de los precios se opera con dos bonos de cinco años contra uno de diez. Este spread neutraliza la diferencia de plazo y sólo representa el diferencial de intereses entre los dos plazos, pudiendo operar perfectamente a la expectativa de que ese diferencial se contraiga o se expanda.

Como se puede ver en el gráfico, el diferencial que ahora está cerca de sus mínimos parece que va a volver a aumentar. Se deberían aprovechar las pequeñas correcciones que se producirán en este spread para entrar al alza.
Para operar al alza en este spread se compran dos BOBL y se vende un BUND, de esta manera se aprovechará la tendencia que se ha iniciado a que aumente el diferencial de intereses entre ambos, independientemente que los bonos o los intereses suban o bajen. Siempre que aumente el diferencial de intereses se ganará.

CONFIGURACION DEL GRAFICO DEL SPREAD

Una vez instalada la herramienta, para confeccionar el indicador se inserta primero el gráfico del fut. del BOBL - Después el del BUND, por último, se inserta el indicador "llinares" poniendo los siguientes parámetros:

Price Source = Data1

Factor1 = 2
Factor2 = -1
Factor3 = 0
Factor4 = 0
Factor5 = 0
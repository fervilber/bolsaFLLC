---
title: "Gráficos compuestos: Russell 2000 vs Dow Jones"
date: 2008-02-27
source: https://www.rankia.com/blog/llinares/364763-graficos-compuestos-russell-2000-vs-dow-jones
author: Francisco Llinares Coloma
blog: Rankia
---

# Gráficos compuestos: Russell 2000 vs Dow Jones

Para los que no hayan leído los artículos anteriores sobre gráficos compuestos les recomiendo que antes de seguir se lean el primero de esta serie: Análisis técnico avanzado: gráficos compuestos. Ahí encontrarán los motivos para la operativa en este tipo de spreads y la manera de instalar la herramienta.

Me han preguntado varias veces por un spread entre grandes y pequeñas empresas. Esto se puede hacer de muchas maneras, pero he elegido una que es sencilla de operar, tiene liquidez y el montante total de la inversión es pequeño. De esta forma cada uno puede ajustar la operativa a sus recursos y exposición personal.

La elección ha recaído en un contrato del mini Russell 2000 contra uno del mini Dow Jones. En esta combinación se reúne una similitud bastante grande en el precio total de los contratos (71.000 $ vs 63.000$ en estos momentos) y un tamaño nominal pequeño de los dos. Además, ambos se pueden operar durante muchas horas en mercado electrónico con horquillas bastante decentes.

Como los precios son bastante dispares, para simplificar la comprensión del spread he confeccionado el gráfico en dólares directamente. O sea, la cifra que se refleja en el gráfico es la cantidad total de dólares que hay de diferencia entre el valor total de un contrato y el valor total del otro. Por tanto, la operativa es de uno contra uno.

Como se puede ver en el gráfico del spread, hace poco ha cambiado la tendencia primaria del diferencial, por lo cual, a partir de ahora hay que situarse vendido de mini Russell 2000 y comprado del mini Dow Jones. Los códigos de mercado de ambos son: ER2 - YM.

Como el futuro del mini Russell 2000 vale 100$ el punto, se multiplicará por 100 en el Factor 1 del indicador. El del mini Dow se multiplica por 5$, por lo tanto se procederá a poner -5 en el Factor 2.

Configuración del spread

Se inserta primero el gráfico del Russell 2000. Después el del Dow Jones. Por último, se inserta el indicador "llinares" poniendo los siguientes parámetros:

Price Source = Data1
Factor1 = 100
Factor2 = -5
Factor3 = 0
Factor4 = 0
Factor5 = 0

Artículos relacionados:
Graficos compuestos: SAN contra BBVA
A río revuelto ganancia de gráficos compuestos
Gráficos compuestos: como operar en la curva de intereses

Ya ha entrado la orden de renta fija de Solvay, pronto actualizaré la cartera.
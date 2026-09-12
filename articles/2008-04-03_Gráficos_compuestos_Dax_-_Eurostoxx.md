---
title: "Gráficos compuestos: Dax - Eurostoxx"
date: 2008-04-03
source: https://www.rankia.com/blog/llinares/364777-graficos-compuestos-dax-eurostoxx
author: Francisco Llinares Coloma
blog: Rankia
---

# Gráficos compuestos: Dax - Eurostoxx

Para los que no hayan leído los artículos anteriores sobre gráficos compuestos les recomiendo que antes de seguir se lean el primero de esta serie: Análisis técnico avanzado: gráficos compuestos. Ahí encontrarán los motivos para la operativa en este tipo de spreads y la manera de instalar la herramienta.

En varios comentarios me han pedido que haga este spread, también he leído algunos comentarios que no acaban de entender la aplicación de un factor determinado para confeccionar un spread. Voy a intentar aclarar estos conceptos.

Voy a utilizar un contrato del Dax contra cuatro contratos del Eurostoxx 50. Esto es un intento de que el valor nominal de cada lote sea lo más parecido posible. Llegada la hora de operar se comprará un Dax y se venderán 4 eurostoxx para posicionarse al alza en el gráfico del spread, y viceversa para aprovechar las bajadas.

Para ver la correlación entre los dos lotes, la manera más sencilla y clarificadora es que el gráfico represente la diferencia en euros del valor nominal de un contrato del Dax menos el valor nominal de 4 contratos del Eurostoxx 50, que en el momento de hacer el gráfico ascendía a 17.520 euros.

Para conseguir esa diferencia en euros se aplicará la cantidad de 25 al factor 1, que corresponde a los 25 euros que vale cada punto del contrato del Dax. En el factor 2 se restarán 40, que sale de multiplicar los 4 contratos por los 10 euros por punto de los contratos del Eurostoxx.

Un Dax menos cuatro Eurostoxx 50

Como se puede ver, el gráfico está a punto de romper una cabeza con hombros a la baja, si ocurre ese cambio de tendencia del spread se podrá aprovechar vendiendo un Dax y comprando 4 Eurostoxx.
Configuración del spread

Se inserta primero el gráfico del Dax.
Luego el del Eurostoxx

Por último, se inserta el indicador "llinares" poniendo los siguientes parámetros:

Price Source = Data1

Factor1 = 25
Factor2 = -40
Factor3 = 0
Factor4 = 0
Factor5 = 0

Artículos relacionados:

De esto que no se entere nadie

Gráficos compuestos: vigilando el vencimiento de derivados

Graficos compuestos: SAN contra BBVA

A río revuelto ganancia de gráficos compuestos

Gráficos compuestos: Russell 2000 vs Dow Jones

Graficos Compuestos: el complejo de la soja

Gráficos compuestos: cabalgando la curva de intereses USA

Gráficos compuestos: como operar en la curva de intereses
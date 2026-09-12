---
title: "Los cuatro jinetes contra el ibex"
date: 2008-04-30
source: https://www.rankia.com/blog/llinares/364665-cuatro-jinetes-contra-ibex
author: Francisco Llinares Coloma
blog: Rankia
---

# Los cuatro jinetes contra el ibex

Para los que no hayan leído los artículos anteriores sobre gráficos compuestos les recomiendo que antes de seguir se lean el primero de esta serie: Análisis técnico avanzado: gráficos compuestos. Ahí encontrarán los motivos para la operativa en este tipo de spreads y la manera de instalar la herramienta.

Hoy vamos a hacer un spread de los cuatro valores con más ponderación del Ibex contra el mismo Ibex. Para tener una idea clara de cómo se mueve el spread en cada momento y ejercer un control absoluto de la situación, el gráfico del spread mostrará la cantidad de euros de diferencia entre el lote de los cuatro valores y un futuro del MiniIbex.

El lote de valores estará compuesto por:

300 Telefónica
300 BSCH
200 BBVA
200 Iberdrola

A todo este lote se le restará el valor nominal de un futuro del MiniIbex. Para los que quieran operar con cantidades mayores pueden multiplicar el número de títulos de las cuatro acciones por diez y usar un futuro grande del Ibex.

Este spread puede servir para tres operativas diferentes:

1 - Tener el lote siempre comprado, y sin deshacer la cartera ni pagar a hacienda, vender un Mini Ibex cada vez que cambie la tendencia secundaria del mercado a bajista. Una forma cómoda de librarse de las correcciones sin tener que pagar muchas comisiones ni tributar a hacienda por las plusvalías latentes.

2 - Operar a favor de los movimientos del diferencial, comprando los 4 valores y vendiendo un MiniIbex cuando el gráfico de señal alcista y viceversa en los movimientos a la baja.

3 - Teniendo en cuenta que este diferencial nunca tendrá una tendencia vertical a ningún lado, se podría usar para vender constantemente volatilidad del spread. Viendo que el deslizamiento a largo plazo del spread es al alza, recomiendo que las operaciones para vender volatilidad siempre se inicien comprando los cuatro valores y vendiendo un MiniIbex cerca de algún soporte y nunca se opere al revés para la venta de volatilidad.

Para comprender como se puede vender volatilidad de algo que no tiene opciones cotizando recomiendo leer los cinco artículos que hablan sobre volatilidad pinchando en la etiqueta del mismo nombre.

Configuración del spread

Se inserta primero el gráfico de Telefónica
En segundo lugar el del BSCH
Luego el del BBVA
En cuarto lugar Iberdrola
Y por último el del Ibex

Por último, se inserta el indicador "llinares" poniendo los siguientes parámetros:

Price Source = Data1
Factor1 = 300
Factor2 = 300
Factor3 = 200
Factor4 = 200
Factor5 = -1

Artículos relacionados:

De esto que no se entere nadie

Gráficos compuestos: vigilando el vencimiento de derivados

Graficos compuestos: SAN contra BBVA

A río revuelto ganancia de gráficos compuestos

Gráficos compuestos: Russell 2000 vs Dow Jones

Graficos Compuestos: el complejo de la soja

Gráficos compuestos: cabalgando la curva de intereses USA

Gráficos compuestos: como operar en la curva de intereses
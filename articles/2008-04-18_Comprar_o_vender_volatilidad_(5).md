---
title: "Comprar o vender volatilidad (5)"
date: 2008-04-18
source: https://www.rankia.com/blog/llinares/365101-comprar-vender-volatilidad-5
author: Francisco Llinares Coloma
blog: Rankia
---

# Comprar o vender volatilidad (5)

En el coloquio de ayer, hablamos sobre programas de simulación de estrategias que nos den luz para escoger entre las miles de posibilidades que tenemos a nuestro alcance. Me comprometí a escribir en este blog algunas ideas interesantes para que los programadores pudieran escoger las que les parecieran más interesantes, o las que a los usuarios les gustaran más.

Para dar una pista a los que tienen que implementar el software de la prioridad que los usuarios conceden a cada estrategia o sistema, sería conveniente que en los comentarios de este artículo, cada lector interesado en obtener un simulador para hacer funcionar esta estrategia, ponga un comentario otorgando una puntuación de 1 a 10.

De esta manera será fácil sumar el número de votos de cada propuesta y empezar por aquellas que hayan captado el mayor interés.

Antes del planteamiento y para una mejor comprensión, recomiendo leer los cuatro artículos anteriores sobre comprar o vender volatilidad que se pueden pinchar al final.

VOLATILIDAD DIRECCIONAL O CONTENIDA DENTRO DE UN RANGO

Entre dos productos que tengan la misma volatilidad, no se asume el mismo riesgo con uno que se mueve entre 100 y 200, que con otro cuyo movimiento está contenido dentro de un rango de entre 100 y 110, y ha hecho ese trayecto cinco veces a cada lado. Aunque los dos tengan la misma volatilidad en un determinado momento, y el precio de las primas de las opciones sea igual, el riesgo del primero es muy superior al del segundo. Por lo tanto, cuando la volatilidad y las primas de las opciones sean iguales, habría que comprar opciones del primero y venderlas del segundo.

La volatilidad es el porcentaje total de movimiento a los dos lados, pero a la hora de contabilizar el riesgo, solo debería contar el movimiento porcentual total a un mismo lado, puesto que los movimientos de ida y vuelta, a medio plazo se neutralizan entre si.

Todas las estrategias susceptibles de ser usadas en los mercados, se pueden dividir con una claridad diáfana en dos grupos: las que compran volatilidad y las que la venden.

Las estrategias que compran volatilidad se deben usar en mercados muy direccionales y con pocas congestiones, y las que venden volatilidad, son útiles durante congestiones largas y sólo mientras duren, o en productos que por sus características, su precio fluctúa contenido en un rango estrecho de precios pero con una volatilidad alta.

Después de leer lo anterior, podemos comprender que nos sería muy útil una herramienta que nos fuera indicando en cada momento la conveniencia de comprar o vender volatilidad de cada valor, y por supuesto, que lado es el más seguro para hacer cada operación.

La citada herramienta podría obtener dos datos cuyo rango oscilara entre 0 y 100. Uno de los datos indicaría el momento oportuno para comprar o vender volatilidad al alza, y el otro daría la señal para hacer lo propio a la baja.

INDICADOR DE VOLATILIDAD AL ALZA

0 - 20 venta clara de CALLS
20 - 40 venta de CALLS con algo de riesgo
40 - 60 abstenerse de operar, ni comprando ni vendiendo volatilidad
60 - 80 compra de CALLS con algo de riesgo
80 - 100 compra clara de CALLS o incluso compra directa del subyacente.

INDICADOR DE VOLATILIDAD A LA BAJA

0 - 20 venta clara de PUTS
20 - 40 venta de PUTS con algo de riesgo
40 - 60 abstenerse de operar, ni comprando ni vendiendo volatilidad
60 - 80 compra de PUTS con algo de riesgo
80 - 100 compra clara de PUTS o incluso venta directa del subyacente a crédito o a futuro.

El rango de los indicadores se obtendrá de comparar el movimiento porcentual total de un periodo determinado con el movimiento porcentual total en cada una de las dos direcciones durante el mismo periodo.

De esta forma sabremos cuando una de las dos direcciones es mayor o menor y en que grado es superior o inferior a la volatilidad total. Caso de que se considere interesante esta propuesta se podrá debatir con mayor profundidad.

Artículos relacionados

Comprar o vender volatilidad (1)

Comprar o vender volatilidad (2)

Comprar o vender volatilidad (3)

Comprar o vender volatilidad: sistemas para la Ruleta
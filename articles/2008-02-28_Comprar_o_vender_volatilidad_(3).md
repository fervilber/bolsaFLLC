---
title: "Comprar o vender volatilidad (3)"
date: 2008-02-28
source: https://www.rankia.com/blog/llinares/365030-comprar-vender-volatilidad-3
author: Francisco Llinares Coloma
blog: Rankia
---

# Comprar o vender volatilidad (3)

Antes de empezar aconsejo leer las dos partes anteriores sobre volatilidad:

Comprar o vender volatilidad (1)

Comprar o vender volatilidad (2)

En estas partes se habla de la venta de opciones sintéticas, o sea, de vender opciones sobre productos que no tienen derivados cotizando, incluso opciones sobre spreads que no existen en la realidad.

Para replicar opciones sintéticas se utiliza algo llamado "cobertura Delta Neutral", aplicando este sistema se consiguen cuatro estrategias diferentes con una fiabilidad altísima. Además, la equivalencia de las posiciones sintéticas comparada con lo que hubiera resultado de tener posiciones con opciones reales es idéntica. Estas son las cuatro posibilidades:

1 - Cubrir una cartera de opciones compradas.
2 - Cubrir una cartera de opciones vendidas.
3 - Replicar opciones compradas operando sólo con el subyacente.
4 - Replicar opciones vendidas operando sólo con el subyacente.

Todo ello se consigue con la simple acción continuada de poner el delta total de la cartera a cero comprando o vendiendo las cantidades adecuadas del subyacente.

Como aplicar con exactitud la cobertura delta neutral en tiempo real no está al alcance de todos. Se puede realizar una maqueta de foto fija de la citada cobertura para que pueda ser aplicada por cualquier persona que no disponga de los medios que tienen a su alcance los creadores de mercado. Los resultados no serán exactos, pero servirán para desarrollar una estrategia compleja con herramientas rudimentarias.

VENTA DE PUTS DE ERCROS O DE JAZZTEL

Como dijimos en el artículo anterior se pueden vender puts de ERCROS a pesar de que no existen, obteniendo los mismos resultados que si se hiciera con opciones reales.

Vamos a hacer una venta escalonada de puts, pensando que a la baja le queda poco recorrido y con el tiempo ganaremos las primas de la venta de los PUTS.

Antes de empezar hago la advertencia de que este ejemplo no es una recomendación de hacer esta operación. Hay que tener en cuenta que estas empresas pueden dejar de cotizar en cualquier momento y se afrontaría una pérdida del 100%. Antes de vender puts se deben de tener en cuenta las posibilidades de que el subyacente suba, baje o quiebre.

Se empieza comprando un número determinado de acciones a un precio que se considera cerca de un suelo. A partir de ese momento pueden pasar dos cosas: que suba un 15% o que lo baje.

Si sube el 15% se vende y se considera que el beneficio es debido a la prima cobrada por vender puts. Si vuelve a bajar al precio anterior se vuelve a comprar para cuando suba volver a vender. Esta operación se repite tantas veces como se pueda y cada vez se va cobrando la prima del put.

Si baja un 15% se hace otra compra de igual tamaño y cuando suba se vende. Esto se repite indefinidamente.

De esta manera, cada movimiento del subyacente de un 15%, producirá un ingreso de igual cantidad, muy parecido a la venta de puts, que producirían ingresos periódicos por el cobro de las primas.

Como se puede ver, los resultados serán muy parecidos a tener puts vendidos: Si baja mucho y sin rebotes se tendrán pérdidas fuertes, y si se congestiona o sube se obtendrá limpio el ingreso de las primas.

Venta de PUTS de algo que no existe y por lo tanto no puede quebrar.

Este me gusta más, porque se vende volatilidad con un riesgo mucho más controlado. La operativa es un poco más embrollada, pero a cambio se obtiene un ingreso por venta de volatilidad con un riesgo proporcionalmente pequeño a los ingresos.

Vamos a vender volatilidad del Gráfico Compuesto SAN vs BBVA

Si miramos el gráfico del spread vemos que entre el 0 y el 2 se vende casi todo el pescado. Para vender la volatilidad de estos movimientos como si vendiéramos puts, y teniendo en cuenta que ni cotizan puts sobre el spread, ni tan siquiera cotiza el subyacente de ese gráfico, haremos lo siguiente:
Cuando el spread baje hasta 5 euros compraremos 3 SAN y venderemos 2 BBVA, a 3 euros haremos lo mismo, y repetiremos la operación a 1 euro. Cada vez que por cada lote se ganen 2 euros se desharán las dos posiciones de ese lote con la consiguiente ganancia. Se continuará la estrategia durante toda la vida del vendedor de puts (estrategia a largo plazo, para que digan que en AT siempre vamos a corto).

Cada vez que el spread se sitúe por encima de 7 euros no se tendrá ninguna posición. A partir de 9 euros se podría empezar la venta de CALLS, esto es: Venta de 3 SAN y compra de 2 BBVA, se vende otro lote a 11 y se van deshaciendo cuando baja dos euros para llegar a 7 euros sin ningún lote en cartera, ni comprado ni vendido.

Tener en cuenta que todas estas operaciones se pueden hacer sin desembolsar la mayor parte del dinero, y sin tener que pagar intereses por el dinero no desembolsado. Y por supuesto, descorrelacionadas de la tendencia del mercado.

Próximo estreno: Comprar o vender volatilidad en la Ruleta
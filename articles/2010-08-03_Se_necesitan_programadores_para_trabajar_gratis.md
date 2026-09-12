---
title: "Se necesitan programadores para trabajar gratis"
date: 2010-08-03
source: https://www.rankia.com/blog/llinares/533513-necesitan-programadores-para-trabajar-gratis
author: Francisco Llinares Coloma
blog: Rankia
---

# Se necesitan programadores para trabajar gratis

Se requiere buena presencia y espíritu de sacrificio.


Se ofrece la posibilidad de ahorrarse el dinero que no se gastarán en juergas mientras estén trabajando gratis.





RESUMEN DE LOS ACONTECIMIENTOS


Uno de los lectores de este blog, AX0X0, me ha mandado un trabajo que ha desarrollado sobre la curva de intereses del dólar. Ha hecho una estadística de cómo se comportan los spreads de GE en los últimos 6 meses antes del vencimiento.


Hemos estado comentando el tema y me pareció interesante, pues yo nunca había estudiado ese tramo debido a que, durante ese plazo de la curva, los intereses están en manos del capitoste que corta el bacalao en la Reserva Federal. Por supuesto, unido a los amos del mundo por un cordón umbilical de cáñamo.


El estudio que ha hecho AX0X0 demuestra que ese tramo de la curva no es tan aleatorio como se pudiera suponer y que hay sesgos aprovechables.


Al hablar de todo esto, vimos que es posible que haya otros tramos de la curva que presenten algo parecido. Y la única manera de saberlo es currándose la curva en tramos de 3 meses.


Como desde que faltan unos 3 años hasta que falta un año y medio la cosa está bastante clara (hay que estar comprados del spread), ahora falta averiguar con detalle los pormenores del último año y medio. Aquí es donde entra la petición de programadores, pues AX0X0 se ha pegado la paliza de hacer la Excel que se adjunta casi toda a mano.


La idea es hacer casi el mismo trabajo que ha hecho AX0X0, pero en periodos de tres meses desde un año y medio antes de vencer hasta los últimos tres meses. Los interesados en colaborar pueden proponerse en los comentarios y ya quedaremos para concretar los detalles.


El estudio de la curva de intereses puede ser sólo el primer paso de un proyecto más amplio. Siempre que haya voluntarios, se puede hacer algo parecido, pero con diferentes objetivos sobre otros productos.





DESCRIPCIÓN DE LA EXCEL QUE HA HECHO AX0X0


La idea es ver cómo evolucionan los futuros sobre los tipos de interés del dólar (GE). En este caso estudio cómo evoluciona el diferencial entre dos contratos entre los que hay un año. Me explico: edz83 - edz84 o edm97 contra edm98. Es decir, hago el spread entre diciembres, marzos, septiembres y junios consecutivos (dic contra dic, marzo contra marzo, junio contra junio, septiembre contra septiembre) y miro cómo se comporta este spread cuando queda menos de medio año para su vencimiento.


Esto empezó porque, al ver gráficos, veía que el spread de diciembre, cuando le quedaba menos de medio año, tendía a caer (la estadística se hace con el contrato cercano menos el lejano). He decidido graficar todos estos spreads desde el 83 (que es hasta donde llega la base de datos de mfgloblalfutures) y pasar esa información a una Excel. El procedimiento es sacar el gráfico y visualmente ver la apertura, el máximo, mínimo y cierre del spread. Esto se hace  cuando le quedan 6 meses de vida al contrato que vence antes. El proceso para sacar los datos no es muy fiable y puede que no sean del todo exactos. La idea no es saber la información exactamente sino ver si existe un sesgo en estos spreads.


En la Excel he puesto toda esta información y en estas líneas voy a intentar explicarlo brevemente.


En la columna A muestro si el contrato es D (DICIEMBRE), M (MARZO), J (JUNIO), S (SEPTIEMBRE).




En las columnas B y C están los años de los contratos. Siempre compramos el cercano y vendemos el lejano.




De las columnas D a la G están la apertura (en el periodo), máximo, mínimo y cierre.




En la columna H está la diferencia entre el cierre y la apertura (apertura-cierre).




En la columna I están aquellos casos que, independientemente del vencimiento de los contratos, el resultado es positivo, es decir, vendes el spread y a vencimiento lo compras más barato. Si es 1, el resultado ha sido >0 y viceversa.




En la columna J están los casos en que el resultado es negativo. Si es 1, el resultado ha sido < 0 y viceversa.




En la columna K están los resultados que han sido positivos y en la columna L están los casos negativos.




La fila 3 de las columnas  I, J, K y L nos muestra el sumatorio de sus respectivas columnas y por lo tanto: el total de casos positivo, el total de casos negativos, el total que se gana en las operaciones positivas y el total que se pierde con las operaciones negativas.




En la fila 2 y en las mismas columnas (I, J, K y L) se saca la probabilidad de aciertos (I2= I2/(I3+J3)), la probabilidad de fallos (J2= 1-H2), el ratio b/P (K2=K3/ABS(L3)) y el retorno medio (L2=I2*k3+j2*L3).


En la H3 está el resultado total de la estrategia para cualquier vencimiento.


En las columnas H a la L incluidas se muestra la información de la estrategia para los vtos de diciembre, marzo, junio y septiembre. Si queremos ver el resultado de la estrategia para cada uno de estos vencimientos, la podemos ver en las siguientes columnas.




En las columnas N a R están los resultados de los vtos de diciembre.

En las columnas T a X están los resultados de los vtos de marzo.

En las columnas Z a AD están los resultados de los vtos de junio.

En las columnas AF a AJ están los resultados de los vtos de septiembre.


Después de todos los datos, la estrategia (vender el spread), donde mejor funciona es con los contratos de diciembre, donde tiene una tasa de acierto del 70% y por cada USD perdido se ganan 4,5.





Aquí se puede descargar la Excel
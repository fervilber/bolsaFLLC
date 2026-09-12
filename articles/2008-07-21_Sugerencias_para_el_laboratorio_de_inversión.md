---
title: "Sugerencias para el laboratorio de inversión"
date: 2008-07-21
source: https://www.rankia.com/blog/llinares/365131-sugerencias-para-laboratorio-inversion
author: Francisco Llinares Coloma
blog: Rankia
---

# Sugerencias para el laboratorio de inversión

Propongo hacer un millar de gráficos de las opciones del Eurostoxx 50. Esta recomendación se basa en los siguientes motivos:

1 – Es el índice de referencia en Europa.

2 – Cotizan opciones desde una semana de duración que vencen cada viernes hasta los 10 años, cosa que no ocurre con los índices de Estados Unidos.

3 – Son las opciones con mayor liquidez y con la horquilla más cerrada de Europa.

4 – Tener estos gráficos es la única forma de poder comprobar estrategias de compra o venta de volatilidad, calendario spread, etc.

Los datos se deben coger cada día después de cerrar la sesión y antes de la mañana siguiente.
Como dato de cierre hay que poner el Daily Settlem. Price , que es el precio teórico de la prima al precio de cierre del índice aunque esa opción no haya cotizado.

Se deberían hacer los diez años sólo tomando los diciembres, con precios de ejercicio cada 200 puntos.

Por ejemplo:
Z9P3200.E50 Correspondería a diciembre del 2009 put 3200, cuando venza el 2009, en el mismo archivo y sin cambiarle el nombre se añadirá diciembre del 2019. Así no hay que tener abiertos miles de archivos y se tienen todos los diciembres acabados en 9.

Otro ejemplo:
Z8C3400.E50 = Call 3400 de diciembre del 2008, que después de vencido corresponderá a diciembre del 2018.

Se podrían tomar los strikes desde 1000 hasta 6000, que cada 200 puntos representan unos 50 gráficos por cada año y unos 500 en total.

DATOS DE LOS PRIMEROS 12 MESES

Aparte se podrían hacer los gráficos de los primeros 12 meses, mes a mes, con strikes cada 100 puntos que vayan de 2.000 a 5.000.

Ejemplo:
QQC3000.E50 = El call 3000 del primer agosto no vencido, cuando vence, el mismo fichero pasa al agosto siguiente.

Otro ejemplo:
HHP2800.E50 = El put 2800 del primer marzo.

De esta manera tendremos siempre un millar de gráficos a los que no habrá que estar cambiándoles el nombre.

DATOS DE CADA AÑO ATM

Luego se podrían hacer unos pocos gráficos especiales que arrojarían mucha luz y que es imposible conseguir en ningún lado:

Un gráfico por cada año (diez en total) que represente el precio de cada día de una opción teórica que tuviera un precio de ejercicio exactamente igual al cierre del índice. De esta forma se descartan los movimientos de la prima debido a las variaciones del subyacente, y nos quedamos con la parte de la prima que corresponde al tiempo restante hasta el vencimiento y la volatilidad.

Ejemplos:
ATM8.E50 = At The Money diciembre del 2008.ATM9.E50 = At The Money diciembre del 2009. Etc.

Estos diez gráficos se confeccionarían de la forma siguiente:

Cada día se toma el precio de cierre del índice, y para calcular cada año se coge el precio de las cuatro opciones (dos put y dos call) de ese mismo año cuyo precio de ejercicio esté justo por encima y por debajo del precio de cierre del índice. Se suman las cuatro primas y se dividen por cuatro, de esa manera conseguimos el precio de una opción At The Money de ese vencimiento.

VOLATILIDAD EN DIFERENTES PLAZOS

Aparte se podrían hacer tres gráficos más:

1 – Uno que represente la prima de una opción At The Money a la que cada día le faltan seis meses para su vencimiento. Con el paso del tiempo, se mantiene la constante de que siempre le queden seis meses de vida útil.
ATM6M.E50

2 – Uno igual que el anterior, pero la constante de vida útil se establece en dos años.
ATM2A.E50

3 – Otro igual al que siempre le faltan cinco años de vida
ATM5A.E50

En estos tres gráficos hemos eliminado el paso del tiempo y los movimientos del subyacente, por tanto, sólo nos queda el precio de la prima debido a los cambios de volatilidad de cada uno de los plazos indicados.

Estos tres gráficos se calcularán con una regla de tres en base al tiempo transcurrido entre el vencimiento anterior a cada uno de los tres plazos y el posterior.

En el de 2 y 5 años se coge el ATM?.E50 del vencimiento anterior y posterior.

Ejemplo:
En este momento para el de dos años se cogerían el ATM9.E50 que le falta un año y pico y el ATM0.E50 que le restan dos años y cinco meses de vida.

Imaginemos que estamos en el día 200 de los 365 días del año, y que las primas de los vencimientos ATM9.E50 y el ATM0.E50 son de 200 y 250 respectivamente. La diferencia de 50 entre el precio de los dos corresponde a 365 días, por tanto, para el periodo de 200 días corresponderá la cantidad de 27.40 puntos, que sumados a los 200 de diciembre del 2009 nos dará una prima de 227.40 para el ATM2A.E50

Para el de cinco años tomaríamos el ATM2.E50 y el ATM3.E50. Haciendo las mismas operaciones que en el párrafo anterior.

Para el caso del de seis meses perpetuo, el ATM6M.E50, se sumarían los 2 put y call del vencimiento anterior y posterior a los seis meses de vida, se dividirían por cuatro para sacar el precio ATM de cada mes, y luego se haría la regla de tres como en los casos anteriores, pero tomando los días trascurridos del mes en vez del año.

Todo esto puede parecer complejo y enrevesado, pero os garantizo que es muy útil.

Además se haría otro gráfico con el dato de la volatilidad a un mes que sale aquí

Conocer la volatilidad de cada plazo en cada momento es indispensable a la hora de usar una estrategia de calendario spread para aprovechar la desigual curva de caída de la prima por el paso del tiempo. El calendario spread compra volatilidad de un plazo determinado y la vende de otro, sería absurdo operar desconociendo si la volatilidad de cada plazo es favorable a nuestros intereses.

Artículos relacionados

Proyecto interesante de Dalamar

Comprar o vender volatilidad (1)

Comprar o vender volatilidad (2)

Comprar o vender volatilidad (3)

Comprar o vender volatilidad: sistemas para la Ruleta

Comprar o vender volatilidad (5)
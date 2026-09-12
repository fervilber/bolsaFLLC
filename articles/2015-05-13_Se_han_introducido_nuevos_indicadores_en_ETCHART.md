---
title: "Se han introducido nuevos indicadores en ETCHART"
date: 2015-05-13
source: https://www.rankia.com/blog/llinares/2786150-introducido-nuevos-indicadores-etchart
author: Francisco Llinares Coloma
blog: Rankia
---

# Se han introducido nuevos indicadores en ETCHART

Hace medio año intenté explicar los fundamentos de los diferenciales entre dos contratos de futuros.  El efecto acordeón en los diferenciales entre dos contratos de futuros. Entonces ya dije que, para reconocer el momento de comprar crudo, habría que vigilar el diferencial. El problema es que, a medida que va pasando el tiempo, el diferencial se mide con diferentes vencimientos, lo cual produce una distorsión.


Para evitar la distorsión que produce el cambio de vencimiento, además del futuro perpetuo, he introducido otro perpetuo que se confecciona con el vencimiento que cotiza seis meses después del primero. De esta manera siempre tenemos los precios del primer vencimiento y el de seis meses después. Luego, sólo tenemos que hacer un gráfico de la diferencia entre el perpetuo del primero y el del séptimo para poder medir si el diferencial está en backwards o en contango, y si va aumentando o disminuyendo ese diferencial.


El archivo del crudo perpetuo +6 meses se llama "CLPERP6.NYM".


Aquí se puede ver el gráfico de la diferencia entre el perpetuo del primer mes y el perpetuo +6 del crudo.








Cuanto más abajo llega el diferencial, más alta es la probabilidad de un rebote en el precio del crudo.





PERPETUO +6 DEL ORO


También hemos hecho otro perpetuo +6 del oro. El archivo se llama "GCPERP6.CMX".


En este caso, lo que se trata de saber es la disponibilidad de oro físico para entrega inmediata. El diferencial normal en el oro es el contango, pero cuando hay escasez de oro para entrega inmediata, se paga más por el oro al contado que por el que se entregará en el futuro.


Pongo el gráfico del diferencial del oro





Cuanto más arriba está el diferencial, más escasez de oro físico para entrega inmediata.


Al actualizar el programa ETCHART se colocarán automáticamente en la base de datos los nuevos perpetuos que hemos confeccionado con efecto retroactivo para poder analizarlos. También se ha puesto una nueva lista en la carpeta "listas", que se llama PERPETUOS6.lig, en la que se pueden ver los cuatro perpetuos implicados y el spread de los diferenciales.


Para los que quieran iniciarse en el programa de gráficos ETCHART, aquí pueden ver los vídeos con las instrucciones de manejo. Actualización de la base de datos del Egregore en el programa ETCHART.
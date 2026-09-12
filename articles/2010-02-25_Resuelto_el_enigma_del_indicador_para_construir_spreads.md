---
title: "Resuelto el enigma del indicador para construir spreads"
date: 2010-02-25
source: https://www.rankia.com/blog/llinares/411398-resuelto-enigma-indicador-para-construir-spreads
author: Francisco Llinares Coloma
blog: Rankia
---

# Resuelto el enigma del indicador para construir spreads

Gracias a la persistencia de Nerua (al que propondré para presidir el consejo de administración de la futura sicav en la que se aglutinarán las pensiones de una docena de personas), nos hemos enterado de las turbias razones que producían fallos en el indicador para confeccionar spreads.


A pesar de que a él le funcionaba bien el indicador, se puso a investigar lupa en mano las huellas del asesino de spreads en estado de gestación.


Éstas son las conclusiones de sus pesquisas:


Intrigado porque a otras personas el Visual Chart 5 no les permitía confeccionar los spreads con el indicador "llinares", mientras que otras lo hacíamos sin problema; le he dedicado unas 1.999 horas a averiguarlo. He encontrado una causa. Tal vez no sea la única, pero ésta sí lo impide y es algo muy común.


Resulta que si en el VCH5 tenemos una plantilla por defecto para todos los gráficos que queremos abrir (para que siempre salgan velas de colores, escala logarítmica, etc. etc.), el indicador no funciona. Ni siquiera pone a los dos (o más) gráficos en condiciones de aplicarle el indicador. El gráfico siguiente machaca al gráfico anterior y es imposible aplicar el indicador.


Para resolver este problema, se debe pinchar en el globito de arriba a la izquierda donde sale el logo de VCH5 (uffff*). Ahí seleccionar "Configuración", luego "Gráficos", y en esa pantalla DES-TILDAR la opción "Aplicar plantilla al abrir gráficos". A partir de ahí, todo perfecto.


Ojo, una vez hecho lo anterior, cuando vayan a realizar el spread y aplicar el indicador llinares, no rescaten los gráficos que ya tienen guardados previos a la modificación del parámetro descrita, porque esos gráficos todavía vienen con plantilla y les va a aparecer el viejo problema. Tienen que construir los gráficos de nuevo, no utilizar los guardados.


Obviamente en los demás gráficos que queremos ver con nuestra plantilla favorita, ésta habrá que meterla manualmente. Es sencillo: botón derecho sobre las velas del gráfico, pinchar la plantilla que se quiera y listo.


Espero que se le resuelva el problema a algunos que protestaban por este asunto.




Cuando dice 1.999 horas, estoy seguro de que han sido 2.000, pero seguro que pone un número terminado en 99 para que le entre más fácilmente la orden de venta.





Aquí está el indicador para los que todavía no lo tienen:





DESCARGA E INSTALACIÓN DE LA HERRAMIENTA


Pulsar en el siguiente enlace y guardar el archivo descomprimido en C:\Archivos de programa\vChart\Documents\Vba\Indicators





LLINARES.VBA.zip





Una vez guardado el archivo, para instalar el sistema hay que elegir la opción Modificar Indicador del menú Indicadores, seleccionamos el archivo descomprimido que contiene el sistema llamado Llinares.vba y lo abrimos (a los que les dé alergia mi apellido pueden cambiarle el nombre al archivo, seguirá funcionando igual). Para compilarlo hay que ir al menú Debug y seleccionar la opción Publish.





Para confeccionar el gráfico de un spread hay que introducir en la misma hoja los gráficos implicados en el spread, y luego insertar indicador.





Los parámetros que lleva el indicador son los factores (Factor1 para el primer gráfico hasta Factor5) por los que se multiplica el precio de cada uno de los gráfico que se utilizan para calcular el spread. Cuando el valor de uno de los parámetros factor vale cero, permanece desactivado.





Si se va a realizar el spread solo con dos gráficos, los parámetros Factor3, Factor4 y Factor5 se ponen a valor cero. Por ejemplo para hacer el siguiente spread: - Se inserta primero el gráfico del Mini SP500. - Después el del SPXU. - Por último, se inserta el indicador poniendo los siguientes parámetros:





Price Source = Data1


Factor1 = 50

Factor2 = 500

Factor3 = 0

Factor4 = 0

Factor5 = 0





Artículos relacionados








¡Que buenos son los ETFs!, vendidos, claro
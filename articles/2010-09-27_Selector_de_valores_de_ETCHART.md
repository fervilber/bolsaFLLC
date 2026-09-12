---
title: "Selector de valores de ETCHART"
date: 2010-09-27
source: https://www.rankia.com/blog/llinares/565153-selector-valores-etchart
author: Francisco Llinares Coloma
blog: Rankia
---

# Selector de valores de ETCHART

Acabamos de poner en marcha el selector de valores más exigente de la galaxia.


Para ser un ventajista profesional, lo primero que hay que agenciarse es una herramienta potente para quitar las capas de basura y descubrir el diamante en bruto que nos está esperando para poder operar con grandes ventajas.


Un analista técnico se conforma con la ventaja que le ofrece operar a favor de la tendencia o la rotura de alguna figura. Un ventajista se preocupa de colocar a su favor varias ventajas diferentes que se puedan acumular en una sola operación. Como es natural, para conseguir eso necesitará mirar 20.000 gráficos.


Un buen ventajista tiene dos opciones: emplear a 50 empleados que trabajen para él o utilizar el selector de valores de ETCHART.





INSTRUCCIONES DEL SELECTOR


Comandos del selector


//  Las dos barras permiten poner anotaciones de texto


* = multiplicar


/ = dividir


! = operando not


|| (alt grande 1) = or


&& =and: añadir una condición además de la anterior


>< = mayor menor que


if (X >1)  {lo que se quiera } Ejecuta si cumple una condición.





Letras que definen el tipo de dato:


C=Cierre


A=Apertura


MX=Máximo


MN=Mínimo


V=Volumen


Se pone la letra adecuada para el dato que se quiera manejar y entre paréntesis el número de sesión: última =(0), hace un mes =(20), hace un año = (250), etc.





ALGUNOS EJEMPLOS


Empecemos por algo facilito y luego lo vamos complicando.


Vamos a buscar los valores que en el último año han subido más del 300% en el mercado NYSE.


El texto de los archivos está en azul y se tiene que guardar en la carpeta selector con la extensión   .SEL





0,--CODE


return (C(0) / C(250)) >3;


0,--END CODE


2,NYS





Selecciona los “basuritos” que han bajado más del 95% en la última sesión.


0,--CODE


return (C(0) / C(1)) <0.05;


0,--END CODE


2,PNK





Escoge valores que en el último día han dibujado una vela que entre la apertura y el cierre hay más de un 5% en dos mercados.  Para que entren tanto las velas al alza como a la baja se pone el comando “or”.


Se puede ver que ponemos el nombre de la carpeta en ETCHART de dos mercados. Se pueden poner los que se quieran, los repasa todos. Lógicamente, si se ponen muchos valores, tarda más tiempo en sacar la lista.


0,--CODE


return (A(0) / C(0)) >1.05 || (C(0) / A(0)) >1.05;


0,--END CODE


2,NYS


2,QQQ





Escoge valores que en el último día han dibujado una vela que entre la apertura y el cierre hay más de un 10% en dos mercados. Además, tiene que cumplir otra condición: que el volumen de la última sesión sea mayor del triple del volumen de hace 20 sesiones.


0,--CODE


return (A(0) / C(0)) >1.1 || (C(0) / A(0)) >1.1 && (V(0) / V(20)) >3;


0,--END CODE


2,NYS


2,QQQ





Ahora un poco más complicado, para que veáis que el límite es vuestra imaginación.


Después de subir el 50% como mínimo en el último año (250 sesiones), busca una vela fuerte a la baja con un 5% entre apertura y cierre, producida en cualquiera de las últimas 5 sesiones. Además, calcula que el volumen del día sea mayor del 300% de la media del volumen de los últimos 10 días.


Para que no se ralentice la búsqueda, utiliza el comando “IF”, que sólo calcula la media del volumen en el caso que haya pasado el filtro anterior.


0,--CODE


function calcular(sesAtr) {


resultadoParcial = (C(1+sesAtr) / C(250+sesAtr)) > 1.5 && (A(0+sesAtr) / C(0+sesAtr) >= 1.05);


// Lo siguiente calcula la media del volumen sólo en el caso que haya pasado el filtro anterior. Esto se hace para que no se ralentice la búsqueda.


if (resultadoParcial) {


var mediaVolumen = 0;


for (i = 0; i < 10; ++i) {


mediaVolumen = mediaVolumen + V(i+sesAtr);


}


mediaVolumen = mediaVolumen / 10;


return resultadoParcial && (V(0+sesAtr) > mediaVolumen*3);


} else {


return false;


}


}


// llama a la función 'calculo' con 0, 1, 2, 3, 4 y 5 sesiones atrasadas


for (sesionesAtrasar = 0; sesionesAtrasar < 5; ++sesionesAtrasar) {


if(calcular(sesionesAtrasar)) {


return true;


}


}


return false;


0,--END CODE


2,NYS


2,QQQ


Tanto a los que les falta el selector como a los que quieren descargar el software y la base de datos completa, lo pueden descargar aquí:


Descarga del selector de valores de ETCHART
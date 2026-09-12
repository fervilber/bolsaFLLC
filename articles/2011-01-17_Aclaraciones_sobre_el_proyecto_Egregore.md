---
title: "Aclaraciones sobre el proyecto Egregore"
date: 2011-01-17
source: https://www.rankia.com/blog/llinares/652418-aclaraciones-proyecto-egregore
author: Francisco Llinares Coloma
blog: Rankia
---

# Aclaraciones sobre el proyecto Egregore

Antes de hablar del tema de hoy quiero recordar que el miercoles 19 a las 18:30 haremos un coloquio en la sala virtual para todos los principiantes de la ONG del trigo menos maíz. Se empezará pronto para poder ver el trigo-maíz en horario de mercado.


El miércoles por la tarde a las 18:15 pondré el enlace para entrar a la sala en el post de ese día.


PROYECTO EGREGORE


Para que todos los interesados y programadores puedan saber con exactitud qué funciones va a hacer ETCHART con el proyecto Egregore, lo voy a explicar en este post. De esa forma no se duplicaran trabajos y los voluntarios podrán programar cosas que no estén incluidas en lo que podrá hacer ETCHART.


Para simplificar las cosas de cara a los usuarios, empezaremos poniendo comprimida la base de datos descargada con los exprimidores para poder descargarla directamente. Así, los que sólo vayan a ser usuarios estándar,  no tendrán que aprender el manejo de los exprimidores.


Esto será posible porque, como veremos luego, ETCHART podrá seguir los spreads a partir del uno de enero del 2011 con los archivos de la base de datos de ETCHART que se actualiza a diario. De esa forma, con descargar la gran base de datos una sola vez será suficiente. A partir del siguiente año, se pondrán para descargar todos los vencimientos que se han actualizado durante el 2011, para que la descarga anual sea ligera.


¿Qué se podrá hacer con ETCHART y la base de datos del proyecto Egregore?


Será muy parecido a los selectores o las tablas: se hará un archivo de configuración en formato de texto que le dirá todo lo que tiene que hacer.


1 – En este archivo se indicará el número de productos o valores implicados y el año de comienzo del estudio.


2 – Por cada valor se hará una línea de texto que contenga: numero de valor, producto, multiplicador, vencimiento*, año vigente o siguiente**, dato a tratar (último, mínimo, volumen, etc.), días atrás como en las tablas, nombre en Etchart a partir del 1-1-2011 para hacer el spread o el perpetuo actualizado al día sin tener que volver a descargar la base de datos con el exprimidor.


* En vencimiento se podrá poner un contrato concreto, un perpetuo con el más cercano al vencimiento, el continuo del mismo mes de cada año o alguna cosa más que se nos ocurrirá.


** Se pondrá año=1 cuando todos los vencimientos a calcular sean del mismo año y 2 para el año siguiente al que está calculando. Con esto se evitará el problema de que, cuando se quiere calcular diciembre menos junio del mismo año, acabe calculando diciembre menos junio del año siguiente, como ocurre ahora con algunos perpetuos.


3 – Luego se pondrá la fórmula si la hay.


4 – Los resultados podrán salir en formato de archivo por cada vencimiento y año, que será guardado con el nombre que se elija en una carpeta de la base de datos con el mismo nombre elegido. Este archivo se podrá volver a procesar como cualquier otro archivo de la base de datos. De esta forma se podrán encadenar estudios hasta el infinito.


5 – Se podrá pedir si representa los resultados en un gráfico o sólo en archivo de texto. Los gráficos se podrán ver año a año pulsando “intro” para pasar al siguiente o poner 10 superpuestos, uno por cada año de cada década, siempre con los mismos 10 colores.


Para sugerencias utilizar los comentarios
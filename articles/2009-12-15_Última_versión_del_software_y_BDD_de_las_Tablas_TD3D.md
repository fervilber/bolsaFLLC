---
title: "Última versión del software y BDD de las Tablas TD3D"
date: 2009-12-15
source: https://www.rankia.com/blog/llinares/365083-ultima-version-software-bdd-tablas-td3d
author: Francisco Llinares Coloma
blog: Rankia
---

# Última versión del software y BDD de las Tablas TD3D

Ya está disponible la última versión del software y base de datos ampliada para las tablas en tres dimensiones TD3D


Se ha mejorado el software para que cuando calcula un spread de varios productos sincronice las fechas de todos los elementos implicados y evite datos erróneos. Descarta las fechas en las que no encuentra todos los componentes del spread.


Calcula las diferencias porcentuales entre cada día y la sesión anterior y lo presenta en la parte superior de la cuadricula. Esta diferencia se puede mostrar u ocultar a voluntad del usuario. En el fichero \ETCHART\CFG\TABLAS.TXT hay que poner un 1 en la última línea si se quiere presentar la diferencia porcentual y un cero para que no la muestre.


Se han añadido los derivados sobre los índices americanos MINI DOW JONES, MINI SP500 y MINI NASDAQ 100. Aquí se pueden ver los nombres de los componentes: Componentes de la base de datos: derivados sobre índices USA


Para evitar saltos en la actualización de los productos lo más recomendable es que cada usuario haga lo siguiente:


1 – Si ha configurado alguna tabla a su gusto debe guardarla en otra carpeta de su disco duro.


2 -Luego debe borrar toda la carpeta \ETCHART


3 – Descargar la nueva base de datos comprimida con la nueva versión de software y descomprimirla.


4 – Actualizar la nueva base de datos (se actualizará con los mercados que le falten)


5 – Añadir los archivos de configuración de tablas que había guardado.


A partir de ese momento ya tendrá disponibles todos los nuevos mercados que se han incluido y que se pueden consultar aquí. Se incluyen nuevas tablas con nuevas funcionalidades para aprovechar los nuevos mercados incluidos en la base de datos.










Tabla de todas las divisas valoradas en miligramos de oro




Lista de mercados que componen la base de datos:


Componentes de la base de datos: derivados sobre el Eurostoxx50




Componentes de la base de datos: derivados sobre energía


Componentes de la base de datos: futuros del ICE y el NYBOT


Componentes de la base de datos: derivados sobre el euribor


Componentes de la base de datos: tipos de interés del dólar


Componentes de la base de datos: bonos USA


Componentes de la base de datos: divisas


Componentes de la base de datos: derivados sobre divisas






Componentes de la base de datos: metales preciosos





Componentes de la base de datos: cacao, café y azúcar del LIFFE





Componentes de la base de datos: cereales y leguminosas




Componentes de la base de datos: acciones españolas






Componentes de la base de datos: acciones europeas





Componentes de la base de datos: acciones USA






Componentes de la base de datos: índices





Componentes de la base de datos: ETFs apalancados






Componentes de la base de datos: derivados del Eurex





Componentes de la base de datos: estructura temporal de volatilidad del Eurostoxx 50








El archivo comprimido es autoejecutable. Es indispensable que se ejecute para ser descomprimido en el directorio raíz de cualquier disco duro, pues la carpeta principal llamada ETCHART y que contiene todas las demás, debe colgar del raíz de cualquier unidad de disco.


Una vez descomprimida, ya se puede ejecutar el software de presentación de tablas y actualización de la base de datos que se encuentra en \ETCHART\SOFT\ETCHART.EXE


Las instrucciones para el manejo de las tablas TD3D y la confección de nuevos archivos de configuración se pueden consultar aquí Tablas de datos en tres dimensiones TD3D: Instrucciones de manejo














Todos los mercados están actualizados hasta el 15 de diciembre del 2009





Descargar BDD comprimida
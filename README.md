Reconocimiento de texto y análisis de información
=================================================

Plataforma y requisitos
-----------------------

Probado con Python 2.7.6 en Mac OS X 10.9.2. Se requieren dependencias
que no pertenecen a la librería estándar de Python.

Es necesario tener instalados los siguientes módulos:
* tesseract-ocr
* opencv
* numpy

Para instalar **tesseract**:

    $ sudo port install tesseract
    $ sudo port install tesseract-eng

Para instalar **opencv**:

    $ sudo port install opencv +python27

Para instalar **numpy**:

    $ sudo port install py27-numpy


Instalación y uso
-----------------

Descarga el repositorio desde el archivo **.zip**.

Ejecuta el script de python:

    $ python main.py <archivo_de_imagen>


Autor
-----

Creado por Ramón González.


Licencia
--------

Bajo *Licencia Apache Versión 2.0*.

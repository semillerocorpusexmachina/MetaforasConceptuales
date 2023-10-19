## Para hacer uso de los scripts Python se deben instalar las librerias
* pip install py-markdown-table

## Pasos para generar documentos y cargar a la Wiki

1. Una vez instaladas, se debe exportar la información a CSV, 1 archivo por cada fuente de datos.

2. Cuando se tenga la información en CSV, se deben ejecutar los scripts que contienen sufijo CSV en el orden de la numeración **1.GenerarEstructuraDominio.py** y así sucesivamente.

3. Generados los archivos JSON en el paso anterior, es momento de ejecutar los scripts que generan la estructura de documentos markdown para la Wiki (.md), los scripts son los que tienen prefijo Generar y se ejecutan según la numeración.
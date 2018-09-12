# evaluacion-final

1. Hacer scrapy de la página https://es.wikipedia.org/wiki/Prefectos_provinciales_del_Ecuador

Generar un archivo con los siguientes datos:

Nombre|Provincia|Partido|AnioInicio|AnioFin

2.- Ingresar a cada enlace de la columna predecesor

Ejm.
https://es.wikipedia.org/wiki/Anexo:Prefectos_de_Azuay

y agregar datos al primer archivo

Nombre|Provincia|Partido|AnioInicio|AnioFin

3.- Leer el csv final generado y presentar los prefectos en base a la provincia.
- Usar un widget de ipython

4.- Subir todo al repositorio

# instrucciones

colocarse en el directorio ~/spiders
ejecutar el comando "scrapy crawl examen -o final.csv" (genera un csv con el nombre de final.csv)
visualizacion del los ficheros en notebook

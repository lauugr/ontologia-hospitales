# Validación del grafo RDF mediante consultas SPARQL

Se ha realizado la validación del grafo RDF generado a partir del dataset mediante un conjunto de consultas SPARQL ejecutadas sobre el fichero `output-hospital.ttl` (ubicado en `/mappings/output`).

El grafo ha sido construido a partir de reglas RML y materializado con Morph-KGC en formato N-Triples. Posteriormente ha sido convertido a Turtle para facilitar su análisis.

Las consultas se han ejecutado utilizando la librería rdflib de Python con el objetivo de comprobar la calidad, consistencia y completitud de los datos.

# Resultados de la validación
```
Grafo cargado

================================================================================
QUERY 1 - Número total de hospitales
================================================================================
841

================================================================================
QUERY 2 - Hospitales sin nombre
================================================================================
Sin resultados

================================================================================
QUERY 3 - Hospitales sin dirección
================================================================================
Sin resultados

================================================================================
QUERY 4 - Hospitales sin Código CCN
================================================================================
Sin resultados

================================================================================
QUERY 5 - numberOfBeds mal tipado
================================================================================
Sin resultados

================================================================================
QUERY 6 - teachingAccreditation mal tipado
================================================================================
Sin resultados

================================================================================
QUERY 7 - Direcciones sin código postal
================================================================================
Sin resultados

================================================================================
QUERY 8 - Direcciones incompletas
================================================================================
Sin resultados

================================================================================
QUERY 9 - Recursos territoriales sin label
================================================================================
Sin resultados

================================================================================
QUERY 10 - Jerarquía territorial incompleta
================================================================================
Sin resultados

================================================================================
QUERY 11 - ConcertAgreement sin tipo
================================================================================
Sin resultados

================================================================================
QUERY 12 - ConcertAgreement sin label
================================================================================
Sin resultados

================================================================================
QUERY 13 - Duplicados de CCN
================================================================================
Sin resultados
```

# Interpretación de resultados

La primera consulta indica que el grafo contiene 841 instancias de hospitales.

El resto de consultas no devuelve resultados, lo que indica que no se han detectado errores en los aspectos validados.

En consecuencia, el grafo RDF generado presenta un alto nivel de calidad y consistencia.
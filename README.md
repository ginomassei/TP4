A partir del listado de equipos actualizado del Trabajo Práctico anterior, 
se generó el archivo de texto paises.csv que se entrega en este enunciado (haga click aquí o en el nombre del archivo para descargarlo). 
El significado de cada columna en el archivo es el siguiente:

- Confederación (es un valor de 0 a 5 que representa lo siguiente 0: UEFA, 1: CONMEBOL, 2: CONCACAF, 3: CAF, 4: AFC, 5: OFC)
- Nombre del pais
- Puntos de ranking de ese pais
- Cantidad de campeonatos ganados por ese pais

A modo de ejemplo, entonces, la primera línea del archivo con los datos: 4, Afganistán, 1052, 0 significa:

Confederación: 4
Nombre: Afganistán
Puntos: 1052
Cantidad de campeonatos ganados: 0

A partir del archivo de texto paises.csv generar un vector de registros con el contenido del mismo. 
El vector debe generarse ordenado de manera descendente por puntos.

Luego implementar un menú de opciones que permita:

1. Mostrar el listado completo de países, incluyendo el nombre de la confederación según su codificación numérica.

2. Informar cuál es el país con mayor cantidad de campeonatos ganados. Si fueran varios, informar todos.

3. Determinar, para cada confederación, cuántos países ganaron algún campeonato.

4. Generar un nuevo vector conteniendo los países de una confederación X que se ingresa por teclado. Los registros no deben incluir el campo confederación. Ordenar el vector por puntaje descendente y guardarlo en un archivo binario con nombre “clasificacionX.dat” donde X es el código de confederación. Mostrar un mensaje que indique nombre del archivo y cantidad de registros que contiene.

5. Ingresar una confederación por teclado y buscar su archivo de clasificación (realizado en el ítem anterior). 
Si no existe, generar su archivo de clasificación. Si existe, mostrar su contenido.

6. Preparar el fixture del próximo mundial: debe ser una matriz donde cada columna representa un grupo (8 grupos), cada fila el número de integrante de un grupo (4 integrantes por grupo) y la componente guarda el nombre de un país.

    a. En primer lugar, ingresar por teclado el nombre del país organizador (validarlo). Este será cabeza de serie del grupo A, ocupando la fila 0.

    b. Luego, definir los restantes “cabeza de serie”: son los siete países con mayor puntaje (excluyendo al organizador si estuviera entre ellos). Ubicarlos en la fila 0 de los grupos B a H.

    c. Por último, completar los grupos con 3 países más, por sorteo de manera aleatoria entre los 28 mejores restantes. Validar que no se repitan los países dentro de la matriz.

    d. Una vez generado mostrar el fixture por pantalla.

7. Buscar en el fixture realizado en el ítem anterior un país cuyo nombre se ingresa por teclado. Si existe, indicar qué grupo le corresponde. Si no existe, informarlo. (Verificar que el fixture ya se encuentre generado, en caso contrario, informar que no se puede procesar la solicitud).
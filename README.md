# A01422345_A4.2
Actividad 4.2

Hubieron ciertas cosas que tuve que considerar distintas a las especificadas ya que habian varias cosas que no se especificaron o que se obtenian distintas:
P1. Compute Statistics
• P1.TC5 (Delimitadores inusuales): Habían números separados por comas (,) y puntos y coma (;) en lugar de solo espacios o saltos de línea (ej. 23,45 o 11;54). Se implementó una lógica de limpieza para separar estos valores y alcanzar el COUNT de 311 solicitado.
• P1.TC5 (Discrepancia en la Moda): Al limpiar los delimitadores del TC5, el número 11 obtuvo una frecuencia mayor a la esperada en la errata, resultando en una moda técnicamente correcta para los datos procesados, aunque diferente al solicitado en el documento.
• P1.TC7 (Datos no numéricos): Se eliminaron elementos no numéricos como "ABBA" y "ERROR" mediante bloques de excepción para asegurar que el programa continuara, sin mebargo el conteo final es de 12,769 ya que se omiten del conteo estos elementos.
• P1.General (Fórmulas Estadísticas): Se consideró el uso de Varianza y Desviación Estándar Poblacional (dividiendo entre N y no N−1) según las indicaciones adicionales sin embargo habian ligeras irregularidades en los resultados finales.
P2. Converter
• P2.TC4 (Datos Inválidos): Se implementó el manejo de errores para omitir cadenas como "ABC", "ERR" y "VAL", sin embargo esto cambia el count.


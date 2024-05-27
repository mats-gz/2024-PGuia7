
# 🪩 - Trabajo Practico Nº7

En este ejercicio, implementaremos un administrador de contexto utilizando contextlib para manejar la apertura y cierre de archivos de manera segura. La función gestionar_archivo se encargará de abrir un archivo en el modo especificado y asegurar que se cierre correctamente, incluso si ocurre una excepción durante su uso. 
Crearemos una función llamada escribir_archivo que abrirá un archivo en modo escritura y escribirá varias líneas de texto en él. Utilizaremos nuestro administrador de contexto gestionar_archivo para garantizar que el archivo se cierre correctamente después de escribir en él.
Utilizaremos otra función llamada leer_archivo que abrirá un archivo en modo lectura y imprimirá su contenido línea por línea. Nuestro administrador de contexto gestionar_archivo para garantizar que el archivo se cierre correctamente después de leerlo. Además, manejaremos posibles errores como archivos no encontrados utilizando try-except.

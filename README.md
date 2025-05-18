<h1>Proyecto de Criptografía</h1>
<h4>Grupo 16 Materia Comunicación de Datos</h6>

<p>Este proyecto implementa el descifrado de un codigo dado por el enunciado. El método se basa en el uso de tablas de caracteres y el algoritmo del inverso multiplicativo.</p>

<h3>Procedimientos</h3>

<ul>
  <li>Implementación del cálculo del inverso multiplicativo mediante el algoritmo extendido de Euclides.</li>
  <li>Creación tablas de caracteres para cifrado y descifrado.</li>
  <li>Funciones de cifrado y descifrado con soporte para múltiples alfabetos.</li>
  <li>Se utilizan los valores de <code>b</code> dados por el enunciado</li>    
  <li>Se realizan iteraciones con distintos valores de la semilla <code>a</code> (de 1 al valor del tamaño de la tabla) </li>
  <li>Verifica que los valores de la semilla <code>a</code> tengan inverso multiplicativo, en caso contrario lo notifica en forma de mensaje</li>
  <li>Verifica que puede realizarse la conversion correctamente con los valores dados por el ejercicio, en caso contrario muestra mensaje indicando el error </li>
  <li>Muestra el mensaje correctamente descifrado</li>   
  <li>Pruebas para verificar la correcta implementación del algoritmo.</li>
</ul>


<h3>Requisitos</h3>

Python 3.x

<h3>Instalación</h3>

No se requieren dependencias externas. Solo clona este repositorio o descarga los archivos del proyecto.

<h3>Funciones Principales</h3>

<ol>
  <li>
    <strong>inverso_multiplicativo(a, m)</strong><br>
    Calcula el inverso multiplicativo de <code>a</code> módulo <code>m</code> utilizando el algoritmo extendido de Euclides.
  </li>
  <li>
    <strong>crear_tabla1() y crear_tabla2()</strong><br>
    Genera la primera y segunda tabla de caracteres dada por el enunciado para el cifrado y descifrado de mensajes, la tercera no se utiliza porque algunos de los caracteres del mensaje no se encuentran en esta.
  </li>
  <li>
    <strong>crear_tabla_inversa(table)</strong><br>
    Crea una tabla inversa para permitir la rápida búsqueda de valores en el proceso de cifrado y descifrado.
  </li>
  <li>
    <strong>encrypt(text, a, b, m, table, inv_table)</strong><br>
    Cifra un mensaje de texto utilizando los parámetros <code>a</code>, <code>b</code>, <code>m</code>, y las tablas de caracteres.
  </li>
  <li>
    <strong>decrypt(cipher, a_inv, b, m, table, inv_table)</strong><br>
    Descifra un mensaje cifrado usando las mismas tablas y parámetros.
  </li>
</ol>

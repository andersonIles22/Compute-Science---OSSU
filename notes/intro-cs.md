# MIT 6.0001 - Notas
# Intro to CS — MIT 6.0001

**Progreso general:** 2/12 lectures completadas

---

## 📌 LECTURE 1 - Introduction
**Estado:** ✅ Completada
**Fecha:** 02/04/2026

### Conceptos clave
- Tipos: int, float, str, bool
- Variable vs valor
- Conocimiento declarativo vs imperativo
- IDEs

### Finger Exercises
- [✓] FE 1.1 - Declarar y asignar variables
- [✓] FE 1.2 - Operaciones con valores
- [✓] FE 1.3 - Entender referencias

### 💡 Aprendizajes personales
- En JS usa `let` o `var`, en Python `=` directamente
- Las variables son referencias, no copias
- La mutabilidad es clave en ambos lenguajes


### Problem Set 1
**Estado:** Completado
**Problemas:** 1/1 completados
**Commits:** ps0.py


---

##  LECTURE 2 - String, In/Out, Branching
**Estado:** ✅ Completada
**Fecha:** 07/04/2026

### Conceptos clave
- input() y print() para in/out  
- Tipos: int, float, str, bool
- Operadores de comparación: ==, !=, <, >, <=, >=
- Operadores lógicos: and, or, not
- Ramificación
- Identación

### Finger Exercises
- [✓] FE 2.1 - Asignación de variables
- [✓] FE 2.2 - Comparaciones
- [✓] FE 2.3 - Ramificación

###  Aprendizajes personales
- '14' (string) != 14 (int) aunque se vean igual
- Indentación en Python es OBLIGATORIA (diferente a JS)
- Los operadores logicos (and, or y not) son diferentes a la sintaxis de JS (&&,||,!)
- f-strings es similar a usar las plantillas de cadena ``, que permite interpolar variables y expresiones directamente.

### Problem Set 2
**Estado:** ⏳ Pendiente
**Problemas:** 1/3 completados
**Commits:** ps1/ps1.py, ps1/ps2.py, ...
---
## Lecture 3 - Loops
**Estado:** ✅ Completada
**Fecha:** 09/04/2026

### Conceptos clave
- iteracción 
- While loops vs for loops
- función range()

### Finger Exercises
- [✓] FE 3.1 - While loop básico
- [✓] FE 3.2 - For loop con range

### Recitation Exercises
- [✓] Rec 3.1 - 4 ejercios resueltos (commit: `feat: rec3 - 4 exercises (string manipulation and loop)`)

### Aprendizajes personales
- En JS uso while/for igual, pero Python range() es más limpio

---
## Lecture 4 - Loops over Strings, binary
**Estado:** ✅ Completada
**Fecha:** 09/04/2026

### Conceptos clave
- break statement 
- strings and Loops
- loops nested
- float and binary numbers

### Finger Exercises
- [✓] FE 4.1 - for loop with range()
- [✓] FE 4s.2 - funtion abs() to keep the integer positive


### Aprendizajes personales
- Python prioriza la simplicidad sobre encapsulación por lo que al utilizar el ciclo for, la variable i u otra variable que se establezca existe fuera del loop, por lo que se puede usarlo.
- Un caso similar con JS que tambien no tiene block scope si y solo si no se declara la variable con let dado que si tiene block scope, si se declara con var o simplemente el nombre de la variable y el valor conviritiendo en una variable global o con scope superior, por lo que no tendrá blcok scope commo en python. Permitiendo usar el valor de la variable fuera de for, provando algunos bugs si no se tiene cuidado.
- Los puntos flotantes en python son usados para aproximar a numeros reales. Y se denominan puntos flotantes a la manera que estos numeros son almacenados. 
- Los puntos flotantes son el estandar para manegar los numeros racionales. Dado que los numeros racionales se conforman de un numeros enteros y numeros decimales, y estos decimales pueden ser infinitos y la memoria que puede almacenar es limitada. Se establecieron las UPF (Unidades de puntos flotantes), estos limitan hasta que unidad decimal aproximado se puede almacenar. 
- Es por eso que (0.3\*3)+0.2 no es igual a 1.1, debido a que el hardware que los procesa los interpreta como ((1/3)\*3)+(0.2) donde 1/3= 0.3333333... con infinitas decimales. 
- La representación de los puntos flotantes no dependen de la implementación del lenguaje de programación, sino del hardware informático.
- Todo se representa como secuencia de bits (0 o 1). Dado que es facil de implementar en la construcción de hardware, debido a sus estados ( 1 y 0).

---
## Lecture 5 - Floats and Approximation Methods
**Estado:** ✅ Completada
**Fecha:** 28/04/2026

### Conceptos clave
- while and for loops
- float and binary numbers

### Finger Exercises
- [✓] FE 5.1 - extract strings when the index is even. 


### Aprendizajes personales
- La conversión de numeros enteros de base 10 a binario se aplica un algoritmo basico que mendiate la división del cociente y la obtención del residuo se puede obtener el numero entero en binario.
- Los numeros fraccionarios al ser irracionales, con numeros infinitos en la parte decimal, se deben establecer limites para no superar la capacidad de almacenamiento. Este limite afecta a la precisión del valor real.
- La conversión de numeros fraccionarios a binarios es un poco complicada debido a que se debe tener en cuenta la limitación del almacenamiento y procesamiento del hardware. Para esto surge la estandarización IEEE 754 que dicta ciertos parametros para que estos numeros puedan ser almacenados en 32 y 64 bits.
- En el caso de 32 bits, toma en cuenta 1 bit para el signo, 8 bits para exponente y 23 bits para la precisión.
- Los puntos flotantes existen para optimizar el almacenamiento del numero sin perder presición total. 
- La estandarización establece que los puntos flotantes sean la representación de la conversión de numero fraccionario a binario. Como: 84,125=1.010100001*2^6. Donde el primer valor siempre es 1, el valor despues del punto decimal es la precisión real del número, y 6 es el exponente que establece si se movio a la derecha o a la izquierda hasta el primer 1 a la izquierda.
- Epsilon, un numero que se puede establecer dependiendo del margen de error que se desea obtener el calculo de la raíz de un valor. Con la finalidad de obtener un numero suficientemente bueno y proximo al valor real. Esto evita un procesamiento infinito y usar almacenamiento innecesario.

---
## Lecture 6 - Bisection Search
**Estado:** ✅ Completada
**Fecha:** 28/04/2026

### Conceptos clave
- while
- int and float numbers
- math.floor

### Finger Exercises
- [✓] FE 6.1 - write a piece of code to find N between 0 and 1000, and return the attemps and the number.
- [✓] FE 6.2 - Use bisection search


### Aprendizajes personales
- Evitar el tratar de buscar la respuesta exactaa todos los problemas, debido a que solo se puede encontrar un valor con cierto marge de error lo suficientemente bueno.
- La busqueda binaria es mas eficiente en cuando a la implementación de ciertos algoritmos para encontrar la raíz de un numero de manera aproximada.
- La busqueda binaria se basa en tomar un punto medio y preguntar si ese valor es menor o mayor al valor que se desea encontrar, y dependiendo de la respuesta descartar valores que no cumplen con la condición establecida. Para eso se debe utilizar ciclos que permitan iterar hasta encontrar el valor deseado.
- El implementar la busqueda binaria para resolver problemas con dos endpoints, cuando los valores estan ordenados si o si, y cuando existe fedback sobre las predicciones (muy alto, muy bajo, correcto, mal, etc.)
- La implemantación de metodos no es al azar, es debido a que escalan de forma logaritmica y no exponencial, esto permite ahorrar tiempo y recursos. Y ademas son eficientes aun cuando los valores son gigantes.

---
## Lecture 7 - Functions: decomposition, abstraction
**Estado:** ✅ Completada
**Fecha:** 12/05/2026

### Conceptos clave
- functions
- loops
- indentation

### Finger Exercises
- [✓] FE 7.1 - write the instructions to eval quadratic
- [✓] FE 7.2 - write the instructions to get the sum of two evaluation of quadractics

### Recitation Exercises
- [✓] Rec 7.1 - 3 de 4 ejercios resueltos (commit: `feat: rec7 - 3 exercises (function and algorithms of approximation)`)

### Aprendizajes personales
- Las funciones permite abstracción al establecer detalles que son las instrucciones de lo que la función hace y mediante la interfaz planteada puede ser utilizada en varias partes del codigo. 
- El establecer funciones permite la reutilización de codigo, permite mostrar al usuario solo que hace la función, más no como lo hace. 
- Las funciones retornan un resultado mediante los parámetros de entrada, aunque pueden no tener parametros. Todo esto mientras oculta la información detallada de la función al usuario. 
- Se puede establecer documentación a las funciones, esta documentación es como un contrato que dicta que tipos de valores de entradas puede recibir y que se espera como resultado al utilzar la función.
- Las funciones son objetos, al ser objetos ocupan espacio en memoria. Sin embargo estas funciones son utiles mientras son invocados o llamados, caso contrario solo ocupan espacio.
- Estas funciones una vez establecidos puede ser invocados desde cualquier parte del codigo y cuantas veces sean necesarias.
- El almacenar funciones en variables, permite almacenar lo que retorna la función más no en si lo que es la función. 

---
## Lecture 8 - Functions: environment, scope, function as object
**Estado:** ✅ Completada
**Fecha:** 19/05/2026

### Conceptos clave
- functions
- in
- loops

### Finger Exercises
- [✓] FE 8.1 - write a function that eval if str1 has the same characters that str2.


### Aprendizajes personales
- El uso de funciones en la mayoría de los casos retorna un valor. Este valor puede ser almacenado en una variable o puede ser presentado en consola mediante la función print(). 
- return es esclusivo de las funciones y son establecidas para retornar un valor por cada llamado de la función.
- Print() presenta en consola el resultado de las instrucciones de una función, pero este no puede ser almacenado. Mientrás que return retorna un valor que puede ser almacenado y utilizado en otras partes de codigo. 
- Si no se establece un valor a retornar de una función, al intentar visualizar el resultado será el valor None.
- Al establecer y llamar a una función se establece un entorno muy aparte del entorno global que tiene python. En el entorno de la función se puede declarar variables, realizar operaciones, condicionales, etc. Al ser diferentes entornos, la unica manera de que los dos entornos se intervenga es mendiante el uso de parametros como entrada de datos externos o cuando se retorna el resultado del llamado de la función.
- El scope de la función se limita solo a la función, es decir que si establece instrucciones o variables dentro del entorno de la función, esta solo es valida para este entorno. 
- Las funciones tambien son objetos como: los strings, enteros, flotantes, etc. Son objetos de primera clase, es decir que pueden ser utilizadas sin restricciones, por lo que pueden ser pasadas como parametros de otra función  sin necesidad de agregar los parentesis para evitar su ejecución inmediata, y ser tratadas como cualquier otro dato.
- Las funciones pueden retornar otras funciones.

---
## Lecture 9 - Functions: Lambda, tuples and lists
**Estado:**  Completado
**Fecha:** 21/07/2026

### Conceptos clave
- lambda functions
- tuples
- lists

### Finger Exercises
- [✓] FE 9.1 - write a function that receives two tuples as arguments, and return a tuple of 2 elements, the first is the length of one of the tuples, and the second is the sum of the pairwise products of tA and tB.

### Problem Set 1
**Estado:** Completado
**Problemas:** 2/2 completados
#### Parte A - Set helpers functions
- Objetivo: Establecer funciones que permirá complementar el funcionamiento del juego hangman
- Commit: `feat: ps3a - completed has_player_won, get_word_progress and get_available_letters functions`
#### Parte B - Finish Hangman Game
- Objetivo: Finalizar el juego de manera que al introducir entradas interactue de manera dinamica con las opciones elegidas por el usuario
- Commit: `feat: ps3b - completed hangman game - 14/14 tests passed - add check_is_vowel, get_number_unique_letters and get_letter_not_guessed funcion - reduced nested conditionals and code duplication`

### Recitation Exercises
- [✓] Rec 9.1 - 4 de 4 ejercios resueltos (commit: `feat: rec9 - 4 exercises (function lambda, loops and working with tuples and lists)`)

### Aprendizajes personales
- Las funciones lambda son una alternativas con limitaciones a las funciones estandars. Con la diferencia de que estas son anonimas y contiene una sola a expresión a evaluar para retornar un solo valor.
- Otro tipo de datos compuesto a parte del string, son las tuplas y listas. Ambas estructuras contiene elementos, se diferencia en que las tuplas son inmutables y la listas son mutables.
- Las tuplas al ser inmutables, al establecerse no puede ser modificadas. Puede ser establecidas con parentesis  o simplemente separadas con una coma dentro de una variable. Tiene dos metodos .count(n) para contar las veces que n aparece en la tupla e .index(n) para saber el indice de la primera aparación de n.
- Un caso util de las tuplas es cuando se desea introducir varios elementos como argumentos en una función, para que tome en cuenta muchos argumentos sin establecer una por una se usa un \* en el parametro. En vez de hacer fun(n,m,o,p) se utiliza \*, fun(\*args) donde al ejercutar la función fun(1,2,3,4) con el \* toma en cuenta a todos los valores introducidos. Pero se puede facilitar usando tuplas como argumento, en vez de hacer fun(1,2,3,4) que tiene cual parametros, se utiliza una tupla con los 4 parametros: fun((1,2,3,4)), así la función hace uso de los 4 parametros. 
- Las listas al ser mutables posee metodos que permiten su manipulación como acceder y modificar los datos. Un ejemplo de metodo es .append() para agregar un elemento a la lista. 
---

---
## Lecture 10 - List, Mutability
**Estado:**  Completo
**Fecha:** 04/08/2026

### Conceptos clave
- lists
- mutability
- loops
- strings

### Finger Exercises
- [✓] FE 10.1 - write a function that recieved an int and a list of function. Return True when all function of list return true, otherwise if one of the functions of list return false, Return false
### Recitation Exercises
- [✓] Rec 10.1 - 3 de 3 ejercios resueltos (commit: `feat: rec10 - 3 exercises (application of mutability in lists)`)
### Aprendizajes personales
- Las listas al ser mutables se pueden aplicar funciones y metodos.
- La notación (.)  de object.operation() permite ejecutar los metodos y funciones, usando un parametro que en algunos casos es opcional sobre los objetos mutables, que en este caso una lista.
- Los metodos y funciones mutan al objeto aplicado, por lo que el valor almacenado en memoria cambiará. Por lo que si se desea conservar el objeto original será necesario crear otra variable.
- Los objetos mutables alterados por metodos (in-place) modifican el objeto original por lo cual estos no podran ser almacenados en memoria dado que solo almacenará None, por otro lado los objetos alterados por funciones serán necesarios ser almacenados en una variable debido a que se crea una nueva referencia en memoria.
- En el caso de necesitar remover todos los elementos de una lista, esta deberá ser hecha mediante el metodo .clear(), asi la lista será vacía para todas sus referencias en caso de existir. O también es común usar del(keyword de python) y slice assignment del list[:]. No caer en el error de que al establecer sustitución el objeto original con una lista vacía basta. 
- La palabra clave /"del/", permite eliminar variable o referencia en memoria, en este caso al utilizar list[:], donde se puede establecer desde que indice y hasta que indice eliminar los elementos, o directamento con [:] seleccionar todos los elementos. 
---

## Lecture 11 Aliasing, Cloning
**Estado:**  Completado
**Fecha:** 06/08/2026

### Conceptos clave
- lists
- mutability
- alias
- cloning

### Finger Exercises
- [✓] FE 11.1 - Write a function that remove k elements of List, return the list sorted. If after remove elements and the lists is empty, the function shoul be return nothing. 
### Aprendizajes personales
- Las listas al ser mutables su manera de definir una copia cambian. Como se sabe el establecer una variable permite establecer un referencia entre el nombre y lo que apunta esto la memoria. Entonces al establecer una variable que apunta una lista, y luego establecer otra variable con el nombre de la variable anterior, estos dos apuntaran al mismo espacio en memoria. Permitiendo que dos variables apunten a la misma lista, y recibiendo el mismo cambio a lo que apuntan. 
- Para una buena clonación o copia, se debe usar metodos como el .copy() o utilizar la libreria copy, o usar [:] donde permitirá realizar una copia de todos los elementos pero sus punteros a memoria seran independientes.
- Para remover tambien existe varias tecnicas, como: .remove(n) que remueve desde izquierda a derecha la primera ocurrencia de n, del(obj[i]) permite remover por posición del indice o .pop() que es una función que remueve el ultimo item, si se pasa un indice este será el punto de inicio de posición de izquierda a derecha. 
- Se debe tener en cuenta que los tipos de datos que son mutables pueden afectar al codigo, cuando esta usando y aplicando logica condicionada que pueden afectar el orden y los elementos, donde si este cambia por mutación no tendría el mismo orden o elementos que perjudican cuando se ha establecido un orden especefico a seguir en el codigo. Para solucionar esto es necesario realizar una copia que no afecte al original.
- Como se sabe el establecer una variable como igual a otra variable que apunta a algo en memoria, solo se esta estableciendo un alias, dado que ahora las dos variables apuntan al mismo punto. Esto sucede también cuando se establece argumentos (fn1,fn2,fn3) que serán pasados a una función, y la función tiene nombres diferentes a sus parametros (param1,param2,param3), en este caso los nombres de los parametros son alias, que apuntan al mismo espacio en memoria que los argumentos pasados.
- Se debe tener en cuenta que realizar una copia correctamente no asegura que también realicen un copia independiente de los elementos anidadas, por ejemplo una lista de listas. Al copiar solo se esta copiando la estructura en la primera capa de la lista, por lo que los valores de las listas internas apuntan al mismo espacio en memoria a pesar de ser dos listas independientes en la primera capa.
- Las listas son eficientes debido a que por cada modificación no hay necesadad de crear otra copia, pero pueden producir congruencias si no se tiene en cuenta las mutaciones.
- Las tuplas no pueden ser mutables y son seguras para cuando se manipula datos importantes, además son rapidas en el aspecto de busqueda.
---

## Lecture 12 List comprehension, Funtions as Objects, Testing and Debugging
**Estado:**  Imcompleto
**Fecha:** --------

### Conceptos clave
- lists
- Functions
- testing
- debugging

### Finger Exercises
- [✓] FE 12.1 - write a function that take like input a list of unique and positive integers, and the function return the number of elements that are exact squares.    
### Aprendizajes personales
- List comprehension permite crear sintaxis simples de leer, permitiendo modificar a cada elemento de la lista sin necesidad de utilizar loops. Para esto se debe establecer entre corchetes: [expression for item in iterable if condition]. Esto devolvera la lista modificada.
- Las funciones pueden tener parametros con valores predefinidos, siempre en cuando se tenga en cuenta que debe estar al final de los parametros de la función si tiene mas de un parametro. No al inicio, no en medio, al final siempre, para evitar errores. 
- Cada función tiene su entorno, entonces establecer que una función retorne otra función solo estamos retornando codigo y un entorno que puede utilizar parametros y variables de la función principal o de todos los entornos con scope mas alto.
- El retornar funciones de funciones permite tener un buen diseño de software, manteniendo la descomposición y la abstracción.
- Testing/Validación no es mas que comparar que las salidas o resultados de entradas especeficas sean iguales a las esperadas con dichas entradas.
- Debugging es averiguar y resolver el error que presenta cuando los test fallan. 
- Para facilitar el testing-debugging se debe tener el codigo en modulos independientes que facilita la localización de errores de forma aislada. 
---
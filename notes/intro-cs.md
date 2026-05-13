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

## Lecture 6 - Bisection Search
**Estado:** ✅ Completada
**Fecha:** 28/04/2026

### Conceptos clave
- while
- int and float numbers
- math.floor

### Finger Exercises
- [✓] FE 5.1 - write a piece of code to find N between 0 and 1000, and return the attemps and the number.
- [✓] FE 5.2 - Use bisection search


### Aprendizajes personales
- Evitar el tratar de buscar la respuesta exactaa todos los problemas, debido a que solo se puede encontrar un valor con cierto marge de error lo suficientemente bueno.
- La busqueda binaria es mas eficiente en cuando a la implementación de ciertos algoritmos para encontrar la raíz de un numero de manera aproximada.
- La busqueda binaria se basa en tomar un punto medio y preguntar si ese valor es menor o mayor al valor que se desea encontrar, y dependiendo de la respuesta descartar valores que no cumplen con la condición establecida. Para eso se debe utilizar ciclos que permitan iterar hasta encontrar el valor deseado.
- El implementar la busqueda binaria para resolver problemas con dos endpoints, cuando los valores estan ordenados si o si, y cuando existe fedback sobre las predicciones (muy alto, muy bajo, correcto, mal, etc.)
- La implemantación de metodos no es al azar, es debido a que escalan de forma logaritmica y no exponencial, esto permite ahorrar tiempo y recursos. Y ademas son eficientes aun cuando los valores son gigantes.

## Lecture 7 - Functions: decomposition, abstraction
**Estado:** ✅ Completada
**Fecha:** 12/05/2026

### Conceptos clave
- functions
- loops
- indentation

### Finger Exercises
- [✓] FE 5.1 - write the instructions to eval quadratic
- [✓] FE 5.2 - write the instructions to get the sum of two evaluation of quadractics

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



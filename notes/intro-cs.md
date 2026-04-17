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
- [x] Rec 3.1 - 4 ejercios resueltos (commit: `feat: rec3 - 4 exercises (string manipulation and loop)`)

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
- [✓] FE 3.1 - for loop with range()
- [✓] FE 3.2 - funtion abs() to keep the integer positive


### Aprendizajes personales
- Python prioriza la simplicidad sobre encapsulación por lo que al utilizar el ciclo for, la variable i u otra variable que se establezca existe fuera del loop, por lo que se puede usarlo.
- Un caso similar con JS que tambien no tiene block scope si y solo si no se declara la variable con let dado que si tiene block scope, si se declara con var o simplemente el nombre de la variable y el valor conviritiendo en una variable global o con scope superior, por lo que no tendrá blcok scope commo en python. Permitiendo usar el valor de la variable fuera de for, provando algunos bugs si no se tiene cuidado.
- Los puntos flotantes en python son usados para aproximar a numeros reales. Y se denominan puntos flotantes a la manera que estos numeros son almacenados. 
- Los puntos flotantes son el estandar para manegar los numeros racionales. Dado que los numeros racionales se conforman de un numeros enteros y numeros decimales, y estos decimales pueden ser infinitos y la memoria que puede almacenar es limitada. Se establecieron las UPF (Unidades de puntos flotantes), estos limitan hasta que unidad decimal aproximado se puede almacenar. 
- Es por eso que (0.3\*3)+0.2 no es igual a 1.1, debido a que el hardware que los procesa los interpreta como ((1/3)\*3)+(0.2) donde 1/3= 0.3333333... con infinitas decimales. 
- La representación de los puntos flotantes no dependen de la implementación del lenguaje de programación, sino del hardware informático.
- Todo se representa como secuencia de bits (0 o 1). Dado que es facil de implementar en la construcción de hardware, debido a sus estados ( 1 y 0).



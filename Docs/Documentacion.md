# Documentación Técnica — Encriptación por el Método de Hill (3×3)

## 1. Introducción

El presente documento describe el funcionamiento de un sistema de **encriptación y desencriptación de texto** basado en el **método de Hill**, un algoritmo clásico de criptografía que utiliza conceptos fundamentales del **álgebra lineal** y **aritmética modular**.

El método trabaja con bloques de caracteres y una **matriz llave cuadrada**, permitiendo transformar un mensaje legible en uno cifrado mediante operaciones matriciales.  
La implementación se desarrolló en **Python**, haciendo uso de la librería **NumPy** para el manejo eficiente de matrices.

---

## 2. Diccionario de caracteres

El sistema emplea un diccionario personalizado compuesto por **27 caracteres**:

- Las **26 letras del alfabeto inglés**
- El **espacio**

Cada carácter se asocia a un valor numérico entero:

A → 0, B → 1, ..., Z → 25, Espacio → 26

> Nota: El carácter **Ñ** se sustituye por **N** para mantener la compatibilidad con el alfabeto definido.

Este diccionario permite convertir texto a valores numéricos y viceversa.

---

## 3. Preprocesamiento del texto

Antes de realizar la encriptación, el texto pasa por las siguientes etapas:

1. Conversión del texto a **mayúsculas**
2. Sustitución de caracteres según el diccionario
3. Verificación de longitud:
   - Si la cantidad de caracteres **no es múltiplo de 3**, se agregan espacios como *padding*

Este proceso garantiza que el texto pueda organizarse correctamente en bloques compatibles con la matriz llave.

---

## 4. Construcción de la matriz del mensaje

Los valores numéricos obtenidos se organizan en una **matriz A**, donde:

- Cada **columna representa un bloque de 3 caracteres**
- La matriz tiene siempre **3 filas**
- El número de columnas depende de la longitud del mensaje

Forma general:

A =
| a11 a12 a13 ... |
| a21 a22 a23 ... |
| a31 a32 a33 ... |

Esta matriz representa el mensaje original en forma matricial.

---

## 5. Matriz llave

La encriptación utiliza una **matriz llave B de tamaño 3×3**, definida previamente:

B =
| 35  53  12 |
| 12  21   5 |
|  2   4   1 |

Para que el método funcione correctamente, la matriz debe cumplir:

- Tener **determinante distinto de 0**
- Ser **invertible bajo módulo 27**

Esto asegura que el proceso de desencriptación sea posible.

---

## 6. Proceso de encriptación

La encriptación se realiza mediante la siguiente operación matricial:

A' = B · A

Posteriormente, a cada elemento de la matriz resultante se le aplica **módulo 27**:

Cij = A'ij mod 27

La matriz resultante **C** representa el mensaje cifrado en forma numérica.

Finalmente, cada valor de la matriz se convierte nuevamente a caracteres utilizando el diccionario inverso, obteniendo el **texto encriptado**.

---

## 7. Proceso de desencriptación

Para recuperar el mensaje original se siguen los pasos inversos:

1. Conversión del texto cifrado a valores numéricos
2. Construcción de la matriz cifrada **C**
3. Cálculo de la matriz inversa modular de la llave:

B⁻¹ mod 27

Ejemplo de matriz inversa (ya reducida módulo 27):

B⁻¹ =
|  1  -5  13 |
| -2  11 -31 |
|  6 -34  99 | mod 27

4. Multiplicación:

A = B⁻¹ · C

5. Aplicación del módulo 27 a cada elemento
6. Conversión de los valores numéricos a caracteres

El resultado final es el **mensaje original recuperado**.

---

## 8. Implementación en Python

La implementación se desarrolló en **Python**, utilizando:

- **NumPy** para:
  - Operaciones matriciales
  - Manejo de matrices
  - Cálculo de inversas

El código está estructurado para separar:
- Conversión de texto
- Encriptación
- Desencriptación

Esto mejora la legibilidad y el mantenimiento del proyecto.

---

## 9. Diagramas recomendados

Para mejorar la comprensión del algoritmo, se recomienda agregar:

1. **Diagrama de flujo del proceso**
   - Entrada del texto
   - Conversión a valores numéricos
   - Construcción de la matriz A
   - Multiplicación por la matriz B
   - Aplicación del módulo 27
   - Conversión a texto cifrado

2. **Diagrama de bloques**
   - Texto → Conversión → Matriz A → Encriptación → Matriz C → Texto cifrado

Estos diagramas pueden elaborarse en herramientas como Draw.io, Lucidchart o PowerPoint.

---

## 10. Alcances y limitaciones

- El algoritmo **no está diseñado para criptografía moderna**
- Se utiliza con fines **educativos y académicos**
- No incluye mecanismos de seguridad avanzada
- Demuestra la aplicación práctica del álgebra lineal en criptografía clásica

---

## 11. Conclusión

Este proyecto demuestra cómo los conceptos de **álgebra lineal**, como matrices, inversas y operaciones modulares, pueden aplicarse directamente a la encriptación de información.

El método de Hill, aunque obsoleto en contextos reales de seguridad, sigue siendo una herramienta valiosa para comprender los fundamentos matemáticos detrás de los sistemas criptográficos.

---

**Autor:**  
Brayan Rojas Muñoz  
Ingeniería de Software  
Universidad Autónoma de Zacatecas

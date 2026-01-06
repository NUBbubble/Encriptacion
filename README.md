# Hill Cipher Encryption (3x3)

Implementación en Python del método de **encriptación por el metodo de Hill**, basado en álgebra lineal y aritmética modular.  
El proyecto utiliza matrices de tamaño **3×3** para cifrar y descifrar texto mediante operaciones matriciales.

## 📌 Descripción general

Este proyecto implementa un sistema de **encriptación y desencriptación de texto** usando el **método de Hill**, trabajando con bloques de caracteres y una matriz llave invertible bajo módulo 27.

La solución está orientada a fines **académicos y educativos**, mostrando una aplicación práctica del álgebra lineal en criptografía clásica.

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **NumPy**  
  Utilizado para el manejo eficiente de matrices y operaciones algebraicas.

## ⚙️ Características principales

- Conversión de texto a valores numéricos mediante un diccionario personalizado.
- Encriptación por bloques usando matrices 3×3.
- Aplicación de aritmética modular (mod 27).
- Proceso inverso para la desencriptación del mensaje original.
- Manejo automático de padding cuando el texto no cumple con el tamaño requerido.

## 📦 Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

```bash
pip install numpy

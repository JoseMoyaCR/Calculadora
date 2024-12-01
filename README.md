# Calculadora - Validación de Sistemas Embebidos

## Descripción del Proyecto
Este proyecto consiste en la implementación de una calculadora básica desarrollada en Python, la cual incluye operaciones fundamentales como suma, resta, multiplicación, división, potenciación y cálculo de raíces cuadradas. La calculadora está diseñada siguiendo principios de validación y pruebas, haciendo énfasis en el manejo de errores y valores límite.

Este proyecto forma parte del **Ejercicio Práctico 2** del curso **"Validación de Sistemas Embebidos"** TSEV-008 del programa de Técnico en Sistemas Embebidos de la Universidad Fidélitas. Su objetivo es aplicar técnicas de pruebas unitarias para garantizar la robustez del sistema, identificando posibles fallos en la implementación.

---

## Funciones Implementadas
Las funciones disponibles en la calculadora son:
- **Suma:** Operación de adición entre dos números.
- **Resta:** Operación de sustracción entre dos números.
- **Producto:** Operación de multiplicación entre dos números.
- **División:** Operación de división entre dos números, validando divisores diferentes de cero.
- **Potencia:** Cálculo de potencias al cuadrado y de n-ésima potencia.
- **Raíz cuadrada:** Cálculo de la raíz cuadrada de un número positivo.

---

## Pruebas Unitarias
Se implementaron pruebas unitarias utilizando el módulo `unittest` de Python para validar cada función. Las pruebas están diseñadas para abarcar:

### Casos de Prueba
1. **Casos típicos:** Verifican el comportamiento esperado con entradas comunes.
2. **Errores esperados:** Evalúan situaciones como divisores iguales a cero, valores no numéricos (`nan`) y raíces cuadradas de números negativos.
3. **Valores extremos:** Validan la precisión de las operaciones con números muy grandes o muy pequeños.

---

### Ejemplo de Pruebas
#### Función Suma:
- Caso típico: Suma de dos números positivos.
- Error esperado: Validación de `nan` como entrada.
- Valor extremo: Suma de dos números extremadamente grandes.

#### Función División:
- Caso típico: División de dos números positivos.
- Error esperado: División entre cero.
- Valor extremo: División de un número muy grande entre otro muy pequeño.

---

## Resultados de las Pruebas
Todas las pruebas fueron ejecutadas en una **Raspberry Pi 5**. Durante el proceso se identificaron algunos problemas relacionados con los límites de precisión de los números de punto flotante, que fueron solucionados ajustando las tolerancias en las pruebas.

---

# Sistema para cajero automatico POO - Ivan Santiago Bejarano Sua
**Autor de readme de prueba:** [Ivan Santiago Bejarano Sua]
**Carrera:** Ingeniera Informatica
**Ciclo:** Tecnico Profesional de Soporte de Sistemas y Redes
**Clase:** Programacion 2
**Semestre:** Segundo Semestre

# Descripcion del Proyecto
Simulador de banco que permite gestionar acciones bancaria desarrollado con el lenguaje de programacion Python mediante uso de POO.  

## Conceptos Aplicados
En el codigo del proyecto aparentes elemento como, Abstracciones, Encapsulamientos y Herencias entre otros.
*   **Abstracción:** Utilizar clases como bases que no se puede instanciar.
*   **Encapsulamiento:** Son atributos protegidos como el saldo para la seguridad necesaria de aplicar.
*   **Herencia:** Crear mas de un tipo de cuenta espesifica apartir de la base previamente establecida.

## Investigación: Getters y Setters Tarea de Investigacion de Getters y Setters
Al manejar la funciones de **Encapsulamiento**, Se usan decoradores especiales que son el Getter y el Setter. 
1. **Getter (`@property`):** Deja leer el saldo de banco sin aplicar modificaciones al valor.
   - *Ejemplo:* `print(mi_cuenta.saldo)`
2. **Setter (`@saldo.setter`):** Permite cambiar el saldo pero con reglas (ejemplo: no números negativos). Deja cambiar el valor de saldo pero bajo ciertas reglas por eejemplo que los numeros no sean negativos:
   - *Ejemplo:* `mi_cuenta.saldo = 500` (El código acepta que el monto es real).

## Forma de Ejecución
Para iniciar el programa, ejecutar el comando en la terminal:
bash
python cajero_poo.py
# 🐋 Cultura General


## Docker == Contenedor?

Existen preguntas existenciales que al inicio pueden ser confusos de entender, pero conforme avancemos en el curso, se clarificarán, te lo aseguro!

Unas de las mayores confusiones de las personas a la hora de iniciar con estos demas es:

¿Qué es Docker? ¿Qué es un contenedor? ¿Y en qué se diferencian?

Muy bien, se suele relacionar Docker con un contenedor, pero al final del día es como los Post-It a pesar de que es un simple papel adhesivo de color y hay muchas marcas que lo fabrican, al popularizarse la marca todos les llaman así.

Lo mismo pasa con los contenedores y Docker, Docker se ha popularizado por ser la herramienta principal cuando hablamos de administrar contenedores, pero enrealidad hay muchas otras herramientas que tienen una funcionalidad similar para crear, correr y administrar estos contenedores, entre ellas:

-Podman
-Contaiderd
-LXC/LXD
-Entre otras

Sin embargo Docker, herramienta creada por Docker.Inc se ha popularizado por su practicidad y agilidad.

Entonces concluimos que Docker es el motor/herramienta que nos permite crear y administrar nuestros contenedores.

## Contenedor 🧱

Un contenedor es una unidad ligera, portátil y autosuficiente que permite ejecutar aplicaciones de forma aislada

📦 ¿Qué hace exactamente un contenedor?
- Empaqueta el código de la aplicación, junto con librerías, dependencias, configuraciones, y todo lo necesario para que se ejecute de manera estable.
- Lo aísla del sistema operativo del host, evitando conflictos con otras aplicaciones.
- Se ejecuta en segundos y ocupa menos recursos que una máquina virtual.

🎯 ¿Por qué son tan útiles?
- ✅ Portabilidad: Puedes moverlo entre servidores sin preocuparte por el entorno.
- ✅ Consistencia: Se ejecuta igual en producción, pruebas y desarrollo.
- ✅ Rapidez: Se crea y destruye más rápido que una máquina virtual.
- ✅ Escalabilidad: Ideal para arquitecturas modernas como microservicios.

🧪 Ejemplo real
Imagina que desarrollas una aplicación web en Node.js. En lugar de instalar Node, dependencias y configuración en cada servidor, creas un contenedor con todo eso ya dentro. El contenedor se puede desplegar directamente en cualquier máquina con Docker, y funcionará igual en todas.

## Contendor VS Maquina Virtual(VM)

Cierto que la funcionalidad de un contenedor suena similar a la de una VM?

¡Veamos cómo se diferencian!

### 🧠 Diferencias entre Contenedores y Máquinas Virtuales (MV)

| Característica        | Contenedor                          | Máquina Virtual (MV)                    |
|-----------------------|-------------------------------------|----------------------------------------|
| **Virtualización**    | A nivel de sistema operativo        | A nivel de hardware                    |
| **Sistema operativo** | Comparte el kernel del host         | Tiene su propio sistema operativo      |
| **Peso**              | Ligero (MB)                         | Pesado (GB)                            |
| **Arranque**          | Muy rápido (segundos)               | Más lento (minutos)                    |
| **Aislamiento**       | Parcial                             | Completo                               |
| **Portabilidad**      | Muy alta                            | Alta, pero menos flexible              |
| **Seguridad**         | Menos aislado, depende del host     | Más seguro por aislamiento total       |

### ✅ Ventajas y Desventajas

#### Ventajas de los Contenedores

- Ocupan menos espacio y recursos
- Se inician y destruyen rápidamente
- Funcionan igual en cualquier entorno con Docker
- Perfectos para microservicios y DevOps

#### Desventajas de los Contenedores

- Menor aislamiento frente a fallos del host
- Limitados al sistema operativo del host

#### Ventajas de las Máquinas Virtuales

- Aislamiento completo entre entornos
- Puedes ejecutar distintos sistemas operativos
- Más seguras para entornos críticos

#### Desventajas de las Máquinas Virtuales

- Consumen más recursos (CPU, RAM, disco)
- Arranque más lento
- Menor densidad de instancias por hardware

### Arquitectura VM VS CONTENEDOR

Imagina que una máquina virtual (VM) es como construir una casa entera para cada aplicación. Cada casa tiene su propio terreno, cimientos, instalaciones eléctricas, su cocina, baño, todo independiente. En el mundo tecnológico, esto significa que cada VM incluye su propio sistema operativo completo —como Linux o Windows—, además del software que vas a ejecutar. Para lograrlo, necesitas un "constructor" especial llamado hipervisor, que es el encargado de gestionar todas esas casas dentro de un mismo edificio. Esto da mucha seguridad porque todo está aislado: si una casa se incendia, las demás no se ven afectadas. Pero también es costoso y lento. Construir una casa toma tiempo y recursos.

En cambio, un contenedor es más parecido a vivir en un apartamento dentro de un mismo edificio. Compartes estructuras comunes, como los muros, el techo y el sistema eléctrico, pero cada apartamento tiene su propia decoración, reglas y habitantes. Técnicamente, todos los contenedores comparten el mismo sistema operativo del host (la estructura del edificio), pero funcionan como espacios separados con sus propios utensilios (dependencias, configuración y código de la aplicación). Esto los hace más livianos, rápidos de montar y más eficientes en el uso de recursos.

La gran diferencia está en esa base: las máquinas virtuales necesitan replicar un sistema operativo completo para cada entorno, mientras que los contenedores se apoyan en el que ya existe. Por eso los contenedores se inician en segundos, mientras que las VMs tardan más. Pero esa eficiencia tiene un costo: los contenedores están menos aislados, así que una falla del sistema operativo anfitrión puede afectar a todos los contenedores.

Ambas arquitecturas son poderosas, y cada una brilla según el tipo de proyecto. Si necesitas seguridad máxima y diferentes sistemas operativos, vas con máquinas virtuales. Si necesitas velocidad, escalabilidad y consistencia para desplegar microservicios o apps web, los contenedores te hacen la vida mucho más fácil.

Esta es una imagen mas técnica de como se ven las difertes arquitecturas

![Texto alternativo](arqui_vm_container.jpg)

## 🚀 Casos de Uso de Contenedores

### 1. Microservicios
Permiten dividir una aplicación en pequeños servicios independientes que se despliegan por separado, lo que facilita el desarrollo, escalado y mantenimiento.

### 2. Integración y entrega continua (CI/CD)
Los contenedores ayudan a automatizar pruebas, compilaciones y despliegues en entornos consistentes, mejorando la velocidad del ciclo de desarrollo.

### 3. Entornos de desarrollo consistentes
Los desarrolladores pueden trabajar con la misma imagen que se usa en producción, evitando conflictos por diferencias de configuración.

### 4. Multinube e infraestructura híbrida
Los contenedores se ejecutan igual en cualquier entorno (local, nube pública o privada), facilitando la portabilidad entre plataformas.

### 5. Ciencia y procesamiento por lotes
Ideal para empaquetar herramientas complejas y ejecutar tareas científicas o de análisis de datos de forma reproducible y eficiente.

### 6. Internet de las cosas (IoT)
Permiten gestionar y actualizar software en dispositivos distribuidos remotamente de manera centralizada y segura.

### 7. Gobierno y seguridad
Se utilizan para modularizar sistemas críticos, mejorar el aislamiento y automatizar procesos administrativos de forma segura.

Muy bien, entendido todo esto, pasemos a los prerequisitos!
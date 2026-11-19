# TransExpress — Los 23 patrones de diseño GoF en una empresa de transporte

Proyecto educativo en Java que implementa **los 23 patrones de diseño** del
[catálogo de Refactoring Guru](https://refactoring.guru/es/design-patterns/catalog)
dentro de un **mismo flujo de negocio**: la empresa ficticia de transporte
*TransExpress*.

El objetivo es que todos los patrones **coexistan y colaboren** en un escenario
realista, no como 23 demos aisladas, aplicando los principios **SOLID** y
evitando antipatrones. Cada patrón se usa en el punto del negocio donde aporta
valor de verdad.

## Cómo ejecutarlo

Requisitos: **JDK 17+** y **Maven 3.9+**.

```bash
mvn compile
mvn exec:java
```

> En entornos donde `~/.m2` no es escribible, añade un repositorio local:
> `mvn -Dmaven.repo.local=./.m2repo compile exec:java`

Al ejecutarlo verás la simulación de un envío de principio a fin, con una línea
por patrón indicando dónde interviene (`[Builder]`, `[Observer]`, etc.).

## Dónde vive cada patrón

Cada patrón está en su propio paquete bajo
`src/main/java/com/transporte/patrones/`.

### Creacionales (`patrones/creacionales`)

| Patrón | Paquete | Uso en el negocio |
|---|---|---|
| **Singleton** | `singleton` | Configuración única de la empresa |
| **Factory Method** | `factory` | Un centro de despacho decide qué vehículo crear |
| **Abstract Factory** | `abstractfactory` | Familias coherentes de servicio (vehículo + embalaje) |
| **Builder** | `builder` | Construir una orden de transporte paso a paso |
| **Prototype** | `prototype` | Clonar plantillas de ruta |

### Estructurales (`patrones/estructurales`)

| Patrón | Paquete | Uso en el negocio |
|---|---|---|
| **Adapter** | `adapter` | Integrar una API de mapas externa |
| **Bridge** | `bridge` | Separar tipo de envío del medio de transporte |
| **Composite** | `composite` | Rutas formadas por tramos y sub-rutas |
| **Decorator** | `decorator` | Añadir extras al envío (seguro, urgencia) |
| **Facade** | `facade` | Una fachada "cotizar" que esconde el subsistema |
| **Flyweight** | `flyweight` | Compartir datos de modelos de vehículo |
| **Proxy** | `proxy` | Caché sobre el servicio de tarifas |

### De comportamiento (`patrones/comportamiento`)

| Patrón | Paquete | Uso en el negocio |
|---|---|---|
| **Chain of Responsibility** | `chain` | Validar una orden por eslabones |
| **Command** | `command` | Operaciones sobre envíos con deshacer |
| **Iterator** | `iterator` | Recorrer la flota |
| **Mediator** | `mediator` | Centro de despacho que coordina conductores |
| **Memento** | `memento` | Guardar y restaurar el estado de un paquete |
| **Observer** | `observer` | Notificar al cliente los cambios de estado |
| **State** | `state` | Ciclo de vida del envío (CREADO → EN_RUTA → ENTREGADO) |
| **Strategy** | `strategy` | Algoritmos de cálculo de tarifa intercambiables |
| **Template Method** | `template` | Esqueleto fijo del proceso de entrega |
| **Visitor** | `visitor` | Facturación recorriendo tipos de envío |

## Colaboraciones entre patrones

Algunos patrones trabajan juntos sobre el mismo objeto, igual que en un sistema real:

- **Observer + State + Memento + Command** conviven en la clase `Paquete`:
  el paquete cambia de **estado** (State), **notifica** a los clientes (Observer),
  cada avance se envuelve en un **comando** con deshacer (Command) y el deshacer
  se apoya en una instantánea (Memento).
- **Facade** coordina el **Adapter** (distancia) y el **Proxy** (tarifas) en una
  sola operación de cotización.

## Estructura del proyecto

```
src/main/java/com/transporte/
├── Main.java                 # Escenario que integra los 23 patrones
├── dominio/                  # Modelo compartido (Ubicacion, TipoVehiculo)
└── patrones/
    ├── creacionales/
    ├── estructurales/
    └── comportamiento/
```

## Contribuir

Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de abrir un pull request.

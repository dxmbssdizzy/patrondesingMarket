# Guía de colaboración

Este proyecto lo mantenemos entre varias personas. Para que el código se
mantenga limpio y coherente, seguimos estas pautas.

## Flujo de trabajo con Git

1. No hagas commits directos a `main`.
2. Crea una rama por cada cambio:
   - `feat/...` para nuevas funcionalidades.
   - `fix/...` para correcciones.
   - `docs/...` para documentación.
3. Abre un **Pull Request** hacia `main` y espera la revisión del otro
   colaborador antes de integrar.
4. Mensajes de commit claros y en imperativo (ej. `feat: agrega ejemplo de Observer`).

## Convenciones de código

- **Un patrón por paquete** bajo `com.transporte.patrones.<categoria>.<patron>`.
- Cada patrón lleva un **comentario Javadoc** en su clase principal que explica:
  qué patrón es, su categoría y qué resuelve en el negocio.
- Prioriza que el ejemplo sea **sencillo y fácil de entender**. Si hay que elegir
  entre "más realista" y "más claro", elige claro.
- Respeta los principios **SOLID**:
  - Cada clase con una sola responsabilidad.
  - Depende de interfaces, no de clases concretas.
  - Abierto a extensión, cerrado a modificación.
- Evita antipatrones: nada de clases "Dios", ni condicionales gigantes donde un
  patrón (State/Strategy) lo resuelve mejor, ni Singletons usados como variables
  globales mutables.
- Clases inmutables siempre que sea posible (`final`, sin setters innecesarios).

## Antes de abrir el PR

Comprueba que compila y ejecuta sin errores:

```bash
mvn compile
mvn exec:java
```

Si tocas un patrón, verifica que su línea correspondiente sigue apareciendo en la
salida de la simulación.

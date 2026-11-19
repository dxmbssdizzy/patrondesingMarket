package com.transporte.patrones.comportamiento.visitor;

/**
 * PATRÓN VISITOR (Comportamiento).
 *
 * Elemento que acepta un visitante. El método {@link #aceptar(VisitanteCobro)}
 * permite añadir nuevas operaciones (visitantes) sobre la jerarquía sin
 * modificar las clases de los elementos.
 */
public interface ElementoFacturable {

    double aceptar(VisitanteCobro visitante);
}

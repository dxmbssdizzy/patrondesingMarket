package com.transporte.patrones.comportamiento.chain;

import com.transporte.patrones.creacionales.builder.OrdenTransporte;

/**
 * PATRÓN CHAIN OF RESPONSIBILITY (Comportamiento).
 *
 * Cada validador decide si la orden pasa su regla y, si procede, delega en el
 * siguiente eslabón de la cadena. Así se pueden añadir, quitar o reordenar
 * validaciones sin tocar las demás.
 */
public abstract class ValidadorOrden {

    private ValidadorOrden siguiente;

    public ValidadorOrden encadenar(ValidadorOrden siguiente) {
        this.siguiente = siguiente;
        return siguiente;
    }

    /** Devuelve null si todo es válido, o un mensaje de error si falla. */
    public String validar(OrdenTransporte orden) {
        String error = revisar(orden);
        if (error != null) {
            return error;
        }
        if (siguiente != null) {
            return siguiente.validar(orden);
        }
        return null;
    }

    protected abstract String revisar(OrdenTransporte orden);
}

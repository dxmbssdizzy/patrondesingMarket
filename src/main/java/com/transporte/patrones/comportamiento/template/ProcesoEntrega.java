package com.transporte.patrones.comportamiento.template;

import java.util.ArrayList;
import java.util.List;

/**
 * PATRÓN TEMPLATE METHOD (Comportamiento).
 *
 * Define en {@link #procesar()} el esqueleto fijo del proceso de entrega y deja
 * que las subclases personalicen pasos concretos (recoger, transportar). El
 * método plantilla es final para que no se altere el orden de los pasos.
 */
public abstract class ProcesoEntrega {

    /**
     * Método plantilla: fija el orden de los pasos y devuelve lo que hizo cada
     * uno, para que la capa de salida lo muestre. No imprime.
     */
    public final List<String> procesar() {
        List<String> pasos = new ArrayList<>();
        pasos.add(recoger());
        pasos.add(transportar());
        pasos.add(confirmar());
        return pasos;
    }

    protected abstract String recoger();

    protected abstract String transportar();

    /** Paso común a todas las entregas. */
    private String confirmar() {
        return "Entrega confirmada y firmada.";
    }
}

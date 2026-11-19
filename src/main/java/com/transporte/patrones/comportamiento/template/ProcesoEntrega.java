package com.transporte.patrones.comportamiento.template;

/**
 * PATRÓN TEMPLATE METHOD (Comportamiento).
 *
 * Define en {@link #procesar()} el esqueleto fijo del proceso de entrega y deja
 * que las subclases personalicen pasos concretos (recoger, transportar). El
 * método plantilla es final para que no se altere el orden de los pasos.
 */
public abstract class ProcesoEntrega {

    public final void procesar() {
        recoger();
        transportar();
        confirmar();
    }

    protected abstract void recoger();

    protected abstract void transportar();

    /** Paso común a todas las entregas. */
    private void confirmar() {
        System.out.println("    [Template Method] Entrega confirmada y firmada.");
    }
}

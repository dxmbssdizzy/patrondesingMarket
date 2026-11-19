package com.transporte.patrones.estructurales.bridge;

/**
 * PATRÓN BRIDGE (Estructural).
 *
 * Lado "Abstracción": el tipo de envío. Mantiene una referencia a un
 * {@link MedioTransporte} (la implementación) y delega en él la parte física.
 *
 * Así el tipo de envío (nacional, internacional...) y el medio (terrestre,
 * aéreo...) evolucionan por separado sin multiplicar subclases.
 */
public abstract class Envio {

    protected final MedioTransporte medio;

    protected Envio(MedioTransporte medio) {
        this.medio = medio;
    }

    public abstract String entregar();
}

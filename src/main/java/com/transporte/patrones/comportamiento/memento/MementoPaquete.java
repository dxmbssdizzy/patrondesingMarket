package com.transporte.patrones.comportamiento.memento;

import com.transporte.patrones.comportamiento.state.EstadoEnvio;

/**
 * PATRÓN MEMENTO (Comportamiento).
 *
 * Captura una instantánea del estado interno de un paquete (su estado de envío)
 * sin exponer sus detalles. Solo el paquete que lo creó puede volver a leerlo,
 * de modo que el encapsulamiento se mantiene.
 */
public final class MementoPaquete {

    private final EstadoEnvio estado;

    public MementoPaquete(EstadoEnvio estado) {
        this.estado = estado;
    }

    EstadoEnvio getEstado() {
        return estado;
    }
}

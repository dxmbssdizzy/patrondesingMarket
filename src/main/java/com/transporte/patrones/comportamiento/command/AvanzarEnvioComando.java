package com.transporte.patrones.comportamiento.command;

import com.transporte.patrones.comportamiento.memento.MementoPaquete;
import com.transporte.patrones.comportamiento.memento.Paquete;

/**
 * Comando concreto: avanza el estado de un paquete. Para poder deshacerse,
 * guarda una instantánea (Memento) antes de ejecutar, y la restaura al deshacer.
 *
 * Es un buen ejemplo de cómo Command y Memento colaboran de forma natural.
 */
public final class AvanzarEnvioComando implements Comando {

    private final Paquete paquete;
    private MementoPaquete respaldo;

    public AvanzarEnvioComando(Paquete paquete) {
        this.paquete = paquete;
    }

    @Override
    public void ejecutar() {
        respaldo = paquete.guardar();
        paquete.avanzar();
    }

    @Override
    public void deshacer() {
        if (respaldo != null) {
            paquete.restaurar(respaldo);
        }
    }
}

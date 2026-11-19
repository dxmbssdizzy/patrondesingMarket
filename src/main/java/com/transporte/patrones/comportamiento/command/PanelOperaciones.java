package com.transporte.patrones.comportamiento.command;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * Invocador del Command: ejecuta comandos y mantiene un historial para poder
 * deshacer la última operación. No conoce los detalles de cada comando.
 */
public final class PanelOperaciones {

    private final Deque<Comando> historial = new ArrayDeque<>();

    public void ejecutar(Comando comando) {
        comando.ejecutar();
        historial.push(comando);
    }

    public void deshacerUltimo() {
        if (!historial.isEmpty()) {
            historial.pop().deshacer();
        }
    }
}

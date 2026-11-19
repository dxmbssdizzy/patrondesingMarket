package com.transporte.patrones.comportamiento.command;

/**
 * PATRÓN COMMAND (Comportamiento).
 *
 * Encapsula una operación como un objeto, lo que permite ejecutarla, deshacerla
 * y guardarla en un historial. El invocador no sabe qué hace cada comando.
 */
public interface Comando {

    void ejecutar();

    void deshacer();
}

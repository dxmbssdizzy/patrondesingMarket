package com.transporte.patrones.comportamiento.observer;

import java.util.function.Consumer;

/**
 * Observador concreto: notifica al cliente por un canal (SMS, email...).
 *
 * Un notificador produce salida por naturaleza, pero no imprime por su cuenta:
 * recibe el destino de la salida como un {@link Consumer} (inyección de
 * dependencia), de modo que la capa de salida sigue siendo el único canal real.
 */
public final class NotificadorCliente implements ObservadorEnvio {

    private final String canal;
    private final Consumer<String> salida;

    public NotificadorCliente(String canal, Consumer<String> salida) {
        this.canal = canal;
        this.salida = salida;
    }

    @Override
    public void actualizar(String numeroEnvio, String nuevoEstado) {
        salida.accept("(" + canal + ") Envío " + numeroEnvio
                + " ahora está: " + nuevoEstado);
    }
}

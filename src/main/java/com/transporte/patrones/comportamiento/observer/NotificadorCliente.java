package com.transporte.patrones.comportamiento.observer;

/**
 * Observador concreto: notifica al cliente por un canal (SMS, email...).
 */
public final class NotificadorCliente implements ObservadorEnvio {

    private final String canal;

    public NotificadorCliente(String canal) {
        this.canal = canal;
    }

    @Override
    public void actualizar(String numeroEnvio, String nuevoEstado) {
        System.out.println("    [Observer] (" + canal + ") Envío " + numeroEnvio
                + " ahora está: " + nuevoEstado);
    }
}

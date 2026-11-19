package com.transporte.patrones.comportamiento.observer;

/**
 * PATRÓN OBSERVER (Comportamiento).
 *
 * Suscriptor que es notificado cuando el envío observado cambia de estado.
 */
public interface ObservadorEnvio {

    void actualizar(String numeroEnvio, String nuevoEstado);
}

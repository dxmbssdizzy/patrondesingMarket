package com.transporte.patrones.comportamiento.mediator;

/**
 * Colega del Mediator. Solo conoce al centro de despacho, no a los demás
 * conductores. Envía mensajes a través del mediador y recibe los que este le pasa.
 */
public final class Conductor {

    private final String nombre;
    private final CentroDespacho central;

    public Conductor(String nombre, CentroDespacho central) {
        this.nombre = nombre;
        this.central = central;
        central.registrar(this);
    }

    public void transmitir(String mensaje) {
        System.out.println("    [Mediator] " + nombre + " transmite: \"" + mensaje + "\"");
        central.enviar(mensaje, this);
    }

    public void recibir(String mensaje) {
        System.out.println("    [Mediator] " + nombre + " recibe: \"" + mensaje + "\"");
    }

    public String getNombre() {
        return nombre;
    }
}

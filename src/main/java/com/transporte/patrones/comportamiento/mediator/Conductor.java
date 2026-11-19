package com.transporte.patrones.comportamiento.mediator;

import java.util.ArrayList;
import java.util.List;

/**
 * Colega del Mediator. Solo conoce al centro de despacho, no a los demás
 * conductores. Envía mensajes a través del mediador y recibe los que este le pasa.
 *
 * No imprime: guarda los mensajes recibidos para que la capa de salida los muestre.
 */
public final class Conductor {

    private final String nombre;
    private final CentroDespacho central;
    private final List<String> recibidos = new ArrayList<>();

    public Conductor(String nombre, CentroDespacho central) {
        this.nombre = nombre;
        this.central = central;
        central.registrar(this);
    }

    public void transmitir(String mensaje) {
        central.enviar(mensaje, this);
    }

    public void recibir(String mensaje) {
        recibidos.add(mensaje);
    }

    public List<String> mensajesRecibidos() {
        return List.copyOf(recibidos);
    }

    public String getNombre() {
        return nombre;
    }
}

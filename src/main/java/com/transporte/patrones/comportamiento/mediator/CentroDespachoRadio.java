package com.transporte.patrones.comportamiento.mediator;

import java.util.ArrayList;
import java.util.List;

/**
 * Mediador concreto: retransmite por "radio" el mensaje de un conductor a todos
 * los demás conductores registrados.
 */
public final class CentroDespachoRadio implements CentroDespacho {

    private final List<Conductor> conductores = new ArrayList<>();

    @Override
    public void registrar(Conductor conductor) {
        conductores.add(conductor);
    }

    /** Conductores registrados (solo lectura), para que la salida los consulte. */
    public List<Conductor> conductores() {
        return List.copyOf(conductores);
    }

    @Override
    public void enviar(String mensaje, Conductor emisor) {
        for (Conductor conductor : conductores) {
            if (conductor != emisor) {
                conductor.recibir(mensaje);
            }
        }
    }
}

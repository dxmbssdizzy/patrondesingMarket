package com.transporte.patrones.comportamiento.state;

public final class EstadoEntregado implements EstadoEnvio {

    @Override
    public EstadoEnvio siguiente() {
        return this; // estado final: no avanza más
    }

    @Override
    public String nombre() {
        return "ENTREGADO";
    }

    @Override
    public boolean esFinal() {
        return true;
    }
}

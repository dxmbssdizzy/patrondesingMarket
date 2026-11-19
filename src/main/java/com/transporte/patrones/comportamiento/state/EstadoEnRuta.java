package com.transporte.patrones.comportamiento.state;

public final class EstadoEnRuta implements EstadoEnvio {

    @Override
    public EstadoEnvio siguiente() {
        return new EstadoEntregado();
    }

    @Override
    public String nombre() {
        return "EN_RUTA";
    }

    @Override
    public boolean esFinal() {
        return false;
    }
}

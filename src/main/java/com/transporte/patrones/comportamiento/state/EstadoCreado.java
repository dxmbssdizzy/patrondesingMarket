package com.transporte.patrones.comportamiento.state;

public final class EstadoCreado implements EstadoEnvio {

    @Override
    public EstadoEnvio siguiente() {
        return new EstadoEnRuta();
    }

    @Override
    public String nombre() {
        return "CREADO";
    }

    @Override
    public boolean esFinal() {
        return false;
    }
}

package com.transporte.patrones.creacionales.factory;

public final class Furgoneta implements Vehiculo {

    @Override
    public String descripcion() {
        return "Furgoneta de reparto";
    }

    @Override
    public int capacidadKg() {
        return 800;
    }
}

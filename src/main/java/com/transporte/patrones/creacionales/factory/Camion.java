package com.transporte.patrones.creacionales.factory;

public final class Camion implements Vehiculo {

    @Override
    public String descripcion() {
        return "Camión de carga pesada";
    }

    @Override
    public int capacidadKg() {
        return 10_000;
    }
}

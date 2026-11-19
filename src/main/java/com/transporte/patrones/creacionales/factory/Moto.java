package com.transporte.patrones.creacionales.factory;

public final class Moto implements Vehiculo {

    @Override
    public String descripcion() {
        return "Moto de reparto urbano";
    }

    @Override
    public int capacidadKg() {
        return 20;
    }
}

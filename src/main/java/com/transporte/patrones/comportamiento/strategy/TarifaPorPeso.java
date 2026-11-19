package com.transporte.patrones.comportamiento.strategy;

public final class TarifaPorPeso implements EstrategiaTarifa {

    @Override
    public double calcular(double distanciaKm, double pesoKg) {
        return pesoKg * 0.8 + distanciaKm * 0.5;
    }

    @Override
    public String nombre() {
        return "por peso";
    }
}

package com.transporte.patrones.comportamiento.strategy;

public final class TarifaPorDistancia implements EstrategiaTarifa {

    @Override
    public double calcular(double distanciaKm, double pesoKg) {
        return distanciaKm * 1.5;
    }

    @Override
    public String nombre() {
        return "por distancia";
    }
}

package com.transporte.patrones.estructurales.flyweight;

/**
 * PATRÓN FLYWEIGHT (Estructural).
 *
 * Flyweight: almacena el estado INTRÍNSECO (compartido) de un modelo de
 * vehículo: marca, modelo y consumo. Muchos vehículos de la flota comparten
 * una misma instancia de este objeto para ahorrar memoria.
 */
public final class ModeloVehiculo {

    private final String marca;
    private final String modelo;
    private final double consumoLitrosPorKm;

    public ModeloVehiculo(String marca, String modelo, double consumoLitrosPorKm) {
        this.marca = marca;
        this.modelo = modelo;
        this.consumoLitrosPorKm = consumoLitrosPorKm;
    }

    public String descripcion() {
        return marca + " " + modelo;
    }

    public double consumoLitrosPorKm() {
        return consumoLitrosPorKm;
    }
}

package com.transporte.patrones.estructurales.flyweight;

/**
 * Contexto que combina el estado extrínseco (placa, propio de cada unidad) con
 * una referencia al flyweight {@link ModeloVehiculo} (estado compartido).
 */
public final class UnidadFlota {

    private final String placa;
    private final ModeloVehiculo modelo;

    public UnidadFlota(String placa, ModeloVehiculo modelo) {
        this.placa = placa;
        this.modelo = modelo;
    }

    public String descripcion() {
        return "[" + placa + "] " + modelo.descripcion();
    }
}

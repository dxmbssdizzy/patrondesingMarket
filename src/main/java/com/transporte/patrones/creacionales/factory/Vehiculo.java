package com.transporte.patrones.creacionales.factory;

/**
 * Abstracción de un vehículo de la flota.
 *
 * Es el "Producto" para los patrones Factory Method y Abstract Factory.
 */
public interface Vehiculo {

    String descripcion();

    /** Capacidad de carga en kilogramos. */
    int capacidadKg();
}

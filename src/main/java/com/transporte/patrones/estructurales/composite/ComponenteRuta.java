package com.transporte.patrones.estructurales.composite;

/**
 * PATRÓN COMPOSITE (Estructural).
 *
 * Componente común que permite tratar de forma uniforme a un tramo simple
 * (hoja) y a una ruta que agrupa varios tramos (compuesto).
 */
public interface ComponenteRuta {

    /** Distancia total en km (un tramo devuelve la suya; una ruta, la suma). */
    double distanciaKm();

    String describir();
}

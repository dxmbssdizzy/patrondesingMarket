package com.transporte.patrones.estructurales.adapter;

/**
 * Librería externa de mapas (el "Adaptee"). No podemos modificar su firma:
 * trabaja con coordenadas crudas y devuelve metros, no nuestra interfaz.
 */
public final class ApiMapasExterna {

    public double distanciaEnMetros(double latA, double lonA, double latB, double lonB) {
        // Aproximación simple (distancia euclídea escalada) suficiente para el ejemplo.
        double dLat = latA - latB;
        double dLon = lonA - lonB;
        return Math.sqrt(dLat * dLat + dLon * dLon) * 111_000;
    }
}

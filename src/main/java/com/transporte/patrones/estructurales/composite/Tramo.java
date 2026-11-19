package com.transporte.patrones.estructurales.composite;

/**
 * Hoja del Composite: un tramo directo entre dos puntos.
 */
public final class Tramo implements ComponenteRuta {

    private final String desde;
    private final String hasta;
    private final double km;

    public Tramo(String desde, String hasta, double km) {
        this.desde = desde;
        this.hasta = hasta;
        this.km = km;
    }

    @Override
    public double distanciaKm() {
        return km;
    }

    @Override
    public String describir() {
        return desde + "->" + hasta;
    }
}

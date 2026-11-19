package com.transporte.dominio;

/**
 * Valor inmutable que representa un punto geográfico (una parada de la ruta).
 */
public final class Ubicacion {

    private final String nombre;
    private final double latitud;
    private final double longitud;

    public Ubicacion(String nombre, double latitud, double longitud) {
        this.nombre = nombre;
        this.latitud = latitud;
        this.longitud = longitud;
    }

    public String getNombre() {
        return nombre;
    }

    public double getLatitud() {
        return latitud;
    }

    public double getLongitud() {
        return longitud;
    }

    @Override
    public String toString() {
        return nombre;
    }
}

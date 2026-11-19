package com.transporte.app;

import com.transporte.dominio.Ubicacion;

/**
 * Responsabilidad única: PROVEER LOS DATOS DE ENTRADA.
 *
 * Es la única fuente de datos del programa. El {@link Cliente} le pide los datos
 * que necesita y no sabe de dónde salen. Hoy devuelve valores de ejemplo fijos;
 * mañana podría leerlos de la consola, de un archivo o de una base de datos sin
 * que el resto del programa cambie.
 */
public final class Entrada {

    public Ubicacion bodegaCentral() {
        return new Ubicacion("Bodega Central", 10.0, -66.9);
    }

    public Ubicacion casaCliente() {
        return new Ubicacion("Casa del Cliente", 10.5, -66.5);
    }

    public String nombreCliente() {
        return "Ana Pérez";
    }

    public double pesoPaqueteKg() {
        return 12.5;
    }

    public String zonaTarifa() {
        return "centro";
    }

    public double distanciaEjemploKm() {
        return 15.0;
    }

    public String numeroEnvio() {
        return "ENV-0001";
    }

    public java.util.List<String> unidadesFlota() {
        return java.util.List.of("Moto AB-123", "Furgoneta CD-456", "Camión EF-789");
    }

    public java.util.List<String> nombresConductores() {
        return java.util.List.of("Luis", "Marta", "Pedro");
    }

    public String mensajeRadio() {
        return "Tráfico en la autopista, tomen la ruta 2";
    }
}

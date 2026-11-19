package com.transporte.patrones.estructurales.adapter;

import com.transporte.dominio.Ubicacion;

/**
 * Interfaz que nuestra aplicación espera para calcular distancias.
 * Es el "Target" del patrón Adapter.
 */
public interface ServicioDistancia {

    /** Distancia en kilómetros entre dos ubicaciones. */
    double calcularKm(Ubicacion origen, Ubicacion destino);
}

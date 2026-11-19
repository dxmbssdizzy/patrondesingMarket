package com.transporte.patrones.estructurales.proxy;

/**
 * Servicio real: simula una consulta costosa (p. ej. a un sistema remoto).
 */
public final class ServicioTarifasReal implements ServicioTarifas {

    @Override
    public double tarifaPorKm(String zona) {
        // Operación costosa simulada. La presentación es responsabilidad de la
        // capa de salida, no del patrón.
        return switch (zona) {
            case "centro" -> 1.2;
            case "periferia" -> 1.8;
            default -> 1.5;
        };
    }
}

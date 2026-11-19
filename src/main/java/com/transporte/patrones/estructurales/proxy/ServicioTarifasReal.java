package com.transporte.patrones.estructurales.proxy;

/**
 * Servicio real: simula una consulta costosa (p. ej. a un sistema remoto).
 */
public final class ServicioTarifasReal implements ServicioTarifas {

    @Override
    public double tarifaPorKm(String zona) {
        System.out.println("    [Proxy] Consulta COSTOSA al servicio real para zona: " + zona);
        return switch (zona) {
            case "centro" -> 1.2;
            case "periferia" -> 1.8;
            default -> 1.5;
        };
    }
}

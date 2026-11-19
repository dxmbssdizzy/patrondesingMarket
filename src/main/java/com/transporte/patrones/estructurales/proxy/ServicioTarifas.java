package com.transporte.patrones.estructurales.proxy;

/**
 * Interfaz común al servicio real y a su proxy (requisito del patrón Proxy).
 */
public interface ServicioTarifas {

    /** Consulta la tarifa por km para una zona (operación costosa). */
    double tarifaPorKm(String zona);
}

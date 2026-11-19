package com.transporte.patrones.comportamiento.chain;

import com.transporte.patrones.creacionales.builder.OrdenTransporte;

public final class ValidadorPeso extends ValidadorOrden {

    private static final double PESO_MAXIMO_KG = 10_000;

    @Override
    protected String revisar(OrdenTransporte orden) {
        if (orden.getPesoKg() <= 0) {
            return "El peso debe ser mayor que cero";
        }
        if (orden.getPesoKg() > PESO_MAXIMO_KG) {
            return "El peso supera el máximo permitido (" + PESO_MAXIMO_KG + " kg)";
        }
        return null;
    }
}

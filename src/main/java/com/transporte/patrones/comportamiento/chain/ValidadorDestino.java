package com.transporte.patrones.comportamiento.chain;

import com.transporte.patrones.creacionales.builder.OrdenTransporte;

public final class ValidadorDestino extends ValidadorOrden {

    @Override
    protected String revisar(OrdenTransporte orden) {
        if (orden.getDestino() == null) {
            return "La orden no tiene destino";
        }
        if (orden.getDestino().equals(orden.getOrigen())) {
            return "El origen y el destino no pueden ser iguales";
        }
        return null;
    }
}

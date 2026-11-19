package com.transporte.patrones.estructurales.decorator;

public final class ConEntregaUrgente extends ExtraEnvio {

    public ConEntregaUrgente(ServicioEnvio envuelto) {
        super(envuelto);
    }

    @Override
    public double costo() {
        return envuelto.costo() + 12.0;
    }

    @Override
    public String descripcion() {
        return envuelto.descripcion() + " + entrega urgente";
    }
}

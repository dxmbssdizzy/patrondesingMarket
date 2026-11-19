package com.transporte.patrones.estructurales.decorator;

public final class ConSeguro extends ExtraEnvio {

    public ConSeguro(ServicioEnvio envuelto) {
        super(envuelto);
    }

    @Override
    public double costo() {
        return envuelto.costo() + 5.0;
    }

    @Override
    public String descripcion() {
        return envuelto.descripcion() + " + seguro";
    }
}

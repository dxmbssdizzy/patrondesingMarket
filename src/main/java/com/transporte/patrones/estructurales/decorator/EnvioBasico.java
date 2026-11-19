package com.transporte.patrones.estructurales.decorator;

/**
 * Componente concreto sin extras: el servicio de envío básico.
 */
public final class EnvioBasico implements ServicioEnvio {

    private final double costoBase;

    public EnvioBasico(double costoBase) {
        this.costoBase = costoBase;
    }

    @Override
    public double costo() {
        return costoBase;
    }

    @Override
    public String descripcion() {
        return "Envío básico";
    }
}

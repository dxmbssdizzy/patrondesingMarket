package com.transporte.patrones.estructurales.bridge;

public final class EnvioNacional extends Envio {

    public EnvioNacional(MedioTransporte medio) {
        super(medio);
    }

    @Override
    public String entregar() {
        return "Envío nacional entregado " + medio.mover();
    }
}

package com.transporte.patrones.estructurales.bridge;

public final class EnvioInternacional extends Envio {

    public EnvioInternacional(MedioTransporte medio) {
        super(medio);
    }

    @Override
    public String entregar() {
        return "Envío internacional (con aduana) entregado " + medio.mover();
    }
}

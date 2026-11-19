package com.transporte.patrones.estructurales.bridge;

public final class TransporteAereo implements MedioTransporte {

    @Override
    public String mover() {
        return "por vía aérea";
    }
}

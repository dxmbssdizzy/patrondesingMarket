package com.transporte.patrones.estructurales.bridge;

public final class TransporteTerrestre implements MedioTransporte {

    @Override
    public String mover() {
        return "por carretera";
    }
}

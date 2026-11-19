package com.transporte.patrones.comportamiento.visitor;

public final class EnvioLocal implements ElementoFacturable {

    private final double km;

    public EnvioLocal(double km) {
        this.km = km;
    }

    public double getKm() {
        return km;
    }

    @Override
    public double aceptar(VisitanteCobro visitante) {
        return visitante.visitarEnvioLocal(this);
    }
}

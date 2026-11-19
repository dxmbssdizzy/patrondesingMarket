package com.transporte.patrones.comportamiento.visitor;

public final class EnvioInternacional implements ElementoFacturable {

    private final double km;
    private final double aranceles;

    public EnvioInternacional(double km, double aranceles) {
        this.km = km;
        this.aranceles = aranceles;
    }

    public double getKm() {
        return km;
    }

    public double getAranceles() {
        return aranceles;
    }

    @Override
    public double aceptar(VisitanteCobro visitante) {
        return visitante.visitarEnvioInternacional(this);
    }
}

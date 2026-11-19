package com.transporte.patrones.comportamiento.visitor;

/**
 * Visitante concreto que calcula el importe de facturación de cada tipo de envío.
 */
public final class VisitanteFacturacion implements VisitanteCobro {

    @Override
    public double visitarEnvioLocal(EnvioLocal envio) {
        return envio.getKm() * 1.5;
    }

    @Override
    public double visitarEnvioInternacional(EnvioInternacional envio) {
        return envio.getKm() * 2.0 + envio.getAranceles();
    }
}

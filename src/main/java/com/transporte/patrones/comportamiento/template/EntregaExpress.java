package com.transporte.patrones.comportamiento.template;

public final class EntregaExpress extends ProcesoEntrega {

    @Override
    protected String recoger() {
        return "Recogida prioritaria en 15 minutos.";
    }

    @Override
    protected String transportar() {
        return "Transporte directo sin paradas.";
    }
}

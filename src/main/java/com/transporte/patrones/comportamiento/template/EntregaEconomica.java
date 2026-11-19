package com.transporte.patrones.comportamiento.template;

public final class EntregaEconomica extends ProcesoEntrega {

    @Override
    protected String recoger() {
        return "Recogida agrupada al día siguiente.";
    }

    @Override
    protected String transportar() {
        return "Transporte con paradas compartidas.";
    }
}

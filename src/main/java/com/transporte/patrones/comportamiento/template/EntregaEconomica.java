package com.transporte.patrones.comportamiento.template;

public final class EntregaEconomica extends ProcesoEntrega {

    @Override
    protected void recoger() {
        System.out.println("    [Template Method] Recogida agrupada al día siguiente.");
    }

    @Override
    protected void transportar() {
        System.out.println("    [Template Method] Transporte con paradas compartidas.");
    }
}

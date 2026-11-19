package com.transporte.patrones.comportamiento.template;

public final class EntregaExpress extends ProcesoEntrega {

    @Override
    protected void recoger() {
        System.out.println("    [Template Method] Recogida prioritaria en 15 minutos.");
    }

    @Override
    protected void transportar() {
        System.out.println("    [Template Method] Transporte directo sin paradas.");
    }
}

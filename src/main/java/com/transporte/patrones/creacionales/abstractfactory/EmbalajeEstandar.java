package com.transporte.patrones.creacionales.abstractfactory;

public final class EmbalajeEstandar implements Embalaje {

    @Override
    public String tipo() {
        return "Caja de cartón estándar";
    }
}

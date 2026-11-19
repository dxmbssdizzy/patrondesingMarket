package com.transporte.patrones.creacionales.abstractfactory;

public final class EmbalajePremium implements Embalaje {

    @Override
    public String tipo() {
        return "Caja reforzada con protección acolchada";
    }
}

package com.transporte.patrones.creacionales.abstractfactory;

import com.transporte.patrones.creacionales.factory.Furgoneta;
import com.transporte.patrones.creacionales.factory.Vehiculo;

public final class FabricaServicioPremium implements FabricaServicio {

    @Override
    public Vehiculo crearVehiculo() {
        return new Furgoneta();
    }

    @Override
    public Embalaje crearEmbalaje() {
        return new EmbalajePremium();
    }
}

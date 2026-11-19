package com.transporte.patrones.creacionales.abstractfactory;

import com.transporte.patrones.creacionales.factory.Moto;
import com.transporte.patrones.creacionales.factory.Vehiculo;

public final class FabricaServicioEconomico implements FabricaServicio {

    @Override
    public Vehiculo crearVehiculo() {
        return new Moto();
    }

    @Override
    public Embalaje crearEmbalaje() {
        return new EmbalajeEstandar();
    }
}

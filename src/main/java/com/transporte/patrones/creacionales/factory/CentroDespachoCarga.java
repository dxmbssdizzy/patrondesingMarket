package com.transporte.patrones.creacionales.factory;

public final class CentroDespachoCarga extends CentroDespacho {

    @Override
    protected Vehiculo crearVehiculo() {
        return new Camion();
    }
}

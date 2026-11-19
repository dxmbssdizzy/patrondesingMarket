package com.transporte.patrones.creacionales.factory;

public final class CentroDespachoUrbano extends CentroDespacho {

    @Override
    protected Vehiculo crearVehiculo() {
        return new Moto();
    }
}

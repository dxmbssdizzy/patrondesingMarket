package com.transporte.patrones.estructurales.decorator;

/**
 * Decorador base: envuelve un {@link ServicioEnvio} y reenvía las llamadas.
 * Las subclases añaden su costo y descripción al del servicio envuelto.
 */
public abstract class ExtraEnvio implements ServicioEnvio {

    protected final ServicioEnvio envuelto;

    protected ExtraEnvio(ServicioEnvio envuelto) {
        this.envuelto = envuelto;
    }
}

package com.transporte.patrones.estructurales.facade;

import com.transporte.dominio.Ubicacion;
import com.transporte.patrones.estructurales.adapter.ServicioDistancia;
import com.transporte.patrones.estructurales.proxy.ServicioTarifas;

/**
 * PATRÓN FACADE (Estructural).
 *
 * Ofrece una interfaz única y simple ("cotizar un envío") que esconde la
 * complejidad de coordinar varios subsistemas: el cálculo de distancia
 * (Adapter) y la consulta de tarifas (Proxy). El cliente solo habla con la
 * fachada y no necesita conocer el subsistema.
 */
public final class FachadaReservas {

    private final ServicioDistancia servicioDistancia;
    private final ServicioTarifas servicioTarifas;

    public FachadaReservas(ServicioDistancia servicioDistancia, ServicioTarifas servicioTarifas) {
        this.servicioDistancia = servicioDistancia;
        this.servicioTarifas = servicioTarifas;
    }

    public double cotizar(Ubicacion origen, Ubicacion destino, String zona) {
        double km = servicioDistancia.calcularKm(origen, destino);
        double tarifa = servicioTarifas.tarifaPorKm(zona);
        return km * tarifa;
    }
}

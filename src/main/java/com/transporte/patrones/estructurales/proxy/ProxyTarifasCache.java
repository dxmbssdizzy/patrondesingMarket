package com.transporte.patrones.estructurales.proxy;

import java.util.HashMap;
import java.util.Map;

/**
 * PATRÓN PROXY (Estructural).
 *
 * Proxy de caché: tiene la misma interfaz que {@link ServicioTarifasReal} y lo
 * sustituye de forma transparente. Guarda resultados ya consultados para evitar
 * repetir la operación costosa. El cliente no nota la diferencia.
 */
public final class ProxyTarifasCache implements ServicioTarifas {

    private final ServicioTarifas servicioReal;
    private final Map<String, Double> cache = new HashMap<>();

    public ProxyTarifasCache(ServicioTarifas servicioReal) {
        this.servicioReal = servicioReal;
    }

    @Override
    public double tarifaPorKm(String zona) {
        if (cache.containsKey(zona)) {
            System.out.println("    [Proxy] Tarifa servida desde CACHÉ para zona: " + zona);
            return cache.get(zona);
        }
        double tarifa = servicioReal.tarifaPorKm(zona);
        cache.put(zona, tarifa);
        return tarifa;
    }
}

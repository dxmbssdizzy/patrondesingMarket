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

    private int consultasReales;
    private int consultasEnCache;

    public ProxyTarifasCache(ServicioTarifas servicioReal) {
        this.servicioReal = servicioReal;
    }

    @Override
    public double tarifaPorKm(String zona) {
        if (cache.containsKey(zona)) {
            consultasEnCache++;
            return cache.get(zona);
        }
        consultasReales++;
        double tarifa = servicioReal.tarifaPorKm(zona);
        cache.put(zona, tarifa);
        return tarifa;
    }

    /** Veces que hubo que ir al servicio real (consulta costosa). */
    public int consultasReales() {
        return consultasReales;
    }

    /** Veces que la tarifa se sirvió desde la caché. */
    public int consultasEnCache() {
        return consultasEnCache;
    }
}

package com.transporte.patrones.estructurales.flyweight;

import java.util.HashMap;
import java.util.Map;

/**
 * Fábrica de flyweights: garantiza que cada modelo se cree UNA sola vez y se
 * reutilice. Si el modelo ya existe en la caché, devuelve la misma instancia.
 */
public final class FabricaModelos {

    private final Map<String, ModeloVehiculo> cache = new HashMap<>();

    public ModeloVehiculo obtener(String marca, String modelo, double consumoLitrosPorKm) {
        String clave = marca + "|" + modelo;
        return cache.computeIfAbsent(clave,
                k -> new ModeloVehiculo(marca, modelo, consumoLitrosPorKm));
    }

    public int modelosCreados() {
        return cache.size();
    }
}

package com.transporte.patrones.estructurales.adapter;

import com.transporte.dominio.Ubicacion;

/**
 * PATRÓN ADAPTER (Estructural).
 *
 * Adapta la {@link ApiMapasExterna} (coordenadas crudas, metros) a la interfaz
 * {@link ServicioDistancia} que nuestra aplicación entiende (ubicaciones, km).
 * El resto del sistema no se entera de la API externa.
 */
public final class AdaptadorApiMapas implements ServicioDistancia {

    private final ApiMapasExterna apiExterna;

    public AdaptadorApiMapas(ApiMapasExterna apiExterna) {
        this.apiExterna = apiExterna;
    }

    @Override
    public double calcularKm(Ubicacion origen, Ubicacion destino) {
        double metros = apiExterna.distanciaEnMetros(
                origen.getLatitud(), origen.getLongitud(),
                destino.getLatitud(), destino.getLongitud());
        return metros / 1000.0;
    }
}

package com.transporte.patrones.creacionales.prototype;

import com.transporte.dominio.Ubicacion;
import java.util.ArrayList;
import java.util.List;

/**
 * PATRÓN PROTOTYPE (Creacional).
 *
 * Permite crear nuevas rutas copiando una plantilla ya configurada, en vez de
 * construirlas desde cero. El método {@link #clonar()} devuelve una copia
 * independiente (copia profunda de la lista de paradas).
 */
public final class PlantillaRuta {

    private String nombre;
    private final List<Ubicacion> paradas;

    public PlantillaRuta(String nombre) {
        this.nombre = nombre;
        this.paradas = new ArrayList<>();
    }

    /** Constructor de copia usado por {@link #clonar()}. */
    private PlantillaRuta(PlantillaRuta original) {
        this.nombre = original.nombre;
        this.paradas = new ArrayList<>(original.paradas);
    }

    public PlantillaRuta agregarParada(Ubicacion parada) {
        paradas.add(parada);
        return this;
    }

    public void renombrar(String nuevoNombre) {
        this.nombre = nuevoNombre;
    }

    public PlantillaRuta clonar() {
        return new PlantillaRuta(this);
    }

    public String getNombre() {
        return nombre;
    }

    public List<Ubicacion> getParadas() {
        return List.copyOf(paradas);
    }

    @Override
    public String toString() {
        return nombre + " " + paradas;
    }
}

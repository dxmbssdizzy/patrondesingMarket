package com.transporte.patrones.estructurales.composite;

import java.util.ArrayList;
import java.util.List;
import java.util.StringJoiner;

/**
 * Compuesto del Composite: una ruta formada por varios componentes, que a su
 * vez pueden ser tramos u otras rutas. Delega las operaciones en sus hijos.
 */
public final class RutaCompuesta implements ComponenteRuta {

    private final String nombre;
    private final List<ComponenteRuta> componentes = new ArrayList<>();

    public RutaCompuesta(String nombre) {
        this.nombre = nombre;
    }

    public RutaCompuesta agregar(ComponenteRuta componente) {
        componentes.add(componente);
        return this;
    }

    @Override
    public double distanciaKm() {
        return componentes.stream().mapToDouble(ComponenteRuta::distanciaKm).sum();
    }

    @Override
    public String describir() {
        StringJoiner joiner = new StringJoiner(" + ", nombre + "(", ")");
        for (ComponenteRuta componente : componentes) {
            joiner.add(componente.describir());
        }
        return joiner.toString();
    }
}

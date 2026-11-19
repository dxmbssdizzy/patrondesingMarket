package com.transporte.patrones.comportamiento.iterator;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

/**
 * PATRÓN ITERATOR (Comportamiento).
 *
 * La flota es una colección que expone un {@link Iterator} para recorrer sus
 * unidades sin revelar su estructura interna. Implementa {@link Iterable} para
 * integrarse con el for-each de Java de forma idiomática.
 */
public final class Flota implements Iterable<String> {

    private final List<String> unidades = new ArrayList<>();

    public void agregar(String unidad) {
        unidades.add(unidad);
    }

    @Override
    public Iterator<String> iterator() {
        return new IteradorFlota();
    }

    /** Iterador concreto que recorre las unidades en orden. */
    private final class IteradorFlota implements Iterator<String> {

        private int indice = 0;

        @Override
        public boolean hasNext() {
            return indice < unidades.size();
        }

        @Override
        public String next() {
            if (!hasNext()) {
                throw new NoSuchElementException("No hay más unidades en la flota");
            }
            return unidades.get(indice++);
        }
    }
}

package com.transporte.patrones.comportamiento.strategy;

/**
 * PATRÓN STRATEGY (Comportamiento).
 *
 * Define una familia de algoritmos de cálculo de precio intercambiables.
 * El contexto elige una estrategia concreta en tiempo de ejecución sin cambiar
 * su propio código (abierto/cerrado, OCP de SOLID).
 */
public interface EstrategiaTarifa {

    double calcular(double distanciaKm, double pesoKg);

    String nombre();
}

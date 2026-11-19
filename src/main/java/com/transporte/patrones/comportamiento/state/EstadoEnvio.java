package com.transporte.patrones.comportamiento.state;

/**
 * PATRÓN STATE (Comportamiento).
 *
 * Representa un estado del ciclo de vida del envío. Cada estado concreto sabe
 * cuál es el siguiente y su propio nombre, de modo que la transición vive en
 * los estados y no en una cadena de if/switch (evita el antipatrón de
 * condicionales gigantes).
 */
public interface EstadoEnvio {

    /** Devuelve el estado al que se avanza; si es final, se devuelve a sí mismo. */
    EstadoEnvio siguiente();

    String nombre();

    boolean esFinal();
}

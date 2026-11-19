package com.transporte.app;

/**
 * Responsabilidad única: PRESENTACIÓN.
 *
 * Es el único punto del programa que escribe en la salida estándar. Ninguna
 * clase de patrón imprime por su cuenta: todas devuelven datos y el {@link Cliente}
 * se los entrega a esta clase para que los interprete y los muestre.
 *
 * Así, si mañana se quisiera escribir a un archivo, a un log o a una interfaz
 * gráfica, solo cambiaría esta clase.
 */
public final class Salida {

    public void titulo(String texto) {
        System.out.println("===== " + texto + " =====\n");
    }

    public void seccion(String texto) {
        System.out.println("--- " + texto + " ---");
    }

    /** Línea de un patrón: la etiqueta entre corchetes y su mensaje. */
    public void patron(String patron, String mensaje) {
        System.out.println("  [" + patron + "] " + mensaje);
    }

    /** Línea de detalle, con sangría mayor (sub-paso de un patrón). */
    public void detalle(String mensaje) {
        System.out.println("    " + mensaje);
    }

    public void linea(String texto) {
        System.out.println(texto);
    }

    public void saltoLinea() {
        System.out.println();
    }
}

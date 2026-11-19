package com.transporte;

import com.transporte.app.Cliente;
import com.transporte.app.Entrada;
import com.transporte.app.Salida;

/**
 * Punto de entrada de la aplicación.
 *
 * Su única responsabilidad es ensamblar las piezas (Entrada, Salida, Cliente) y
 * ejecutar el Cliente. Toda la lógica vive en {@link Cliente}; la entrada y la
 * salida de datos viven en {@link Entrada} y {@link Salida}.
 */
public final class Main {

    public static void main(String[] args) {
        Entrada entrada = new Entrada();
        Salida salida = new Salida();
        Cliente cliente = new Cliente(entrada, salida);
        cliente.ejecutar();
    }
}

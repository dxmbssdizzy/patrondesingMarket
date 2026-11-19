package com.transporte.patrones.estructurales.decorator;

/**
 * PATRÓN DECORATOR (Estructural).
 *
 * Componente base: un servicio de envío con un costo y una descripción.
 * Los decoradores añadirán responsabilidades (extras) envolviendo este objeto.
 */
public interface ServicioEnvio {

    double costo();

    String descripcion();
}

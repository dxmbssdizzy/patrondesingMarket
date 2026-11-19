package com.transporte.patrones.creacionales.abstractfactory;

import com.transporte.patrones.creacionales.factory.Vehiculo;

/**
 * PATRÓN ABSTRACT FACTORY (Creacional).
 *
 * Declara la creación de una FAMILIA de productos relacionados (vehículo +
 * embalaje) sin acoplar al cliente a las clases concretas. Cada fábrica concreta
 * garantiza que los productos que entrega son coherentes entre sí
 * (p. ej. el servicio premium siempre combina furgoneta con embalaje premium).
 */
public interface FabricaServicio {

    Vehiculo crearVehiculo();

    Embalaje crearEmbalaje();
}

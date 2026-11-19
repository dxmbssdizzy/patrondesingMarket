package com.transporte.patrones.creacionales.factory;

/**
 * PATRÓN FACTORY METHOD (Creacional).
 *
 * Define el esqueleto para asignar un vehículo a un despacho, pero deja que las
 * subclases decidan QUÉ vehículo concreto crear mediante el método fábrica
 * {@link #crearVehiculo()}.
 *
 * Así el código que asigna vehículos no depende de clases concretas (DIP de SOLID).
 */
public abstract class CentroDespacho {

    /** Método fábrica: cada centro decide qué vehículo produce. */
    protected abstract Vehiculo crearVehiculo();

    /** Operación de negocio que usa el producto creado por el método fábrica. */
    public Vehiculo asignarVehiculo() {
        Vehiculo vehiculo = crearVehiculo();
        System.out.println("  [Factory Method] Asignado: " + vehiculo.descripcion()
                + " (" + vehiculo.capacidadKg() + " kg)");
        return vehiculo;
    }
}

package com.transporte.app;

import com.transporte.dominio.Ubicacion;
import com.transporte.patrones.creacionales.abstractfactory.Embalaje;
import com.transporte.patrones.creacionales.abstractfactory.FabricaServicio;
import com.transporte.patrones.creacionales.abstractfactory.FabricaServicioPremium;
import com.transporte.patrones.creacionales.builder.OrdenTransporte;
import com.transporte.patrones.creacionales.factory.CentroDespachoUrbano;
import com.transporte.patrones.creacionales.factory.Vehiculo;
import com.transporte.patrones.creacionales.prototype.PlantillaRuta;
import com.transporte.patrones.creacionales.singleton.ConfiguracionEmpresa;

/**
 * Responsabilidad única: LÓGICA CENTRAL.
 *
 * El Cliente orquesta el escenario de negocio usando los patrones de diseño.
 * Obtiene todos sus datos de {@link Entrada} y envía todo lo que hay que mostrar
 * a {@link Salida}. No lee ni imprime por su cuenta: así la lógica queda separada
 * de la entrada y la salida (principio de responsabilidad única).
 */
public final class Cliente {

    private final Entrada entrada;
    private final Salida salida;

    public Cliente(Entrada entrada, Salida salida) {
        this.entrada = entrada;
        this.salida = salida;
    }

    /** Punto de arranque de la lógica, invocado por Main. */
    public void ejecutar() {
        ConfiguracionEmpresa config = ConfiguracionEmpresa.getInstancia();
        salida.titulo(config.getNombreEmpresa() + " — Simulación de un envío");

        creacionales();

        salida.titulo("Fin de la simulación");
    }

    // ---------------------------------------------------------------------
    // PATRONES CREACIONALES
    // ---------------------------------------------------------------------
    private void creacionales() {
        salida.seccion("Creacionales");

        Ubicacion bodega = entrada.bodegaCentral();
        Ubicacion cliente = entrada.casaCliente();

        // SINGLETON: una única configuración compartida en todo el programa.
        ConfiguracionEmpresa config = ConfiguracionEmpresa.getInstancia();
        salida.patron("Singleton", "Empresa: " + config.getNombreEmpresa()
                + " | Moneda: " + config.getMoneda());

        // BUILDER: se arma una orden compleja paso a paso.
        OrdenTransporte orden = new OrdenTransporte.Builder(entrada.nombreCliente(), bodega, cliente)
                .conPeso(entrada.pesoPaqueteKg())
                .fragil()
                .urgente()
                .construir();
        salida.patron("Builder", orden.toString());

        // FACTORY METHOD: un centro urbano decide qué vehículo crear.
        Vehiculo vehiculo = new CentroDespachoUrbano().asignarVehiculo();
        salida.patron("Factory Method", "Asignado: " + vehiculo.descripcion()
                + " (" + vehiculo.capacidadKg() + " kg)");

        // ABSTRACT FACTORY: familia coherente de productos (premium).
        FabricaServicio fabrica = new FabricaServicioPremium();
        Vehiculo vehiculoPremium = fabrica.crearVehiculo();
        Embalaje embalaje = fabrica.crearEmbalaje();
        salida.patron("Abstract Factory", "Servicio premium: "
                + vehiculoPremium.descripcion() + " + " + embalaje.tipo());

        // PROTOTYPE: se clona una plantilla de ruta y se adapta el clon.
        PlantillaRuta base = new PlantillaRuta("Ruta base")
                .agregarParada(bodega)
                .agregarParada(cliente);
        PlantillaRuta copia = base.clonar();
        copia.renombrar("Ruta del día");
        salida.patron("Prototype", "Original: " + base);
        salida.patron("Prototype", "Clon:     " + copia);

        salida.saltoLinea();
    }
}

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
import com.transporte.patrones.estructurales.adapter.AdaptadorApiMapas;
import com.transporte.patrones.estructurales.adapter.ApiMapasExterna;
import com.transporte.patrones.estructurales.adapter.ServicioDistancia;
import com.transporte.patrones.estructurales.bridge.EnvioNacional;
import com.transporte.patrones.estructurales.bridge.TransporteAereo;
import com.transporte.patrones.estructurales.composite.ComponenteRuta;
import com.transporte.patrones.estructurales.composite.RutaCompuesta;
import com.transporte.patrones.estructurales.composite.Tramo;
import com.transporte.patrones.estructurales.decorator.ConEntregaUrgente;
import com.transporte.patrones.estructurales.decorator.ConSeguro;
import com.transporte.patrones.estructurales.decorator.EnvioBasico;
import com.transporte.patrones.estructurales.decorator.ServicioEnvio;
import com.transporte.patrones.estructurales.facade.FachadaReservas;
import com.transporte.patrones.estructurales.flyweight.FabricaModelos;
import com.transporte.patrones.estructurales.flyweight.ModeloVehiculo;
import com.transporte.patrones.estructurales.flyweight.UnidadFlota;
import com.transporte.patrones.estructurales.proxy.ProxyTarifasCache;
import com.transporte.patrones.estructurales.proxy.ServicioTarifasReal;

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
        estructurales();

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

    // ---------------------------------------------------------------------
    // PATRONES ESTRUCTURALES
    // ---------------------------------------------------------------------
    private void estructurales() {
        salida.seccion("Estructurales");

        Ubicacion bodega = entrada.bodegaCentral();
        Ubicacion cliente = entrada.casaCliente();
        String zona = entrada.zonaTarifa();

        // ADAPTER: adaptamos una API de mapas externa a nuestra interfaz.
        ServicioDistancia distancia = new AdaptadorApiMapas(new ApiMapasExterna());

        // PROXY: envolvemos el servicio de tarifas con una caché.
        ProxyTarifasCache tarifas = new ProxyTarifasCache(new ServicioTarifasReal());

        // FACADE: una sola llamada esconde distancia (Adapter) + tarifa (Proxy).
        FachadaReservas reservas = new FachadaReservas(distancia, tarifas);
        double costo1 = reservas.cotizar(bodega, cliente, zona);
        double costo2 = reservas.cotizar(bodega, cliente, zona); // segunda vez: caché
        salida.patron("Facade", String.format("Cotización 1: %.2f | Cotización 2: %.2f",
                costo1, costo2));
        salida.patron("Proxy", "Consultas reales: " + tarifas.consultasReales()
                + " | Servidas desde caché: " + tarifas.consultasEnCache());

        // BRIDGE: tipo de envío y medio de transporte varían por separado.
        EnvioNacional envio = new EnvioNacional(new TransporteAereo());
        salida.patron("Bridge", envio.entregar());

        // COMPOSITE: una ruta compuesta por tramos y sub-rutas.
        ComponenteRuta primeraMilla = new Tramo("Bodega", "Hub", 8.0);
        RutaCompuesta ultimaMilla = new RutaCompuesta("Última milla")
                .agregar(new Tramo("Hub", "Barrio", 5.0))
                .agregar(new Tramo("Barrio", "Cliente", 2.0));
        RutaCompuesta rutaTotal = new RutaCompuesta("Ruta total")
                .agregar(primeraMilla)
                .agregar(ultimaMilla);
        salida.patron("Composite", String.format("%s = %.1f km",
                rutaTotal.describir(), rutaTotal.distanciaKm()));

        // DECORATOR: añadimos extras al envío básico.
        ServicioEnvio servicio = new ConEntregaUrgente(new ConSeguro(new EnvioBasico(10.0)));
        salida.patron("Decorator", String.format("%s = %.2f",
                servicio.descripcion(), servicio.costo()));

        // FLYWEIGHT: muchas unidades comparten el mismo objeto "modelo".
        FabricaModelos modelos = new FabricaModelos();
        ModeloVehiculo sprinter = modelos.obtener("Mercedes", "Sprinter", 0.12);
        UnidadFlota u1 = new UnidadFlota("AB-123", sprinter);
        UnidadFlota u2 = new UnidadFlota("CD-456",
                modelos.obtener("Mercedes", "Sprinter", 0.12));
        salida.patron("Flyweight", u1.descripcion() + " y " + u2.descripcion());
        salida.patron("Flyweight", "Modelos distintos creados en memoria: "
                + modelos.modelosCreados());

        salida.saltoLinea();
    }
}

package com.transporte;

import com.transporte.dominio.Ubicacion;
import com.transporte.patrones.comportamiento.chain.ValidadorDestino;
import com.transporte.patrones.comportamiento.chain.ValidadorOrden;
import com.transporte.patrones.comportamiento.chain.ValidadorPeso;
import com.transporte.patrones.comportamiento.command.AvanzarEnvioComando;
import com.transporte.patrones.comportamiento.command.PanelOperaciones;
import com.transporte.patrones.comportamiento.iterator.Flota;
import com.transporte.patrones.comportamiento.mediator.CentroDespachoRadio;
import com.transporte.patrones.comportamiento.mediator.Conductor;
import com.transporte.patrones.comportamiento.memento.Paquete;
import com.transporte.patrones.comportamiento.observer.NotificadorCliente;
import com.transporte.patrones.comportamiento.strategy.EstrategiaTarifa;
import com.transporte.patrones.comportamiento.strategy.TarifaPorDistancia;
import com.transporte.patrones.comportamiento.strategy.TarifaPorPeso;
import com.transporte.patrones.comportamiento.template.EntregaEconomica;
import com.transporte.patrones.comportamiento.template.EntregaExpress;
import com.transporte.patrones.comportamiento.template.ProcesoEntrega;
import com.transporte.patrones.comportamiento.visitor.ElementoFacturable;
import com.transporte.patrones.comportamiento.visitor.EnvioLocal;
import com.transporte.patrones.comportamiento.visitor.VisitanteFacturacion;
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
import com.transporte.patrones.estructurales.proxy.ServicioTarifas;
import com.transporte.patrones.estructurales.proxy.ServicioTarifasReal;
import java.util.List;

/**
 * Escenario de negocio de la empresa de transporte TransExpress.
 *
 * Simula el ciclo completo de un envío y, en cada paso del negocio, usa uno o
 * varios de los 23 patrones de diseño GoF. Todos coexisten en el mismo flujo.
 */
public final class Main {

    public static void main(String[] args) {
        ConfiguracionEmpresa config = ConfiguracionEmpresa.getInstancia();
        System.out.println("===== " + config.getNombreEmpresa()
                + " — Simulación de un envío =====\n");

        Ubicacion bodega = new Ubicacion("Bodega Central", 10.0, -66.9);
        Ubicacion cliente = new Ubicacion("Casa del Cliente", 10.5, -66.5);

        creacionales(bodega, cliente);
        estructurales(bodega, cliente);
        comportamiento();

        System.out.println("\n===== Fin de la simulación =====");
    }

    // ---------------------------------------------------------------------
    // PATRONES CREACIONALES
    // ---------------------------------------------------------------------
    private static void creacionales(Ubicacion bodega, Ubicacion cliente) {
        System.out.println("--- Creacionales ---");

        // SINGLETON ya se usó arriba para la configuración.

        // BUILDER: se arma una orden compleja paso a paso.
        OrdenTransporte orden = new OrdenTransporte.Builder("Ana Pérez", bodega, cliente)
                .conPeso(12.5)
                .fragil()
                .urgente()
                .construir();
        System.out.println("  [Builder] " + orden);

        // FACTORY METHOD: un centro urbano decide qué vehículo asignar.
        new CentroDespachoUrbano().asignarVehiculo();

        // ABSTRACT FACTORY: familia coherente de productos (premium).
        FabricaServicio fabrica = new FabricaServicioPremium();
        Vehiculo vehiculoPremium = fabrica.crearVehiculo();
        Embalaje embalaje = fabrica.crearEmbalaje();
        System.out.println("  [Abstract Factory] Servicio premium: "
                + vehiculoPremium.descripcion() + " + " + embalaje.tipo());

        // PROTOTYPE: se clona una plantilla de ruta y se adapta.
        PlantillaRuta base = new PlantillaRuta("Ruta base")
                .agregarParada(bodega)
                .agregarParada(cliente);
        PlantillaRuta copia = base.clonar();
        copia.renombrar("Ruta del día");
        System.out.println("  [Prototype] Original: " + base);
        System.out.println("  [Prototype] Clon:     " + copia);

        System.out.println();
    }

    // ---------------------------------------------------------------------
    // PATRONES ESTRUCTURALES
    // ---------------------------------------------------------------------
    private static void estructurales(Ubicacion bodega, Ubicacion cliente) {
        System.out.println("--- Estructurales ---");

        // ADAPTER: adaptamos una API de mapas externa a nuestra interfaz.
        ServicioDistancia distancia = new AdaptadorApiMapas(new ApiMapasExterna());

        // PROXY: envolvemos el servicio de tarifas con una caché.
        ServicioTarifas tarifas = new ProxyTarifasCache(new ServicioTarifasReal());

        // FACADE: una sola llamada esconde distancia (Adapter) + tarifa (Proxy).
        FachadaReservas reservas = new FachadaReservas(distancia, tarifas);
        double costo1 = reservas.cotizar(bodega, cliente, "centro");
        double costo2 = reservas.cotizar(bodega, cliente, "centro"); // segunda vez: caché
        System.out.printf("  [Facade] Cotización 1: %.2f | Cotización 2: %.2f%n", costo1, costo2);

        // BRIDGE: tipo de envío y medio de transporte varían por separado.
        EnvioNacional envio = new EnvioNacional(new TransporteAereo());
        System.out.println("  [Bridge] " + envio.entregar());

        // COMPOSITE: una ruta compuesta por tramos y sub-rutas.
        ComponenteRuta primeraMilla = new Tramo("Bodega", "Hub", 8.0);
        RutaCompuesta ultimaMilla = new RutaCompuesta("Última milla")
                .agregar(new Tramo("Hub", "Barrio", 5.0))
                .agregar(new Tramo("Barrio", "Cliente", 2.0));
        RutaCompuesta rutaTotal = new RutaCompuesta("Ruta total")
                .agregar(primeraMilla)
                .agregar(ultimaMilla);
        System.out.printf("  [Composite] %s = %.1f km%n",
                rutaTotal.describir(), rutaTotal.distanciaKm());

        // DECORATOR: añadimos extras al envío básico.
        ServicioEnvio servicio = new ConEntregaUrgente(new ConSeguro(new EnvioBasico(10.0)));
        System.out.printf("  [Decorator] %s = %.2f%n",
                servicio.descripcion(), servicio.costo());

        // FLYWEIGHT: muchas unidades comparten el mismo objeto "modelo".
        FabricaModelos modelos = new FabricaModelos();
        ModeloVehiculo sprinter = modelos.obtener("Mercedes", "Sprinter", 0.12);
        UnidadFlota u1 = new UnidadFlota("AB-123", sprinter);
        UnidadFlota u2 = new UnidadFlota("CD-456", modelos.obtener("Mercedes", "Sprinter", 0.12));
        System.out.println("  [Flyweight] " + u1.descripcion() + " y " + u2.descripcion());
        System.out.println("  [Flyweight] Modelos distintos creados en memoria: "
                + modelos.modelosCreados());

        System.out.println();
    }

    // ---------------------------------------------------------------------
    // PATRONES DE COMPORTAMIENTO
    // ---------------------------------------------------------------------
    private static void comportamiento() {
        System.out.println("--- Comportamiento ---");

        Ubicacion bodega = new Ubicacion("Bodega Central", 10.0, -66.9);
        Ubicacion cliente = new Ubicacion("Casa del Cliente", 10.5, -66.5);

        // CHAIN OF RESPONSIBILITY: validamos la orden con una cadena.
        OrdenTransporte orden = new OrdenTransporte.Builder("Ana Pérez", bodega, cliente)
                .conPeso(12.5)
                .construir();
        ValidadorOrden validador = new ValidadorPeso();
        validador.encadenar(new ValidadorDestino());
        String error = validador.validar(orden);
        System.out.println("  [Chain of Responsibility] Validación: "
                + (error == null ? "OK" : "ERROR -> " + error));

        // STRATEGY: elegimos el algoritmo de tarifa en tiempo de ejecución.
        for (EstrategiaTarifa estrategia : List.of(new TarifaPorDistancia(), new TarifaPorPeso())) {
            double precio = estrategia.calcular(15.0, 12.5);
            System.out.printf("  [Strategy] Tarifa %s = %.2f%n", estrategia.nombre(), precio);
        }

        // OBSERVER + STATE + MEMENTO + COMMAND trabajando sobre un mismo paquete.
        Paquete paquete = new Paquete("ENV-0001");
        paquete.suscribir(new NotificadorCliente("SMS"));
        paquete.suscribir(new NotificadorCliente("Email"));

        PanelOperaciones panel = new PanelOperaciones();
        System.out.println("  [State] Estado inicial: " + paquete.estadoActual());
        panel.ejecutar(new AvanzarEnvioComando(paquete)); // -> EN_RUTA (notifica: Observer)
        panel.ejecutar(new AvanzarEnvioComando(paquete)); // -> ENTREGADO (notifica: Observer)
        System.out.println("  [State] Estado final: " + paquete.estadoActual());
        panel.deshacerUltimo(); // Command + Memento: vuelve a EN_RUTA
        System.out.println("  [State] Tras deshacer: " + paquete.estadoActual());

        // ITERATOR: recorremos la flota sin conocer su estructura interna.
        Flota flota = new Flota();
        flota.agregar("Moto AB-123");
        flota.agregar("Furgoneta CD-456");
        flota.agregar("Camión EF-789");
        System.out.print("  [Iterator] Flota:");
        for (String unidad : flota) {
            System.out.print(" [" + unidad + "]");
        }
        System.out.println();

        // MEDIATOR: los conductores se coordinan a través del centro de despacho.
        CentroDespachoRadio central = new CentroDespachoRadio();
        Conductor luis = new Conductor("Luis", central);
        new Conductor("Marta", central);
        new Conductor("Pedro", central);
        luis.transmitir("Tráfico en la autopista, tomen la ruta 2");

        // TEMPLATE METHOD: el esqueleto del proceso de entrega es fijo.
        System.out.println("  [Template Method] Entrega Express:");
        ProcesoEntrega express = new EntregaExpress();
        express.procesar();
        System.out.println("  [Template Method] Entrega Económica:");
        ProcesoEntrega economica = new EntregaEconomica();
        economica.procesar();

        // VISITOR: un visitante de facturación recorre envíos de distinto tipo.
        VisitanteFacturacion facturacion = new VisitanteFacturacion();
        List<ElementoFacturable> facturables = List.of(
                new EnvioLocal(15.0),
                new com.transporte.patrones.comportamiento.visitor.EnvioInternacional(1200.0, 50.0));
        double total = 0;
        for (ElementoFacturable elemento : facturables) {
            total += elemento.aceptar(facturacion);
        }
        System.out.printf("  [Visitor] Facturación total: %.2f%n", total);

        System.out.println();
    }
}

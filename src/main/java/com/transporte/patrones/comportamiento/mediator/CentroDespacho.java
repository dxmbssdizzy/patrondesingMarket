package com.transporte.patrones.comportamiento.mediator;

/**
 * PATRÓN MEDIATOR (Comportamiento).
 *
 * Define cómo se comunican los conductores entre sí. En vez de que cada
 * conductor conozca a los demás (acoplamiento en malla), todos hablan solo con
 * el mediador, que coordina los mensajes.
 */
public interface CentroDespacho {

    void registrar(Conductor conductor);

    void enviar(String mensaje, Conductor emisor);
}

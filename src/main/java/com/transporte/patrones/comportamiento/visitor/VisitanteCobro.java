package com.transporte.patrones.comportamiento.visitor;

/**
 * Visitante: declara una operación por cada tipo concreto de elemento.
 * Aquí calcula el importe a cobrar de cada tipo de servicio.
 */
public interface VisitanteCobro {

    double visitarEnvioLocal(EnvioLocal envio);

    double visitarEnvioInternacional(EnvioInternacional envio);
}

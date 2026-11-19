package com.transporte.patrones.creacionales.singleton;

/**
 * PATRÓN SINGLETON (Creacional).
 *
 * Garantiza que exista una única instancia de la configuración de la empresa
 * y ofrece un punto de acceso global a ella.
 *
 * Implementación con "initialization-on-demand holder": es segura entre hilos
 * y perezosa sin necesidad de bloqueos (synchronized), evitando el antipatrón
 * del Singleton con doble verificación mal hecho.
 */
public final class ConfiguracionEmpresa {

    private final String nombreEmpresa;
    private final String moneda;

    private ConfiguracionEmpresa() {
        this.nombreEmpresa = "TransExpress";
        this.moneda = "USD";
    }

    private static final class Holder {
        private static final ConfiguracionEmpresa INSTANCIA = new ConfiguracionEmpresa();
    }

    public static ConfiguracionEmpresa getInstancia() {
        return Holder.INSTANCIA;
    }

    public String getNombreEmpresa() {
        return nombreEmpresa;
    }

    public String getMoneda() {
        return moneda;
    }
}

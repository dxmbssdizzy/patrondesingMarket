package com.transporte.patrones.creacionales.builder;

import com.transporte.dominio.Ubicacion;

/**
 * Producto construido por el Builder: una orden de transporte.
 *
 * Es inmutable y solo se puede crear a través de su {@link Builder},
 * evitando constructores telescópicos (antipatrón) con muchos parámetros.
 */
public final class OrdenTransporte {

    private final String cliente;
    private final Ubicacion origen;
    private final Ubicacion destino;
    private final double pesoKg;
    private final boolean fragil;
    private final boolean urgente;

    private OrdenTransporte(Builder builder) {
        this.cliente = builder.cliente;
        this.origen = builder.origen;
        this.destino = builder.destino;
        this.pesoKg = builder.pesoKg;
        this.fragil = builder.fragil;
        this.urgente = builder.urgente;
    }

    public String getCliente() {
        return cliente;
    }

    public Ubicacion getOrigen() {
        return origen;
    }

    public Ubicacion getDestino() {
        return destino;
    }

    public double getPesoKg() {
        return pesoKg;
    }

    public boolean esFragil() {
        return fragil;
    }

    public boolean esUrgente() {
        return urgente;
    }

    @Override
    public String toString() {
        return String.format("Orden[%s: %s -> %s, %.1f kg%s%s]",
                cliente, origen, destino, pesoKg,
                fragil ? ", frágil" : "",
                urgente ? ", urgente" : "");
    }

    /**
     * PATRÓN BUILDER (Creacional).
     *
     * Separa la construcción de una orden compleja de su representación,
     * permitiendo crearla paso a paso con una API fluida y legible.
     */
    public static final class Builder {

        private final String cliente;
        private final Ubicacion origen;
        private final Ubicacion destino;
        private double pesoKg;
        private boolean fragil;
        private boolean urgente;

        public Builder(String cliente, Ubicacion origen, Ubicacion destino) {
            this.cliente = cliente;
            this.origen = origen;
            this.destino = destino;
        }

        public Builder conPeso(double pesoKg) {
            this.pesoKg = pesoKg;
            return this;
        }

        public Builder fragil() {
            this.fragil = true;
            return this;
        }

        public Builder urgente() {
            this.urgente = true;
            return this;
        }

        public OrdenTransporte construir() {
            return new OrdenTransporte(this);
        }
    }
}

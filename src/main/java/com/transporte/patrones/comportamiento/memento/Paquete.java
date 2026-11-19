package com.transporte.patrones.comportamiento.memento;

import com.transporte.patrones.comportamiento.observer.ObservadorEnvio;
import com.transporte.patrones.comportamiento.state.EstadoCreado;
import com.transporte.patrones.comportamiento.state.EstadoEnvio;
import java.util.ArrayList;
import java.util.List;

/**
 * Paquete en tránsito. Esta clase hace de punto de encuentro de tres patrones
 * de comportamiento:
 *
 *  - OBSERVER: es el sujeto observable; notifica a sus observadores en cada
 *    cambio de estado.
 *  - STATE: delega su ciclo de vida (CREADO -> EN_RUTA -> ENTREGADO) en
 *    objetos {@link EstadoEnvio}.
 *  - MEMENTO: es el "Originator" que crea y restaura {@link MementoPaquete}.
 */
public final class Paquete {

    private final String numero;
    private EstadoEnvio estado;
    private final List<ObservadorEnvio> observadores = new ArrayList<>();

    public Paquete(String numero) {
        this.numero = numero;
        this.estado = new EstadoCreado();
    }

    // --- Observer ---

    public void suscribir(ObservadorEnvio observador) {
        observadores.add(observador);
    }

    private void notificar() {
        for (ObservadorEnvio observador : observadores) {
            observador.actualizar(numero, estado.nombre());
        }
    }

    // --- State ---

    public void avanzar() {
        if (estado.esFinal()) {
            return;
        }
        estado = estado.siguiente();
        notificar();
    }

    public String estadoActual() {
        return estado.nombre();
    }

    // --- Memento ---

    public MementoPaquete guardar() {
        return new MementoPaquete(estado);
    }

    public void restaurar(MementoPaquete memento) {
        // Restaura el estado; la presentación la hace la capa de salida.
        this.estado = memento.getEstado();
    }

    public String numero() {
        return numero;
    }
}

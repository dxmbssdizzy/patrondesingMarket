#!/usr/bin/env python3
"""
Genera el documento de patrones de diseño (.docx) de TransExpress.

Para cada patrón incrusta el CÓDIGO FUENTE COMPLETO de cada una de sus clases
(atributos, métodos, anotaciones), leído directamente de los archivos .java del
proyecto, de modo que el documento siempre refleja el código vigente.

Uso:
    PYTHONPATH=/projects/sandbox/.pylibs python3 docs/generar_documentacion.py

El documento se guarda en docs/Patrones_TransExpress.docx.
"""

import os
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(RAIZ, "src", "main", "java", "com", "transporte")

AZUL = RGBColor(0x1F, 0x4E, 0x79)
GRIS = RGBColor(0x59, 0x59, 0x59)
FONDO_CODIGO = "F2F2F2"


# ---------------------------------------------------------------------------
# Clases de infraestructura (arquitectura en capas) y dominio.
# ---------------------------------------------------------------------------
INFRAESTRUCTURA = [
    ("Main", "Punto de entrada. Ensambla las piezas y ejecuta el Cliente.",
     "Main.java"),
    ("Cliente", "Lógica central. Orquesta los patrones; pide datos a Entrada y "
                "muestra con Salida.", "app/Cliente.java"),
    ("Entrada", "Única fuente de datos de la aplicación.", "app/Entrada.java"),
    ("Salida", "Único punto que muestra información.", "app/Salida.java"),
]

DOMINIO = [
    ("Ubicacion", "Valor inmutable: un punto geográfico (una parada).",
     "dominio/Ubicacion.java"),
    ("TipoVehiculo", "Enumeración de los tipos de vehículo.",
     "dominio/TipoVehiculo.java"),
]


# ---------------------------------------------------------------------------
# Catálogo de patrones: cada uno con su intención, uso de negocio y la lista de
# archivos .java (relativos a src/.../transporte) que lo componen.
# ---------------------------------------------------------------------------
PATRONES = [
    # ----------------------------- CREACIONALES ---------------------------
    {
        "nombre": "Singleton", "categoria": "Creacional",
        "paquete": "patrones.creacionales.singleton",
        "intencion": "Garantizar que una clase tenga una única instancia y "
                     "ofrecer un punto de acceso global a ella.",
        "uso_negocio": "Mantiene una sola configuración de la empresa compartida "
                       "por todo el programa.",
        "archivos": ["patrones/creacionales/singleton/ConfiguracionEmpresa.java"],
    },
    {
        "nombre": "Factory Method", "categoria": "Creacional",
        "paquete": "patrones.creacionales.factory",
        "intencion": "Definir una interfaz para crear un objeto, pero dejar que "
                     "las subclases decidan de qué clase concreta será.",
        "uso_negocio": "Cada centro de despacho decide qué vehículo asignar.",
        "archivos": [
            "patrones/creacionales/factory/Vehiculo.java",
            "patrones/creacionales/factory/Moto.java",
            "patrones/creacionales/factory/Furgoneta.java",
            "patrones/creacionales/factory/Camion.java",
            "patrones/creacionales/factory/CentroDespacho.java",
            "patrones/creacionales/factory/CentroDespachoUrbano.java",
            "patrones/creacionales/factory/CentroDespachoCarga.java",
        ],
    },
    {
        "nombre": "Abstract Factory", "categoria": "Creacional",
        "paquete": "patrones.creacionales.abstractfactory",
        "intencion": "Crear familias de objetos relacionados sin especificar sus "
                     "clases concretas.",
        "uso_negocio": "Cada tipo de servicio produce una familia coherente de "
                       "vehículo + embalaje.",
        "archivos": [
            "patrones/creacionales/abstractfactory/Embalaje.java",
            "patrones/creacionales/abstractfactory/EmbalajeEstandar.java",
            "patrones/creacionales/abstractfactory/EmbalajePremium.java",
            "patrones/creacionales/abstractfactory/FabricaServicio.java",
            "patrones/creacionales/abstractfactory/FabricaServicioEconomico.java",
            "patrones/creacionales/abstractfactory/FabricaServicioPremium.java",
        ],
    },
    {
        "nombre": "Builder", "categoria": "Creacional",
        "paquete": "patrones.creacionales.builder",
        "intencion": "Separar la construcción de un objeto complejo de su "
                     "representación, permitiendo construirlo paso a paso.",
        "uso_negocio": "Construir una orden de transporte con campos opcionales "
                       "sin constructores con muchos parámetros.",
        "archivos": ["patrones/creacionales/builder/OrdenTransporte.java"],
    },
    {
        "nombre": "Prototype", "categoria": "Creacional",
        "paquete": "patrones.creacionales.prototype",
        "intencion": "Crear nuevos objetos copiando un prototipo existente en "
                     "lugar de construirlos desde cero.",
        "uso_negocio": "Clonar una plantilla de ruta ya configurada y modificar "
                       "el clon sin afectar al original.",
        "archivos": ["patrones/creacionales/prototype/PlantillaRuta.java"],
    },
    # ----------------------------- ESTRUCTURALES --------------------------
    {
        "nombre": "Adapter", "categoria": "Estructural",
        "paquete": "patrones.estructurales.adapter",
        "intencion": "Permitir que colaboren objetos con interfaces incompatibles.",
        "uso_negocio": "Adapta una API de mapas externa a la interfaz que usa la "
                       "aplicación.",
        "archivos": [
            "patrones/estructurales/adapter/ServicioDistancia.java",
            "patrones/estructurales/adapter/ApiMapasExterna.java",
            "patrones/estructurales/adapter/AdaptadorApiMapas.java",
        ],
    },
    {
        "nombre": "Bridge", "categoria": "Estructural",
        "paquete": "patrones.estructurales.bridge",
        "intencion": "Separar una abstracción de su implementación para que ambas "
                     "varíen de forma independiente.",
        "uso_negocio": "El tipo de envío y el medio de transporte evolucionan por "
                       "separado.",
        "archivos": [
            "patrones/estructurales/bridge/MedioTransporte.java",
            "patrones/estructurales/bridge/TransporteTerrestre.java",
            "patrones/estructurales/bridge/TransporteAereo.java",
            "patrones/estructurales/bridge/Envio.java",
            "patrones/estructurales/bridge/EnvioNacional.java",
            "patrones/estructurales/bridge/EnvioInternacional.java",
        ],
    },
    {
        "nombre": "Composite", "categoria": "Estructural",
        "paquete": "patrones.estructurales.composite",
        "intencion": "Componer objetos en estructuras de árbol y tratar de forma "
                     "uniforme a objetos individuales y a composiciones.",
        "uso_negocio": "Una ruta formada por tramos simples y por sub-rutas.",
        "archivos": [
            "patrones/estructurales/composite/ComponenteRuta.java",
            "patrones/estructurales/composite/Tramo.java",
            "patrones/estructurales/composite/RutaCompuesta.java",
        ],
    },
    {
        "nombre": "Decorator", "categoria": "Estructural",
        "paquete": "patrones.estructurales.decorator",
        "intencion": "Añadir responsabilidades a un objeto de forma dinámica "
                     "envolviéndolo.",
        "uso_negocio": "Añadir extras al envío (seguro, entrega urgente) sin "
                       "modificar el servicio base.",
        "archivos": [
            "patrones/estructurales/decorator/ServicioEnvio.java",
            "patrones/estructurales/decorator/EnvioBasico.java",
            "patrones/estructurales/decorator/ExtraEnvio.java",
            "patrones/estructurales/decorator/ConSeguro.java",
            "patrones/estructurales/decorator/ConEntregaUrgente.java",
        ],
    },
    {
        "nombre": "Facade", "categoria": "Estructural",
        "paquete": "patrones.estructurales.facade",
        "intencion": "Ofrecer una interfaz simple a un subsistema complejo.",
        "uso_negocio": "Una sola operación de cotización esconde el cálculo de "
                       "distancia y la consulta de tarifas.",
        "archivos": ["patrones/estructurales/facade/FachadaReservas.java"],
    },
    {
        "nombre": "Flyweight", "categoria": "Estructural",
        "paquete": "patrones.estructurales.flyweight",
        "intencion": "Compartir eficientemente gran cantidad de objetos con "
                     "estado común.",
        "uso_negocio": "Muchas unidades de la flota comparten el mismo objeto "
                       "'modelo de vehículo'.",
        "archivos": [
            "patrones/estructurales/flyweight/ModeloVehiculo.java",
            "patrones/estructurales/flyweight/FabricaModelos.java",
            "patrones/estructurales/flyweight/UnidadFlota.java",
        ],
    },
    {
        "nombre": "Proxy", "categoria": "Estructural",
        "paquete": "patrones.estructurales.proxy",
        "intencion": "Proporcionar un sustituto de otro objeto para controlar el "
                     "acceso a él.",
        "uso_negocio": "Una caché que evita repetir la consulta costosa de tarifas.",
        "archivos": [
            "patrones/estructurales/proxy/ServicioTarifas.java",
            "patrones/estructurales/proxy/ServicioTarifasReal.java",
            "patrones/estructurales/proxy/ProxyTarifasCache.java",
        ],
    },
    # --------------------------- COMPORTAMIENTO ---------------------------
    {
        "nombre": "Chain of Responsibility", "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.chain",
        "intencion": "Pasar una petición por una cadena de manejadores hasta que "
                     "uno la atienda.",
        "uso_negocio": "Validar una orden mediante una cadena de validadores.",
        "archivos": [
            "patrones/comportamiento/chain/ValidadorOrden.java",
            "patrones/comportamiento/chain/ValidadorPeso.java",
            "patrones/comportamiento/chain/ValidadorDestino.java",
        ],
    },
    {
        "nombre": "Command", "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.command",
        "intencion": "Encapsular una petición como un objeto, permitiendo "
                     "deshacerla y guardarla en un historial.",
        "uso_negocio": "Operaciones sobre envíos con posibilidad de deshacer.",
        "archivos": [
            "patrones/comportamiento/command/Comando.java",
            "patrones/comportamiento/command/AvanzarEnvioComando.java",
            "patrones/comportamiento/command/PanelOperaciones.java",
        ],
    },
    {
        "nombre": "Iterator", "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.iterator",
        "intencion": "Recorrer los elementos de una colección sin exponer su "
                     "estructura interna.",
        "uso_negocio": "Recorrer las unidades de la flota.",
        "archivos": ["patrones/comportamiento/iterator/Flota.java"],
    },
    {
        "nombre": "Mediator", "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.mediator",
        "intencion": "Centralizar la comunicación entre objetos para reducir el "
                     "acoplamiento entre ellos.",
        "uso_negocio": "El centro de despacho coordina a los conductores.",
        "archivos": [
            "patrones/comportamiento/mediator/CentroDespacho.java",
            "patrones/comportamiento/mediator/Conductor.java",
            "patrones/comportamiento/mediator/CentroDespachoRadio.java",
        ],
    },
    {
        "nombre": "Memento", "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.memento",
        "intencion": "Capturar y restaurar el estado interno de un objeto sin "
                     "violar su encapsulamiento.",
        "uso_negocio": "Guardar y restaurar el estado de un paquete.",
        "archivos": [
            "patrones/comportamiento/memento/MementoPaquete.java",
            "patrones/comportamiento/memento/Paquete.java",
        ],
    },
    {
        "nombre": "Observer", "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.observer",
        "intencion": "Notificar automáticamente a varios objetos cuando otro "
                     "cambia de estado.",
        "uso_negocio": "Notificar al cliente los cambios de estado del envío.",
        "archivos": [
            "patrones/comportamiento/observer/ObservadorEnvio.java",
            "patrones/comportamiento/observer/NotificadorCliente.java",
        ],
    },
    {
        "nombre": "State", "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.state",
        "intencion": "Permitir que un objeto cambie su comportamiento cuando "
                     "cambia su estado interno.",
        "uso_negocio": "Ciclo de vida del envío: CREADO -> EN_RUTA -> ENTREGADO.",
        "archivos": [
            "patrones/comportamiento/state/EstadoEnvio.java",
            "patrones/comportamiento/state/EstadoCreado.java",
            "patrones/comportamiento/state/EstadoEnRuta.java",
            "patrones/comportamiento/state/EstadoEntregado.java",
        ],
    },
    {
        "nombre": "Strategy", "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.strategy",
        "intencion": "Definir una familia de algoritmos intercambiables y "
                     "seleccionarlos en tiempo de ejecución.",
        "uso_negocio": "Distintos algoritmos de cálculo de tarifa.",
        "archivos": [
            "patrones/comportamiento/strategy/EstrategiaTarifa.java",
            "patrones/comportamiento/strategy/TarifaPorDistancia.java",
            "patrones/comportamiento/strategy/TarifaPorPeso.java",
        ],
    },
    {
        "nombre": "Template Method", "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.template",
        "intencion": "Definir el esqueleto de un algoritmo dejando que las "
                     "subclases rellenen algunos pasos.",
        "uso_negocio": "Proceso de entrega con pasos fijos y pasos variables.",
        "archivos": [
            "patrones/comportamiento/template/ProcesoEntrega.java",
            "patrones/comportamiento/template/EntregaExpress.java",
            "patrones/comportamiento/template/EntregaEconomica.java",
        ],
    },
    {
        "nombre": "Visitor", "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.visitor",
        "intencion": "Separar un algoritmo de la estructura de objetos sobre la "
                     "que opera, permitiendo añadir operaciones sin modificarla.",
        "uso_negocio": "Calcular la facturación recorriendo distintos tipos de "
                       "envío.",
        "archivos": [
            "patrones/comportamiento/visitor/ElementoFacturable.java",
            "patrones/comportamiento/visitor/VisitanteCobro.java",
            "patrones/comportamiento/visitor/EnvioLocal.java",
            "patrones/comportamiento/visitor/EnvioInternacional.java",
            "patrones/comportamiento/visitor/VisitanteFacturacion.java",
        ],
    },
]


# ---------------------------------------------------------------------------
# Utilidades de formato.
# ---------------------------------------------------------------------------
def leer_codigo(ruta_relativa):
    ruta = os.path.join(SRC, ruta_relativa)
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read().rstrip("\n")


def nombre_clase(ruta_relativa):
    return os.path.basename(ruta_relativa).replace(".java", "")


def sombrear(parrafo, color_hex):
    """Pinta el fondo de un párrafo (bloque de código)."""
    ppr = parrafo._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color_hex)
    ppr.append(shd)


def agregar_codigo(doc, codigo):
    """Inserta un bloque de código monoespaciado con fondo gris."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Pt(6)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    sombrear(p, FONDO_CODIGO)
    run = p.add_run(codigo)
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    return p


# ---------------------------------------------------------------------------
# Secciones del documento.
# ---------------------------------------------------------------------------
def agregar_portada(doc):
    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run("TransExpress")
    r.font.size = Pt(28)
    r.font.bold = True
    r.font.color.rgb = AZUL

    s = doc.add_paragraph()
    s.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = s.add_run("Documentación y código de los patrones de diseño (GoF)")
    r.font.size = Pt(14)
    r.font.color.rgb = GRIS

    d = doc.add_paragraph()
    d.alignment = WD_ALIGN_PARAGRAPH.CENTER
    d.add_run(
        "Empresa de servicio de transporte que integra los 23 patrones de diseño "
        "coexistiendo en un mismo flujo de negocio, aplicando los principios SOLID. "
        "Este documento incluye el código fuente completo de cada clase."
    ).italic = True
    doc.add_paragraph()


def agregar_arquitectura(doc):
    doc.add_heading("Arquitectura de la aplicación", level=1)
    doc.add_paragraph(
        "La ejecución separa responsabilidades en cuatro clases, de modo que cada "
        "una tiene una única razón para cambiar. Las clases de patrones no leen ni "
        "imprimen: devuelven datos y solo el Cliente habla con Entrada y Salida."
    )
    for nombre, desc, ruta in INFRAESTRUCTURA:
        doc.add_heading(nombre, level=2)
        doc.add_paragraph(desc)
        agregar_codigo(doc, leer_codigo(ruta))
    doc.add_page_break()

    doc.add_heading("Modelo de dominio", level=1)
    doc.add_paragraph("Clases de datos compartidas por los patrones.")
    for nombre, desc, ruta in DOMINIO:
        doc.add_heading(nombre, level=2)
        doc.add_paragraph(desc)
        agregar_codigo(doc, leer_codigo(ruta))
    doc.add_page_break()


def agregar_patron(doc, patron):
    doc.add_heading(f"{patron['nombre']}  ({patron['categoria']})", level=2)

    p = doc.add_paragraph()
    p.add_run("Paquete: ").bold = True
    p.add_run(f"com.transporte.{patron['paquete']}").italic = True

    p = doc.add_paragraph()
    p.add_run("Intención (GoF): ").bold = True
    p.add_run(patron["intencion"])

    p = doc.add_paragraph()
    p.add_run("Qué hace en el negocio: ").bold = True
    p.add_run(patron["uso_negocio"])

    doc.add_heading("Código fuente de las clases", level=3)
    for ruta in patron["archivos"]:
        sub = doc.add_paragraph()
        r = sub.add_run(nombre_clase(ruta) + ".java")
        r.bold = True
        r.font.color.rgb = AZUL
        agregar_codigo(doc, leer_codigo(ruta))

    doc.add_heading("Diagrama UML", level=3)
    m = doc.add_paragraph()
    r = m.add_run("[ Espacio reservado para el diagrama UML de este patrón ]")
    r.italic = True
    r.font.color.rgb = GRIS

    doc.add_paragraph()


def main():
    doc = Document()
    agregar_portada(doc)
    agregar_arquitectura(doc)

    titulos = {
        "Creacional": "Patrones Creacionales",
        "Estructural": "Patrones Estructurales",
        "Comportamiento": "Patrones de Comportamiento",
    }
    categoria_actual = None
    for patron in PATRONES:
        if patron["categoria"] != categoria_actual:
            categoria_actual = patron["categoria"]
            doc.add_page_break()
            doc.add_heading(titulos[categoria_actual], level=1)
        agregar_patron(doc, patron)

    salida = os.path.join(RAIZ, "docs", "Patrones_TransExpress.docx")
    doc.save(salida)
    total_clases = (len(INFRAESTRUCTURA) + len(DOMINIO)
                    + sum(len(p["archivos"]) for p in PATRONES))
    print(f"Documento generado: {salida}")
    print(f"Patrones documentados: {len(PATRONES)}")
    print(f"Clases con código incrustado: {total_clases}")


if __name__ == "__main__":
    main()

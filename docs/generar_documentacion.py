#!/usr/bin/env python3
"""
Genera el documento de patrones de diseño (.docx) de TransExpress.

Uso:
    PYTHONPATH=/projects/sandbox/.pylibs python3 docs/generar_documentacion.py

El documento se guarda en docs/Patrones_TransExpress.docx.
Está pensado para ampliarse con las clasificaciones estructurales y de
comportamiento añadiendo más secciones a la lista PATRONES.
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH


# ---------------------------------------------------------------------------
# CONTENIDO: una entrada por patrón.
# ---------------------------------------------------------------------------
# Cada patrón: nombre, categoria, intencion, uso_negocio, clases (lista de
# (clase, rol, descripcion)), anotaciones (lista de strings).
PATRONES = [
    {
        "nombre": "Singleton",
        "categoria": "Creacional",
        "paquete": "patrones.creacionales.singleton",
        "intencion": "Garantizar que una clase tenga una única instancia y "
                     "ofrecer un punto de acceso global a ella.",
        "uso_negocio": "Mantiene una sola configuración de la empresa "
                       "(nombre, moneda) compartida por todo el programa.",
        "clases": [
            ("ConfiguracionEmpresa", "Singleton",
             "Clase final con constructor privado. Guarda la configuración de "
             "la empresa de forma inmutable (solo lectura)."),
            ("ConfiguracionEmpresa.Holder", "Soporte de inicialización",
             "Clase interna estática que crea la instancia única la primera "
             "vez que se usa (initialization-on-demand holder)."),
        ],
        "anotaciones": [
            "Usa el patrón 'initialization-on-demand holder': es seguro entre "
            "hilos y perezoso, sin necesidad de bloqueos (synchronized).",
            "La instancia es inmutable, por lo que no se convierte en una "
            "variable global mutable (evita ese antipatrón).",
            "Acceso mediante el método estático getInstancia().",
        ],
    },
    {
        "nombre": "Factory Method",
        "categoria": "Creacional",
        "paquete": "patrones.creacionales.factory",
        "intencion": "Definir una interfaz para crear un objeto, pero dejar que "
                     "las subclases decidan de qué clase concreta será.",
        "uso_negocio": "Cada centro de despacho decide qué tipo de vehículo "
                       "asignar a un reparto.",
        "clases": [
            ("CentroDespacho", "Creador",
             "Clase abstracta. Declara el método fábrica crearVehiculo() y la "
             "operación de negocio asignarVehiculo() que lo usa."),
            ("CentroDespachoUrbano", "Creador concreto",
             "Produce una Moto."),
            ("CentroDespachoCarga", "Creador concreto",
             "Produce un Camión."),
            ("Vehiculo", "Producto",
             "Interfaz común de los vehículos (descripción y capacidad)."),
            ("Moto / Furgoneta / Camion", "Productos concretos",
             "Implementaciones concretas de Vehiculo."),
        ],
        "anotaciones": [
            "El método fábrica crearVehiculo() es abstract y protected: solo "
            "las subclases lo implementan.",
            "asignarVehiculo() devuelve el vehículo; la presentación la hace la "
            "capa de salida, no el patrón (separación de responsabilidades).",
            "El código que asigna vehículos no depende de clases concretas (DIP).",
        ],
    },
    {
        "nombre": "Abstract Factory",
        "categoria": "Creacional",
        "paquete": "patrones.creacionales.abstractfactory",
        "intencion": "Crear familias de objetos relacionados sin especificar sus "
                     "clases concretas.",
        "uso_negocio": "Cada tipo de servicio (económico o premium) produce una "
                       "familia coherente de vehículo + embalaje.",
        "clases": [
            ("FabricaServicio", "Fábrica abstracta",
             "Interfaz que declara crearVehiculo() y crearEmbalaje()."),
            ("FabricaServicioEconomico", "Fábrica concreta",
             "Combina Moto + EmbalajeEstandar."),
            ("FabricaServicioPremium", "Fábrica concreta",
             "Combina Furgoneta + EmbalajePremium."),
            ("Embalaje", "Producto abstracto",
             "Interfaz de los embalajes."),
            ("EmbalajeEstandar / EmbalajePremium", "Productos concretos",
             "Tipos de embalaje de cada familia."),
        ],
        "anotaciones": [
            "Cada fábrica concreta garantiza que los productos que entrega "
            "combinan bien entre sí.",
            "Se diferencia del Factory Method en que crea VARIOS productos "
            "relacionados, no uno solo.",
            "Reutiliza la interfaz Vehiculo del Factory Method.",
        ],
    },
    {
        "nombre": "Builder",
        "categoria": "Creacional",
        "paquete": "patrones.creacionales.builder",
        "intencion": "Separar la construcción de un objeto complejo de su "
                     "representación, permitiendo construirlo paso a paso.",
        "uso_negocio": "Construir una orden de transporte con campos opcionales "
                       "(frágil, urgente) sin constructores con muchos parámetros.",
        "clases": [
            ("OrdenTransporte", "Producto",
             "Objeto inmutable con constructor privado: solo se crea a través "
             "de su Builder."),
            ("OrdenTransporte.Builder", "Constructor (Builder)",
             "Clase interna estática con API fluida (conPeso, fragil, urgente) "
             "que termina en construir()."),
        ],
        "anotaciones": [
            "Variante 'fluent builder': cada método devuelve this para encadenar "
            "llamadas.",
            "Evita el antipatrón del constructor telescópico (muchos "
            "constructores sobrecargados).",
            "El producto resultante es inmutable (todos los campos final).",
        ],
    },
    {
        "nombre": "Prototype",
        "categoria": "Creacional",
        "paquete": "patrones.creacionales.prototype",
        "intencion": "Crear nuevos objetos copiando un prototipo existente en "
                     "lugar de construirlos desde cero.",
        "uso_negocio": "Clonar una plantilla de ruta ya configurada y modificar "
                       "el clon sin afectar al original.",
        "clases": [
            ("PlantillaRuta", "Prototipo",
             "Tiene un método clonar() y un constructor de copia privado que "
             "crea una lista de paradas nueva e independiente."),
        ],
        "anotaciones": [
            "Usa un constructor de copia en vez de la interfaz Cloneable de "
            "Java (que es problemática).",
            "La lista de paradas se copia; las Ubicacion que contiene son "
            "inmutables, por lo que compartir sus referencias es seguro.",
            "Modificar el clon (renombrar, agregar paradas) no afecta al original.",
        ],
    },
]


# ---------------------------------------------------------------------------
# Construcción del documento.
# ---------------------------------------------------------------------------
AZUL = RGBColor(0x1F, 0x4E, 0x79)
GRIS = RGBColor(0x59, 0x59, 0x59)


def agregar_portada(doc):
    titulo = doc.add_paragraph()
    titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = titulo.add_run("TransExpress")
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = AZUL

    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = sub.add_run("Documentación de los patrones de diseño (GoF)")
    run.font.size = Pt(14)
    run.font.color.rgb = GRIS

    desc = doc.add_paragraph()
    desc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    desc.add_run(
        "Empresa de servicio de transporte que integra los 23 patrones de "
        "diseño coexistiendo en un mismo flujo de negocio, aplicando los "
        "principios SOLID."
    ).italic = True

    doc.add_paragraph()


def agregar_arquitectura(doc):
    doc.add_heading("Arquitectura de la aplicación", level=1)
    doc.add_paragraph(
        "La ejecución separa responsabilidades en cuatro clases de infraestructura, "
        "de modo que cada una tiene una única razón para cambiar:"
    )
    capas = [
        ("Main", "Punto de entrada. Solo ensambla las piezas y ejecuta el Cliente."),
        ("Cliente", "Lógica central. Orquesta los patrones del negocio. Pide los "
                    "datos a Entrada y envía los resultados a Salida."),
        ("Entrada", "Única fuente de datos. El Cliente le pide los datos y no sabe "
                    "de dónde vienen."),
        ("Salida", "Única responsable de mostrar información. Ningún patrón imprime "
                   "por su cuenta."),
    ]
    for nombre, desc in capas:
        p = doc.add_paragraph(style="List Bullet")
        r = p.add_run(nombre + ": ")
        r.bold = True
        p.add_run(desc)
    doc.add_paragraph(
        "Regla de diseño: las clases de patrones no leen ni imprimen; devuelven "
        "datos. Solo el Cliente habla con Entrada y Salida."
    )
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

    doc.add_heading("Clases y su rol", level=3)
    tabla = doc.add_table(rows=1, cols=3)
    tabla.style = "Light Grid Accent 1"
    enc = tabla.rows[0].cells
    enc[0].paragraphs[0].add_run("Clase").bold = True
    enc[1].paragraphs[0].add_run("Rol en el patrón").bold = True
    enc[2].paragraphs[0].add_run("Qué hace").bold = True
    for clase, rol, descripcion in patron["clases"]:
        fila = tabla.add_row().cells
        fila[0].text = clase
        fila[1].text = rol
        fila[2].text = descripcion

    doc.add_heading("Anotaciones", level=3)
    for nota in patron["anotaciones"]:
        doc.add_paragraph(nota, style="List Bullet")

    # Espacio reservado para el UML que agregará el equipo.
    doc.add_heading("Diagrama UML", level=3)
    marcador = doc.add_paragraph()
    run = marcador.add_run("[ Espacio reservado para el diagrama UML de este patrón ]")
    run.italic = True
    run.font.color.rgb = GRIS

    doc.add_paragraph()


def main():
    doc = Document()
    agregar_portada(doc)
    agregar_arquitectura(doc)

    titulos_categoria = {
        "Creacional": "Patrones Creacionales",
        "Estructural": "Patrones Estructurales",
        "Comportamiento": "Patrones de Comportamiento",
    }
    categoria_actual = None
    for patron in PATRONES:
        if patron["categoria"] != categoria_actual:
            categoria_actual = patron["categoria"]
            doc.add_heading(titulos_categoria[categoria_actual], level=1)
        agregar_patron(doc, patron)

    salida = "docs/Patrones_TransExpress.docx"
    doc.save(salida)
    print(f"Documento generado: {salida}")
    print(f"Patrones documentados: {len(PATRONES)}")


if __name__ == "__main__":
    main()

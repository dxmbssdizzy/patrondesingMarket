#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el informe final de TransExpress en formato .docx.

Sigue la plantilla acordada con el equipo:
  Portada -> Tabla de contenido -> 1. Diagrama -> 2. Explicación ->
  3. Explicación de clases -> 4. Entradas y salidas -> 5. Código

La prosa y el catálogo de patrones viven en contenido_informe.py.
El código fuente de cada clase se lee en vivo de los archivos .java,
de modo que el informe siempre refleja el código vigente.

Espacios reservados para imágenes:
  - Figura 1 (UML): el equipo la inserta manualmente.
  - Figura 2 (salida de consola): se incrusta el texto; el equipo puede
    reemplazarlo por una captura.

Uso:
    PYTHONPATH=/projects/sandbox/.pylibs python3 docs/generar_informe.py
"""

import os
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import contenido_informe as C

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(RAIZ, "src", "main", "java", "com", "transporte")

AZUL = RGBColor(0x1F, 0x4E, 0x79)
GRIS = RGBColor(0x59, 0x59, 0x59)
FONDO_CODIGO = "F2F2F2"

TITULOS_CATEGORIA = {
    "Creacional": "Patrones Creacionales",
    "Estructural": "Patrones Estructurales",
    "Comportamiento": "Patrones de Comportamiento",
}


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def leer_codigo(ruta_relativa):
    ruta = os.path.join(SRC, ruta_relativa)
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read().rstrip("\n")


def sombrear(parrafo, color_hex):
    ppr = parrafo._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color_hex)
    ppr.append(shd)


def bloque_codigo(doc, codigo):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Pt(6)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    sombrear(p, FONDO_CODIGO)
    run = p.add_run(codigo)
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)


def parrafo_italico_gris(doc, texto, centrado=False):
    p = doc.add_paragraph()
    if centrado:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(texto)
    r.italic = True
    r.font.color.rgb = GRIS
    return p


def marcador_imagen(doc, texto):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(texto)
    r.italic = True
    r.font.color.rgb = GRIS


# ---------------------------------------------------------------------------
# Secciones
# ---------------------------------------------------------------------------
def agregar_portada(doc):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(C.PORTADA["universidad_linea1"])
    r.font.size = Pt(13)
    r.font.color.rgb = GRIS

    marcador_imagen(doc, "[ Espacio reservado para el logo de la universidad ]")

    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(C.PORTADA["materia"])
    r.font.size = Pt(14)
    r.bold = True
    r.font.color.rgb = AZUL

    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(C.PORTADA["titulo"])
    r.font.size = Pt(26)
    r.bold = True
    r.font.color.rgb = AZUL

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(C.PORTADA["subtitulo"])
    r.font.size = Pt(13)
    r.italic = True
    r.font.color.rgb = GRIS

    for _ in range(3):
        doc.add_paragraph()

    for linea, size in [
        (C.PORTADA["autor"], 13),
        (C.PORTADA["codigo"], 12),
        (C.PORTADA["correo"], 12),
    ]:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(linea)
        r.font.size = Pt(size)

    doc.add_page_break()


def agregar_tabla_contenido(doc):
    doc.add_heading("Tabla de contenido", level=1)
    entradas = [
        "1. Diagrama",
        "2. Explicación",
        "3. Explicación de clases",
        "    3.1 Infraestructura y dominio",
        "    3.2 Patrones creacionales",
        "    3.3 Patrones estructurales",
        "    3.4 Patrones de comportamiento",
        "4. Entradas y salidas",
        "5. Código",
        "    5.1 Infraestructura y dominio",
        "    5.2 Patrones creacionales",
        "    5.3 Patrones estructurales",
        "    5.4 Patrones de comportamiento",
    ]
    for e in entradas:
        doc.add_paragraph(e)
    doc.add_page_break()


def agregar_diagrama(doc):
    doc.add_heading("1. Diagrama", level=1)
    doc.add_paragraph(
        "A continuación se presenta el diagrama de clases UML del proyecto "
        "TransExpress, que muestra las clases de infraestructura (Main, "
        "Cliente, Entrada y Salida), el modelo de dominio y los 22 patrones "
        "de diseño agrupados por familia, así como las relaciones entre ellos."
    )
    marcador_imagen(doc, "[ Espacio reservado para el diagrama UML del proyecto ]")
    parrafo_italico_gris(
        doc, "Figura 1. Diagrama de clases UML del proyecto TransExpress.",
        centrado=True)
    doc.add_page_break()


def agregar_explicacion(doc):
    doc.add_heading("2. Explicación", level=1)
    for parrafo in C.EXPLICACION_GENERAL:
        doc.add_paragraph(parrafo)
    doc.add_page_break()


def agregar_explicacion_clases(doc):
    doc.add_heading("3. Explicación de clases", level=1)

    # 3.1 Infraestructura y dominio
    doc.add_heading("3.1 Infraestructura y dominio", level=2)
    doc.add_paragraph(
        "Estas cuatro clases de infraestructura (más el modelo de dominio) "
        "separan las responsabilidades de la ejecución. Se presentan primero "
        "porque son el marco sobre el que se orquestan todos los patrones."
    )
    for clase in C.INFRAESTRUCTURA:
        p = doc.add_paragraph()
        r = p.add_run(clase["nombre"] + " (" + clase["rol"] + "). ")
        r.bold = True
        p.add_run(clase["descripcion"])

    # 3.2 / 3.3 / 3.4 por categoría
    numeracion = {"Creacional": "3.2", "Estructural": "3.3",
                  "Comportamiento": "3.4"}
    categoria_actual = None
    for patron in C.PATRONES:
        if patron["categoria"] != categoria_actual:
            categoria_actual = patron["categoria"]
            doc.add_heading(
                numeracion[categoria_actual] + " " +
                TITULOS_CATEGORIA[categoria_actual], level=2)
        doc.add_heading(patron["nombre"], level=3)
        for parrafo in patron["explicacion"]:
            doc.add_paragraph(parrafo)
        # Resumen de roles de las clases
        p = doc.add_paragraph()
        p.add_run("Clases: ").bold = True
        roles = ["{} ({})".format(c["nombre"], c["rol"])
                 for c in patron["clases"]]
        p.add_run("; ".join(roles) + ".")
    doc.add_page_break()


def agregar_entradas_salidas(doc, salida_consola):
    doc.add_heading("4. Entradas y salidas", level=1)
    for parrafo in C.ENTRADAS_SALIDAS:
        doc.add_paragraph(parrafo)
    bloque_codigo(doc, salida_consola)
    parrafo_italico_gris(
        doc,
        "Figura 2. Salida por consola de la ejecución del programa "
        "(reemplazable por una captura de pantalla).",
        centrado=True)
    doc.add_page_break()


def agregar_codigo(doc):
    doc.add_heading("5. Código", level=1)

    # 5.1 Infraestructura y dominio
    doc.add_heading("5.1 Infraestructura y dominio", level=2)
    for clase in C.INFRAESTRUCTURA:
        sub = doc.add_paragraph()
        r = sub.add_run(clase["nombre"] + ".java")
        r.bold = True
        r.font.color.rgb = AZUL
        bloque_codigo(doc, leer_codigo(clase["archivo"]))

    numeracion = {"Creacional": "5.2", "Estructural": "5.3",
                  "Comportamiento": "5.4"}
    categoria_actual = None
    for patron in C.PATRONES:
        if patron["categoria"] != categoria_actual:
            categoria_actual = patron["categoria"]
            doc.add_heading(
                numeracion[categoria_actual] + " " +
                TITULOS_CATEGORIA[categoria_actual], level=2)
        doc.add_heading(patron["nombre"], level=3)
        for clase in patron["clases"]:
            sub = doc.add_paragraph()
            r = sub.add_run(clase["nombre"] + ".java")
            r.bold = True
            r.font.color.rgb = AZUL
            bloque_codigo(doc, leer_codigo(clase["archivo"]))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    salida_consola_path = os.path.join(RAIZ, "docs", "salida_consola.txt")
    if os.path.exists(salida_consola_path):
        with open(salida_consola_path, "r", encoding="utf-8") as f:
            salida_consola = f.read().rstrip("\n")
    else:
        salida_consola = "[ Ejecuta el programa y pega aquí la salida. ]"

    doc = Document()
    agregar_portada(doc)
    agregar_tabla_contenido(doc)
    agregar_diagrama(doc)
    agregar_explicacion(doc)
    agregar_explicacion_clases(doc)
    agregar_entradas_salidas(doc, salida_consola)
    agregar_codigo(doc)

    salida = os.path.join(RAIZ, "docs", "Informe_TransExpress.docx")
    doc.save(salida)

    total_clases = (len(C.INFRAESTRUCTURA)
                    + sum(len(p["clases"]) for p in C.PATRONES))
    print("Informe generado:", salida)
    print("Patrones documentados:", len(C.PATRONES))
    print("Clases con código incrustado:", total_clases)


if __name__ == "__main__":
    main()

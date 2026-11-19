# -*- coding: utf-8 -*-
"""
Contenido textual del informe de TransExpress.

Separado del generador para que la prosa sea fácil de leer y editar.
El generador (generar_informe.py) importa estas estructuras y las vuelca
al documento .docx siguiendo la plantilla acordada.

Nota: el texto en prosa de cada patrón (campos "explicacion") está pensado
para ser revisado por el equipo; describe la intención GoF, cómo se aplica al
dominio de la empresa de transporte y cómo colabora con otros patrones.
"""

# ---------------------------------------------------------------------------
# Datos de portada
# ---------------------------------------------------------------------------
PORTADA = {
    "universidad_linea1": "Universidad Distrital Francisco José de Caldas",
    "materia": "Modelos de Programación",
    "titulo": "Proyecto Final - TransExpress",
    "subtitulo": "Los 22 patrones de diseño GoF conviviendo en un mismo sistema",
    "autor": "Juan Diego Charry Rodriguez",
    "codigo": "20241020125",
    "correo": "jdcharryr@udistrital.edu.co",
}


# ---------------------------------------------------------------------------
# Sección 2: Explicación general del proyecto (prosa).
# Cada elemento es un párrafo.
# ---------------------------------------------------------------------------
EXPLICACION_GENERAL = [
    "TransExpress es una empresa ficticia de servicio de transporte y "
    "paquetería construida como aplicación Java con un único objetivo "
    "didáctico: que los 22 patrones de diseño del catálogo de la Gang of "
    "Four (según el catálogo de Refactoring Guru) coexistan y colaboren "
    "dentro de un mismo flujo de negocio, en lugar de presentarse como 22 "
    "ejemplos aislados. La simulación recorre el ciclo de vida de un envío "
    "—desde que se arma la orden hasta que se factura— y, en cada paso, "
    "entra en juego uno o varios patrones.",

    "El proyecto aplica los principios SOLID y evita antipatrones comunes. "
    "Por ejemplo, el patrón State reemplaza las cadenas de condicionales que "
    "normalmente gobiernan el ciclo de vida de un pedido; el Singleton se usa "
    "de forma inmutable para no degenerar en una variable global mutable; y "
    "el Builder evita el antipatrón del constructor telescópico. Cada patrón "
    "se mantiene lo más sencillo y legible posible, priorizando la claridad "
    "sobre el realismo exhaustivo.",

    "La ejecución separa responsabilidades en cuatro clases de "
    "infraestructura. Main es el punto de entrada: solo ensambla las piezas "
    "y lanza al Cliente. Cliente contiene la lógica central y orquesta los "
    "patrones; es el único que conoce a Entrada y a Salida. Entrada es la "
    "única fuente de datos del programa, y Salida es el único punto que "
    "muestra información por consola. Gracias a esta separación, ninguna "
    "clase de patrón lee ni imprime por su cuenta: todas devuelven datos y "
    "el Cliente los entrega a Salida. Así se obtiene una responsabilidad "
    "simple y bien delimitada en cada capa.",

    "Los patrones se agrupan en tres familias. Los creacionales (Singleton, "
    "Factory Method, Abstract Factory, Builder y Prototype) se encargan de "
    "crear objetos del dominio: la configuración de la empresa, los "
    "vehículos, las familias de servicio, las órdenes y las plantillas de "
    "ruta. Los estructurales (Adapter, Bridge, Composite, Decorator, Facade, "
    "Flyweight y Proxy) ensamblan esos objetos en estructuras más grandes: "
    "integran una API externa, separan el tipo de envío del medio de "
    "transporte, construyen rutas compuestas, añaden extras al servicio, "
    "esconden subsistemas, comparten datos de modelos y cachean tarifas. "
    "Los de comportamiento (Chain of Responsibility, Command, Iterator, "
    "Mediator, Memento, Observer, State, Strategy, Template Method y Visitor) "
    "reparten responsabilidades y algoritmos: validan órdenes, encapsulan "
    "operaciones con deshacer, recorren la flota, coordinan conductores, "
    "guardan y restauran estados, notifican al cliente, modelan el ciclo de "
    "vida del envío, calculan tarifas, fijan el esqueleto de la entrega y "
    "recorren la estructura para facturar.",

    "La mejor evidencia de convivencia es la clase Paquete, que reúne cuatro "
    "patrones de comportamiento sobre un mismo objeto: cambia de estado "
    "(State), notifica a sus observadores en cada transición (Observer), cada "
    "avance se envuelve en un comando con deshacer (Command) y ese deshacer "
    "se apoya en una instantánea (Memento). En el plano estructural, la "
    "fachada de reservas (Facade) coordina a su vez el cálculo de distancia "
    "(Adapter) y la consulta de tarifas (Proxy). De esta manera, los patrones "
    "no solo están presentes, sino que se apoyan entre sí dentro del mismo "
    "escenario.",
]


# ---------------------------------------------------------------------------
# Clases de infraestructura y dominio (van primero, por pedido del equipo).
# nombre, rol, descripcion (prosa breve), archivo (ruta relativa a src/.../transporte)
# ---------------------------------------------------------------------------
INFRAESTRUCTURA = [
    {
        "nombre": "Entrada",
        "rol": "Fuente de datos",
        "descripcion":
            "Única fuente de datos del programa. El Cliente le pide los datos "
            "que necesita (ubicaciones, nombre del cliente, peso del paquete, "
            "zona de tarifa, unidades de la flota, etc.) y no sabe de dónde "
            "salen. Hoy devuelve valores de ejemplo fijos; mañana podría "
            "leerlos de consola, de un archivo o de una base de datos sin que "
            "el resto del programa cambie.",
        "archivo": "app/Entrada.java",
    },
    {
        "nombre": "Salida",
        "rol": "Presentación",
        "descripcion":
            "Único punto del programa que escribe en la salida estándar. "
            "Ninguna clase de patrón imprime por su cuenta: todas devuelven "
            "datos y el Cliente se los entrega a esta clase para que los "
            "interprete y los muestre. Si se quisiera escribir a un archivo o "
            "a una interfaz gráfica, solo cambiaría esta clase.",
        "archivo": "app/Salida.java",
    },
    {
        "nombre": "Cliente",
        "rol": "Lógica central",
        "descripcion":
            "Contiene la lógica central del escenario. Orquesta los 22 "
            "patrones agrupados en tres métodos (creacionales, estructurales y "
            "comportamiento). Obtiene todos sus datos de Entrada y envía todo "
            "lo que hay que mostrar a Salida, de modo que la lógica queda "
            "separada de la entrada y de la salida.",
        "archivo": "app/Cliente.java",
    },
    {
        "nombre": "Main",
        "rol": "Punto de entrada",
        "descripcion":
            "Punto de entrada de la aplicación. Su única responsabilidad es "
            "ensamblar las piezas (Entrada, Salida y Cliente) y ejecutar el "
            "Cliente. No contiene lógica de negocio.",
        "archivo": "Main.java",
    },
    {
        "nombre": "Ubicacion",
        "rol": "Modelo de dominio",
        "descripcion":
            "Valor inmutable que representa un punto geográfico (una parada de "
            "la ruta), con nombre, latitud y longitud. Al ser inmutable, "
            "puede compartirse con seguridad entre varios objetos.",
        "archivo": "dominio/Ubicacion.java",
    },
    {
        "nombre": "TipoVehiculo",
        "rol": "Modelo de dominio",
        "descripcion":
            "Enumeración de los tipos de vehículo que maneja la empresa "
            "(moto, furgoneta y camión).",
        "archivo": "dominio/TipoVehiculo.java",
    },
]


# ---------------------------------------------------------------------------
# Catálogo de patrones.
# Cada patrón: nombre, categoria, paquete, explicacion (lista de párrafos),
#              clases (lista de dicts: nombre, rol, archivo).
# El orden de "clases" define el orden en que aparece el código.
# ---------------------------------------------------------------------------
PATRONES = [
    # =====================  CREACIONALES  =====================
    {
        "nombre": "Singleton",
        "categoria": "Creacional",
        "paquete": "patrones.creacionales.singleton",
        "explicacion": [
            "Singleton garantiza que una clase tenga una única instancia y "
            "ofrece un punto de acceso global a ella. En TransExpress se usa "
            "para la configuración de la empresa (nombre y moneda), que debe "
            "ser la misma en todo el programa.",
            "La implementación emplea la técnica del initialization-on-demand "
            "holder: una clase interna estática crea la instancia la primera "
            "vez que se la solicita. Es segura entre hilos y perezosa sin "
            "necesidad de bloqueos (synchronized), evitando el antipatrón del "
            "doble chequeo mal implementado. Además, la instancia es "
            "inmutable (solo lectura), por lo que no degenera en una variable "
            "global mutable.",
        ],
        "clases": [
            {"nombre": "ConfiguracionEmpresa", "rol": "Singleton",
             "archivo": "patrones/creacionales/singleton/ConfiguracionEmpresa.java"},
        ],
    },
    {
        "nombre": "Factory Method",
        "categoria": "Creacional",
        "paquete": "patrones.creacionales.factory",
        "explicacion": [
            "Factory Method define una interfaz para crear un objeto, pero "
            "deja que las subclases decidan de qué clase concreta será. En "
            "TransExpress, un centro de despacho define el proceso de asignar "
            "un vehículo, pero cada centro concreto decide qué vehículo crea.",
            "La clase abstracta CentroDespacho declara el método fábrica "
            "crearVehiculo() y la operación de negocio asignarVehiculo() que "
            "lo utiliza. El centro urbano produce una Moto y el de carga "
            "produce un Camión. Así, el código que asigna vehículos no depende "
            "de clases concretas, respetando el principio de inversión de "
            "dependencias. La presentación del resultado la realiza la capa de "
            "salida, no el patrón.",
        ],
        "clases": [
            {"nombre": "Vehiculo", "rol": "Producto",
             "archivo": "patrones/creacionales/factory/Vehiculo.java"},
            {"nombre": "Moto", "rol": "Producto concreto",
             "archivo": "patrones/creacionales/factory/Moto.java"},
            {"nombre": "Furgoneta", "rol": "Producto concreto",
             "archivo": "patrones/creacionales/factory/Furgoneta.java"},
            {"nombre": "Camion", "rol": "Producto concreto",
             "archivo": "patrones/creacionales/factory/Camion.java"},
            {"nombre": "CentroDespacho", "rol": "Creador (abstracto)",
             "archivo": "patrones/creacionales/factory/CentroDespacho.java"},
            {"nombre": "CentroDespachoUrbano", "rol": "Creador concreto",
             "archivo": "patrones/creacionales/factory/CentroDespachoUrbano.java"},
            {"nombre": "CentroDespachoCarga", "rol": "Creador concreto",
             "archivo": "patrones/creacionales/factory/CentroDespachoCarga.java"},
        ],
    },
    {
        "nombre": "Abstract Factory",
        "categoria": "Creacional",
        "paquete": "patrones.creacionales.abstractfactory",
        "explicacion": [
            "Abstract Factory crea familias de objetos relacionados sin "
            "especificar sus clases concretas. En TransExpress, cada tipo de "
            "servicio produce una familia coherente formada por un vehículo y "
            "un embalaje que combinan entre sí.",
            "La interfaz FabricaServicio declara crearVehiculo() y "
            "crearEmbalaje(). La fábrica económica combina Moto con embalaje "
            "estándar, y la premium combina Furgoneta con embalaje premium. "
            "Cada fábrica concreta garantiza la coherencia de la familia que "
            "entrega, lo que distingue a este patrón del Factory Method: aquí "
            "se crean varios productos relacionados, no uno solo. Reutiliza la "
            "interfaz Vehiculo definida en el Factory Method.",
        ],
        "clases": [
            {"nombre": "Embalaje", "rol": "Producto abstracto",
             "archivo": "patrones/creacionales/abstractfactory/Embalaje.java"},
            {"nombre": "EmbalajeEstandar", "rol": "Producto concreto",
             "archivo": "patrones/creacionales/abstractfactory/EmbalajeEstandar.java"},
            {"nombre": "EmbalajePremium", "rol": "Producto concreto",
             "archivo": "patrones/creacionales/abstractfactory/EmbalajePremium.java"},
            {"nombre": "FabricaServicio", "rol": "Fábrica abstracta",
             "archivo": "patrones/creacionales/abstractfactory/FabricaServicio.java"},
            {"nombre": "FabricaServicioEconomico", "rol": "Fábrica concreta",
             "archivo": "patrones/creacionales/abstractfactory/FabricaServicioEconomico.java"},
            {"nombre": "FabricaServicioPremium", "rol": "Fábrica concreta",
             "archivo": "patrones/creacionales/abstractfactory/FabricaServicioPremium.java"},
        ],
    },
    {
        "nombre": "Builder",
        "categoria": "Creacional",
        "paquete": "patrones.creacionales.builder",
        "explicacion": [
            "Builder separa la construcción de un objeto complejo de su "
            "representación, permitiendo crearlo paso a paso. En TransExpress "
            "se usa para armar una orden de transporte que tiene campos "
            "opcionales (si es frágil, si es urgente) además de los "
            "obligatorios (cliente, origen y destino).",
            "Se emplea la variante fluent builder: cada método de "
            "configuración devuelve el propio builder para encadenar llamadas, "
            "y la construcción termina con construir(). El producto resultante, "
            "OrdenTransporte, es inmutable y solo puede crearse a través de su "
            "Builder. De este modo se evita el antipatrón del constructor "
            "telescópico, es decir, múltiples constructores sobrecargados con "
            "cada vez más parámetros.",
        ],
        "clases": [
            {"nombre": "OrdenTransporte", "rol": "Producto + Builder anidado",
             "archivo": "patrones/creacionales/builder/OrdenTransporte.java"},
        ],
    },
    {
        "nombre": "Prototype",
        "categoria": "Creacional",
        "paquete": "patrones.creacionales.prototype",
        "explicacion": [
            "Prototype crea nuevos objetos copiando un prototipo existente en "
            "lugar de construirlos desde cero. En TransExpress se aplica a las "
            "plantillas de ruta: se parte de una ruta base ya configurada y se "
            "clona para adaptarla sin afectar al original.",
            "El método clonar() usa un constructor de copia privado, una "
            "alternativa más segura que la interfaz Cloneable de Java. La "
            "lista de paradas se copia a una lista nueva e independiente; como "
            "las Ubicacion que contiene son inmutables, compartir sus "
            "referencias es seguro y no hace falta copiarlas una a una. "
            "Modificar el clon (renombrarlo o agregar paradas) no altera el "
            "prototipo original.",
        ],
        "clases": [
            {"nombre": "PlantillaRuta", "rol": "Prototipo",
             "archivo": "patrones/creacionales/prototype/PlantillaRuta.java"},
        ],
    },
    # =====================  ESTRUCTURALES  =====================
    {
        "nombre": "Adapter",
        "categoria": "Estructural",
        "paquete": "patrones.estructurales.adapter",
        "explicacion": [
            "Adapter permite que colaboren objetos con interfaces "
            "incompatibles. En TransExpress hay una librería externa de mapas "
            "que trabaja con coordenadas crudas y devuelve metros, pero la "
            "aplicación espera trabajar con ubicaciones y kilómetros.",
            "Se usa la variante de object adapter (por composición): "
            "AdaptadorApiMapas implementa la interfaz que la aplicación espera "
            "(ServicioDistancia) y envuelve la API externa (ApiMapasExterna), "
            "traduciendo las llamadas y convirtiendo metros a kilómetros. El "
            "resto del sistema no se entera de la existencia de la API "
            "externa.",
        ],
        "clases": [
            {"nombre": "ServicioDistancia", "rol": "Interfaz esperada (Target)",
             "archivo": "patrones/estructurales/adapter/ServicioDistancia.java"},
            {"nombre": "ApiMapasExterna", "rol": "Clase externa (Adaptee)",
             "archivo": "patrones/estructurales/adapter/ApiMapasExterna.java"},
            {"nombre": "AdaptadorApiMapas", "rol": "Adaptador",
             "archivo": "patrones/estructurales/adapter/AdaptadorApiMapas.java"},
        ],
    },
    {
        "nombre": "Bridge",
        "categoria": "Estructural",
        "paquete": "patrones.estructurales.bridge",
        "explicacion": [
            "Bridge separa una abstracción de su implementación para que ambas "
            "puedan variar de forma independiente. En TransExpress, el tipo de "
            "envío (nacional, internacional) y el medio de transporte "
            "(terrestre, aéreo) evolucionan por separado.",
            "La abstracción Envio mantiene por composición una referencia a un "
            "MedioTransporte y le delega la parte física del traslado. De este "
            "modo se evita la explosión combinatoria de subclases: en lugar de "
            "crear una clase por cada combinación de tipo y medio, se combinan "
            "libremente en tiempo de ejecución.",
        ],
        "clases": [
            {"nombre": "MedioTransporte", "rol": "Implementación (Implementor)",
             "archivo": "patrones/estructurales/bridge/MedioTransporte.java"},
            {"nombre": "TransporteTerrestre", "rol": "Implementación concreta",
             "archivo": "patrones/estructurales/bridge/TransporteTerrestre.java"},
            {"nombre": "TransporteAereo", "rol": "Implementación concreta",
             "archivo": "patrones/estructurales/bridge/TransporteAereo.java"},
            {"nombre": "Envio", "rol": "Abstracción",
             "archivo": "patrones/estructurales/bridge/Envio.java"},
            {"nombre": "EnvioNacional", "rol": "Abstracción refinada",
             "archivo": "patrones/estructurales/bridge/EnvioNacional.java"},
            {"nombre": "EnvioInternacional", "rol": "Abstracción refinada",
             "archivo": "patrones/estructurales/bridge/EnvioInternacional.java"},
        ],
    },
    {
        "nombre": "Composite",
        "categoria": "Estructural",
        "paquete": "patrones.estructurales.composite",
        "explicacion": [
            "Composite compone objetos en estructuras de árbol y permite "
            "tratar de forma uniforme a los objetos individuales y a sus "
            "composiciones. En TransExpress, una ruta puede estar formada por "
            "tramos simples y por otras sub-rutas, a cualquier nivel de "
            "profundidad.",
            "La interfaz ComponenteRuta es común a la hoja (Tramo) y al "
            "compuesto (RutaCompuesta). El compuesto delega recursivamente en "
            "sus hijos: la distancia total es la suma de las distancias de sus "
            "componentes. Se eligió la variante segura del patrón, en la que "
            "solo el compuesto tiene el método para agregar hijos; así una "
            "hoja no expone operaciones de gestión que no tendrían sentido.",
        ],
        "clases": [
            {"nombre": "ComponenteRuta", "rol": "Componente",
             "archivo": "patrones/estructurales/composite/ComponenteRuta.java"},
            {"nombre": "Tramo", "rol": "Hoja",
             "archivo": "patrones/estructurales/composite/Tramo.java"},
            {"nombre": "RutaCompuesta", "rol": "Compuesto",
             "archivo": "patrones/estructurales/composite/RutaCompuesta.java"},
        ],
    },
    {
        "nombre": "Decorator",
        "categoria": "Estructural",
        "paquete": "patrones.estructurales.decorator",
        "explicacion": [
            "Decorator añade responsabilidades a un objeto de forma dinámica "
            "envolviéndolo en otro objeto con la misma interfaz. En "
            "TransExpress se usa para agregar extras a un envío (seguro, "
            "entrega urgente) sin modificar el servicio base.",
            "El componente ServicioEnvio define costo y descripción. El "
            "decorador abstracto ExtraEnvio mantiene una referencia al "
            "servicio envuelto, y cada decorador concreto suma su costo y su "
            "texto a los del objeto que envuelve. Como los decoradores "
            "comparten la interfaz del componente, se pueden apilar "
            "libremente: por ejemplo, un envío básico con seguro y entrega "
            "urgente.",
        ],
        "clases": [
            {"nombre": "ServicioEnvio", "rol": "Componente",
             "archivo": "patrones/estructurales/decorator/ServicioEnvio.java"},
            {"nombre": "EnvioBasico", "rol": "Componente concreto",
             "archivo": "patrones/estructurales/decorator/EnvioBasico.java"},
            {"nombre": "ExtraEnvio", "rol": "Decorador (abstracto)",
             "archivo": "patrones/estructurales/decorator/ExtraEnvio.java"},
            {"nombre": "ConSeguro", "rol": "Decorador concreto",
             "archivo": "patrones/estructurales/decorator/ConSeguro.java"},
            {"nombre": "ConEntregaUrgente", "rol": "Decorador concreto",
             "archivo": "patrones/estructurales/decorator/ConEntregaUrgente.java"},
        ],
    },
    {
        "nombre": "Facade",
        "categoria": "Estructural",
        "paquete": "patrones.estructurales.facade",
        "explicacion": [
            "Facade ofrece una interfaz simple y unificada a un subsistema "
            "complejo. En TransExpress, cotizar un envío implica calcular la "
            "distancia y consultar la tarifa; la fachada esconde esa "
            "complejidad detrás de una sola operación.",
            "FachadaReservas coordina dos subsistemas que, a su vez, son otros "
            "patrones: el cálculo de distancia (resuelto con el Adapter) y la "
            "consulta de tarifas (resuelta con el Proxy). El cliente solo "
            "llama a cotizar() y no necesita conocer el subsistema. Este "
            "patrón es un buen ejemplo de convivencia, porque apoya su trabajo "
            "en Adapter y Proxy.",
        ],
        "clases": [
            {"nombre": "FachadaReservas", "rol": "Fachada",
             "archivo": "patrones/estructurales/facade/FachadaReservas.java"},
        ],
    },
    {
        "nombre": "Flyweight",
        "categoria": "Estructural",
        "paquete": "patrones.estructurales.flyweight",
        "explicacion": [
            "Flyweight comparte eficientemente gran cantidad de objetos que "
            "tienen estado común, para ahorrar memoria. En TransExpress, "
            "muchas unidades de la flota pueden ser del mismo modelo de "
            "vehículo, por lo que conviene compartir ese dato en lugar de "
            "duplicarlo.",
            "El flyweight ModeloVehiculo guarda el estado intrínseco "
            "(compartido): marca, modelo y consumo. La FabricaModelos actúa "
            "como caché y garantiza que cada modelo se cree una sola vez y se "
            "reutilice. La UnidadFlota combina el estado extrínseco (la placa, "
            "propia de cada unidad) con una referencia al flyweight. El "
            "flyweight es inmutable, requisito del patrón, ya que un objeto "
            "compartido no debe tener estado mutable.",
        ],
        "clases": [
            {"nombre": "ModeloVehiculo", "rol": "Flyweight",
             "archivo": "patrones/estructurales/flyweight/ModeloVehiculo.java"},
            {"nombre": "FabricaModelos", "rol": "Fábrica de flyweights",
             "archivo": "patrones/estructurales/flyweight/FabricaModelos.java"},
            {"nombre": "UnidadFlota", "rol": "Contexto (estado extrínseco)",
             "archivo": "patrones/estructurales/flyweight/UnidadFlota.java"},
        ],
    },
    {
        "nombre": "Proxy",
        "categoria": "Estructural",
        "paquete": "patrones.estructurales.proxy",
        "explicacion": [
            "Proxy proporciona un sustituto de otro objeto para controlar el "
            "acceso a él. En TransExpress se usa un proxy de caché sobre el "
            "servicio de tarifas, que simula una consulta costosa.",
            "El proxy ProxyTarifasCache comparte la interfaz del servicio real "
            "(ServicioTarifas) y lo sustituye de forma transparente: si una "
            "zona ya fue consultada, devuelve el valor cacheado sin volver a "
            "llamar al servicio real. El cliente no nota la diferencia. El "
            "proxy expone contadores de consultas reales y servidas desde "
            "caché para que la capa de salida pueda mostrarlos, de modo que el "
            "patrón no imprime por su cuenta.",
        ],
        "clases": [
            {"nombre": "ServicioTarifas", "rol": "Interfaz común",
             "archivo": "patrones/estructurales/proxy/ServicioTarifas.java"},
            {"nombre": "ServicioTarifasReal", "rol": "Objeto real",
             "archivo": "patrones/estructurales/proxy/ServicioTarifasReal.java"},
            {"nombre": "ProxyTarifasCache", "rol": "Proxy",
             "archivo": "patrones/estructurales/proxy/ProxyTarifasCache.java"},
        ],
    },
    # ===================  COMPORTAMIENTO  ===================
    {
        "nombre": "Chain of Responsibility",
        "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.chain",
        "explicacion": [
            "Chain of Responsibility pasa una petición por una cadena de "
            "manejadores hasta que uno la atiende o la rechaza. En "
            "TransExpress se usa para validar una orden de transporte "
            "aplicando varias reglas encadenadas.",
            "La clase base ValidadorOrden mantiene la referencia al siguiente "
            "eslabón y define el método validar(), que revisa su propia regla "
            "y delega en el siguiente si todo está bien. Hay un validador de "
            "peso y uno de destino. Gracias a la cadena, se pueden añadir, "
            "quitar o reordenar validaciones sin tocar las demás.",
        ],
        "clases": [
            {"nombre": "ValidadorOrden", "rol": "Manejador (abstracto)",
             "archivo": "patrones/comportamiento/chain/ValidadorOrden.java"},
            {"nombre": "ValidadorPeso", "rol": "Manejador concreto",
             "archivo": "patrones/comportamiento/chain/ValidadorPeso.java"},
            {"nombre": "ValidadorDestino", "rol": "Manejador concreto",
             "archivo": "patrones/comportamiento/chain/ValidadorDestino.java"},
        ],
    },
    {
        "nombre": "Command",
        "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.command",
        "explicacion": [
            "Command encapsula una operación como un objeto, lo que permite "
            "ejecutarla, deshacerla y guardarla en un historial. En "
            "TransExpress se usa para las operaciones sobre un envío, con "
            "posibilidad de deshacer.",
            "La interfaz Comando define ejecutar() y deshacer(). El comando "
            "concreto AvanzarEnvioComando adelanta el estado de un paquete y, "
            "para poder deshacerse, guarda una instantánea antes de ejecutar "
            "(apoyándose en el patrón Memento) y la restaura al deshacer. El "
            "invocador PanelOperaciones ejecuta comandos y mantiene un "
            "historial, sin conocer los detalles de cada comando. Es un buen "
            "ejemplo de colaboración entre Command y Memento.",
        ],
        "clases": [
            {"nombre": "Comando", "rol": "Comando (interfaz)",
             "archivo": "patrones/comportamiento/command/Comando.java"},
            {"nombre": "AvanzarEnvioComando", "rol": "Comando concreto",
             "archivo": "patrones/comportamiento/command/AvanzarEnvioComando.java"},
            {"nombre": "PanelOperaciones", "rol": "Invocador",
             "archivo": "patrones/comportamiento/command/PanelOperaciones.java"},
        ],
    },
    {
        "nombre": "Iterator",
        "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.iterator",
        "explicacion": [
            "Iterator permite recorrer los elementos de una colección sin "
            "exponer su representación interna. En TransExpress se usa para "
            "recorrer las unidades de la flota.",
            "La clase Flota implementa Iterable e incluye un iterador interno "
            "con hasNext() y next(). Al implementar la interfaz estándar de "
            "Java, la flota se integra de forma idiomática con el bucle "
            "for-each. El iterador lanza NoSuchElementException cuando se "
            "agota, respetando el contrato de Iterator.",
        ],
        "clases": [
            {"nombre": "Flota", "rol": "Colección iterable + iterador interno",
             "archivo": "patrones/comportamiento/iterator/Flota.java"},
        ],
    },
    {
        "nombre": "Mediator",
        "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.mediator",
        "explicacion": [
            "Mediator centraliza la comunicación entre objetos para reducir el "
            "acoplamiento entre ellos. En TransExpress, un centro de despacho "
            "coordina a los conductores, que no se conocen entre sí.",
            "La interfaz CentroDespacho define cómo se comunican los "
            "conductores. Cada Conductor (colega) solo conoce al mediador: le "
            "envía mensajes y recibe los que este le reenvía. El mediador "
            "concreto CentroDespachoRadio retransmite el mensaje de un "
            "conductor a todos los demás. Para respetar la separación de "
            "responsabilidades, el conductor guarda los mensajes recibidos en "
            "lugar de imprimirlos, y el Cliente los muestra a través de Salida.",
        ],
        "clases": [
            {"nombre": "CentroDespacho", "rol": "Mediador (interfaz)",
             "archivo": "patrones/comportamiento/mediator/CentroDespacho.java"},
            {"nombre": "Conductor", "rol": "Colega",
             "archivo": "patrones/comportamiento/mediator/Conductor.java"},
            {"nombre": "CentroDespachoRadio", "rol": "Mediador concreto",
             "archivo": "patrones/comportamiento/mediator/CentroDespachoRadio.java"},
        ],
    },
    {
        "nombre": "Memento",
        "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.memento",
        "explicacion": [
            "Memento captura y restaura el estado interno de un objeto sin "
            "violar su encapsulamiento. En TransExpress se usa para guardar y "
            "restaurar el estado de un paquete, lo que permite deshacer "
            "operaciones.",
            "MementoPaquete guarda el estado de envío y expone su lectura con "
            "visibilidad de paquete (package-private), de modo que solo el "
            "originador (Paquete), que vive en el mismo paquete, puede leerlo. "
            "Esta es la técnica correcta en Java para preservar el "
            "encapsulamiento del Memento. El Paquete es, además, el punto de "
            "encuentro de cuatro patrones de comportamiento (State, Observer, "
            "Memento y, a través del comando, Command).",
        ],
        "clases": [
            {"nombre": "MementoPaquete", "rol": "Memento",
             "archivo": "patrones/comportamiento/memento/MementoPaquete.java"},
            {"nombre": "Paquete", "rol": "Originador (State + Observer + Memento)",
             "archivo": "patrones/comportamiento/memento/Paquete.java"},
        ],
    },
    {
        "nombre": "Observer",
        "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.observer",
        "explicacion": [
            "Observer notifica automáticamente a varios objetos cuando otro "
            "cambia de estado. En TransExpress, cuando un paquete cambia de "
            "estado, se notifica al cliente por distintos canales (SMS, "
            "email).",
            "El sujeto observable es la clase Paquete, que mantiene una lista "
            "de observadores y los notifica en cada transición. El observador "
            "concreto NotificadorCliente produce salida por naturaleza, pero "
            "no imprime por su cuenta: recibe el destino de la salida como una "
            "dependencia inyectada (un Consumer de texto), de modo que la capa "
            "de salida sigue siendo el único canal real. Así se respeta la "
            "regla de que solo el Cliente habla con Salida.",
        ],
        "clases": [
            {"nombre": "ObservadorEnvio", "rol": "Observador (interfaz)",
             "archivo": "patrones/comportamiento/observer/ObservadorEnvio.java"},
            {"nombre": "NotificadorCliente", "rol": "Observador concreto",
             "archivo": "patrones/comportamiento/observer/NotificadorCliente.java"},
        ],
    },
    {
        "nombre": "State",
        "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.state",
        "explicacion": [
            "State permite que un objeto cambie su comportamiento cuando "
            "cambia su estado interno. En TransExpress modela el ciclo de vida "
            "de un envío: CREADO, EN_RUTA y ENTREGADO.",
            "La interfaz EstadoEnvio define la transición al siguiente estado "
            "y el nombre de cada uno. Cada estado concreto sabe cuál es su "
            "sucesor; el estado final (ENTREGADO) se devuelve a sí mismo. El "
            "contexto (Paquete) delega en el estado actual. La ventaja clave "
            "es que las transiciones viven en los estados y no en una cadena "
            "gigante de condicionales dentro del paquete, evitando ese "
            "antipatrón.",
        ],
        "clases": [
            {"nombre": "EstadoEnvio", "rol": "Estado (interfaz)",
             "archivo": "patrones/comportamiento/state/EstadoEnvio.java"},
            {"nombre": "EstadoCreado", "rol": "Estado concreto",
             "archivo": "patrones/comportamiento/state/EstadoCreado.java"},
            {"nombre": "EstadoEnRuta", "rol": "Estado concreto",
             "archivo": "patrones/comportamiento/state/EstadoEnRuta.java"},
            {"nombre": "EstadoEntregado", "rol": "Estado concreto (final)",
             "archivo": "patrones/comportamiento/state/EstadoEntregado.java"},
        ],
    },
    {
        "nombre": "Strategy",
        "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.strategy",
        "explicacion": [
            "Strategy define una familia de algoritmos intercambiables y "
            "permite seleccionarlos en tiempo de ejecución. En TransExpress se "
            "usa para calcular la tarifa de un envío con distintos criterios.",
            "La interfaz EstrategiaTarifa declara el cálculo del precio. Una "
            "estrategia cobra por distancia y otra por peso. El contexto (el "
            "Cliente) elige la estrategia a usar sin cambiar su propio código, "
            "lo que respeta el principio abierto/cerrado: se pueden añadir "
            "nuevas estrategias sin modificar al llamador. Cada estrategia "
            "devuelve el valor calculado; no imprime.",
        ],
        "clases": [
            {"nombre": "EstrategiaTarifa", "rol": "Estrategia (interfaz)",
             "archivo": "patrones/comportamiento/strategy/EstrategiaTarifa.java"},
            {"nombre": "TarifaPorDistancia", "rol": "Estrategia concreta",
             "archivo": "patrones/comportamiento/strategy/TarifaPorDistancia.java"},
            {"nombre": "TarifaPorPeso", "rol": "Estrategia concreta",
             "archivo": "patrones/comportamiento/strategy/TarifaPorPeso.java"},
        ],
    },
    {
        "nombre": "Template Method",
        "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.template",
        "explicacion": [
            "Template Method define el esqueleto de un algoritmo y deja que "
            "las subclases rellenen algunos pasos sin alterar su estructura. "
            "En TransExpress modela el proceso de entrega, que tiene pasos "
            "fijos y pasos que varían.",
            "La clase abstracta ProcesoEntrega define el método plantilla "
            "procesar(), que fija el orden de los pasos (recoger, transportar "
            "y confirmar) y es final para que no se altere. Los pasos recoger "
            "y transportar son abstractos y cada subclase (express o "
            "económica) los personaliza; confirmar es un paso común. Para "
            "respetar la separación de responsabilidades, los pasos devuelven "
            "texto y procesar() devuelve la secuencia para que la capa de "
            "salida la muestre.",
        ],
        "clases": [
            {"nombre": "ProcesoEntrega", "rol": "Clase plantilla (abstracta)",
             "archivo": "patrones/comportamiento/template/ProcesoEntrega.java"},
            {"nombre": "EntregaExpress", "rol": "Subclase concreta",
             "archivo": "patrones/comportamiento/template/EntregaExpress.java"},
            {"nombre": "EntregaEconomica", "rol": "Subclase concreta",
             "archivo": "patrones/comportamiento/template/EntregaEconomica.java"},
        ],
    },
    {
        "nombre": "Visitor",
        "categoria": "Comportamiento",
        "paquete": "patrones.comportamiento.visitor",
        "explicacion": [
            "Visitor separa un algoritmo de la estructura de objetos sobre la "
            "que opera, permitiendo añadir nuevas operaciones sin modificar "
            "esas clases. En TransExpress se usa para calcular la facturación "
            "recorriendo distintos tipos de envío.",
            "Cada elemento facturable implementa aceptar(visitante) y realiza "
            "la doble despacho (double dispatch) llamando al método específico "
            "del visitante para su tipo. El visitante VisitanteFacturacion "
            "define un método de cobro por cada tipo de envío (local e "
            "internacional). Así se puede agregar una nueva operación (otro "
            "visitante) sin tocar las clases de los elementos.",
        ],
        "clases": [
            {"nombre": "ElementoFacturable", "rol": "Elemento (interfaz)",
             "archivo": "patrones/comportamiento/visitor/ElementoFacturable.java"},
            {"nombre": "VisitanteCobro", "rol": "Visitante (interfaz)",
             "archivo": "patrones/comportamiento/visitor/VisitanteCobro.java"},
            {"nombre": "EnvioLocal", "rol": "Elemento concreto",
             "archivo": "patrones/comportamiento/visitor/EnvioLocal.java"},
            {"nombre": "EnvioInternacional", "rol": "Elemento concreto",
             "archivo": "patrones/comportamiento/visitor/EnvioInternacional.java"},
            {"nombre": "VisitanteFacturacion", "rol": "Visitante concreto",
             "archivo": "patrones/comportamiento/visitor/VisitanteFacturacion.java"},
        ],
    },
]


# ---------------------------------------------------------------------------
# Sección 4: Entradas y salidas (prosa + salida de consola).
# ---------------------------------------------------------------------------
ENTRADAS_SALIDAS = [
    "El programa no recibe entrada del usuario: todos los datos (ubicaciones, "
    "nombre del cliente, peso del paquete, zona de tarifa, unidades de la "
    "flota, nombres de conductores y mensaje de radio) están definidos en la "
    "clase Entrada como parte de la demostración. Esta clase es la única "
    "fuente de datos; el Cliente se los pide y no sabe de dónde provienen, de "
    "modo que en el futuro podrían leerse de consola o de un archivo sin "
    "afectar al resto del programa.",

    "La salida se produce exclusivamente a través de la clase Salida, que es "
    "el único punto del programa que escribe por consola. Ninguna clase de "
    "patrón imprime por su cuenta: todas devuelven datos y el Cliente los "
    "entrega a Salida. La simulación recorre las tres familias de patrones en "
    "orden (creacionales, estructurales y de comportamiento) e imprime una "
    "línea por patrón, rotulada con su nombre entre corchetes, indicando dónde "
    "interviene en el ciclo de vida del envío.",

    "En la salida se aprecian las colaboraciones entre patrones. Por ejemplo, "
    "en la sección de comportamiento, el mismo paquete cambia de estado "
    "(State), lo notifica a los canales SMS y Email (Observer), avanza "
    "mediante comandos (Command) y luego se deshace restaurando una "
    "instantánea (Memento), volviendo de ENTREGADO a EN_RUTA. En la sección "
    "estructural, la fachada produce una cotización y el proxy informa cuántas "
    "consultas fueron reales y cuántas se sirvieron desde la caché.",
]

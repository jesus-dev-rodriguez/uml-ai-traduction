# **2 Conformidad (Conformance)**

Existen cinco tipos distintos de conformidad, los cuales se enumeran a continuación. A menos que se indique lo contrario, estos tipos de conformidad son independientes.

- 1 _Conformidad de sintaxis abstracta._ Una herramienta que demuestra conformidad de sintaxis abstracta proporciona una interfaz de usuario y/o API que permite crear, leer, actualizar y eliminar instancias de **metaclases** concretas de UML. La herramienta también debe proporcionar una forma de validar la corrección formal (*well-formedness*) de los modelos que corresponda a las restricciones definidas en el **metamodelo** de UML.

- 2 _Conformidad de sintaxis concreta._ Una herramienta que demuestra conformidad de sintaxis concreta proporciona una interfaz de usuario y/o API que permite crear, leer, actualizar y eliminar instancias de la **notación** de UML. Tenga en cuenta que una herramienta conforme puede proporcionar la capacidad de crear, leer, actualizar y eliminar diagramas y elementos de notación adicionales que no estén definidos en UML.

- 3 _Conformidad de intercambio de modelos._ Una herramienta que demuestra conformidad de intercambio de modelos puede importar y exportar XMI conforme para todos los modelos UML válidos, incluidos los modelos con perfiles definidos y/o aplicados. La conformidad de intercambio de modelos implica conformidad de **sintaxis abstracta**. Una herramienta UML 2.5 conforme debe ser capaz de cargar y guardar XMI en formato UML 2.4.1 así como en formato UML 2.5 (consulte el Anexo E).

- 4 _Conformidad de intercambio de diagramas._ Una herramienta que demuestra conformidad de intercambio de diagramas puede importar y exportar DI conforme (consulte el Anexo B) para todos los modelos UML válidos con diagramas, incluidos los modelos con perfiles definidos y/o aplicados. La conformidad de intercambio de diagramas implica tanto la conformidad de sintaxis concreta como la conformidad de intercambio de modelos.

- 5 _Conformidad semántica._ Una herramienta que demuestra conformidad semántica proporciona una forma demostrable de interpretar la **semántica** de UML (por ejemplo, mediante la generación de código, ejecución de modelos o análisis de modelos semánticos). La especificación normativa para la semántica de UML incluye la cláusula 6.3 además de las subdivisiones de Semántica de las cláusulas 7 a 22. La conformidad semántica implica conformidad de **sintaxis abstracta**.

Donde la especificación de UML proporciona opciones para una herramienta conforme, estas se establecen explícitamente en la especificación. En otros casos, ciertos aspectos de la semántica se enumeran como "indefinidos", "intencionalmente no especificados" o "no especificados", lo que permite personalizaciones específicas de dominio o aplicación. Solo las personalizaciones que no contradigan las disposiciones de esta especificación se considerarán conformes con ella. Sin embargo, los modelos cuyo significado se base en tales personalizaciones solo podrán intercambiarse sin pérdidas con herramientas que admitan las mismas personalizaciones o compatibles.

Esta especificación comprende este documento junto con la serialización XMI contenida en los archivos legibles por máquina enumerados en la página de portada. Si hubiera algún conflicto entre este documento y los archivos legibles por máquina, estos últimos tendrán preferencia.

---
*Unified Modeling Language 2.5.1*

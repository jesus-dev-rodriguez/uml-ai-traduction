# Lenguaje Unificado de Modelado (UML) - Especificación 2.5.1

Traducción y adaptación al español de la especificación oficial de OMG UML 2.5.1 (`formal/2017-12-05`).

---


# **1 Alcance (Scope)**

Esta especificación define el Lenguaje Unificado de Modelado (UML), revisión 2. El objetivo de UML es proporcionar a los arquitectos de sistemas, ingenieros de software y desarrolladores herramientas para el análisis, diseño y la implementación de sistemas basados en software, así como para el modelado de procesos de negocio y procesos similares.

Las versiones iniciales de UML (UML 1) se originaron a partir de tres métodos orientados a objetos líderes (Booch, OMT y OOSE) e incorporaron una serie de mejores prácticas provenientes del diseño de lenguajes de modelado, la programación orientada a objetos y los lenguajes de descripción arquitectónica. En relación con UML 1, esta revisión de UML se ha mejorado con definiciones significativamente más precisas de sus reglas de **sintaxis abstracta** y semántica, una estructura de lenguaje más modular y una capacidad enormemente mejorada para el modelado de sistemas a gran escala.

Uno de los objetivos principales de UML es hacer avanzar el estado de la industria permitiendo la interoperabilidad de herramientas de modelado visual de objetos. Sin embargo, para permitir un intercambio significativo de información de modelos entre herramientas, se requiere un acuerdo sobre la semántica y la sintaxis. UML satisface los siguientes requisitos:

- Una definición formal de un **metamodelo** común basado en MOF que especifica la **sintaxis abstracta** de UML. La sintaxis abstracta define el conjunto de conceptos de modelado de UML, sus **atributos** y sus relaciones, así como las reglas para combinar estos conceptos con el fin de construir modelos UML parciales o completos.

- Una explicación detallada de la **semántica** de cada concepto de modelado de UML. La semántica define, de manera independiente de la tecnología, cómo los conceptos de UML deben ser realizados por las computadoras.

- Una especificación de los elementos de **notación** legibles por humanos para representar los conceptos individuales de modelado de UML, así como las reglas para combinarlos en una variedad de tipos de diagramas diferentes correspondientes a distintos aspectos de los sistemas modelados.

---
*Unified Modeling Language 2.5.1*


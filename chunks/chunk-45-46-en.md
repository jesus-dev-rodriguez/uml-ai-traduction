# **2 Conformance** 

There are five distinct types of conformance. These are listed below. Unless otherwise stated these types of conformance are independent. 

- 1 _Abstract syntax conformance._ A tool demonstrating abstract syntax conformance provides a user interface and/or API that enables instances of concrete UML metaclasses to be created, read, updated, and deleted. The tool must also provide a way to validate the well-formedness of models that corresponds to the constraints defined in the UML metamodel. 

- 2 _Concrete syntax conformance._ A tool demonstrating concrete syntax conformance provides a user interface and/or API that enables instances of UML notation to be created, read, updated, and deleted. Note that a conforming tool may provide the ability to create, read, update and delete additional diagrams and notational elements that are not defined in UML. 

- 3 _Model interchange conformance._ A tool demonstrating model interchange conformance can import and export conformant XMI for all valid UML models, including models with profiles defined and/or applied. Model interchange conformance implies abstract syntax conformance. A conforming UML 2.5 tool shall be able to load and save XMI in UML 2.4.1 format as well as UML 2.5 format (see Annex E). 

- 4 _Diagram interchange conformance._ A tool demonstrating diagram interchange conformance can import and export conformant DI (see Annex B) for all valid UML models with diagrams, including models with profiles defined and/or applied. Diagram interchange conformance implies both concrete syntax conformance and model interchange conformance. 

- 5 _Semantic conformance._ A tool demonstrating semantic conformance provides a demonstrable way to interpret UML semantics, e.g., code generation, model execution, or semantic model analysis. The normative specification for UML semantics includes clause 6.3 in addition to the Semantics subdivisions of clauses 7-22. Semantic conformance implies Abstract Syntax conformance. 

Where the UML specification provides options for a conforming tool, these are explicitly stated in the specification. In a number of other cases, certain aspects of the semantics are listed as "undefined" or “intentionally not specified” or “not specified”, allowing for domain- or application-specific customizations. Only customizations that do not contradict the provisions of this specification will be deemed to conform to it. However, models whose meaning is based on such customizations can only be interchanged without loss with tools that support the same or compatible customizations. 

This specification comprises this document together with XMI serialization contained in machine-consumable files as listed on the cover page. If there are any conflicts between this document and the machine-consumable files, the machine-consumable files take precedence. 

**3** 

Unified Modeling Language 2.5.1 


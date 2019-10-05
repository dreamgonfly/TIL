# ERD

Entity Relationship Diagram, also known as ERD, ER Diagram or ER model, is a type of structural diagram for use in database design. An ERD contains different symbols and connectors that visualize two important information: **The major entities within the system scope**, and the **inter-relationships among these entities**. And that's why it's called "Entity" "Relationship" diagram (ERD)!

![](images/Untitled-b669c709-a6c3-4641-8695-61f3048b8db0.png)
# Entity

An ERD entity is a definable thing or concept within a system, such as a person/role (e.g. Student), object (e.g. Invoice), concept (e.g. Profile) or event (e.g. Transaction) When determining entities, think of them as nouns.

![](images/Untitled-27ebf66e-10b5-4e7b-b679-fe4065255862.png)
## Entity Attributes

Also known as a **column**, an attribute is a property or characteristic of the entity that holds it.

![](images/Untitled-7833203b-60fe-4a72-8559-fdfbcf804562.png)
## Primary Key

Also known as PK, a primary key is a special kind of entity attribute that uniquely defines a record in a database table.

## Foreign Key

Also known as FK, a foreign key is a reference to a primary key in a table.

![](images/Untitled-c7a1b866-477c-4511-8cd5-c1aca18877d5.png)
# Relationship

**Cardinality** defines the possible number of occurrences in one entity which is associated with the number of occurrences in another. For example, ONE team has MANY players. When present in an ERD, the entity Team and Player are inter-connected with a one-to-many relationship.

In an ER diagram, cardinality is represented as a crow's foot at the connector's ends. The three common cardinal relationships are one-to-one, one-to-many, and many-to-many.

## One-to-One cardinality example

A one-to-one relationship is mostly used to split an entity in two to provide information concisely and make it more understandable.

![](images/Untitled-723057a8-e3cb-4321-86bf-6f64cd3735a1.png)
## One-to-Many cardinality example

A one-to-many relationship refers to the relationship between two entities X and Y in which an instance of X may be linked to many instances of Y, but an instance of Y is linked to only one instance of X. The figure below shows an example of a one-to-many relationship.

![](images/Untitled-430bcf60-2636-42b5-9916-f61b593824de.png)
## Many-to-Many cardinality example

A many-to-many relationship refers to the relationship between two entities X and Y in which X may be linked to many instances of Y and vice versa. Note that a many-to-many relationship is split into a pair of one-to-many relationships in a physical ERD.

![](images/Untitled-daac7659-58ef-4ac7-9a23-21914133d552.png)
# Conceptual, Logical and Physical data models

An ER model is typically drawn at up to three levels of abstraction:

- [Conceptual ERD / Conceptual data model](https://www.visual-paradigm.com/guide/data-modeling/what-is-entity-relationship-diagram/#erd-data-models-conceptual)
- [Logical ERD / Logical data model](https://www.visual-paradigm.com/guide/data-modeling/what-is-entity-relationship-diagram/#erd-data-models-logical)
- [Physical ERD / Physical data model](https://www.visual-paradigm.com/guide/data-modeling/what-is-entity-relationship-diagram/#erd-data-models-physical)

A general understanding to the three data models is that business analyst uses a conceptual and logical model to model the business objects exist in the system, while database designer or database engineer elaborates the conceptual and logical ER model to produce the physical model that presents the physical database structure ready for database creation.

![](images/Untitled-128b234a-de1c-4706-a73a-8d6b455ca89d.png)
## Conceptual data model

Conceptual ERD models the business objects that should exist in a system and the relationships between them. A conceptual model is developed to present an overall picture of the system by recognizing the business objects involved. For example, 'many to many' tables may exist in a logical or physical data model but they are just shown as a relationship with no cardinality under the conceptual data model.

![](images/Untitled-ad48a77c-8ae0-4967-81ae-51e79553ce0f.png)
Conceptual ERD supports the use of generalization in modeling the 'a kind of' relationship between two entities, for instance, Triangle, is a kind of Shape. The usage is like generalization in UML. Notice that only conceptual ERD supports generalization.

## Logical data model

Logical ERD is a detailed version of a Conceptual ERD.

![](images/Untitled-f9f3be1c-b947-4b92-8244-3ceaa91500c0.png)
## Physical data model

Physical ERD represents the actual design blueprint of a relational database. A physical data model elaborates on the logical data model by assigning each column with type, length, nullable, etc. Make sure the column types are supported by the DBMS and reserved words are not used in naming entities and columns.

![](images/Untitled-e4ac7bfc-ff66-4b06-ab69-7cbe5dc38436.png)
# Examples

## Movie Rental System

![](images/Untitled-2ca5cec5-8c22-4107-9e3f-9002813237eb.png)
# References

[What is Entity Relationship Diagram (ERD)?](https://www.visual-paradigm.com/guide/data-modeling/what-is-entity-relationship-diagram/)
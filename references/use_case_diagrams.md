# Use Case Diagrams

Use case diagrams show how actors (users or external systems) interact with a system, illustrating the system's functionality from the user's perspective.

## Basic Elements

```puml
@startuml
left to right direction

actor Customer
actor Admin

rectangle "E-Commerce System" {
  Customer -- (Browse Products)
  Customer -- (Place Order)
  (Place Order) ..> (Process Payment) : include
  (Place Order) ..|> (Save Order) : extends

  Admin -- (Manage Inventory)
  Admin -- (View Reports)
}
@enduml
```

## Actor Types

```puml
@startuml
:User: as U
:Admin: as A
actor "System Administrator" as SA

U --> (Login)
A --> (Manage Users)
SA --> (Configure System)
@enduml
```

## Relationships

- `--` **Association** - Actor uses use case
- `..>` **Include** - Mandatory inclusion
- `..|>` **Extend** - Optional extension
- `<|--` **Generalization** - Inheritance

```puml
@startuml
:User: as U
:Premium User: as PU

PU --|> U : extends

(Basic Search) as BS
(Advanced Search) as AS
(Export Results) as ER

U --> BS
PU --> AS
AS --|> BS : extends
AS ..> ER : <<include>>
@enduml
```

## System Boundaries

```puml
@startuml
left to right direction

actor Customer
actor Support

rectangle "Online Banking" {
  Customer -- (View Balance)
  Customer -- (Transfer Money)
  (Transfer Money) ..> (Verify Identity) : <<include>>
}

rectangle "Admin Panel" {
  Support -- (View Logs)
  Support -- (Manage Users)
}
@enduml
```

## Conversion

```bash
java -jar plantuml.jar -tsvg usecase.puml
```

See [toc.md](toc.md) for all diagram types.

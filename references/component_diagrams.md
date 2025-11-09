# Component Diagrams

Component diagrams show how a system is decomposed into components and how these components depend on each other through interfaces and ports.

## Basic Structure

```puml
@startuml
[Web Frontend]
[API Gateway]
[Database]

[Web Frontend] --> [API Gateway] : HTTP/REST
[API Gateway] --> [Database] : SQL
@enduml
```

## Interfaces and Ports

```puml
@startuml
interface "REST API" as REST
interface "Database" as DB

component "Application Server" {
  [Business Logic] as BL
  [Data Access] as DA
}

REST - BL
BL - DA
DA - DB
@enduml
```

## Dependencies

```puml
@startuml
package "Frontend" {
  [Web UI]
  [Mobile App]
}

package "Backend" {
  [Auth Service]
  [User Service]
}

[Web UI] ..> [Auth Service] : depends on
[Mobile App] ..> [Auth Service] : depends on
@enduml
```

See [toc.md](toc.md) for all diagram types.

# PlantUML Styling Guide

Comprehensive guide to modern PlantUML styling using the `<style>` tag with CSS-like syntax.

## Table of Contents

1. [Why Modern `<style>` Over Legacy `skinparam`](#why-modern-style-over-legacy-skinparam)
2. [Basic `<style>` Syntax](#basic-style-syntax)
3. [Element Selectors](#element-selectors)
4. [Stereotype Selectors](#stereotype-selectors)
5. [Common Style Properties](#common-style-properties)
6. [Styling by Diagram Type](#styling-by-diagram-type)
7. [Advanced Styling Techniques](#advanced-styling-techniques)
8. [Creole Text Formatting](#creole-text-formatting)
9. [Complete Styling Examples](#complete-styling-examples)

---

## Why Modern `<style>` Over Legacy `skinparam`

### The Dual-Engine System

PlantUML supports two styling approaches:

1. **Legacy `skinparam`** - Imperative commands scattered throughout diagrams
2. **Modern `<style>`** - Declarative CSS-like rules in dedicated style blocks

### Why Choose `<style>`?

✅ **Separation of Concerns**: Style separate from content
✅ **CSS-Familiar Syntax**: Uses standard CSS properties
✅ **Better Organization**: All styles in one place
✅ **Reusability**: Define styles once, apply via stereotypes
✅ **Maintainability**: Easier to update and manage

### Comparison Example

**Legacy `skinparam` approach** (avoid):
```puml
@startuml
skinparam class {
  BackgroundColor PaleGreen
  BorderColor SeaGreen
  ArrowColor SeaGreen
}
skinparam classFontColor Blue
skinparam classFontSize 14

class User {
  +username
  +email
}
@enduml
```

**Modern `<style>` approach** (recommended):
```puml
@startuml
<style>
classDiagram {
  class {
    BackgroundColor PaleGreen
    BorderColor SeaGreen
    FontColor Blue
    FontSize 14
  }
  arrow {
    LineColor SeaGreen
  }
}
</style>

class User {
  +username
  +email
}
@enduml
```

---

## Basic `<style>` Syntax

### Structure

```puml
@startuml
<style>
diagramType {
  element {
    Property Value
    Property Value
  }
}
</style>

' Your diagram content here
@enduml
```

### Simple Example

```puml
@startuml
<style>
classDiagram {
  class {
    BackgroundColor LightBlue
    BorderColor Navy
    FontColor DarkBlue
  }
}
</style>

class Example
@enduml
```

---

## Element Selectors

### Common Elements Across Diagram Types

| Element | Description | Applies To |
|---------|-------------|------------|
| `class` | Class boxes | Class diagrams |
| `component` | Component boxes | Component diagrams |
| `actor` | Actor symbols | Use case, sequence |
| `participant` | Participants | Sequence diagrams |
| `entity` | Entity boxes | ER diagrams |
| `state` | State boxes | State diagrams |
| `activity` | Activity boxes | Activity diagrams |
| `node` | Deployment nodes | Deployment diagrams |
| `arrow` | All arrows/lines | Most diagrams |
| `note` | Note boxes | All diagrams |
| `package` | Package containers | Class, component |
| `frame` | Frame boxes | Sequence diagrams |

### Example: Styling Multiple Elements

```puml
@startuml
<style>
classDiagram {
  class {
    BackgroundColor #E8F4F8
    BorderColor #0277BD
    FontColor #01579B
    FontSize 14
    FontStyle bold
  }

  arrow {
    LineColor #0277BD
    LineThickness 2
  }

  note {
    BackgroundColor #FFF9C4
    BorderColor #F57F17
    FontColor #E65100
  }

  package {
    BackgroundColor #F3E5F5
    BorderColor #7B1FA2
    FontColor #4A148C
  }
}
</style>

package "Domain Model" {
  class User {
    +id: Long
    +username: String
  }

  class Order {
    +orderId: Long
    +total: BigDecimal
  }

  User "1" --> "*" Order
}

note right of User
  Primary domain entity
end note
@enduml
```

---

## Stereotype Selectors

### What Are Stereotypes?

Stereotypes allow you to define reusable style classes and apply them to specific elements using `<<stereotype_name>>`.

### Defining Stereotype Styles

```puml
@startuml
<style>
classDiagram {
  .entity {
    BackgroundColor LightYellow
    BorderColor Orange
    FontColor DarkOrange
  }

  .service {
    BackgroundColor LightBlue
    BorderColor Blue
    FontColor DarkBlue
  }

  .repository {
    BackgroundColor LightGreen
    BorderColor Green
    FontColor DarkGreen
  }
}
</style>

class User <<entity>> {
  +id
  +name
}

class UserService <<service>> {
  +createUser()
  +findUser()
}

class UserRepository <<repository>> {
  +save()
  +findById()
}
@enduml
```

### Multiple Stereotypes

```puml
@startuml
<style>
classDiagram {
  .important {
    BorderThickness 3
    FontStyle bold
  }

  .deprecated {
    BackgroundColor #FFE0E0
    FontColor #999999
    FontStyle italic
  }

  .experimental {
    BackgroundColor #E0F0FF
    BorderStyle dashed
  }
}
</style>

class CriticalService <<important>>
class OldAPI <<deprecated>>
class BetaFeature <<experimental>>
@enduml
```

---

## Common Style Properties

### Color Properties

| Property | Description | Example Values |
|----------|-------------|----------------|
| `BackgroundColor` | Fill color | `LightBlue`, `#E8F4F8` |
| `BorderColor` | Border/stroke color | `Navy`, `#0277BD` |
| `FontColor` | Text color | `DarkBlue`, `#01579B` |
| `LineColor` | Line/arrow color | `SeaGreen`, `#2E7D32` |

**Named Colors**: Red, Blue, Green, Yellow, Orange, Purple, Pink, Gray, Black, White, and their variants (Light*, Dark*, Pale*)

**Hex Colors**: `#RRGGBB` format (e.g., `#FF5722`, `#4CAF50`)

### Font Properties

| Property | Description | Values |
|----------|-------------|--------|
| `FontSize` | Text size | `10`, `12`, `14`, `16` |
| `FontStyle` | Text style | `normal`, `bold`, `italic` |
| `FontName` | Font family | `Arial`, `Courier`, `SansSerif` |

### Border Properties

| Property | Description | Values |
|----------|-------------|--------|
| `BorderThickness` | Border width | `1`, `2`, `3`, `4` |
| `BorderStyle` | Line style | `solid`, `dashed`, `dotted` |
| `RoundCorner` | Corner radius | `0`, `5`, `10`, `15` |

### Spacing Properties

| Property | Description | Values |
|----------|-------------|--------|
| `Padding` | Internal spacing | `5`, `10`, `15` |
| `Margin` | External spacing | `5`, `10`, `15` |

---

## Styling by Diagram Type

### Class Diagrams

```puml
@startuml
<style>
classDiagram {
  class {
    BackgroundColor #FFFDE7
    BorderColor #F57F17
    FontColor #E65100
    FontSize 13
    RoundCorner 10
  }

  interface {
    BackgroundColor #E8EAF6
    BorderColor #3F51B5
    FontColor #1A237E
    FontStyle italic
  }

  abstract {
    BackgroundColor #F3E5F5
    BorderColor #9C27B0
    FontStyle italic
  }

  arrow {
    LineColor #616161
    LineThickness 2
  }
}
</style>

interface Repository {
  +save()
  +findById()
}

abstract class BaseEntity {
  #id: Long
  #createdAt: Date
}

class User extends BaseEntity {
  +username: String
  +email: String
}

class UserRepository implements Repository
@enduml
```

### Sequence Diagrams

```puml
@startuml
<style>
sequenceDiagram {
  participant {
    BackgroundColor #E1F5FE
    BorderColor #0277BD
    FontColor #01579B
    FontSize 13
  }

  actor {
    BackgroundColor #FFF9C4
    BorderColor #F57F17
    FontColor #E65100
  }

  arrow {
    LineColor #00796B
    LineThickness 2
  }

  lifeLine {
    LineColor #0277BD
    LineStyle dashed
  }
}
</style>

actor User
participant "Web App" as Web
participant "API Service" as API
database "Database" as DB

User -> Web : Login request
activate Web
Web -> API : Authenticate
activate API
API -> DB : Query user
DB --> API : User data
API --> Web : Auth token
deactivate API
Web --> User : Success
deactivate Web
@enduml
```

### Activity Diagrams

```puml
@startuml
<style>
activityDiagram {
  activity {
    BackgroundColor #C8E6C9
    BorderColor #388E3C
    FontColor #1B5E20
    RoundCorner 15
  }

  diamond {
    BackgroundColor #FFECB3
    BorderColor #F57C00
    FontColor #E65100
  }

  arrow {
    LineColor #424242
    LineThickness 2
  }
}
</style>

start
:Receive order;
if (Stock available?) then (yes)
  :Process payment;
  :Ship order;
else (no)
  :Notify customer;
  :Backorder item;
endif
stop
@enduml
```

### Component Diagrams

```puml
@startuml
<style>
componentDiagram {
  component {
    BackgroundColor #BBDEFB
    BorderColor #1976D2
    FontColor #0D47A1
    FontSize 12
  }

  interface {
    BackgroundColor #C8E6C9
    BorderColor #388E3C
    FontColor #1B5E20
  }

  package {
    BackgroundColor #F5F5F5
    BorderColor #9E9E9E
    FontColor #424242
  }
}
</style>

package "Frontend" {
  component [Web UI]
  component [Mobile App]
}

package "Backend" {
  component [API Gateway]
  component [Auth Service]
  component [Data Service]
}

[Web UI] --> [API Gateway]
[Mobile App] --> [API Gateway]
[API Gateway] --> [Auth Service]
[API Gateway] --> [Data Service]
@enduml
```

### State Diagrams

```puml
@startuml
<style>
stateDiagram {
  state {
    BackgroundColor #E1BEE7
    BorderColor #8E24AA
    FontColor #4A148C
    RoundCorner 10
  }

  arrow {
    LineColor #6A1B9A
    LineThickness 2
    FontColor #4A148C
  }
}
</style>

[*] --> Draft
Draft --> InReview : Submit
InReview --> Approved : Accept
InReview --> Rejected : Decline
Rejected --> Draft : Revise
Approved --> Published : Publish
Published --> [*]
@enduml
```

### Entity-Relationship Diagrams

```puml
@startuml
<style>
entityRelationshipDiagram {
  entity {
    BackgroundColor #FFF3E0
    BorderColor #EF6C00
    FontColor #E65100
    FontSize 12
  }

  arrow {
    LineColor #BF360C
    LineThickness 2
  }
}
</style>

entity Customer {
  *customer_id : UUID <<PK>>
  --
  email : VARCHAR
  name : VARCHAR
}

entity Order {
  *order_id : UUID <<PK>>
  --
  #customer_id : UUID <<FK>>
  order_date : TIMESTAMP
  total : DECIMAL
}

entity OrderItem {
  *item_id : UUID <<PK>>
  --
  #order_id : UUID <<FK>>
  #product_id : UUID <<FK>>
  quantity : INTEGER
  price : DECIMAL
}

Customer ||--o{ Order
Order ||--o{ OrderItem
@enduml
```

### Use Case Diagrams

```puml
@startuml
<style>
usecaseDiagram {
  usecase {
    BackgroundColor #E8F5E9
    BorderColor #388E3C
    FontColor #1B5E20
    FontSize 12
  }

  actor {
    BackgroundColor #FFF9C4
    BorderColor #F57F17
    FontColor #E65100
  }

  arrow {
    LineColor #689F38
    LineThickness 2
  }
}
</style>

actor Customer
actor Admin

rectangle "E-Commerce System" {
  usecase "Browse Products" as UC1
  usecase "Add to Cart" as UC2
  usecase "Checkout" as UC3
  usecase "Manage Inventory" as UC4
  usecase "View Reports" as UC5
}

Customer --> UC1
Customer --> UC2
Customer --> UC3
Admin --> UC4
Admin --> UC5
@enduml
```

---

## Advanced Styling Techniques

### Conditional Styling with Stereotypes

```puml
@startuml
<style>
classDiagram {
  .critical {
    BackgroundColor #FFCDD2
    BorderColor #D32F2F
    BorderThickness 3
    FontColor #B71C1C
    FontStyle bold
  }

  .warning {
    BackgroundColor #FFF9C4
    BorderColor #FBC02D
    BorderThickness 2
    FontColor #F57F17
  }

  .info {
    BackgroundColor #E1F5FE
    BorderColor #0288D1
    FontColor #01579B
  }

  .success {
    BackgroundColor #C8E6C9
    BorderColor #388E3C
    FontColor #1B5E20
  }
}
</style>

class PaymentService <<critical>> {
  +processPayment()
  +refund()
}

class NotificationService <<warning>> {
  +sendEmail()
  +sendSMS()
}

class LoggingService <<info>> {
  +logEvent()
  +logError()
}

class HealthCheck <<success>> {
  +ping()
  +getStatus()
}
@enduml
```

### Layer-Based Styling

```puml
@startuml
<style>
classDiagram {
  .presentation {
    BackgroundColor #E3F2FD
    BorderColor #1976D2
    FontColor #0D47A1
  }

  .business {
    BackgroundColor #FFF3E0
    BorderColor #F57C00
    FontColor #E65100
  }

  .data {
    BackgroundColor #F3E5F5
    BorderColor #7B1FA2
    FontColor #4A148C
  }
}
</style>

package "Presentation Layer" {
  class UserController <<presentation>>
  class OrderController <<presentation>>
}

package "Business Layer" {
  class UserService <<business>>
  class OrderService <<business>>
}

package "Data Layer" {
  class UserRepository <<data>>
  class OrderRepository <<data>>
}

UserController --> UserService
OrderController --> OrderService
UserService --> UserRepository
OrderService --> OrderRepository
@enduml
```

### Technology-Specific Styling

```puml
@startuml
<style>
componentDiagram {
  .react {
    BackgroundColor #61DAFB
    BorderColor #20232A
    FontColor #20232A
  }

  .spring {
    BackgroundColor #6DB33F
    BorderColor #FFF
    FontColor #FFF
  }

  .postgres {
    BackgroundColor #336791
    BorderColor #FFF
    FontColor #FFF
  }

  .redis {
    BackgroundColor #DC382D
    BorderColor #FFF
    FontColor #FFF
  }
}
</style>

component [React Frontend] <<react>>
component [Spring Boot API] <<spring>>
database [PostgreSQL] <<postgres>>
database [Redis Cache] <<redis>>

[React Frontend] --> [Spring Boot API]
[Spring Boot API] --> [PostgreSQL]
[Spring Boot API] --> [Redis Cache]
@enduml
```

### Gradient Effects (Limited Support)

```puml
@startuml
<style>
classDiagram {
  .gradient {
    BackgroundColor LightBlue-Blue
    FontColor White
    BorderColor DarkBlue
  }
}
</style>

class GradientExample <<gradient>> {
  +method()
}
@enduml
```

---

## Creole Text Formatting

Creole is PlantUML's wiki-style text markup system for inline formatting.

### Basic Text Formatting

| Syntax | Result | Example |
|--------|--------|---------|
| `**text**` | **Bold** | `**Important**` |
| `//text//` | *Italic* | `//Optional//` |
| `--text--` | ~~Strikethrough~~ | `--Deprecated--` |
| `__text__` | Underline | `__Required__` |
| `""text""` | Monospace | `""code()""` |

### Example in Diagram

```puml
@startuml
class User {
  +**username**: String
  +//email//: String
  +--oldPassword--: String
  +__required__ validate()
  +""toString()"": String
}

note right
  **Important**: Username must be unique
  //This is a draft specification//
  --Old API deprecated--
end note
@enduml
```

### Colors in Text

```puml
@startuml
class ColorExample {
  +<color:red>errorMessage</color>: String
  +<color:green>successFlag</color>: Boolean
  +<color:#FF5722>warningCode</color>: Integer
}

note left
  <color:blue>Blue text</color>
  <color:#4CAF50>Green with hex</color>
end note
@enduml
```

### Text Size

```puml
@startuml
class SizeExample {
  +<size:18>largeProperty</size>: String
  +<size:10>smallProperty</size>: Integer
}

note right
  <size:16>**Large heading**</size>
  <size:12>Normal text</size>
  <size:8>Small footnote</size>
end note
@enduml
```

### Hyperlinks

```puml
@startuml
class Documentation {
  +[[https://example.com See docs]]
  +[[https://api.example.com/user API Reference]]
}

note bottom
  Visit [[https://plantuml.com PlantUML site]]
  for more information
end note
@enduml
```

### Lists in Notes

```puml
@startuml
class TaskManager

note right
  **Features**:
  * Create tasks
  * Assign priorities
  * Set deadlines

  **Requirements**:
  # User authentication
  # Database connection
  # Email service
end note
@enduml
```

### Combining Formatting

```puml
@startuml
class AdvancedFormatting {
  +**<color:red>criticalError</color>**: String
  +//<size:10>optionalField</size>//: Integer
  +--<color:gray>deprecated</color>--: Boolean
}

note right
  **<color:blue>Status</color>**: <color:green>//Active//</color>
  **Version**: ""<size:10>2.1.0</size>""

  See [[https://docs.example.com documentation]]
  for details.
end note
@enduml
```

---

## Complete Styling Examples

### Example 1: Modern Enterprise Application

```puml
@startuml
<style>
classDiagram {
  .controller {
    BackgroundColor #E3F2FD
    BorderColor #1976D2
    FontColor #0D47A1
    FontSize 12
    RoundCorner 8
  }

  .service {
    BackgroundColor #FFF3E0
    BorderColor #F57C00
    FontColor #E65100
    FontSize 12
    RoundCorner 8
  }

  .repository {
    BackgroundColor #F3E5F5
    BorderColor #7B1FA2
    FontColor #4A148C
    FontSize 12
    RoundCorner 8
  }

  .entity {
    BackgroundColor #C8E6C9
    BorderColor #388E3C
    FontColor #1B5E20
    FontSize 12
    RoundCorner 8
  }

  arrow {
    LineColor #616161
    LineThickness 2
  }

  package {
    BackgroundColor #FAFAFA
    BorderColor #BDBDBD
    FontColor #424242
  }
}
</style>

package "Controllers" {
  class UserController <<controller>> {
    -userService: UserService
    +getUser(id: Long): User
    +createUser(dto: UserDTO): User
  }

  class OrderController <<controller>> {
    -orderService: OrderService
    +getOrder(id: Long): Order
    +createOrder(dto: OrderDTO): Order
  }
}

package "Services" {
  class UserService <<service>> {
    -userRepository: UserRepository
    +findById(id: Long): User
    +save(user: User): User
    +delete(id: Long): void
  }

  class OrderService <<service>> {
    -orderRepository: OrderRepository
    -userService: UserService
    +createOrder(order: Order): Order
    +calculateTotal(order: Order): BigDecimal
  }
}

package "Repositories" {
  class UserRepository <<repository>> {
    +findById(id: Long): Optional<User>
    +save(user: User): User
    +deleteById(id: Long): void
  }

  class OrderRepository <<repository>> {
    +findById(id: Long): Optional<Order>
    +save(order: Order): Order
    +findByUserId(userId: Long): List<Order>
  }
}

package "Entities" {
  class User <<entity>> {
    -id: Long
    -username: String
    -email: String
    -orders: List<Order>
  }

  class Order <<entity>> {
    -id: Long
    -userId: Long
    -orderDate: LocalDateTime
    -total: BigDecimal
  }
}

UserController --> UserService
OrderController --> OrderService
UserService --> UserRepository
OrderService --> OrderRepository
OrderService --> UserService
UserRepository ..> User
OrderRepository ..> Order
User "1" --> "*" Order
@enduml
```

### Example 2: Microservices Architecture

```puml
@startuml
<style>
componentDiagram {
  .gateway {
    BackgroundColor #2196F3
    BorderColor #0D47A1
    FontColor White
    FontSize 13
    FontStyle bold
  }

  .service {
    BackgroundColor #4CAF50
    BorderColor #1B5E20
    FontColor White
    FontSize 12
  }

  .database {
    BackgroundColor #9C27B0
    BorderColor #4A148C
    FontColor White
    FontSize 12
  }

  .cache {
    BackgroundColor #FF5722
    BorderColor #BF360C
    FontColor White
    FontSize 12
  }

  .queue {
    BackgroundColor #FF9800
    BorderColor #E65100
    FontColor White
    FontSize 12
  }

  arrow {
    LineColor #424242
    LineThickness 2
  }
}
</style>

component [API Gateway] <<gateway>>

component [User Service] <<service>>
component [Order Service] <<service>>
component [Inventory Service] <<service>>
component [Notification Service] <<service>>

database [User DB] <<database>>
database [Order DB] <<database>>
database [Inventory DB] <<database>>

database [Redis Cache] <<cache>>
queue [Message Queue] <<queue>>

[API Gateway] --> [User Service]
[API Gateway] --> [Order Service]
[API Gateway] --> [Inventory Service]

[User Service] --> [User DB]
[Order Service] --> [Order DB]
[Inventory Service] --> [Inventory DB]

[User Service] --> [Redis Cache]
[Order Service] --> [Redis Cache]

[Order Service] --> [Message Queue]
[Notification Service] <-- [Message Queue]
@enduml
```

### Example 3: Database Schema with Status Colors

```puml
@startuml
<style>
entityRelationshipDiagram {
  .core {
    BackgroundColor #E8F5E9
    BorderColor #2E7D32
    FontColor #1B5E20
    BorderThickness 2
  }

  .transactional {
    BackgroundColor #E3F2FD
    BorderColor #1565C0
    FontColor #0D47A1
    BorderThickness 2
  }

  .audit {
    BackgroundColor #FFF3E0
    BorderColor #EF6C00
    FontColor #E65100
  }

  arrow {
    LineColor #424242
    LineThickness 2
  }
}
</style>

entity User <<core>> {
  *user_id : UUID <<PK>>
  --
  **username** : VARCHAR(50) <<unique>>
  **email** : VARCHAR(255) <<unique>>
  password_hash : VARCHAR(255)
  created_at : TIMESTAMP
  updated_at : TIMESTAMP
}

entity Customer <<core>> {
  *customer_id : UUID <<PK>>
  --
  #user_id : UUID <<FK>>
  first_name : VARCHAR(100)
  last_name : VARCHAR(100)
  phone : VARCHAR(20)
}

entity Order <<transactional>> {
  *order_id : UUID <<PK>>
  --
  #customer_id : UUID <<FK>>
  order_date : TIMESTAMP
  status : VARCHAR(20)
  total_amount : DECIMAL(10,2)
  currency : VARCHAR(3)
}

entity OrderItem <<transactional>> {
  *item_id : UUID <<PK>>
  --
  #order_id : UUID <<FK>>
  #product_id : UUID <<FK>>
  quantity : INTEGER
  unit_price : DECIMAL(10,2)
  subtotal : DECIMAL(10,2)
}

entity Product <<core>> {
  *product_id : UUID <<PK>>
  --
  **sku** : VARCHAR(50) <<unique>>
  name : VARCHAR(200)
  description : TEXT
  price : DECIMAL(10,2)
  stock_quantity : INTEGER
}

entity AuditLog <<audit>> {
  *log_id : UUID <<PK>>
  --
  #user_id : UUID <<FK>>
  action : VARCHAR(50)
  entity_type : VARCHAR(50)
  entity_id : UUID
  timestamp : TIMESTAMP
  details : JSONB
}

User ||--|| Customer
Customer ||--o{ Order
Order ||--o{ OrderItem
Product ||--o{ OrderItem
User ||--o{ AuditLog
@enduml
```

### Example 4: State Machine with Emotion Colors

```puml
@startuml
<style>
stateDiagram {
  .initial {
    BackgroundColor #E0E0E0
    BorderColor #616161
    FontColor #212121
  }

  .active {
    BackgroundColor #C8E6C9
    BorderColor #388E3C
    FontColor #1B5E20
  }

  .warning {
    BackgroundColor #FFF9C4
    BorderColor #FBC02D
    FontColor #F57F17
  }

  .error {
    BackgroundColor #FFCDD2
    BorderColor #D32F2F
    FontColor #B71C1C
  }

  .success {
    BackgroundColor #B2DFDB
    BorderColor #00897B
    FontColor #004D40
  }

  arrow {
    LineColor #424242
    LineThickness 2
    FontSize 11
  }
}
</style>

[*] --> Created <<initial>>

state Created <<initial>> {
  [*] --> Draft
  Draft --> Submitted : submit()
}

state Active <<active>> {
  Submitted --> InReview : assign()
  InReview --> Testing : approve()
  Testing --> Testing : test_failed()
}

state Warning <<warning>> {
  InReview --> Revision : request_changes()
  Revision --> InReview : resubmit()
}

state Error <<error>> {
  Testing --> Failed : critical_bug()
  Failed --> InReview : fix_and_retry()
}

state Success <<success>> {
  Testing --> Approved : all_tests_pass()
  Approved --> Deployed : deploy()
}

Created --> Active
Active --> Warning
Active --> Error
Warning --> Active
Error --> Active
Active --> Success
Deployed --> [*]
@enduml
```

---

## Summary

### Modern Styling Best Practices

1. ✅ **Always use `<style>` tags** instead of `skinparam`
2. ✅ **Group styles by diagram type** for organization
3. ✅ **Use stereotypes** for reusable style classes
4. ✅ **Prefer named colors** for readability (or hex for precision)
5. ✅ **Apply consistent theming** across related diagrams
6. ✅ **Use Creole formatting** for rich text in notes and labels
7. ✅ **Keep styles separate** from diagram content

### Quick Reference

**Basic Template**:
```puml
@startuml
<style>
diagramType {
  element {
    BackgroundColor <color>
    BorderColor <color>
    FontColor <color>
    FontSize <number>
  }
}
</style>

' Your diagram here
@enduml
```

**With Stereotypes**:
```puml
@startuml
<style>
diagramType {
  .styleName {
    BackgroundColor <color>
    BorderColor <color>
  }
}
</style>

element Name <<styleName>>
@enduml
```

---

See [toc.md](toc.md) for all diagram types and [common_format.md](common_format.md) for universal diagram elements.

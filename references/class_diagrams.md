# Class Diagrams

Class diagrams show the static structure of a system, depicting classes, their attributes, methods, relationships, and how they relate to one another. They are foundational for object-oriented design documentation.

## Basic Class Definition

Define classes using the `class` keyword with attributes and methods specified inside curly braces:

```puml
@startuml
class Vehicle {
  -make : String
  -model : String
  #year : int
  +mileage : double
  ~registrationNumber : String

  +startEngine() : void
  +stopEngine() : void
  -calculateDepreciation() : double
  #performMaintenance() : void
}
@enduml
```

## Visibility Modifiers

PlantUML uses standard UML visibility symbols:

- `+` **Public** - Accessible everywhere
- `-` **Private** - Accessible only within the class
- `#` **Protected** - Accessible in this class and subclasses
- `~` **Package/Internal** - Accessible within the package

**Example:**

```puml
@startuml
class BankAccount {
  - accountNumber : String
  - balance : double
  # transactionHistory : List<Transaction>
  + accountHolder : String
  ~ branchCode : String

  + deposit(amount : double) : void
  + withdraw(amount : double) : boolean
  - validateTransaction(amount : double) : boolean
  # logTransaction(transaction : Transaction) : void
}
@enduml
```

### Alternative Icon Visibility

```puml
@startuml
skinparam classAttributeIconSize 0

class Example {
  + publicField
  - privateField
  # protectedField
  ~ packageField
}
@enduml
```

## Class Relationships

### Inheritance/Generalization (`<|--`)

Inheritance represents an "is-a" relationship:

```puml
@startuml
class Animal {
  # name : String
  # age : int
  + eat() : void
  + sleep() : void
}

class Dog {
  - breed : String
  + bark() : void
  + fetch() : void
}

class Cat {
  - indoor : boolean
  + meow() : void
  + purr() : void
}

Animal <|-- Dog
Animal <|-- Cat
@enduml
```

### Composition (`*--`)

Composition represents strong ownership - if the container is destroyed, so are the components:

```puml
@startuml
class Company {
  - name : String
  + dissolve() : void
}

class Department {
  - deptName : String
  - budget : double
}

class Employee {
  - employeeId : String
  - salary : double
}

Company *-- "1..*" Department : contains
Department *-- "1" Employee : has manager
@enduml
```

**Key Point:** In composition, the lifecycle of the part is tied to the whole. When Company is destroyed, Departments cease to exist.

### Aggregation (`o--`)

Aggregation represents weak ownership - parts can exist independently:

```puml
@startuml
class Department {
  - deptName : String
}

class Employee {
  - employeeId : String
  - name : String
}

class Project {
  - projectName : String
  - deadline : Date
}

Department o-- "*" Employee : employs
Employee "*" o-- "*" Project : works on
@enduml
```

**Key Point:** Employees can exist without a Department, and can work on multiple Projects.

### Association (`--`)

Association shows a general relationship:

```puml
@startuml
class Person {
  - name : String
  - dateOfBirth : Date
}

class Address {
  - street : String
  - city : String
  - zipCode : String
}

class PhoneNumber {
  - number : String
  - type : String
}

Person "1" -- "0..1" Address : lives at >
Person "1" -- "*" PhoneNumber : has >
@enduml
```

### Dependency (`..>`)

Dependency shows that one class uses another:

```puml
@startuml
class OrderService {
  + createOrder(items : List<Item>) : Order
  + calculateTotal(order : Order) : Money
}

class Order {
  - orderId : String
  - items : List<Item>
}

class EmailService {
  + sendConfirmation(email : String) : void
}

class Logger {
  + log(message : String) : void
}

OrderService ..> Order : creates
OrderService ..> EmailService : uses
OrderService ..> Logger : uses
@enduml
```

**Key Point:** Dependency means changes to the target class may require changes to the source class.

## Multiplicity

Express the number of instances in relationships:

- `1` - Exactly one
- `0..1` - Zero or one
- `*` or `0..*` - Zero or more
- `1..*` - One or more
- `m..n` - Between m and n (e.g., `3..7`)

```puml
@startuml
class University {
  - name : String
}

class Department {
  - name : String
}

class Professor {
  - name : String
  - tenure : boolean
}

class Student {
  - studentId : String
  - major : String
}

class Course {
  - courseCode : String
  - credits : int
}

University "1" *-- "1..*" Department
Department "1" o-- "5..50" Professor
Department "1" o-- "0..*" Student
Professor "1" -- "1..4" Course : teaches
Student "*" -- "*" Course : enrolled in
@enduml
```

## Abstract Classes and Interfaces

### Abstract Classes

```puml
@startuml
abstract class Shape {
  # color : String
  # position : Point
  + {abstract} calculateArea() : double
  + {abstract} draw() : void
  + setColor(c : String) : void
}

class Circle extends Shape {
  - radius : double
  + calculateArea() : double
  + draw() : void
}

class Rectangle extends Shape {
  - width : double
  - height : double
  + calculateArea() : double
  + draw() : void
}

Shape <|-- Circle
Shape <|-- Rectangle
@enduml
```

### Interfaces

```puml
@startuml
interface Drawable {
  + draw() : void
  + resize(width : int, height : int) : void
}

interface Serializable {
  + serialize() : String
  + deserialize(data : String) : void
}

class Component {
  - id : String
}

Drawable <|.. Component : implements
Serializable <|.. Component : implements
@enduml
```

**Dashed line (`<|..`)** is used for interface implementation.

## Enumerations

```puml
@startuml
enum OrderStatus {
  PENDING
  PROCESSING
  SHIPPED
  DELIVERED
  CANCELLED
}

enum PaymentMethod {
  CREDIT_CARD
  DEBIT_CARD
  PAYPAL
  BANK_TRANSFER
}

class Order {
  - orderId : String
  - status : OrderStatus
  - paymentMethod : PaymentMethod
  + updateStatus(status : OrderStatus) : void
}

Order --> OrderStatus
Order --> PaymentMethod
@enduml
```

## Stereotypes and Annotations

```puml
@startuml
class UserService <<Service>> {
  + createUser() : User
  + findUser(id : String) : User
}

class User <<Entity>> {
  - userId : String
  - username : String
  - email : String
}

class UserDTO <<DTO>> {
  + userId : String
  + username : String
}

class UserRepository <<Repository>> {
  + save(user : User) : void
  + findById(id : String) : User
}

UserService ..> User : creates
UserService ..> UserDTO : returns
UserService --> UserRepository : uses
@enduml
```

## Packages and Namespaces

```puml
@startuml
package "com.example.domain" {
  class User {
    - userId : String
    - username : String
  }

  class Order {
    - orderId : String
    - orderDate : Date
  }

  User "1" -- "*" Order : places
}

package "com.example.service" {
  class UserService {
    + createUser() : User
    + findUser(id : String) : User
  }

  class OrderService {
    + createOrder() : Order
    + findOrders(userId : String) : List<Order>
  }
}

package "com.example.repository" {
  interface UserRepository {
    + save(user : User) : void
    + findById(id : String) : User
  }

  interface OrderRepository {
    + save(order : Order) : void
    + findByUserId(userId : String) : List<Order>
  }
}

UserService --> "com.example.domain.User" : uses
OrderService --> "com.example.domain.Order" : uses
UserService --> UserRepository : uses
OrderService --> OrderRepository : uses
@enduml
```

## Generics

```puml
@startuml
class ArrayList<T> {
  - elements : T[]
  + add(element : T) : void
  + get(index : int) : T
  + size() : int
}

class HashMap<K, V> {
  - entries : Entry<K,V>[]
  + put(key : K, value : V) : void
  + get(key : K) : V
  + containsKey(key : K) : boolean
}

interface Repository<T, ID> {
  + save(entity : T) : void
  + findById(id : ID) : T
  + delete(entity : T) : void
}

class UserRepository implements Repository {
}

Repository <|.. UserRepository : implements Repository<User, String>
@enduml
```

## Notes and Documentation

```puml
@startuml
class PaymentProcessor {
  + processPayment(amount : Money) : PaymentResult
}

note right of PaymentProcessor
  This class handles all payment
  processing operations.

  **Thread-safe:** Yes
  **Retry logic:** 3 attempts
end note

note "Implements PCI DSS compliance" as N1
PaymentProcessor .. N1
@enduml
```

## Real-World Example: E-Commerce Domain Model

```puml
@startuml
package "Domain Model" {
  abstract class Entity {
    # id : UUID
    # createdAt : DateTime
    # updatedAt : DateTime
  }

  class Customer extends Entity {
    - email : String
    - firstName : String
    - lastName : String
    - passwordHash : String
    + register() : void
    + login(password : String) : boolean
  }

  class Order extends Entity {
    - orderNumber : String
    - orderDate : DateTime
    - status : OrderStatus
    - totalAmount : Money
    + calculateTotal() : Money
    + addItem(item : OrderItem) : void
    + checkout() : PaymentResult
  }

  class OrderItem {
    - quantity : int
    - unitPrice : Money
    + getSubtotal() : Money
  }

  class Product extends Entity {
    - sku : String
    - name : String
    - description : String
    - price : Money
    - stockQuantity : int
    + isAvailable() : boolean
    + reduceStock(quantity : int) : void
  }

  class ShoppingCart {
    - items : List<CartItem>
    + addProduct(product : Product, quantity : int) : void
    + removeProduct(product : Product) : void
    + getTotal() : Money
    + checkout() : Order
  }

  class Address <<Value Object>> {
    - street : String
    - city : String
    - state : String
    - zipCode : String
    - country : String
  }

  enum OrderStatus {
    PENDING
    PAID
    PROCESSING
    SHIPPED
    DELIVERED
    CANCELLED
  }

  Customer "1" -- "0..1" ShoppingCart : has
  Customer "1" -- "*" Order : places
  Customer "1" -- "*" Address : has shipping/billing
  Order "1" *-- "1..*" OrderItem : contains
  OrderItem "*" -- "1" Product : references
  Order --> OrderStatus
  Order "1" -- "1" Address : ships to
}
@enduml
```

## Tips and Best Practices

1. **Keep it focused** - One diagram per concern (don't mix persistence, service, and domain layers)
2. **Use packages** - Group related classes
3. **Show key relationships only** - Don't include every field/method
4. **Use stereotypes** - `<<Entity>>`, `<<Service>>`, `<<Repository>>`
5. **Leverage abstract classes** - Show common behavior at the right level
6. **Be consistent with naming** - Follow your project's conventions
7. **Add notes sparingly** - Document non-obvious design decisions
8. **Use multiplicity** - Make cardinality explicit

## Common Patterns

### Repository Pattern

```puml
@startuml
interface Repository<T> {
  + save(entity : T) : void
  + findById(id : ID) : T
  + findAll() : List<T>
  + delete(entity : T) : void
}

class UserRepository implements Repository {
  + findByEmail(email : String) : User
}

class OrderRepository implements Repository {
  + findByCustomerId(customerId : ID) : List<Order>
}

Repository <|.. UserRepository : <User, UUID>
Repository <|.. OrderRepository : <Order, UUID>
@enduml
```

### Factory Pattern

```puml
@startuml
interface Product {
  + use() : void
}

class ConcreteProductA implements Product {
  + use() : void
}

class ConcreteProductB implements Product {
  + use() : void
}

abstract class Creator {
  + {abstract} factoryMethod() : Product
  + someOperation() : void
}

class ConcreteCreatorA extends Creator {
  + factoryMethod() : Product
}

class ConcreteCreatorB extends Creator {
  + factoryMethod() : Product
}

Creator ..> Product : creates
ConcreteCreatorA ..> ConcreteProductA : creates
ConcreteCreatorB ..> ConcreteProductB : creates
@enduml
```

## Conversion to Images

```bash
# PNG
java -jar plantuml.jar class_diagram.puml

# SVG (recommended)
java -jar plantuml.jar -tsvg class_diagram.puml
```

See [plantuml_reference.md](plantuml_reference.md) for comprehensive CLI documentation.

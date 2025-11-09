# Entity-Relationship (ER) Diagrams

ER diagrams model database structure, showing entities, attributes, and relationships between entities. They are essential for database design and documentation.

## Basic Entity Definition

Define entities and their attributes:

```puml
@startuml
entity Customer {
  *customer_id : INTEGER <<PK>>
  --
  first_name : VARCHAR(50)
  last_name : VARCHAR(50)
  email : VARCHAR(100) <<unique>>
  phone : VARCHAR(20)
  created_at : TIMESTAMP
}

entity Order {
  *order_id : INTEGER <<PK>>
  --
  order_date : DATE
  total_amount : DECIMAL(10,2)
  status : VARCHAR(20)
  #customer_id : INTEGER <<FK>>
}
@enduml
```

## Attribute Notation

- `*` - **Primary Key** (PK)
- `#` - **Foreign Key** (FK)
- `--` - **Separator** between identifier and descriptive attributes

```puml
@startuml
entity Product {
  *product_id : INT <<PK>>
  *variant_id : INT <<PK>>
  --
  name : VARCHAR(100)
  description : TEXT
  price : DECIMAL(10,2)
  #category_id : INT <<FK>>
  created_at : TIMESTAMP
  updated_at : TIMESTAMP
}
@enduml
```

## Relationship Cardinality

PlantUML uses special notation for cardinality:

- `||` - **Exactly one**
- `|o` or `o|` - **Zero or one**
- `|{` or `}|` - **One or more**
- `o{` or `}o` - **Zero or more**

### One-to-Many Relationship

```puml
@startuml
entity Customer {
  *customer_id : INT <<PK>>
  --
  name : VARCHAR
  email : VARCHAR
}

entity Order {
  *order_id : INT <<PK>>
  --
  order_date : DATE
  #customer_id : INT <<FK>>
}

Customer ||--o{ Order : "places"
@enduml
```

**Reading:** One Customer places zero or more Orders.

### One-to-One Relationship

```puml
@startuml
entity User {
  *user_id : INT <<PK>>
  --
  username : VARCHAR
  email : VARCHAR
}

entity UserProfile {
  *profile_id : INT <<PK>>
  --
  bio : TEXT
  avatar_url : VARCHAR
  #user_id : INT <<FK>> <<unique>>
}

User ||--|| UserProfile : "has"
@enduml
```

**Reading:** One User has exactly one UserProfile.

### Many-to-Many Relationship

```puml
@startuml
entity Student {
  *student_id : INT <<PK>>
  --
  name : VARCHAR
  email : VARCHAR
}

entity Course {
  *course_id : INT <<PK>>
  --
  course_name : VARCHAR
  credits : INT
}

entity Enrollment {
  *student_id : INT <<PK,FK>>
  *course_id : INT <<PK,FK>>
  --
  enrollment_date : DATE
  grade : VARCHAR(2)
}

Student ||--o{ Enrollment
Course ||--o{ Enrollment
@enduml
```

**Reading:** Students and Courses have a many-to-many relationship through Enrollment.

## Cardinality Examples

```puml
@startuml
entity Author {
  *author_id : INT <<PK>>
  --
  name : VARCHAR
}

entity Book {
  *book_id : INT <<PK>>
  --
  title : VARCHAR
  isbn : VARCHAR
  #author_id : INT <<FK>>
}

entity Publisher {
  *publisher_id : INT <<PK>>
  --
  name : VARCHAR
}

entity Category {
  *category_id : INT <<PK>>
  --
  name : VARCHAR
}

entity BookCategory {
  *book_id : INT <<PK,FK>>
  *category_id : INT <<PK,FK>>
}

' One author writes one or more books
Author ||--|{ Book : writes

' Zero or one publisher publishes zero or more books
Publisher |o--o{ Book : publishes

' Books belong to many categories (many-to-many)
Book }o--|| BookCategory
Category ||--o{ BookCategory
@enduml
```

## Real-World Example: E-Commerce Database

```puml
@startuml
!define PK <<PK>>
!define FK <<FK>>

entity Customer {
  *customer_id : UUID PK
  --
  email : VARCHAR(255) <<unique>>
  password_hash : VARCHAR(255)
  first_name : VARCHAR(100)
  last_name : VARCHAR(100)
  phone : VARCHAR(20)
  created_at : TIMESTAMP
  updated_at : TIMESTAMP
}

entity Address {
  *address_id : UUID PK
  --
  #customer_id : UUID FK
  address_type : VARCHAR(20)
  street : VARCHAR(255)
  city : VARCHAR(100)
  state : VARCHAR(50)
  zip_code : VARCHAR(20)
  country : VARCHAR(50)
  is_default : BOOLEAN
}

entity Order {
  *order_id : UUID PK
  --
  #customer_id : UUID FK
  #shipping_address_id : UUID FK
  #billing_address_id : UUID FK
  order_number : VARCHAR(50) <<unique>>
  order_date : TIMESTAMP
  status : VARCHAR(20)
  subtotal : DECIMAL(10,2)
  tax : DECIMAL(10,2)
  shipping_cost : DECIMAL(10,2)
  total_amount : DECIMAL(10,2)
  created_at : TIMESTAMP
  updated_at : TIMESTAMP
}

entity OrderItem {
  *order_item_id : UUID PK
  --
  #order_id : UUID FK
  #product_id : UUID FK
  quantity : INTEGER
  unit_price : DECIMAL(10,2)
  subtotal : DECIMAL(10,2)
}

entity Product {
  *product_id : UUID PK
  --
  #category_id : UUID FK
  sku : VARCHAR(50) <<unique>>
  name : VARCHAR(255)
  description : TEXT
  price : DECIMAL(10,2)
  stock_quantity : INTEGER
  is_active : BOOLEAN
  created_at : TIMESTAMP
  updated_at : TIMESTAMP
}

entity Category {
  *category_id : UUID PK
  --
  #parent_category_id : UUID FK
  name : VARCHAR(100)
  description : TEXT
  display_order : INTEGER
}

entity Payment {
  *payment_id : UUID PK
  --
  #order_id : UUID FK
  payment_method : VARCHAR(50)
  payment_status : VARCHAR(20)
  transaction_id : VARCHAR(255)
  amount : DECIMAL(10,2)
  payment_date : TIMESTAMP
}

entity Review {
  *review_id : UUID PK
  --
  #product_id : UUID FK
  #customer_id : UUID FK
  rating : INTEGER
  title : VARCHAR(255)
  comment : TEXT
  created_at : TIMESTAMP
}

' Relationships
Customer ||--o{ Address : "has"
Customer ||--o{ Order : "places"
Customer ||--o{ Review : "writes"

Order }o--|| Address : "ships to"
Order }o--|| Address : "bills to"
Order ||--|{ OrderItem : "contains"
Order ||--o| Payment : "paid by"

Product ||--o{ OrderItem : "ordered in"
Product }o--|| Category : "belongs to"
Product ||--o{ Review : "reviewed in"

Category ||--o{ Category : "has subcategory"
@enduml
```

## Composite Primary Keys

```puml
@startuml
entity CourseSection {
  *course_id : INT PK, FK
  *section_number : INT PK
  *semester : VARCHAR(20) PK
  *year : INT PK
  --
  #instructor_id : INT FK
  room_number : VARCHAR(20)
  max_enrollment : INT
  current_enrollment : INT
}

entity Course {
  *course_id : INT PK
  --
  course_name : VARCHAR
  credits : INT
}

entity Instructor {
  *instructor_id : INT PK
  --
  name : VARCHAR
  department : VARCHAR
}

Course ||--o{ CourseSection
Instructor ||--o{ CourseSection
@enduml
```

## Self-Referencing Relationships

```puml
@startuml
entity Employee {
  *employee_id : INT PK
  --
  first_name : VARCHAR
  last_name : VARCHAR
  email : VARCHAR
  #manager_id : INT FK
  #department_id : INT FK
}

entity Department {
  *department_id : INT PK
  --
  department_name : VARCHAR
  #manager_employee_id : INT FK
}

Employee }o--o| Employee : "manages"
Employee }o--|| Department : "works in"
Department }o--|| Employee : "managed by"
@enduml
```

## Weak Entities

Weak entities depend on a strong entity for their existence:

```puml
@startuml
entity Building {
  *building_id : INT PK
  --
  building_name : VARCHAR
  address : VARCHAR
}

entity Room {
  *building_id : INT PK, FK
  *room_number : VARCHAR PK
  --
  floor : INT
  capacity : INT
  room_type : VARCHAR
}

Building ||--|{ Room : "contains"
@enduml
```

## Advanced Example: Multi-Tenant SaaS Database

```puml
@startuml
entity Tenant {
  *tenant_id : UUID PK
  --
  tenant_name : VARCHAR(255)
  subdomain : VARCHAR(100) <<unique>>
  plan : VARCHAR(50)
  status : VARCHAR(20)
  created_at : TIMESTAMP
}

entity User {
  *user_id : UUID PK
  --
  #tenant_id : UUID FK
  email : VARCHAR(255)
  password_hash : VARCHAR(255)
  role : VARCHAR(50)
  is_active : BOOLEAN
  last_login : TIMESTAMP
  created_at : TIMESTAMP
}

entity Project {
  *project_id : UUID PK
  --
  #tenant_id : UUID FK
  #owner_user_id : UUID FK
  project_name : VARCHAR(255)
  description : TEXT
  status : VARCHAR(20)
  created_at : TIMESTAMP
}

entity ProjectMember {
  *project_id : UUID PK, FK
  *user_id : UUID PK, FK
  --
  role : VARCHAR(50)
  joined_at : TIMESTAMP
}

entity Task {
  *task_id : UUID PK
  --
  #project_id : UUID FK
  #assigned_to_user_id : UUID FK
  #created_by_user_id : UUID FK
  title : VARCHAR(255)
  description : TEXT
  status : VARCHAR(20)
  priority : VARCHAR(20)
  due_date : DATE
  created_at : TIMESTAMP
}

entity Comment {
  *comment_id : UUID PK
  --
  #task_id : UUID FK
  #user_id : UUID FK
  comment_text : TEXT
  created_at : TIMESTAMP
}

entity Attachment {
  *attachment_id : UUID PK
  --
  #task_id : UUID FK
  #uploaded_by_user_id : UUID FK
  file_name : VARCHAR(255)
  file_path : VARCHAR(512)
  file_size : BIGINT
  mime_type : VARCHAR(100)
  uploaded_at : TIMESTAMP
}

' Relationships
Tenant ||--o{ User : "has"
Tenant ||--o{ Project : "owns"

User ||--o{ Project : "owns"
Project ||--o{ ProjectMember
User ||--o{ ProjectMember

Project ||--o{ Task : "contains"
User ||--o{ Task : "assigned"
User ||--o{ Task : "created"

Task ||--o{ Comment
User ||--o{ Comment : "writes"

Task ||--o{ Attachment
User ||--o{ Attachment : "uploads"
@enduml
```

## Tips and Best Practices

1. **Use UUIDs for distributed systems** - Better for microservices and sharding
2. **Add indexes as notes** - Document performance-critical indexes
3. **Show data types** - Helps with implementation
4. **Mark unique constraints** - Use `<<unique>>` stereotype
5. **Document cascading deletes** - Add notes for ON DELETE CASCADE
6. **Separate concerns** - Create multiple diagrams for complex schemas
7. **Use meaningful names** - Follow database naming conventions
8. **Add timestamps** - created_at, updated_at for audit trails

## Common Patterns

### Audit Log Pattern

```puml
@startuml
entity User {
  *user_id : UUID PK
  --
  username : VARCHAR
}

entity UserAuditLog {
  *audit_id : UUID PK
  --
  #user_id : UUID FK
  action : VARCHAR(50)
  old_value : JSONB
  new_value : JSONB
  changed_at : TIMESTAMP
  changed_by : UUID
}

User ||--o{ UserAuditLog
@enduml
```

### Soft Delete Pattern

```puml
@startuml
entity Product {
  *product_id : UUID PK
  --
  name : VARCHAR
  price : DECIMAL
  deleted_at : TIMESTAMP
  deleted_by : UUID
}

note right of Product
  NULL deleted_at = active
  Non-NULL deleted_at = soft deleted
end note
@enduml
```

## Conversion to Images

```bash
# PNG
java -jar plantuml.jar er_diagram.puml

# SVG (recommended)
java -jar plantuml.jar -tsvg er_diagram.puml
```

See [plantuml_reference.md](plantuml_reference.md) for comprehensive CLI documentation.

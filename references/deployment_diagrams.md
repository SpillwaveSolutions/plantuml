# Deployment Diagrams

Deployment diagrams show the execution architecture—how software artifacts are deployed onto nodes (hardware devices or execution environments).

## Basic Structure

```puml
@startuml
node "Web Server" as web {
  artifact "app.war"
}

node "Database Server" as db {
  database "PostgreSQL"
}

web --> db : JDBC
@enduml
```

## Cloud Infrastructure

```puml
@startuml
cloud "AWS" {
  node "EC2 Instance" {
    component "Application"
  }

  database "RDS" {
    storage "PostgreSQL"
  }

  node "S3" {
    folder "Media Files"
  }
}

actor User
User --> "EC2 Instance" : HTTPS
"EC2 Instance" --> RDS : Query
"EC2 Instance" --> S3 : Store/Retrieve
@enduml
```

See [toc.md](toc.md) for all diagram types.

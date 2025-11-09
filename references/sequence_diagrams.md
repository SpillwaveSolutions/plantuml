# Sequence Diagrams

Sequence diagrams illustrate how participants interact over time, showing the flow of messages and temporal ordering of events. They excel at documenting interaction protocols, communication flows, and complex multi-actor processes.

## Basic Syntax

The simplest sequence diagram declares participants and defines messages between them. Participants can be implicit (created on first mention) or explicit (declared with the `participant` keyword for more control):

```puml
@startuml
participant User
participant "Web Server" as WS
database "Database" as DB

User -> WS : Send Request
WS -> DB : Query Data
DB --> WS : Return Results
WS --> User : Send Response
@enduml
```

## Participant Types

PlantUML supports specialized participant types beyond standard boxes:

- `participant` - Standard rectangular box
- `actor` - Stick figure for human actors
- `boundary` - System boundary representation
- `control` - Control/logic component
- `entity` - Data entities
- `database` - Database systems
- `collections` - Collection of items
- `queue` - Message queues

**Example:**

```puml
@startuml
actor User
boundary "Web Interface" as Web
control "Auth Controller" as Auth
entity "Session" as Session
database "User DB" as DB

User -> Web : Login
Web -> Auth : Authenticate
Auth -> DB : Verify Credentials
DB --> Auth : User Data
Auth -> Session : Create Session
Session --> Web : Session Token
Web --> User : Login Success
@enduml
```

## Participant Customization

### Renaming with Aliases

```puml
@startuml
participant "Very Long Participant Name" as VLP
participant "Another Long Name" as ALN

VLP -> ALN : Message
@enduml
```

### Controlling Order

```puml
@startuml
participant Last order 30
participant First order 10
participant Middle order 20

First -> Middle : Message 1
Middle -> Last : Message 2
@enduml
```

### Multiline Participant Names

```puml
@startuml
participant MyParticipant [
=Title
----
**Subtitle**
....
Additional Info
]

MyParticipant -> Other : Message
@enduml
```

### Colored Participants

```puml
@startuml
actor Bob #lightblue
participant Alice #FF9999
database DB #palegreen

Bob -> Alice : Request
Alice -> DB : Query
@enduml
```

## Activation and Lifelines

Activation (lifelines) shows when a participant is active or processing:

```puml
@startuml
participant User
participant Service

User -> Service: Request
activate Service #FFBBBB

Service -> Service: Internal Processing
activate Service #DarkSalmon
Service --> User: Partial Response
deactivate Service

Service --> User: Final Response
deactivate Service
@enduml
```

### Shorthand Activation Syntax

```puml
@startuml
alice -> bob ++ : Activate bob
bob -> charlie ++ : Activate charlie
charlie --> bob -- : Deactivate charlie
bob --> alice -- : Deactivate bob
@enduml
```

### Creation and Destruction

```puml
@startuml
participant User
User -> Session ** : Create session
activate Session

Session -> Database : Store data
activate Database
Database --> Session : ACK
deactivate Database

User -> Session !! : Destroy session
@enduml
```

## Message Types and Arrows

PlantUML supports various message arrow styles:

- `->` Solid arrow (synchronous message)
- `-->` Dashed arrow (return/async message)
- `->>` Asynchronous message
- `<-` Reverse solid (for code readability)
- `<--` Reverse dashed
- `-\\` Lost message (message that doesn't reach destination)
- `/-` Found message (message from unknown source)
- `->x` Message with destruction
- `->o` Message to boundary
- `->>o` Async message to boundary

**Example:**

```puml
@startuml
Client -> Server : Synchronous Request
Client ->> Server : Asynchronous Request
Server --> Client : Response
Client <-- Server : Alternate Response (same rendering)

Client ->x Server : Destroy message
Client -\\ : Lost message
/- Client : Found message
@enduml
```

## System Boundary Messages

Messages from/to system boundaries:

```puml
@startuml
?-> Alice : Incoming from outside
[-> Alice : Message from start
[x-> Alice : Message from start with destruction
Alice ->] : Message to end
Alice ->o] : Message to end with open circle
Alice ->x] : Message to end with X
@enduml
```

## Messages to Self

Show internal processing:

```puml
@startuml
participant Service

Service -> Service : Validate Input
activate Service
Service -> Service : Process Data
Service -> Service : Log Result
deactivate Service
@enduml
```

## Grouping and Control Structures

### Alt/Else (Alternative Paths)

```puml
@startuml
Alice -> Bob : Authentication Request

alt Successful Authentication
    Bob --> Alice : Authentication Accepted
else Authentication Failure
    Bob --> Alice : Authentication Rejected
else Connection Error
    Bob --> Alice : Connection Timeout
end
@enduml
```

### Opt (Optional)

```puml
@startuml
Alice -> Bob : Request

opt Cache Available
    Bob -> Cache : Check Cache
    Cache --> Bob : Cached Data
end

Bob --> Alice : Response
@enduml
```

### Loop

```puml
@startuml
Client -> Server : Initial Request

loop Every 5 minutes
    Client -> Server : Heartbeat
    Server --> Client : ACK
end
@enduml
```

### Par (Parallel)

```puml
@startuml
Service -> Database : Start Transaction

par Process Order
    Service -> Inventory : Check Stock
else Process Payment
    Service -> PaymentGateway : Charge Card
else Send Notification
    Service -> EmailService : Send Confirmation
end

Service -> Database : Commit Transaction
@enduml
```

### Group

```puml
@startuml
group Authentication [Optional Label]
    Client -> Server : Username & Password
    Server -> Database : Verify Credentials
    Database --> Server : User Data
end

group Authorization
    Server -> Server : Check Permissions
    Server --> Client : Access Token
end
@enduml
```

## Notes and Annotations

### Basic Notes

```puml
@startuml
Alice -> Bob : Message
note left: This is a note on the left side
note right: This is a note on the right side
note over Alice: Note over Alice
note over Alice, Bob
    This note spans across
    both Alice and Bob
end note
@enduml
```

### Note Styles

```puml
@startuml
Alice -> Bob : Message
note left #lightblue: Colored note

hnote over Alice : Hexagonal note
rnote over Bob : Rectangle note
@enduml
```

### Notes on Messages

```puml
@startuml
Alice -> Bob : Message
note on link
    This note is directly
    on the message arrow
end note
@enduml
```

## Spacing and Formatting

### Manual Spacing

```puml
@startuml
Alice -> Bob : Message 1

|||

Alice -> Bob : Message 2 (with automatic spacing)

||50||

Alice -> Bob : Message 3 (with 50 pixels spacing)
@enduml
```

### Dividers

```puml
@startuml
== Initialization ==
Alice -> Bob : Connect

== Authentication ==
Alice -> Bob : Login
Bob --> Alice : Token

== Data Transfer ==
Alice -> Bob : Request Data
Bob --> Alice : Send Data

== Cleanup ==
Alice -> Bob : Disconnect
@enduml
```

### Delay Marker

```puml
@startuml
Alice -> Bob : Request
...5 minutes later...
Bob --> Alice : Response

...
Alice -> Bob : Another Request
@enduml
```

## Advanced Features

### Reference to Other Diagrams

```puml
@startuml
participant Alice
participant Bob

ref over Alice, Bob : Complex Authentication Process\n(see auth_detail.puml)

Alice -> Bob : Continue with main flow
@enduml
```

### Numbered Messages

```puml
@startuml
autonumber
Alice -> Bob : First message
Bob --> Alice : Response
Alice -> Bob : Second message
Bob --> Alice : Response
@enduml
```

**Customized Numbering:**

```puml
@startuml
autonumber 10 10 "<b>[000]"
Alice -> Bob : Message 10
Bob --> Alice : Response 20
autonumber stop
Alice -> Bob : No number
autonumber resume
Alice -> Bob : Message 30
@enduml
```

### Message Delays

```puml
@startuml
Alice -> Bob : Request
... 5 minutes later ...
Bob --> Alice : Response
@enduml
```

## Real-World Example: Authentication Flow

```puml
@startuml
actor User
participant "Web App" as Web
participant "Auth Service" as Auth
database "User DB" as DB
participant "Email Service" as Email

User -> Web : Enter credentials
activate Web

Web -> Auth : Authenticate(username, password)
activate Auth

Auth -> DB : Query user by username
activate DB
DB --> Auth : User record
deactivate DB

alt Password Valid
    Auth -> Auth : Generate JWT token
    Auth -> DB : Update last_login
    activate DB
    DB --> Auth : Success
    deactivate DB

    Auth --> Web : JWT token
    deactivate Auth

    Web --> User : Redirect to dashboard
    deactivate Web

    par Send notification
        Auth -> Email : Send login notification
        activate Email
        Email --> Auth : Email sent
        deactivate Email
    end

else Password Invalid
    Auth --> Web : Authentication failed
    deactivate Auth

    Web --> User : Show error message
    deactivate Web

    alt Too many failures
        Web -> Auth : Lock account
        activate Auth
        Auth -> DB : Set account_locked = true
        activate DB
        DB --> Auth : Success
        deactivate DB
        Auth -> Email : Send security alert
        activate Email
        Email --> Auth : Email sent
        deactivate Email
        deactivate Auth
    end
end
@enduml
```

## Tips and Best Practices

1. **Use meaningful aliases** - `as` keyword for long names
2. **Order participants logically** - Left to right, user to system
3. **Group related interactions** - Use `group`, `alt`, `loop`
4. **Add notes for clarity** - Explain complex business logic
5. **Use dividers** - Separate major phases with `==`
6. **Activate/deactivate consistently** - Show processing time accurately
7. **Choose appropriate arrow types** - Solid for synchronous, dashed for returns
8. **Autonumber for complex flows** - Easier to reference in discussions

## Common Use Cases

- **API interactions** - RESTful, gRPC, SOAP protocols
- **Authentication flows** - OAuth, SAML, JWT
- **Transaction processing** - Payment, order processing
- **Microservice communication** - Service-to-service calls
- **Database transactions** - Query sequences, ACID operations
- **Error handling** - Retry logic, fallback mechanisms

## Conversion to Images

```bash
# PNG
java -jar plantuml.jar sequence.puml

# SVG (recommended for documentation)
java -jar plantuml.jar -tsvg sequence.puml
```

See [plantuml_reference.md](plantuml_reference.md) for comprehensive CLI documentation.

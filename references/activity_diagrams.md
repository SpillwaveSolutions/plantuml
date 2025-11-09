# Activity Diagrams

Activity diagrams model workflows, business processes, and algorithms, showing sequential and parallel activities, decision points, and control flow.

## Basic Structure

```puml
@startuml
start
:Initialize System;
:Load Configuration;
:Connect to Database;
stop
@enduml
```

## Decision Points

```puml
@startuml
start
:Receive Request;

if (User Logged In?) then (yes)
  :Load Dashboard;
else (no)
  :Show Login Form;
  :Validate Credentials;
  if (Valid?) then (yes)
    :Create Session;
  else (no)
    :Show Error;
    stop
  endif
endif

:Process Request;
stop
@enduml
```

## Loops

```puml
@startuml
start
:Get Items;

repeat
  :Process Item;
  :Log Result;
repeat while (More Items?) is (yes) not (no)

while (Queue Not Empty?) is (yes)
  :Dequeue Item;
  :Handle Item;
endwhile (no)

stop
@enduml
```

## Parallel Processing (Fork/Join)

```puml
@startuml
start
:Receive Order;

fork
  :Send Confirmation Email;
fork again
  :Update Inventory;
fork again
  :Notify Warehouse;
fork again
  :Log Transaction;
end fork

:Order Complete;
stop
@enduml
```

## Swim Lanes

```puml
@startuml
|Customer|
start
:Place Order;

|System|
:Validate Order;
:Process Payment;

|Warehouse|
:Pick Items;
:Pack Order;

|Shipping|
:Ship Package;

|Customer|
:Receive Order;
stop
@enduml
```

## Notes and Documentation

```puml
@startuml
start
:Validate Input;
note right
  Checks for:
  - Required fields
  - Data types
  - Business rules
end note

:Process Data;
stop
@enduml
```

## Conversion

```bash
java -jar plantuml.jar -tsvg activity.puml
```

See [toc.md](toc.md) for all diagram types.

# State Diagrams

State diagrams show how objects transition between states in response to events, useful for modeling stateful systems and protocols.

## Basic Structure

```puml
@startuml
[*] --> Idle

Idle --> Processing : start()
Processing --> Complete : success()
Processing --> Error : error()
Error --> Processing : retry()
Error --> Cancelled : cancel()
Complete --> [*]
Cancelled --> [*]
@enduml
```

## State Actions

```puml
@startuml
[*] --> Active

state Active {
  Active : entry / initialize
  Active : do / process data
  Active : exit / cleanup
}

Active --> Stopped : stop()
Stopped --> [*]
@enduml
```

## Composite States

```puml
@startuml
[*] --> Active

state Active {
  [*] --> Running
  Running --> Paused : pause()
  Paused --> Running : resume()
  Running --> [*]
}

Active --> Stopped : stop()
Stopped --> [*]
@enduml
```

## Concurrent States

```puml
@startuml
[*] --> Active

state Active {
  --
  [*] --> AudioPlaying
  AudioPlaying --> AudioPaused
  --
  [*] --> VideoPlaying
  VideoPlaying --> VideoPaused
}

Active --> [*]
@enduml
```

## Choice Points

```puml
@startuml
[*] --> Checking

state choice <<choice>>
Checking --> choice
choice --> Success : [valid]
choice --> Failure : [invalid]

Success --> [*]
Failure --> [*]
@enduml
```

## Conversion

```bash
java -jar plantuml.jar -tsvg state.puml
```

See [toc.md](toc.md) for all diagram types.

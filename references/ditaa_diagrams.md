# Ditaa Diagrams (ASCII Art)

Ditaa converts ASCII art to diagrams.

## Basic Structure

```puml
@startditaa
+--------+   +-------+
|        +---+ ditaa |
|  Text  |   |diagram|
|Document|   |       |
+--------+   +-------+
@endditaa
```

## With Colors

```puml
@startditaa
/----------\  +-------------+
|cRED      |  |cBLU         |
| Red Box  |  | Blue Box    |
\----------/  +-------------+
@endditaa
```

## Special Tags
- `{d}` Document
- `{s}` Storage
- `{io}` Input/Output
- `{c}` Choice

See [toc.md](toc.md) for all diagram types.

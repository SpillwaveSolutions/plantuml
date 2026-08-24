# WikiTicket SDD, GitHub wiki, and Confluence

GitHub wiki does not render PlantUML source. Confluence does not either.
This skill is not the default for WikiTicket architecture docs.

## When to use this skill

Mermaid (`design-doc-mermaid`) owns class, ER, state, sequence, flowchart,
and C4 on GitHub wiki.

Use PlantUML when Mermaid cannot do the job easily:

- Salt wireframes / UI mocks
- UML use case
- timing
- ArchiMate
- nwdiag networks
- WBS
- JSON or YAML trees

## Rule

Keep PlantUML as a `.puml` file plus a rendered PNG or SVG. Link the image
from the Markdown. Upload the image with the wiki or Confluence page.
Never leave a raw PlantUML fence as the only view.

## Companion skills

| Need | Skill |
|------|--------|
| Prose (STE100 default) | `document-specialist` |
| Class, ER, state, sequence, C4, flowchart on GitHub | `design-doc-mermaid` |
| Wireframe and leftover UML plus image export | this skill |

## Layout

```
docs/designs/current_design_doc.md
docs/diagrams/<doc>_<num>_<type>_<title>.puml
docs/diagrams/<doc>_<num>_<type>_<title>.png
```

```markdown
![Login wireframe](../diagrams/current_design_doc_01_wireframe_login.png)
```

## Publish

| Target | Action |
|--------|--------|
| GitHub wiki | Copy the PNG or SVG into the wiki checkout and keep the Markdown image link. |
| Confluence | Upload the PNG or SVG as an attachment. Replace source fences with the image. |

# WikiTicket SDD and GitHub wiki

GitHub Flavored Markdown and GitHub wiki do not render PlantUML source.
WikiTicket design docs and code walkthroughs live under `docs/designs/` and
publish to the wiki.

## Companion skills

| Need | Skill |
|------|--------|
| Prose (STE100 default) | `document-specialist` |
| C4, flowchart, sequence on GitHub | `design-doc-mermaid` |
| Class, ER, state, component, image export | this skill |

## Rule

Keep PlantUML as a `.puml` file plus a rendered PNG or SVG. Link the image
from the Markdown. Put live GitHub diagrams in Mermaid via `design-doc-mermaid`.

Layout:

```
docs/designs/current_design_doc.md
docs/diagrams/<doc>_<num>_<type>_<title>.puml
docs/diagrams/<doc>_<num>_<type>_<title>.png
```

Markdown image link:

```markdown
![Order state machine](../diagrams/current_design_doc_01_state_order.png)
```

Do not leave a raw PlantUML fence as the only view on a GitHub wiki page.

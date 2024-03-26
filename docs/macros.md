---
hide:
  - navigation
  - toc
---

# Enabling mkdocs-ansible macros

In order to activate the macros inside your documentation project you need to
add:

```yaml
# mkdocs.yml
plugins:
  - macros:
      modules: [mkdocs-ansible:mkdocs_ansible]
```

# Using install_from_adt macro

Inside markdown documentation include a section like below, the expanded
result can be seen after the example.

```markdown
{% raw %}
{{ install_from_adt("ansible-navigator") }}
{% endraw %}
```

{{ install_from_adt("ansible-navigator") }}

# Markdown CMS

#### Esta es una prueba de concepto de [Reflex](https://reflex.dev/)

El objetivo es crear un CMS, con una simple e intuitiva interfaz que le permita al usuario mantener un sitio de contenido sin escribir una sola linea de código.

---

## Referencia de la API:

- Estructura del archivo `_content.json`:

```json
{
  "app_bar_img": {
    "svg_name": "the_svg_name",
    "colors": [
      {
        "custom_color_id": ["light_mode_color", "dark_mode_color"]
      }
      // more colors ...
    ]
  },
  "default_lang": "initial_language",
  "pages": [
    {
      "page_title": "Home",
      "page_route": "home",
      "md_file_en": "home_en.md",
      "md_file_es": "home_es.md"
    }
    //  more pages ...
    // "index" page_route ( `"/"` ) is reserved for initialization porposes
  ]
}
```

- La ruta "index" ( `"/"` ) está reservada para propósitos de inicialización

---

---

## Herramientas relacionadas

- python3.11.6
- [dependencias](requirements.txt)

- Extensiones de VSCode:
  - ms-python.python
  - ms-python.vscode-pylance
  - ms-python.black-formatter
  - ms-python.isort

## Para correr el proyecto:

> Mac | Linux

- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `reflex run`

> Windows

- `py -3.11 -m venv .venv`
- `.venv\Scripts\activate`
- `pip install -r requirements.txt`
- `reflex run`

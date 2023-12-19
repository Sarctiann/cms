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
      // mas colores ...
    ]
  },
  "default_lang": "initial_language",
  "pages": [
    {
      "page_title": "Home",
      "page_route": "home",
      // IMPORTANT: This requires a home_en.md and a home_es.md files
      "md_file": "home"
    }
    //  mas paginas ...
    // "index" page_route ( `"/"` ) está reservado para propósitos de inicialización
  ]
}
```

- Como se aclara arriba cada `md_file` requiere dos archivos,
  uno con terminación `_en.md` y otro con terminación `_es.md`

- La ruta "index" ( `"/"` ) está reservada para propósitos de inicialización

---

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

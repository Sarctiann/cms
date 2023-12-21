# Markdown CMS

#### Esta es una prueba de concepto de [Reflex](https://reflex.dev/)

El objetivo es crear un CMS, con una simple e intuitiva interfaz que le permita al usuario mantener un sitio de contenido sin escribir una sola linea de código.

---

## Referencia de la API:

- Estructura del archivo `_content.json`:

```json
{
  "app_bar_img": {
    "svg_name": "nombre_del_svg",
    "colors": [
      {
        "custom_color_id": ["color_modo_claro", "color_modo_oscuro"]
      }
      // mas colores ...
    ]
  },
  "default_lang": "lenguaje_inicial",
  "pages": [
    {
      "page_title": "Home",
      "page_route": "home",
      // IMPORTANT: This requires a home_en.md and a home_es.md files
      "md_file": "home"
    }
    //  mas paginas ...
    // "index" page_route ( `"/"` ) está reservado para propósitos de inicialización
  ],
  "forms": [
    "algún_archivo_formulario"
    // mas formularios ...
  ],
  "api_files": [
    "algún_archivo_api"
    // mas archivos api ...
  ]
}
```

- Como se aclara arriba cada `md_file` requiere dos archivos,
  uno con terminación `_en.md` y otro con terminación `_es.md`,
  lo mismo aplica para los archivos de formulario pero con `.json` en vez de `.md`.

- La ruta "index" ( `"/"` ) está reservada para propósitos de inicialización

---

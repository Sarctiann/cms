# Markdown CMS

#### This is a [Reflex](https://reflex.dev/)'s proof of concept

The goal is to create a CMS, with a simple and intuitive interface that allows the user to maintain a content site without having to write a single line of code.

---

## API Reference:

- `_content.json` file structure:

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
      "md_file": "home"
      // IMPORTANT: This requires a home_en.md and a home_es.md files
    }
    //  more pages ...
    // "index" page_route ( `"/"` ) is reserved for initialization porposes
  ],
  "forms": [
    "some_form_file"
    // more forms files...
  ],
  "api_files": [
    "some_api_file"
    // more api files...
  ]
}
```

- As stated above each `md_file` requires two files,
  one with `_en.md` ending and another with `_es.md` ending,
  the same applies to form files but with `.json` instead of `.md`.

- "index" route ( `"/"` ) is reserved for initialization purposes

---

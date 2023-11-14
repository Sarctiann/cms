# python-reflex CMS

#### This is a Reflex's proof of concept

The goal is to create a CMS, with a simple and intuitive interface, that allows the Devlights team to maintain the landing website without having to write a single line of code.

## TODO | In Progress:

- create home page md and replace index page
- create components to render with markdown
- unharcode logo in layout and SectionState (needs a lot of work... I must change the logic)

---

---

## API Reference:

- `_content.json` file structure:

```jsonc
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
  "sections": [
    {
      "tab_label": "Home",
      "page_route": "home",
      "markdown_file_en": "home_en.md",
      "markdown_file_es": "home_es.md"
    }
    //  more pages ...
    // "index" page_route ( `"/"` ) is reserved for initialization porposes
  ]
}
```

- "index" route ( `"/"` ) is reserved for initialization porposes

---

---

## Related Tools

- VSCode Extensions:
  - Python
  - Pylance
  - Black Formatter
  - isort

## To run this:

> Mac | Linux

- `python3 -m venv venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `reflex run`

> Windows

- `py -3.11 -m venv venv`
- `.venv\Scripts\activate`
- `pip install -r requirements.txt`
- `reflex run`

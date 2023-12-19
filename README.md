# Markdown CMS

#### This is a [Reflex](https://reflex.dev/)'s proof of concept

The goal is to create a CMS, with a simple and intuitive interface that allows the user to maintain a content site without having to write a single line of code.

## TODO | In Progress:

- implement Forms:

  - FormState
  - Forms representation with rx components
  - Forms tags replacement in the .md files
  - Resolve .json structure

- implement API files:

  - ApiState
  - load handlers dynamically from the api_files

- update the API Reference in the home en/es pages:

  - Add `content` folder structure

---

---

### The initial project contains an API reference to help you get started.

## Related Tools

- python3.11.6
- [dependencies](requirements.txt)

- VSCode Extensions:
  - ms-python.python
  - ms-python.vscode-pylance
  - ms-python.black-formatter
  - ms-python.isort

## To run this:

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

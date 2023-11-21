import reflex as rx

from ..components import component_map
from .use_layout import use_layout

__all__ = ["home"]


@use_layout()
def home() -> rx.Component:
    return rx.fragment(
        rx.markdown(
            """

            ##### TODO: Add support for the missing extended markdown elements

            ---

            Heading	
            
                # H1
                ## H2
                ### H3
                #### H4
                ##### H5
                ###### H6
            # H1
            ## H2
            ### H3
            #### H4
            ##### H5
            ###### H6

            ---

            Bold
            
                **bold text**
            **bold text**
            
            ---

            Italic	
            
                *italicized text*
            *italicized text*
            
            ---

            Blockquote	
            
                > blockquote
            > blockquote

            ---

            Ordered List	
            
                1. First item
                2. Second item
                3. Third item
            1. First item
            2. Second item
            3. Third item

            ---

            Unordered List
            
                - First item
                - Second item
                - Third item
            - First item
            - Second item
            - Third item

            ---

            Code

                `code`
            `code`

            ---

            Horizontal Rule
            
                ---

            ---
            
            ---

            Link	
                
                [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
            [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

            ---
            
            Image	
            
                ![Atlantic Workshop](/roundAW.png)
            ![Atlantic Workshop](/roundAW.png)

            ---

            Table	
            
                | Syntax | Description |
                | :-: | :-: |
                | Header | Title |
                | Paragraph | Text |
            | Syntax | Description |
            | :-: | :-: |
            | Header | Title |
            | Paragraph | Text |

            ---

            Fenced Code Block
            
                ```json
                {
                "firstName": "John",
                "lastName": "Smith",
                "age": 25
                }
                ```
            ```json
            {
            "firstName": "John",
            "lastName": "Smith",
            "age": 25
            }
            ```

            ---

            Footnote

                Here's a sentence with a footnote. [^1]
                [^1]: This is the footnote.
            Here's a sentence with a footnote. [^1]
            [^1]: This is the footnote.

            ---
            
            Strikethrough	
            
                ~The world is flat.~
            ~The world is flat.~

            ---
            
            Task List	
            
                - [x] Write the press release
                - [ ] Update the website
                - [ ] Contact the media
            - [x] Write the press release
            - [ ] Update the website
            - [ ] Contact the media

            ---

            """,
            component_map=component_map,
        ),
    )

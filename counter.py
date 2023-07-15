import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"                 # dastur oynasini nomi
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        # '-' knopka bosganda 1 taga kamayishi
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        # '-' knopka bosganda 1 taga kopayishi
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

#ft.app(target=main)                             # dastur bolib ishga tushadi
ft.app(target=main, view=ft.WEB_BROWSER)        # brauzerda ishga tushiradi




import flet as ft

def main(page: ft.Page):
    page.title = "Flet Two Counters Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # カウンター1の部品とロジック
    txt_number1 = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click1(e):
        txt_number1.value = str(int(txt_number1.value) - 1)
        page.update()

    def plus_click1(e):
        txt_number1.value = str(int(txt_number1.value) + 1)
        page.update()

    # カウンター2の部品とロジック
    txt_number2 = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click2(e):
        txt_number2.value = str(int(txt_number2.value) - 1)
        page.update()

    def plus_click2(e):
        txt_number2.value = str(int(txt_number2.value) + 1)
        page.update()

    # カウンター1とカウンター2のUIを追加
    page.add(
        ft.Column(
            [
                ft.Text("カウンター1"),
                ft.Row(
                    [
                        ft.IconButton(ft.Icons.REMOVE, on_click=minus_click1),
                        txt_number1,
                        ft.IconButton(ft.Icons.ADD, on_click=plus_click1),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text("カウンター2"),
                ft.Row(
                    [
                        ft.IconButton(ft.Icons.REMOVE, on_click=minus_click2),
                        txt_number2,
                        ft.IconButton(ft.Icons.ADD, on_click=plus_click2),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)






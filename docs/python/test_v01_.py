






import flet as ft

def main(page: ft.Page):
    page.title = "Flet Two Counters Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # カウンター1の部品とロジック
    txt_number1 = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    
    # カウンター2の部品とロジック
    txt_number2 = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    
    # 合計を表示するためのテキスト
    total_display = ft.Text(value="合計: 0", size=20, color="blue")
    
    # 合計を更新する関数
    def update_total():
        total = int(txt_number1.value) + int(txt_number2.value)
        total_display.value = f"合計: {total}"
        page.update()

    # カウンター1の操作関数
    def minus_click1(e):
        txt_number1.value = str(int(txt_number1.value) - 1)
        update_total()

    def plus_click1(e):
        txt_number1.value = str(int(txt_number1.value) + 1)
        update_total()

    # カウンター2の操作関数
    def minus_click2(e):
        txt_number2.value = str(int(txt_number2.value) - 1)
        update_total()

    def plus_click2(e):
        txt_number2.value = str(int(txt_number2.value) + 1)
        update_total()

    # UIを構築
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
                ft.Text(""),  # 空行
                total_display,  # 合計表示
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)


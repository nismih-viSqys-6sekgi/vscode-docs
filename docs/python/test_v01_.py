import flet as ft  # Fletライブラリをインポート

# カウンター作成関数
def create_counter(name, page):
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    # 減算ボタンクリックイベント
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        update_total()  # 合計を更新
        page.update()

    # 加算ボタンクリックイベント
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        update_total()  # 合計を更新
        page.update()

    return ft.Column(
        [
            ft.Text(name),  # カウンター名
            ft.Row(
                [
                    ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(ft.Icons.ADD, on_click=plus_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    ), txt_number

# ページのメイン処理
def main(page: ft.Page):
    page.title = "Flet Multi-Counters Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    total_display = ft.Text(value="合計: 0", size=20, color="blue")  # 合計を表示する部品

    counters = []  # 複数のカウンターの参照を保持

    # 合計を更新する関数
    def update_total():
        total = sum(int(counter.value) for _, counter in counters)
        total_display.value = f"合計: {total}"
        page.update()

    # カウンター1とカウンター2を作成
    counter1, txt_number1 = create_counter("カウンター1", page)
    counter2, txt_number2 = create_counter("カウンター2", page)
    counters.append((counter1, txt_number1))
    counters.append((counter2, txt_number2))

    # UIを構築
    page.add(
        ft.Column(
            [
                counter1,  # カウンター1を追加
                counter2,  # カウンター2を追加
                ft.Text(""),
                total_display,  # 合計表示を追加
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)
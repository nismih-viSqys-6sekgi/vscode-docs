import flet as ft

def main(page: ft.Page):
    # アプリケーションのタイトル設定
    page.title = "はじめてのFletアプリ"
    
    # UIコンポーネントの追加
    page.add(
        ft.Text("こんにちは、Flet!",
                size=30,
                color="blue",
                weight="bold")
    )

# アプリケーションの実行
ft.app(target=main)

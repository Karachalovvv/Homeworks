import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое приложение на Flet"
    page.theme_mode = ft.ThemeMode.DARK

    greeting_text = ft.Text("Привет, мир")

    greeting_history = []
    history_text = ft.Text("История приветствий")


    def on_button_click(e):
        name = name_input.value.strip()

        if name:

            if 6 <= datetime.now().hour < 12:
                greeting_text.value = f"Доброе утро, {name}!"
                
            elif 12 <= datetime.now().hour < 18:
                greeting_text.value = f"Добрый день, {name}!"

            elif 18 <= datetime.now().hour < 24:
                greeting_text.value = f"Добрый вечер, {name}!"

            elif 0 <= datetime.now().hour < 6:
                greeting_text.value = f"Доброй ночи, {name}!"
            
            name_input.value = ""
            greeting_button.text = "Поздороваться еще раз"

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{timestamp} - {name}")
            
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйста, введите ваше имя"

        page.update()

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    def copy_greeting(e):
        page.set_clipboard(greeting_text.value)
        page.update()

    name_input = ft.TextField(label='Введите ваше имя', autofocus=True, on_submit = on_button_click)

    clear_button = ft.ElevatedButton("Очистить историю", icon = ft.Icons.DELETE, on_click = clear_history)

    theme_button = ft.IconButton(icon = ft.Icons.BRIGHTNESS_6, tooltip = "Сменить тему", on_click = toggle_theme)

    greeting_button = ft.ElevatedButton("Поздороваться", icon = ft.Icons.HANDSHAKE, on_click=on_button_click)

    copy_button = ft.IconButton(icon = ft.Icons.COPY, tooltip = "Скопировать приветствие", on_click = copy_greeting)

    
    page.add(ft.Row([greeting_text, copy_button], alignment = ft.MainAxisAlignment.CENTER),
             ft.Row([name_input, greeting_button, theme_button, clear_button], alignment = ft.MainAxisAlignment.CENTER),
             history_text)


ft.app(main)
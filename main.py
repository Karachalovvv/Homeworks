import flet as ft
from datetime import datetime
import random

def main(page: ft.Page):
    page.title = "Мое первое приложение на Flet"
    page.theme_mode = ft.ThemeMode.DARK

    greeting_text = ft.Text("Привет, мир")

    greeting_history = []
    # history_text = ft.Text("История приветствий")

    def update_history_view():
        history_controls = [ft.Text("История приветствий:", size='bodyMedium')]
        for ind, name in enumerate(greeting_history):
            history_controls.append(
                ft.Row([
                    ft.Text(name),
                    ft.IconButton(icon=ft.Icons.CLOSE, tooltip='Удалить',
                                  on_click=lambda e, i=ind: remove_name_from_history(i))
                ])
            )
        history_column.controls = history_controls
        page.update()

    def remove_name_from_history(index):
        if 0 <= index < len(greeting_history):
            del greeting_history[index]
            update_history_view()

    def random_name(e):
        names = ["Алексей", "Мария", "Иван", "Ольга"]
        name_input.value = random.choice(names)
        page.update()

    def on_button_click(e):
        name = name_input.value.strip()

        if name:

            # greeting_text.value = f"Привет, {name}!"
            name_input.value = ""

            if 6 <= datetime.now().hour < 12:
                greeting_text.color = ft.Colors.YELLOW
                greeting_text.value = f"Доброе утро, {name}!"
                
            elif 12 <= datetime.now().hour < 18:
                greeting_text.color = ft.Colors.ORANGE
                greeting_text.value = f"Добрый день, {name}!"

            elif 18 <= datetime.now().hour < 24:
                greeting_text.color = ft.Colors.RED
                greeting_text.value = f"Добрый вечер, {name}!"

            elif 0 <= datetime.now().hour < 6:
                greeting_text.color = ft.Colors.BLUE
                greeting_text.value = f"Доброй ночи, {name}!"
            
            greeting_button.text = "Поздороваться еще раз"

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # greeting_history.append(f"{timestamp} - {name}")
            
            # history_text.value = "История приветствий:\n" + "\n".join(greeting_history)

            greeting_history.append(name)
            update_history_view()
        else:
            greeting_text.value = "Пожалуйста, введите ваше имя"

        page.update()

    name_input = ft.TextField(label="Введите ваше имя", autofocus=True, on_submit=on_button_click)

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    def clear_history(_):
        greeting_history.clear()
        # history_text.value = "История приветствий:"
        update_history_view()
        page.update()

    def copy_greeting(e):
        page.set_clipboard(greeting_text.value)
        page.update()

    name_input = ft.TextField(label='Введите ваше имя', autofocus=True, on_submit = on_button_click)

    clear_button = ft.ElevatedButton("Очистить историю", icon = ft.Icons.DELETE, on_click = clear_history)

    theme_button = ft.IconButton(icon = ft.Icons.BRIGHTNESS_6, tooltip = "Сменить тему", on_click = toggle_theme)

    greeting_button = ft.ElevatedButton("Поздороваться", icon = ft.Icons.HANDSHAKE, on_click=on_button_click)

    copy_button = ft.IconButton(icon = ft.Icons.COPY, tooltip = "Скопировать приветствие", on_click = copy_greeting)

    random_name_button = ft.IconButton(icon = ft.Icons.CHANGE_CIRCLE, tooltip = "Случайное имя", on_click = random_name)

    history_column = ft.Column([])
    update_history_view()

    
    page.add(ft.Row([greeting_text, copy_button], alignment = ft.MainAxisAlignment.CENTER),
             ft.Row([name_input, greeting_button, theme_button, clear_button, random_name_button], alignment = ft.MainAxisAlignment.CENTER),
             history_column)


ft.app(main)
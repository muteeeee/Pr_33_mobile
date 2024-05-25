import kivy

kivy.require('1.0.7')
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):

    def animate(self, instance):
        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(200, 100), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))
        animation.start(instance)

    def animate_other_button(self, instance):
        button = instance.parent.children[0]  # Находим первую кнопку в родительском виджете
        self.animate(button)  # Запускаем анимацию для первой кнопки

    def build(self):
        layout = BoxLayout(orientation='vertical')

        button1 = Button(size_hint=(None, None), text='Нажми', on_press=self.animate_other_button)
        layout.add_widget(button1)

        button2 = Button(size_hint=(None, None))
        layout.add_widget(button2)

        return layout


if __name__ == '__main__':
    TestApp().run()
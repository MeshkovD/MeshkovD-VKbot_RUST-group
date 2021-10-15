import vk_api
import time

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from my_bot_token import token

vk_session = vk_api.VkApi(token=token)
vk_session._auth_token()
keyboard = VkKeyboard(one_time=False)
vk = vk_session.get_api()

keyboard.add_button('Когда вайп?', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Промо', color=VkKeyboardColor.POSITIVE)

keyboard.add_line()  # Переход на новую строку
keyboard.add_openlink_button("Наш магазин", "https://galakrond.playrust.ru/products")

keyboard.add_line()  # Переход на новую строку
keyboard.add_button('Хочу стать модератором', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Пиратка?', color=VkKeyboardColor.PRIMARY)

keyboard.add_line()  # Переход на новую строку
keyboard.add_button('Бан\Разбан', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Команды', color=VkKeyboardColor.NEGATIVE)

connection_counter = 0

questions = {
    'Когда вайп?': 'Вайп каждые 5 дней, дату последнего вайпа можно найти на стене сообщества или в нашем '
                   'дискорд канале https://discord.gg/K2kWjvWKnB.',
    'Промо': 'Промокод для новичков "new". Так же вы можете получить вознаграждения за проведенное время на сервере , '
             'используйте команду /case в игре . Важно! Сначала авторизируйтесь в магазине  '
             'https://galakrond.playrust.ru/ перед тем как забрать вознаграждение.',

    'Бан\Разбан': 'Все зявки на разбан рассматриваются в этом топике https://vk.com/topic-185597153_40565047. '
                  'Перед тем как написать заявку, рекомендуем сначала ознакомиться с правилами сервера '
                  'https://vk.com/topic-185597153_40516485.',
    'Команды': 'С доступными командами чата можно ознакомиться тут https://vk.com/@galakrondproject-komandy',
    'Хочу стать модератором': 'https://vk.com/galakrondproject?w=app5708398_-185597153',
    'Пиратка?': 'Нет, наш сервер для владельцев лицензии.',
    'начать': 'Ок, начинаем!',
    'начало': 'Ок, начинаем!',
    'начинаем': 'Ок, начинаем!',
    'start': 'Ок, начинаем!',
    'старт': 'Ок, начинаем!',
}

try:
    def send_reply(event):
        if questions.get(event.text):
            vk.messages.send(  # Отправляем сообщение
                user_id=event.user_id,
                message=questions.get(event.text),
                keyboard=keyboard.get_keyboard(),
                random_id=0
            )


    def main():

        try:
            longpoll = VkLongPoll(vk_session)

            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:  # Слушаем longpoll, если пришло сообщение отвечаем
                    send_reply(event)

        except Exception as ex:
            print(ex)
        finally:
            time.sleep(5)

except Exception as ex:
    print(ex)

if __name__ == '__main__':
    while True:
        main()

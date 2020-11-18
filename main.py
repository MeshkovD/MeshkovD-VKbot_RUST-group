print('*' * 40)
print("Server started")
print('*' * 40)


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

try:
    def main():
        global connection_counter
        connection_counter = connection_counter +1
        print(time.strftime("%H:%M:%S"), '* Попытка подключения №{num}' .format(num = connection_counter))
        try:
            longpoll = VkLongPoll(vk_session)
            print(time.strftime("%H:%M:%S"), "* Успешное подключение")
            print(time.strftime("%H:%M:%S"), "* Бот запущен")
            print('*' * 40)
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                #Слушаем longpoll, если пришло сообщение то:
                    if event.text == 'Когда вайп?': #Если написали заданную фразу
                        if event.from_user: #Если написали в ЛС
                            vk.messages.send( #Отправляем сообщение
                                user_id=event.user_id,
                                message='Вайп каждую пятницу в 10:00 по МСК.',
                                keyboard=keyboard.get_keyboard(),
                                random_id=0
                            )
                    elif event.text == 'Промо': #Если написали заданную фразу
                        vk.messages.send( #Отправляем сообщение
                                user_id=event.user_id,
                                message='Промокод для новичков "new". Так же вы можете получить вознаграждения за проведенное время на сервере , используйте команду /case в игре . Важно! Сначала авторизируйтесь в магазине  https://galakrond.playrust.ru/ перед тем как забрать вознаграждение.',
                                keyboard=keyboard.get_keyboard(),
                                random_id=0
                            )
                    elif event.text == 'Бан\Разбан':
                        vk.messages.send( #Отправляем сообщение
                                user_id=event.user_id,
                                message='Все зявки на разбан рассматриваются в этом топике https://vk.com/topic-185597153_40565047. Перед тем как написать заявку, рекомендуем сначала ознакомиться с правилами сервера https://vk.com/topic-185597153_40516485.',
                                keyboard=keyboard.get_keyboard(),
                                random_id=0
                        )
                    elif event.text == 'Команды':
                        vk.messages.send( #Отправляем сообщение
                                user_id=event.user_id,
                                message='С доступными командами чата можно ознакомиться тут https://vk.com/@galakrondproject-komandy',
                                keyboard=keyboard.get_keyboard(),
                                random_id=0
                        )
                    elif event.text == 'Хочу стать модератором':
                        vk.messages.send( #Отправляем сообщение
                                user_id=event.user_id,
                                message='https://vk.com/@galakrondproject-nabor-moderacii',
                                keyboard=keyboard.get_keyboard(),
                                random_id=0
                        )
                    elif event.text == 'Пиратка?':
                        vk.messages.send(
                                message='Нет, наш сервер для владельцев лицензии.',
                                user_id=event.user_id,
                                keyboard=keyboard.get_keyboard(),
                                random_id=0
                        )
                    elif 'начать' in (event.text).lower() \
                                or 'начало' in (event.text).lower() \
                                or 'начинаем' in (event.text).lower()\
                                or 'start' in (event.text).lower():
                        vk.messages.send(  # Отправляем сообщение
                                user_id=event.user_id,
                                message='Ок, начинаем!',
                                keyboard=keyboard.get_keyboard(),
                                random_id=0
                        )

        except Exception as ex:
            print(time.strftime("%H:%M:%S"), "* Подключиться не удалось")
            print(time.strftime("%H:%M:%S"),"* Причина:", ex)
        finally:

            print(time.strftime("%H:%M:%S"), "* Ждём 5 секунд")
            time.sleep(5)

except Exception as ex:
    print('-' * 20)
    print(time.ctime(), ex)
    print('-' * 20)

if __name__ == '__main__':
    while True:
        main()
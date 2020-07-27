# vk-pagebot
**vk-pagebot** - бот, предназначенный для упрощенного контроля страниц(группы страниц). В его функционал входит:
* Написание сообщений от лица страницы
* Выполнение небольшого кода(eval)
* Смена префиксов команд, задержки после сообщений без перезапуска бота
* Возможность определять доступ пользователей к боту
* Возможность определять список чатов, где бот работает
* Контроль действий с аккаунта через логи
# Установка и запуск
## На Windows
1. Установите Python последней версии с [официального сайта](https://python.org)
2. Установите Git с [сайта](https://git-scm.com/download/win)
3. Создайте папку,перейдите и скопируйте в нее файлы из репозитория командами:
> cd *путь к папке*
>
> git clone https://github.com/N08I40K/vk-pagebot

***Примечание: если у вас папка на другом диске(по стандарту выбирается в консоли диск C), то перейдите в диск где папка командой:***
>*буква диска*:
>
> Например, d:
4. Перейдите в папку с ботом командой:
> cd vk-pagebot
5. Установите нужные библиотеки командой:
> pip install -r requirements.txt
6. Вручную откорректируйте параметры в файле **config.txt**

***Подробнее о них будет дальше***

7. Запустите бота командой:
> python main.py
8. Остановить бота можно комбинацией клавиш **Ctrl + C**
# Параметры
***Здесь указано разъяснение каждой строки файла конфигураций и пример оформления***
Начало строки, ее номер | Параметр, пример
------------------------|-----------------
token=, 1 строка        | Токен ВКонтакте, получается на [сайте](https://vkhost.github.io/). Например, _token=ayylmaodankmemes_
allowedids=, 2 строка   | Айди пользователей, который могут пользоваться ботом(один айди или числа через запятую. Например, _allowedids=1_ или _allowedids=1, 2, 3_ , или _allowedids=0_ если хотите открыть бота всем
allowedchats=, 3 строка | Айди чатов, где бот будет работать(одно число или числа через запятую). Аналогично параметру выше, _в_ _том_ _числе_ _и_ _касательно_ _нуля_
logid=, 4 строка        | Айди пользователя, кому будет вестись отчет о использовании бота. Числа через запятую, одно число или _ноль(работает_ _аналогично_ _параметрам_ _выше)_
index=, 5 строка        | Число, _идентификатор_ бота при применении команд, пишется после префикса команды, например "!1 Привет". Одно число.
delay=, 6 строка        | Задержка после ответа бота в секундах, одно число.
cmdprefix=, 7 строка    | Префикс для команды-повторения, например при _cmdprefix=!_ команда выглядит следующим образом: _"! Привет"_. Любой набор символов
cmdeval=, 8 строка      | Префикс для eval-команды, например при _cmdeval=/_ команда выглядит так: _"/ 1 + 1"_
isthirdpython=, 9 строка| Параметр, зависящий от того, какой командой запускается скрипт: _python_ или _python3_. Значение _0_ и _1_ соответственно вариантам команд. Влияет на перезапуск бота
safeeval=, 10 строка    | Параметр, влияющий на функционал eval. _При_ _значении_ _"0"_ _ограничивает_ _всю_ _работу_ _с_ _модулями_ _и_ _переменными_
reg_warn=, 11 строка	| Параметр, который указывает боту надо ли оповещать о инициализации пользователя в чат.

## Связь с разработчиком
[Я в вк](https://vk.com/id_498094647_you_dont_need_him)

Telegram - @n08i40k

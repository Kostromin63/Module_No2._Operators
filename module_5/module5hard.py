# Дополнительное практическое задание по модулю*
# Дополнительное практическое задание по модулю: "Классы и объекты."
#
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.
#
# Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на
# тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые
# знания программирования.
#
# Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий
# функционал на сайте.
#
# Всего будет 3 класса: UrTube, Video, User.
#
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео,
# авторизации и регистрации пользователя и т.д.
#
# Подробное ТЗ:
#
# Примечания:
# Не забывайте для удобства использовать dunder(магические) методы: __str__, __repr__, __contains__, __eq__ и др.
#
# Чтобы не запутаться рекомендуется после реализации каждого метода проверять как он работает, тестировать разные
# вариации.

from time import sleep


class User:
    """""
    Каждый объект класса User должен обладать следующими атрибутами и методами:
    Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    """""

    def __init__(self, nickname, password, age=0):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    """
    Каждый объект класса Video должен обладать следующими атрибутами и методами:
    Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда
    остановки (изначально 0)),
    adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """

    def __init__(self, title='', duration=0, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title and self.duration == other.duration


class UrTube:
    """
    Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
    Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __str__(self):
        return 'Наш UrTube!'

    def log_in(self, nickname, password):
        """
        Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с
        такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        :param nickname:
        :param password:
        :return:
        """

        for i in self.users:
            if nickname == i.nickname:
                if hash(password) == i.password:
                    self.current_user = i
                else:
                    print(f'Не верный пароль')
            else:
                print(f'Пользователь {nickname} не найден в базе')

    def register(self, nickname, password, age):
        """
        Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
        если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
        "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
        :param nickname:
        :param password:
        :param age:
        :return:
        """
        if len([user_ for user_ in self.users if user_.nickname == nickname]) == 0:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        """
        Метод log_out для сброса текущего пользователя на None.
        :return:
        """
        self.current_user = None

    def add(self, *args):
        """
        Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
        :param args:
        :return:
        """
        list_video = self.videos
        list_titl_video = [video.title for video in list_video]
        add_list = [video for video in args if not str(video) in list_titl_video]
        # проверять на пусто не будем, т.к. ошибки нет и видимо так будет быстрее.
        list_video.extend(add_list)
        self.videos = list_video

    def get_videos(self, search_word):
        """
        Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих
        поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учит/ регистр).
        :param search_word:
        :return:
        """
        all_video = []
        for i in self.videos:
            tv = i.title.lower()
            if tv.find(search_word.lower()) >= 0:
                all_video.append(i.title)
        return all_video

    def watch_video(self, title):
        """
        Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то
        ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После
        текущее время просмотра данного видео сбрасывается.
        Для метода watch_video так же учитывайте следующие особенности:
        Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить
        в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
        Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео"
        :param title:
        :return:
        """
        if self.current_user is None:
            print(f'Войдите в аккаунт, что бы смотреть видео')
        else:
            for video in self.videos:
                if str(video) == title:  # нашли видео.
                    if self.current_user.age < 18 and video.adult_mode:
                        print(f'"Вам нет 18 лет, пожалуйста покиньте страницу"')
                    else:
                        print(f'Распологайтесь в кресле поудобнее, начинаем показ фильма: "{title}"')
                        time_play = 0
                        while time_play < video.duration:
                            time_play += 1
                            print(time_play, end=' ')
                            sleep(1)
                        print('Конец видео')

#  Регистрация или вход пользователя;


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
# #

# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
#
#

# Игра Pacman на Python

#### Описание проекта

На данный момент проект является упрощенной версией игры. Тем не менее, вся основная игровая логика реализована.

#### Реализованный функционал

При запуске игры появляется поле, вот классификация объектов:

| Символ | Обозначение                                 |
| ------ | ------------------------------------------- |
| `.`    | Пустое пространство                         |
| `#`    | Стена                                       |
| `*`    | Таблетка (надо собрать все, чтобы выиграть) |
| `@`    | pacman                                      |
| `R`    | Красный призрак                             |
| `B`    | Голубой призрак                             |
| `P`    | Розовый призрак                             |
| `Y`    | Желтый призрак                              |

Вы можете передвигать pacman, используя `w`, `a`, `s`, `d` + `Enter`. Призраки двигаются сразу после Вашего хода.

Ваша цель - собрать все таблетки, не попавшись не одному призраку.

#### Запуск

Установите python3, если его нет:

```bash
sudo apt update
sudo apt -y upgrad
```

```bash
sudo apt install -y python3-pip
```

Скачайте исходный код:

```bash
git clone https://github.com/AntivistRock/Pacman-Python.git
```

Переключитесь на ветку dev:

```bash
git checkout dev
```

В скачанной директории выполните:

```bash
pyhon3 program.py
```
# Onboarding test

У цьому розділі треба створити проект із віртуальним отеченням в git-репозиторії і підключити його до гітхабу. Обов'язково використати файл `.gitignore`.

Кожне завдання - це окремий python-модуль. Обов'язково додайте обробку помилок та логування. Для виведення прикладів виконання функцій використовуйте випробування.


### Завдання 1 - Піфагорові штани

Створіть функцію, яка прийматиме масив несортованих чисел і поверне `boolean` значення залежно від того, чи можна із заданих значень скласти піфагорів трикутник з відповідними довжинами сторін.

Тести:

```commandline
[5, 3, 4] -> True
[6, 8, 10] -> True
[100, 3, 65] -> False
```

### Завдання 2 – Рослини проти Зомбі

Створіть функцію, яка прийматиме два масиви несортованих чисел (перший - масив рослин, що захищається, другий - атакуючий масив зомбі) і поверне `boolean` значення в залежність від того чи перемогли захисники.

➡️ Умови:

- Кожен елемент масиву атакує елемент іншого масиву з тим самим індексом масиву. Той, хто вижив, - це число з найбільшим значенням.
- Якщо значення однакове, вони обидва гинуть.
- Якщо одне із значень відсутнє (різна довжина масивів), солдат з непустим значенням виживає.
- Щоб вижити, сторона, що обороняється, повинна мати більше тих, хто вижив, ніж атакуюча сторона.
- У випадку, якщо з обох боків однакова кількість людей, що вижили, перемагає команда з найбільшою початковою силою атаки. Якщо загальна сила атаки з обох сторін однакова, поверніть True.
- Початкова сила атаки є сумою всіх значень у кожному масиві.

Тести:

```commandline
zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 6, 8 ] -> True
zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4 ] -> False
zombies=[ 1, 3, 5, 7 ] plants=[ 2, 4, 0, 8 ] -> True
zombies=[ 2, 1, 1, 1 ] plants=[ 1, 2, 1, 1 ] -> True
```

### Завдання 3 – Генератор розкладу

Створіть функцію, яка генерує розклад робочих днів працівника.

➡️ Умови: 

- Функція приймає кількість днів, на які потрібно скласти розклад, кількість днів роботи, кількість днів відпочинку та дату початку розкладу.
- Функція повертає розклад робочих днів співробітника, який генерується починаючи з start_date на days днів уперед, враховуючи що співробітник чергує робочі дні (work_days) та дні відпочинку (rest_days).
- Функція має повернути дані у форматі List[datetime.datetime]

Тести:

```commandline
days: 5, work_days: 2, rest_days: 1, start_date: datetime(2020, 1, 30) ->
[
datetime.datetime(2020, 1, 30, 0, 0),
datetime.datetime(2020, 1, 31, 0, 0),
  datetime.datetime(2020, 2, 2, 0, 0),
datetime.datetime(2020, 2, 3, 0, 0)
]
```
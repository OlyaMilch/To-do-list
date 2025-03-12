Это приложение To-do-list, написанное на Flask. База данных состоит на основе SQLAlchemy и создается автоматически при запуске кода, если базы данных на пк нет.


Это приложение для заметок: что я должна сделать, а что уже сделала. Проще говоря, список дел.

При запуске app.py появляется сервер, при нажатии на который вы переходите на страницу браузера.

Страницы для приложения в браузере написаны в 3-х разных html файлах, чтобы код был почище.

Как это работает? 
1. При просмотре всез задач используйте добавочный /all к локальному адресу, и он выведет все задачи (tasks), которые вы написали.
2. При добавлении /add или нажатии кнопки "Add New Task" на домашней странице вы добавляете новую задачу. Ей будет присвоен id и дефолтно иконка красного креста, означающий, что задача не выполнена. После добавления задачи можно вернуться на страницу со всеми задачами, нажав "Back to list"
3. При выполнении задачи можно использовать /complete/id, где id, это номер вашей задачи. Тогда вместо крестика напротив задачи будет галочка - задание выполнено.
4. При удалении задачи используем /delete/id, тогда задача будет удалена из общего списка /all.
5. Так же уже существующую задачу можно редактировать с помощью /edit/id, там вы ее исправляете/дополняете.

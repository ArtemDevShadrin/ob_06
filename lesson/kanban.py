# Kanban — это подход, ориентированный на поток работы и эффективность процессов. Он визуализирует рабочие задачи на
# kanban-доске, что позволяет команде увидеть статус работ и управлять потоком задач. Популярен в различных отраслях
# благодаря своей гибкости и простоте.
#
# Kanban мы также рассмотрим на примере разработки компьютерной игры.
#
#
#
# Kanban-доска создаётся перед началом работы с проектом. Сначала составляется список задач, причём желательно
# установить ограничение на количество работы, чтобы избежать перегрузки одного человека задачами. Мы ограничиваем
# количество задач, например, до трёх задач (но это число может варьироваться в зависимости от штата разработчиков и
# времени, необходимого на выполнение каждой задачи). Каждый разработчик берёт на себя задачу, присваивает её и двигает
# по графам таблицы.
#
# Kanban-доску, к слову, заимствовали и другие методологии управления проектами, в том числе и в Scrum. У этой доски
# имеются разные вариации, каждый может настраивать её под свои задачи. Доску можно нарисовать самостоятельно, можно
# использовать специальные программы, где есть таск-трекеры с различными полями.
#
# Для примера создадим таблицу с четырьмя графами: To do, In progress, Testing и Done. После этого создадим карточки
# задач. В нашем случае это будут задачи: разработать локацию для игры; создать персонажа; разработать механику ходьбы
# персонажа. Поместим эти карточки в графу To do.
#
#
# В эту графу, конечно, можно прописать сразу все задачи проекта, но обычно так не делают. Лучше прописывать задачи на
# конкретный этап. При этом нужно помнить, что Kanban менее структурен, чем Scrum, поэтому здесь есть лишь примерный
# план на каждый этап.
#
# Таким образом, в графе To do у нас находятся все задачи, которые мы будем постепенно перемещать к графе Done.
# Карточки задач можно добавлять в графу To do по мере работы над проектом. Например, разработчик начинает работать над
# созданием локации игры: при этом он переносит данную карточку в графу In progress. Закончив работу, он переносит
# карточку в графу Testing. Если тестирование прошло успешно, задача переносится в графу Done, и можно браться за
# следующую задачу. Эти доски вариативны: можно сделать больше граф, например, помимо тестирования, включить графу
# “исправление ошибок” и т.д., то есть можно включить сюда столько этапов работы, сколько проходят обычно задачи в
# конкретном проекте.
#
#
#
# Преимущества Kanban для разработки игры
#
# Сразу видна общая картина выполненных и текущих задач, не нужно организовывать встречи и созвоны — вся информация
# доступна на доске. Это позволяет легко адаптироваться к изменениям и быстро вносить правки, так как работа движется
# поэтапно. После завершения этапа информация доводится до заказчика, он представляет обратную связь, и, если требуются
# изменения, в графу To do добавляется новая задача. При этом команда сосредоточена только на тех задачах, которые
# прописаны в to do-листе, что помогает не рассеивать внимание.
#
# При использовании Kanban мы по сути играем в своего рода игру с задачами: перемещаем их по доске, двигая карточки всё
# ближе к цели. У нас есть начало пути и конечная точка, что создаёт интерактивный процесс. Многим нравится работать с
# Kanban, и, как уже упоминалось, этот подход успешно интегрирован не только в Scrum и Agile, но и во многие другие
# методологии.
#
# Плюсы методологии Kanban
#
# Гибкость. Kanban позволяет нам легко изменять приоритеты и задачи без нарушения общего процесса.
# Улучшение видимости общего рабочего процесса. Каждый член команды имеет возможность наблюдать, на каком этапе
# находится проект и разработка.
# Простота внедрения. Это одно из важных качеств Kanban, потому что, например, Scrum из-за его повышенным требованиям к
# дисциплине внедрять намного сложнее. В Kanban есть доска, есть задачи, и команда их выполняет.
# Минусы методологии Kanban
#
# Отсутствие строгих сроков. Если не управлять очерёдностью и загрузкой работ, это может привести к задержкам в
# выполнении задач. Особенно актуален этот аспект в коммерческой разработке, построенной на чётких сроках и требованиях
# своевременной сдачи проекта.
# Может потребоваться дополнительное внимание к управлению приоритетами.
# Kanban недостаточно структурирован для некоторых команд.
# Kanban удобен, когда мы работаем над собственным проектом без строгих временных рамок. Мы определяем свои собственные
# задачи, и наша команда разработчиков также отслеживает прогресс. Нам не нужно ежедневно проводить созвоны, каждый
# работает в своем темпе, но при этом приближается к общей цели. Однако в коммерческой разработке, где работы идут по
# строго заданным срокам и требуется более жёсткая структура, Kanban может стать менее подходящим выбором.
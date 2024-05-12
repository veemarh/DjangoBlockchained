from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from accounts.models import Teacher


def q_search(query):
    # if query.isdigit() and len(query) <= 5: # если у нас будет на сайте какое-то id для каждого препода
    #     return Teacher.objects.filter(id=int(query))

    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(name__icontains=token) # поиск по названию
        # q_objects |= Q(description__icontains=token) # если хотим искать по описания
    # можно добавить какой-то другой вывод, если ничего не нашел поиск
    return Teacher.objects.filter(q_objects)

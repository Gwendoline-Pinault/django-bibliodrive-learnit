# Données créées en base (mémo des requêtes)

from backoffice.models import Author, Publisher, Title
blackmoon = Publisher.objects.get(pubid=2)
meyer = Author.objects.get(au_id=5)
hesitation = Title.objects.create(title='Hésitation', year_published=2007, isbn='2013224591', pubid=blackmoon, description="Deux futurs, deux âmes soeurs... C'était trop pour une seule personne. Je compris que ce n'était pas Edward et Jacob que j'avais essayé de réconcilier, c'étaient les deux parts de moi-même, la Bella d'Edward et la Bella de Jacob. Malheureusement, elles ne pouvaient coexister et j'avais eu tort de tenter de les y contraindre. A présent, je ne doute pas de ce que je désire, ni de ce dont j'ai besoin... ni de ce que je vais faire, là, maintenant.", notes='', subject='Vampires, loups-garou, romance, fantastique', comments='')
hesitation.authors.set(meyer)
hesitation.save()

from backoffice.models import Author, Publisher, Title
flammarion = Publisher.objects.get(pubid=1)
hadrian = Author.objects.get(au_id=4)
filles = Title.objects.create(title='Les Filles du Temps 2', year_published=2021, isbn='0237947984', pubid=flammarion, description="", notes='', subject='fantasy', comments='')
filles.authors.add(hadrian)
filles.save()

from backoffice.models import Author, Publisher, Title
tome2 = Title.objects.get(title_id=5)
tome2.delete()
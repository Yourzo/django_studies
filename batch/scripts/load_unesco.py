import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Region, Category, Iso, State, Site

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)

        cate, _ = Category.objects.get_or_create(name=row[7])
        stat, _ = State.objects.get_or_create(name=row[8])
        i, _ = Iso.objects.get_or_create(name=row[10])
        reg, _ = Region.objects.get_or_create(name=row[9])

        try:
            a = float(row[6])
        except:
            a = None

        try:
            y = int(row[3])
        except:
            y = None

        try:
            just = str(row[2])
        except:
            just = None

        site = Site.objects.create(name=row[0], year=y, latitude=row[5],
                                      longitude=row[4], description=row[1],
                                      justification=just, area_hectares=a, category=cate,
                                      region=reg, iso=i, state=stat)
        site.save()

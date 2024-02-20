from django.contrib import admin


from library.models import *
admin.site.register(Author)
admin.site.register(Country)
admin.site.register(Edition)
admin.site.register(EditionsAuthors)
admin.site.register(EditionsGenres)
admin.site.register(EditionsSubjects)
admin.site.register(Faculty)
admin.site.register(Genre)
admin.site.register(Reader)
admin.site.register(ReadersEditions)
admin.site.register(Status)
admin.site.register(Subject)
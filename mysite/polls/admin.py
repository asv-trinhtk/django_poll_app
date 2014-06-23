from django.contrib import admin
from polls.models import Poll
from polls.models import Choice
# Register your models here.
#admin.site.register(Poll)
#admin.site.register(Choice)

#class PollAdmin(admin.ModelAdmin):
#    fields = ['question', 'pub_date']
#admin.site.register(Poll, PollAdmin)
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 0

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields':['question']}),
        ('Date information',    {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)



from django.contrib import admin
from .models import Programmer, Program


class ProgrammerProgramsInline(admin.TabularInline):
    model = Program.programmers.through


class ProgrammerAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'telephone']
    search_fields = ['username', 'id']
    inlines = [
        ProgrammerProgramsInline,
    ]

class ProgramAdmin(admin.ModelAdmin):
    inlines = [
        ProgrammerProgramsInline,
    ]
    exclude = ('programmers',)

# Register your models here.


admin.site.register(Programmer, ProgrammerAdmin)
admin.site.register(Program, ProgramAdmin)

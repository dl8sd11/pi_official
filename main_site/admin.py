from django.contrib import admin
from .models import Question,Project,Attachment,Group,Author

class AttachmentInline(admin.StackedInline):
    model = Attachment
    extra = 1

class GroupInline(admin.TabularInline):
    model = Group
    extra = 0

class AuthorInline(admin.StackedInline):
    model = Author
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [GroupInline,AuthorInline,AttachmentInline]

admin.site.register(Question)
admin.site.register(Group)
admin.site.register(Project,ProjectAdmin)
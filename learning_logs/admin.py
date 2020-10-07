from django.contrib import admin

# Register your models here.Зарегистрируйте здесь ваши модели.
from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)


from django.contrib import admin
from .models import Users, Fine_information, queue_info, notification, payment

# Create a list of models you want to register
models_to_register = [Users, Fine_information, queue_info, notification, payment]

# Register each model with the admin site
for model in models_to_register:
    admin.site.register(model)



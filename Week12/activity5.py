import sys
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line

# --- Django minimal settings ---
settings.configure(
    DEBUG=True,
    SECRET_KEY='dev-key',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
)

# --- View function ---
def welcome(request, name="Guest"):
    return HttpResponse(f"Welcome {name} to Django!")

# --- URL patterns ---
urlpatterns = [
    path('<str:name>/', welcome),
    path('', welcome),
]

# --- Run Django server ---
if __name__ == "__main__":
    execute_from_command_line(sys.argv)

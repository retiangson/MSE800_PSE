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
    html = f"""
    <html>
        <head>
            <title>Welcome Page</title>
            <style>
                body {{
                    background-color: green;
                    color: red;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 20%;
                    font-size: 2em;
                }}
            </style>
        </head>
        <body>
            <p>Welcome {name} to Django!</p>
        </body>
    </html>
    """
    return HttpResponse(html)

# --- URL patterns ---
urlpatterns = [
    path('<str:name>/', welcome),
    path('', welcome),
]

# --- Run Django server ---
if __name__ == "__main__":
    execute_from_command_line(sys.argv)


from apis import views

# API URLs
api_urls = [
    ("/", views.index, ["GET"], "flask scaffolding index url"),
    ("/login", views.login, ["POST"], "User login API"),
]

# Other URLs (if any)
other_urls = []

# Combine all URLs
all_urls = api_urls + other_urls

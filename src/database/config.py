import os

"""
    Config for db
"""

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    pass
else:
    DATABASE_URL = "postgres://simuel:21092008@localhost:5432/fastapi_dev"
print(DATABASE_URL)

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}

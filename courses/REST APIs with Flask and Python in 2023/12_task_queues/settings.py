import os
from dotenv import load_dotenv

# How to deploy a background worker to render.com
load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
QUEUES = ["emails", "default"]

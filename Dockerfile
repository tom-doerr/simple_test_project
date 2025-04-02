FROM python:3.11-slim

WORKDIR /app
COPY . .

# Install dependencies and required system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove gcc python3-dev

# Ensure textual can run in Docker
ENV PYTHONUNBUFFERED=1
ENV TERM=xterm-256color

CMD ["python", "show_time.py", "crypto", "--textual"]

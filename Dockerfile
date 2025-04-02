FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV TERM=xterm-256color \
    COLORTERM=truecolor

ENTRYPOINT ["python", "show_time.py", "crypto", "--textual"]

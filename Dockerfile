# The brain over HTTP (REST and remote MCP), read only. Standard library only, no build step.
#   docker build -t pico-gtm-brain .
#   docker run -p 8765:8765 -e PICO_BRAIN_TOKEN=$(openssl rand -hex 32) pico-gtm-brain
# Without PICO_BRAIN_TOKEN the server refuses to listen on a public interface.
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PICO_BRAIN_HOST=0.0.0.0 PICO_BRAIN_PORT=8765
WORKDIR /brain
COPY . .
USER nobody
EXPOSE 8765
HEALTHCHECK --interval=30s --timeout=5s CMD ["python3", "-c", "import os, urllib.request; port = os.environ.get('PORT') or os.environ.get('PICO_BRAIN_PORT') or '8765'; urllib.request.urlopen('http://127.0.0.1:' + port + '/health', timeout=4)"]
CMD ["python3", "tools/http_server.py"]

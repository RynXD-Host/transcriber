FROM python:3.9-slim

RUN apt-get update && apt-get install -y nodejs npm ffmpeg

RUN useradd -o -u 1000 user

USER user

ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

RUN pip install --no-cache-dir -r requirements.txt

RUN npm install

COPY --chown=user . $HOME/app

EXPOSE 7860

CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "7860", "--reload"]
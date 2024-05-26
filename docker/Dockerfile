FROM python:3.11.9-slim-bullseye

ARG UID=1032
ARG GID=1032

EXPOSE 5000

WORKDIR /app
COPY . .

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -qq \
  && apt-get -qqq install --no-install-recommends -y pkg-config gcc g++ \
    busybox \
  && apt-get upgrade --assume-yes \
  && apt-get clean \
  && rm -rf /var/lib/apt \
  && mkdir -p /app/db /app/locales \
  &&  addgroup --system --gid ${GID} libretranslate \
  &&  adduser --system --uid ${UID} libretranslate \
  &&  chmod -R 755 /app /app/entrypoint.sh \
  && busybox --install

RUN pip install .
RUN pip cache purge

RUN python /app/scripts/compile_locales.py

#USER libretranslate
WORKDIR /app
RUN mkdir -p /home/libretranslate/.local

# Uncomment whether to include all model in the image
#RUN python scripts/install_models.py

# Uncomment to specify specific language models in the image
#RUN python scripts/install_models.py --load_only_lang_codes <MODEL1, MODEL2>;

CMD ["sh", "/app/entrypoint.sh"]

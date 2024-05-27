FROM python:3.11.9-slim-bullseye as builder

WORKDIR /app

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -qq \
  && apt-get -qqq install --no-install-recommends -y pkg-config gcc g++ \
    busybox \
  && busybox --install \
  && apt-get upgrade --assume-yes \
  && apt-get clean \
  && rm -rf /var/lib/apt

RUN python -mvenv venv && ./venv/bin/pip install --no-cache-dir --upgrade pip

COPY . .

# Install package from source code, compile translations
RUN ./venv/bin/pip install . \
#  && ./venv/bin/python scripts/compile_locales.py \
  && ./venv/bin/pip cache purge

FROM python:3.11.9-slim-bullseye

ARG with_models=false
ARG models=""
ARG UID=1032
ARG GID=1032

RUN addgroup --system --gid ${GID} libretranslate \
 && useradd --system --uid ${UID} -g ${GID} libretranslate \
 && mkdir -p /home/libretranslate/.local /app/db \
 && chown -R libretranslate:libretranslate /home/libretranslate/.local /app/db

USER libretranslate

COPY --from=builder --chown=${UID}:${GID} /app /app
WORKDIR /app

COPY --from=builder --chown=${UID}:${GID} /app/venv/bin/ltmanage /usr/bin/

#RUN if [ "$with_models" = "true" ]; then  \
#  # initialize the language models
#  if [ ! -z "$models" ]; then \
#  ./venv/bin/python scripts/install_models.py --load_only_lang_codes "$models";   \
#  else \
#  ./venv/bin/python scripts/install_models.py;  \
#  fi \
#  fi

EXPOSE 5000
CMD ["top"]
#ENTRYPOINT [ "./venv/bin/libretranslate", "--host", "*" ]

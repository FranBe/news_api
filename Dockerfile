#***************************************************************
#                           Bulder
#***************************************************************
FROM python:3.12-slim-trixie AS builder

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Setting working directory
WORKDIR /app

COPY . /app

RUN uv sync --frozen --no-install-project


# Disable development dependencies
ENV UV_NO_DEV=1

RUN uv sync --locked

CMD ["uv", "run", "python", "-m", "src.main"]



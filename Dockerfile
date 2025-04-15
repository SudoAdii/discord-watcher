FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg \
    fonts-liberation libnss3 libatk-bridge2.0-0 libxss1 libasound2 libxshmfence1 libgbm-dev libgtk-3-0 libu2f-udev xvfb \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Install Google Chrome (specific version)
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb || true

# Install ChromeDriver (matching version: 123.0.6312.86)
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/123.0.6312.86/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && chmod +x /usr/local/bin/chromedriver

# Set display env for Xvfb
ENV DISPLAY=:99

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python script
COPY main.py .

# Run using virtual display
CMD ["xvfb-run", "--auto-servernum", "python", "main.py"]

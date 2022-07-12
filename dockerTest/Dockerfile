FROM 3.11.0b3-alpine3.16

# Make a directory for our application
WORKDIR /app

# Install Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY /app .

# Run our application
CMD [ "python", "hello.py" ]
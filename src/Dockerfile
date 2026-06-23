# 1. Use an official lightweight Python runtime as a parent image
FROM python:3.11-slim

# 2. Set The working directory inside the container structure
WORKDIR /app

# 3. Copy the requirements file first to leverage Docker cache optimization
COPY requirements.txt

# 4. Install all project dependecies inside the isolated container environment
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 5 Copy the entire porject folders into container application directory
COPY models/ ./models/
COPY src/ ./src

# 6. Rxpose the port tha FastApi/Uvicorn will run on inside te container
EXPOSE 8000

# 7. Set the execution environment variable to locate python modules securely
ENV PYTHONPATH=/app

#8. Define the final command to launch our production server using Uvicorn
CMD ["uvicorn", "src.app:app", "--hots", "0.0.0.0", "-port", "8000"]

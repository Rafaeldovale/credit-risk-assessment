# 1. Use an official lightweight Python runtime as a parent image
FROM python:3.11-slim

# 2. Install system dependencies required by LightGBM in Linux environments
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# 3. Set the working directory inside the container structure
WORKDIR /app

# 4. Copy the requirements file first to leverage Docker cache optimization
COPY requirements.txt .

# 5. Install all project dependencies inside the isolated container environment
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Copy the entire project folders into the container application directory
COPY models/ ./models/
COPY src/ ./src/

# 7. Expose the port that FastAPI/Uvicorn will run on inside the container
EXPOSE 8000

# 8. Set the execution environment variable to locate python modules securely
ENV PYTHONPATH=/app

# 9. Define the final command to launch our production server using Uvicorn
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]

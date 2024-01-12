# Django Blog API
![image](https://github.com/mirafzal114/BlogApi/assets/136591233/36d06a53-ca28-4aa2-be14-2fdd4466fb92)

![image](https://github.com/mirafzal114/BlogApi/assets/136591233/b6fc68fb-98d1-4810-b62a-8b3884197d66)

![image](https://github.com/mirafzal114/BlogApi/assets/136591233/ee85e076-cc12-4928-a26b-60f8e1bc0237)

![image](https://github.com/mirafzal114/BlogApi/assets/136591233/018497cd-55da-43a6-b033-e12292e72e4b)





Django Blog API is a simple RESTful API for managing blog posts and user information.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST framework

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mirafzal114/BlogApi.git
    cd BlogApi
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

The API should now be accessible at `http://127.0.0.1:8000/`.

## API Endpoints

- **Create a new post:**
    - Endpoint: `/blogs/new/`
    - Method: POST

- **Get all posts:**
    - Endpoint: `/blogs/`
    - Method: GET

- **Get user posts:**
    - Endpoint: `/blogs/<str:username>/`
    - Method: GET

- **Update, retrieve, or delete a post:**
    - Endpoint: `/blogs/<int:pk>/`
    - Methods: GET, PUT, PATCH, DELETE

## Project Structure

- `blogapi/`: Django project directory.
- `postapi/`: Django app directory containing models, views, serializers, etc.
- `manage.py`: Django management script.
- `requirements.txt`: List of Python dependencies.

### Installation

#### Docker
To run the project using Docker:

1. Ensure Docker is installed on your system.
2. Build the Docker image:
    ```
    docker build -t blogapi .
    ```

3. Run the Docker container:
    ```
    docker run -p 8000:8000 blogapi
    ```

### Local Development

To run the project locally without Docker:

1. Install Python 3.11.

2. Clone the repository:
    ```
    git clone https://github.com/mirafzal114/TodoApi/
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```
    python manage.py migrate
    ```

5. Start the server:
    ```
    python manage.py runserver
    ```

## API Examples

#### Create a Blog

```http
POST /api/blogs/new
Content-Type: application/json

{
    "title": "Sample Task",
    "content": "This is a sample task description."
}

Contributions are welcome! If you find any issues or have suggestions, please open an [issue](https://github.com/mirafzal114/BlogApi/issues) or create a pull request.

## License
```
## Contributions are welcome! If you find any issues or have suggestions, please open an [issue](https://github.com/mirafzal114/BlogApi/issues) or create a pull request.



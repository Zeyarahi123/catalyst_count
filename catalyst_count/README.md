# Catalyst Count

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Zeyarahi123/catalyst_count.git
    cd catalyst_count
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv catalyst-env
    source catalyst-env/bin/activate  # On Windows: catalyst-env\Scripts\activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```
    DB_NAME=catalyst
    DB_USER=media
    DB_PASSWORD=catalyst123
    DB_HOST=localhost
    DB_PORT=5432
    SECRET_KEY=asdfg120qwe86512
    DEBUG=True
    ```

5. **Apply migrations and create a superuser**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## Running Tests

To run the tests, use:
```sh
python manage.py test

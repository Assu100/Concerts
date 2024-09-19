# Concerts
# Concert Domain

This project manages a concert domain using SQLAlchemy. It includes models for `Band`, `Venue`, and `Concert` with relationships and various methods to handle data.

## Setup

1. Install dependencies:
    ```bash
    pipenv install
    pipenv shell
    ```

2. Initialize the database:
    ```python
    from app.database import init_db
    init_db()
    ```

3. Run tests:
    ```bash
    pytest -x
    ```

## Usage

You can use the defined methods in `app/methods.py` to interact with the data. For example:
```python
from app.methods import get_band_concerts
print(get_band_concerts(band_id=1))

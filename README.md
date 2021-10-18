## How to run API

### setup virtual environment

- `python3 -m virtualenv .venv`
- `source .venv/bin/activate`

### install requirements

- `pip install -Ur requirements.txt`

### run application

- `python src/app.py`

### run test cases

- `pytest tests/`

## Assumptions:
- Considering only one user can pay for an expense

## API Signature:

1. `POST /api/v1/user/_create`
    ```
    {
        "Id": 2,
        "Name": "Kalyan",
        "Email": "lpk.ladi@leoforce.com",
        "Phone": "9437724618"
    }
   ```
2. `POST /api/v1/expense/_create`
   ```
    {
        "Title": "expense2",
        "Amount": 100,
        "PaidBy": 2,
        "SplitTo": [
            {
                "UserId": 1,
                "Percentage": 10,
                "Amount": 60
            },
            {
                "UserId": 2,
                "Percentage": 90,
                "Amount": 40
            }
        ],
        "ExpenseType": "Exact"
    }
   ```
3. `GET /api/v1/user/_balancesheet?id=1`
4. `GET /api/v1/user/_settle?from_id=1&to_id=2`
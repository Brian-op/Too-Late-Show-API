#  Too Late Show API

A Flask RESTful API with JWT authentication for managing guests, episodes, appearances, and users on a late-night show.

---

##  Setup Steps

1. **Clone the repo**  
   ```bash
   git clone <repo-url>
   cd Too-Late-Show-API
   ```

2. **Install dependencies**  
   ```bash
   pipenv install
   pipenv shell
   ```
  ```
  
3. **Run the app**  
   ```bash
   flask run
   ```

---

##  Database Setup

1. **Initialize migration**  
   ```bash
   flask db init
   ```

2. **Create migration script**  
   ```bash
   flask db migrate -m "Initial migration"
   ```

3. **Apply migration**  
   ```bash
   flask db upgrade
   ```

4. **Seed the database**  
   ```bash
   python -m server.seed
   ```

---

## 💬 Example Requests

###  Signup
**POST** `/signup`
```json
{
  "username": "mahomes",
  "email": "mahomes@example.com",
  "password": "secret123"
}
```

**Response:**
```json
{
  "id": 1,
  "username": "mahomes"
}
```

---

###  Login
**POST** `/login`
```json
{
  "username": "mahomes",
  "password": "secret123"
}
```

**Response:**
```json
{
  "access_token": "..."
}
```

---

###  Protected Route (e.g. `/episodes`)
Headers:
```
Authorization: Bearer <access_token>
```

---

##  Validation Rules

- `username`: must be unique
- `email`: required and unique
- `password`: required
- `rating`: must be an integer (1-10)

---

##  Postman / Thunder Client

- Make sure to set:
  - `Content-Type: application/json` in headers
  - Authorization header: `Bearer <your_token>`
- Use POST for `/signup` and `/login`, and GET for protected routes after logging in

---


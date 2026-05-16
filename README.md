# Flatiron Cars Flask App

## Description

This Flask application demonstrates the use of static and dynamic routes.

The app allows users to:

- Visit the home page
- Search for car models in the Flatiron fleet

---

## Routes

### Home Route

URL:

```bash
/
```

Response:

```text
Welcome to Flatiron Cars
```

---

### Dynamic Model Route

URL:

```bash
/<model>
```

Example:

```bash
/civic
```

Response:

```text
Flatiron civic is in our fleet!
```

If model does not exist:

```text
No models called ferrari exists in our catalog
```

---

## Technologies Used

- Python
- Flask
- Pipenv

---

## Screenshot
![images./Screenshot(27).png]
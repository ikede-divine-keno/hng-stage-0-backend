# HNG Stage 0 Backend Track Profile API Endpoint 🚀

GitHub repository for the HNG Stage 0 backend track.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.2-green.svg)
![Railway](https://img.shields.io/badge/Deployed-Railway-blueviolet.svg)

A **FastAPI** GET endpoint at `/me` serving profile information and a *random cat fact* fetched from `https://catfact.ninja/fact`. Built with **Python** and **FastAPI**, hosted on **Railway** (free tier), it delivers a JSON response with a dynamic timestamp, fresh cat facts, bot-friendly CORS, and robust error handling.

---

## 📂 Project Structure

```
your-repo/
├── README.md              # Project documentation
├── .gitignore             # Ignores .env, venv/, and other unnecessary files
├── profile-api/
│   ├── main.py            # FastAPI application code
│   ├── requirements.txt   # Project dependencies
│   ├── .env               # Environment variables (not tracked in Git)
│   ├── .env.example       # Template for environment variables
```

---

## 🛠️ Setup Instructions

Follow these steps to run the project locally or deploy it on Railway.

### 1. Clone the Repository

```bash
git clone https://github.com/ikede-divine-keno/hng-stage-0-backend.git
cd hng-stage-0-backend
```

### 2. Navigate to Project Folder

```bash
cd profile-api
```

### 3. Set Up Virtual Environment

**Unix-like (Linux/macOS)**:

```bash
python -m venv venv
source venv/bin/activate
```

**Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

*Note*: If setting up the virtual environment in the repository root, run `python -m venv venv` from `your-repo/`.

### 4. Install Dependencies

Install dependencies listed in `profile-api/requirements.txt`:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install fastapi uvicorn requests python-dotenv
```

### 5. Configure Environment Variables

Copy the example environment file:

```bash
cp profile-api/.env.example profile-api/.env
```

Edit `profile-api/.env` with your details:

```
EMAIL=your.email@example.com
FULL_NAME=Your Full Name
STACK=Python/FastAPI
CAT_FACT_URL=catfact.herokuapp.com
```

---

## 🚀 Running Locally

1. With the virtual environment activated, run the FastAPI application:

```bash
uvicorn main:app --reload
```

2. Open your browser and navigate to:  
   [http://127.0.0.1:8000/me](http://127.0.0.1:8000/me)

3. Verify the JSON response contains:
   - `status`: Success status
   - `user`: Profile information (email, name, stack)
   - `timestamp`: Current UTC timestamp
   - `fact`: A random cat fact

4. Refresh the page to see a new timestamp and cat fact.

5. Optionally, test with curl to check headers:

```bash
curl -i http://127.0.0.1:8000/me
```

---

## 📦 Dependencies

The following packages are listed in `profile-api/requirements.txt`:

| Package          | Purpose                              |
|------------------|--------------------------------------|
| `fastapi`        | Builds the API endpoint              |
| `uvicorn`        | ASGI server for FastAPI             |
| `requests`       | Fetches cat facts from the API      |
| `python-dotenv`  | Loads environment variables from `.env` |

---

## 🔧 Environment Variables

Environment variables are stored in `profile-api/.env` (not tracked in Git; use `.env.example` as a template).

| Variable         | Description                     | Example Value                  |
|------------------|---------------------------------|--------------------------------|
| `EMAIL`          | Your email address              | `your.email@example.com`       |
| `FULL_NAME`      | Your full name                  | `Your Full Name`               |
| `STACK`          | Your tech stack                 | `Python/FastAPI`               |
| `CAT_FACT_URL`   | Cat fact API endpoint           | `https://catfact.ninja/fact`        |

---

## 🌐 Deploying on Railway (Free Tier)

Host the application on Railway at [https://your-app.railway.app/me](https://your-app.railway.app/me).

1. Sign up at [railway.app](https://railway.app) and link your GitHub account.
2. Create a new project, select "Deploy from GitHub," and choose `your-repo`.
3. Set the **Root Directory** to `profile-api/` (contains `main.py`).
4. In **Settings > Deploy > Start Command**, set:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

5. In **Variables**, add:
   - `EMAIL=your.email@example.com`
   - `FULL_NAME=Your Full Name`
   - `STACK=Python/FastAPI`
   - `CAT_FACT_URL=https://catfact.ninja/fact`

6. In **Networking**:
   - Remove TCP Proxy if enabled.
   - Toggle Private Networking off/on if you encounter a "Failed to get private network endpoint" error.
   - Click "Generate Domain" to get `your-app.railway.app`.

7. Deploy the application (automatically triggered on Git push or manually via Redeploy).
8. Access the endpoint: [https://your-app.railway.app/me](https://your-app.railway.app/me).
9. Test with curl:

```bash
curl -i https://your-app.railway.app/me
```

10. Refresh to verify new facts and timestamps.

---

## 📋 API Details

**Endpoint**: `GET /me`

**Response Example**:

```json
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Your Full Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-18T04:13:56.789Z",
  "fact": "Cats can jump up to five times their own height."
}
```

**Features**:
- Dynamic UTC timestamp (ISO 8601 format).
- Random cat fact per request (no caching).
- CORS enabled (`Access-Control-Allow-Origin: *`) for bot testing.
- Fallback fact if the cat fact API fails.
- Error logging to the console.

---

## ✅ Best Practices

- **Environment Variables**: Stored in `.env` and excluded via `.gitignore`.
- **Dependencies**: Reproducible with `requirements.txt`.
- **CORS**: Enabled for bot accessibility.
- **Timeout**: 5-second timeout on API calls.
- **Content-Type**: `application/json` for all responses.

---

## 🧪 Testing

### Local Testing
1. Open [http://127.0.0.1:8000/me](http://127.0.0.1:8000/me) in your browser.
2. Alternatively, use curl:

```bash
curl -i http://127.0.0.1:8000/me
```

### Production Testing
1. Open [https://your-app.railway.app/me](https://your-app.railway.app/me) in your browser.
2. Alternatively, use curl:

```bash
curl -i https://your-app.railway.app/me
```

### Verification
- Ensure HTTP status is `200 OK`.
- Confirm `Content-Type: application/json` and CORS headers are present.
- Verify that `timestamp` and `fact` change on refresh.
- Bots can access the endpoint due to CORS configuration.

For issues, check Railway logs or test with a browser or curl.
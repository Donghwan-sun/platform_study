import uvicorn
from webapp import app

if __name__ == "__main__":
    app = app.start_application()
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)

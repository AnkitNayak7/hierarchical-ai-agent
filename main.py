from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "Hello from Ankit Nayak!",
        "service": "hierarchical-ai-agent"
    }

@app.get("/run-agent")
def run_agent():
    # TODO: integrate your ADK agent here
    return {
        "status": "success",
        "message": "Agent execution placeholder"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
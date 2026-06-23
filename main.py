import httpx
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

# Configuration
REAL_APP_URL = "http://127.0.0.1:3000"
DUMMY_APP_URL = "http://127.0.0.1:4000"

# Malicious signatures to trigger the Honeypot
THREAT_SIGNATURES = ["1=1", "select", "script", "admin", "union", "passwd"]

@app.middleware("http")
async def sentinel_gateway(request: Request, call_next):
    # Poora URL aur parameters scan karna
    full_path = str(request.url).lower()
    
    # Check if request is malicious
    if any(sig in full_path for sig in THREAT_SIGNATURES):
        print(f"🚨 [TRAP TRIGGERED] Malicious request to: {full_path}")
        
        # Honeypot se content fetch karna (Transparent Proxy)
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(DUMMY_APP_URL)
                return Response(
                    content=response.content, 
                    status_code=200, 
                    media_type="text/html"
                )
            except Exception as e:
                return Response(content="Service Temporarily Unavailable", status_code=503)

    # Normal traffic routing (Real App)
    async with httpx.AsyncClient() as client:
        try:
            # Real App se content fetch karna
            response = await client.get(f"{REAL_APP_URL}{request.url.path}")
            return Response(
                content=response.content, 
                status_code=response.status_code, 
                media_type="text/html"
            )
        except:
            return await call_next(request)

@app.get("/")
async def root():
    return {"message": "SentinelEdge Gateway Active"}
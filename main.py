import httpx
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from detector import ThreatDetector
from logger import AuditLogger
from config import settings

app = FastAPI(title="SentinelEdge Gateway", version="2.0.0")
detector = ThreatDetector()
audit = AuditLogger()

@app.middleware("http")
async def sentinel_gateway(request: Request, call_next):
    client_ip = request.client.host if request.client else "unknown"
    path = request.url.path
    query = str(request.url.query)
    user_agent = request.headers.get("user-agent", "")
    referer = request.headers.get("referer", "")

    # Read body (carefully)
    body = ""
    if request.method in ["POST", "PUT", "PATCH"]:
        try:
            body_bytes = await request.body()
            body = body_bytes.decode("utf-8", errors="ignore")
        except Exception:
            body = ""

    request_data = {
        "path": path,
        "query": query,
        "body": body,
        "user_agent": user_agent,
        "referer": referer,
    }

    analysis = detector.analyze(request_data)

    # Decide target
    if analysis["is_threat"]:
        target_url = settings.HONEYPOT_URL
        target_name = "honeypot"
        audit.threat(client_ip, path, analysis)
        print(f"🚨 THREAT | IP: {client_ip} | Score: {analysis['score']} | {analysis['categories']}")
    else:
        target_url = settings.REAL_APP_URL
        target_name = "real_app"
        audit.access(client_ip, path, target_name)

    # Proper reverse proxy
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            url = f"{target_url}{path}"
            if query:
                url += f"?{query}"

            headers = {
                k: v for k, v in request.headers.items()
                if k.lower() not in ["host", "content-length"]
            }

            response = await client.request(
                method=request.method,
                url=url,
                headers=headers,
                content=body.encode() if body else None,
                follow_redirects=False,
            )

            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.headers.get("content-type")
            )
        except Exception as e:
            print(f"Proxy error: {e}")
            return JSONResponse(
                status_code=502,
                content={"error": "Upstream service unavailable"}
            )

@app.get("/health")
async def health():
    return {"status": "active", "service": "SentinelEdge Gateway"}

# SentinelEdge

**Enterprise-Grade Deception Gateway**

SentinelEdge is a lightweight defensive gateway that uses deception techniques to protect applications. It inspects incoming traffic in real time. Legitimate users are routed to the real application. Suspicious or malicious requests are silently redirected to a high-interaction honeypot — without the attacker realizing the switch.

## Features

- **Transparent Deception** — No visible redirects. The attacker stays on the same URL.
- **Multi-vector Detection** — SQL Injection, XSS, Path Traversal, Scanner signatures, and sensitive path probing.
- **Scoring Engine** — Threat scoring instead of simple keyword matching.
- **Structured Audit Logs** — Every threat and access event is logged in JSON for forensic analysis.
- **Zero-Friction for Legitimate Users** — Clean traffic is proxied with minimal latency.
- **Docker Ready** — One command deployment.

## Architecture
Client → Gateway (port 8080)
├── Clean traffic     → Real Application
└── Suspicious traffic → Honeypot (Tarpit)

## Quick Start (Docker)

```bash
docker compose up --build
Test Scenarios
Type,URL Example,Result
Legitimate,http://localhost:8080,Real Dashboard
SQL Injection,http://localhost:8080/login?user=1' OR 1=1--,Honeypot
XSS Attempt,http://localhost:8080/search?q=<script>alert(1),Honeypot
Scanner,"User-Agent containing ""sqlmap"" or ""nikto""",Honeypot

Local Development (without Docker)
pip install -r requirements.txt

# Terminal 1
uvicorn real_site:app --port 3000

# Terminal 2
uvicorn dummy_site:app --port 4000

# Terminal 3
uvicorn main:app --port 8080

Configuration
Edit config.py or use environment variables:

REAL_APP_URL
HONEYPOT_URL
THREAT_THRESHOLD (default 0.6)
LOG_FILE
Audit Logs
All events are written to enterprise_audit.json.
License
MIT

Developed by Ajay Salunkhe

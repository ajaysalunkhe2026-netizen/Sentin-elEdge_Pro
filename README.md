SentinelEdge

> **Lab / prototype — independent work by Ajay Salunkhe.**  
> Not an enterprise product, not a SOC
platform, not a named-customer deployment.  
> Purpose: study transparent deception routing (clean traffic vs honeypot) in a small local gateway.

**Lab deception gateway (prototype)**

SentinelEdge is a lightweight defensive gateway that uses deception techniques to protect applications. It inspects incoming traffic in real time. Legitimate users are routed to the real application. Suspicious or malicious requests are silently redirected to a high-interaction honeypot — without the attacker realizing the switch.

## Features

- **Transparent Deception** — No visible redirects. The attacker stays on the same URL.
- **Multi-vector Detection** — SQL Injection, XSS, Path Traversal, scanner signatures, and sensitive path probing.
- **Scoring Engine** — Threat scoring instead of simple keyword matching.
- **Structured Logs** — Threat and access events logged in JSON for local review.
- **Low friction for clean traffic** — Clean requests are proxied with minimal latency (lab setup).
- **Docker Ready** — One command deployment for local testing.

## Architecture

```text
Client → Gateway (port 8080)
├── Clean traffic      → Real Application
└── Suspicious traffic → Honeypot (Tarpit)
```

## Quick Start (Docker)

```bash
docker compose up --build
```

### Test scenarios

| Type | URL / signal | Result |
|------|----------------|--------|
| Legitimate | `http://localhost:8080` | Real dashboard |
| SQL Injection | `http://localhost:8080/login?user=1' OR 1=1--` | Honeypot |
| XSS attempt | `http://localhost:8080/search?q=<script>alert(1)` | Honeypot |
| Scanner | User-Agent containing `sqlmap` or `nikto` | Honeypot |

## Local development (without Docker)

```bash
pip install -r requirements.txt

# Terminal 1
uvicorn real_site:app --port 3000

# Terminal 2
uvicorn dummy_site:app --port 4000

# Terminal 3
uvicorn main:app --port 8080
```

## Configuration

Edit `config.py` or use environment variables:

- `REAL_APP_URL`
- `HONEYPOT_URL`
- `THREAT_THRESHOLD` (default `0.6`)
- `LOG_FILE`

## Audit logs

Events are written to a local JSON log file (see `LOG_FILE` / project defaults).

## Status

Prototype / learning project. Not marketed as enterprise security software.

## License

MIT

Developed by Ajay Salunkhe
```

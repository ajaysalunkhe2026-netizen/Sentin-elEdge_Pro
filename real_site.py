from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/{path:path}", response_class=HTMLResponse)
async def real_securebank_app(path: str):
    # Ultra-Premium Real Application Dashboard
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Enterprise Global Intranet | Secured</title>
        <style>
            :root {
                --bg-color: #0b1120;
                --panel-bg: #1e293b;
                --accent-blue: #38bdf8;
                --accent-green: #10b981;
                --text-main: #f8fafc;
                --text-muted: #94a3b8;
                --border-color: #334155;
            }
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: var(--bg-color); color: var(--text-main); margin: 0; display: flex; height: 100vh; overflow: hidden; }
            
            /* Sidebar Styling */
            .sidebar { width: 260px; background-color: var(--panel-bg); border-right: 1px solid var(--border-color); display: flex; flex-direction: column; }
            .logo-area { padding: 25px; border-bottom: 1px solid var(--border-color); }
            .logo-area h2 { margin: 0; color: var(--accent-blue); font-size: 22px; letter-spacing: 1px; }
            .nav-menu { padding: 20px 0; flex: 1; }
            .nav-item { padding: 15px 25px; color: var(--text-muted); cursor: pointer; transition: 0.3s; font-weight: 500; }
            .nav-item:hover, .nav-item.active { background-color: rgba(56, 189, 248, 0.1); color: var(--accent-blue); border-right: 3px solid var(--accent-blue); }
            
            /* Main Content Styling */
            .main-content { flex: 1; padding: 40px; overflow-y: auto; }
            .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 20px; margin-bottom: 30px; }
            .header-left h1 { margin: 0; font-size: 28px; font-weight: 400; }
            .sys-info { background: rgba(16, 185, 129, 0.1); border: 1px solid var(--accent-green); padding: 8px 15px; border-radius: 20px; color: var(--accent-green); font-size: 14px; font-weight: bold; display: flex; align-items: center; gap: 8px; }
            
            /* Live Pulse Animation */
            .pulse-dot { height: 10px; width: 10px; background-color: var(--accent-green); border-radius: 50%; display: inline-block; box-shadow: 0 0 10px var(--accent-green); animation: pulse 1.5s infinite; }
            @keyframes pulse { 0% { opacity: 1; transform: scale(1); } 50% { opacity: 0.4; transform: scale(1.2); } 100% { opacity: 1; transform: scale(1); } }
            
            /* Dashboard Grid */
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px; margin-bottom: 30px; }
            .card { background-color: var(--panel-bg); padding: 25px; border-radius: 12px; border: 1px solid var(--border-color); position: relative; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); transition: transform 0.3s; }
            .card:hover { transform: translateY(-5px); }
            .card::before { content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background-color: var(--accent-blue); }
            .card-title { color: var(--text-muted); font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }
            .card-value { font-size: 38px; font-weight: 700; color: var(--text-main); }
            .card-subtext { font-size: 13px; color: var(--accent-green); margin-top: 5px; }
            
            /* Terminal Window */
            .terminal { background-color: #000; border-radius: 8px; border: 1px solid var(--border-color); padding: 20px; font-family: 'Consolas', monospace; color: #a5b4fc; font-size: 14px; height: 150px; overflow-y: hidden; }
            .term-line { margin-bottom: 8px; }
            .term-success { color: var(--accent-green); }
        </style>
    </head>
    <body>
        <div class="sidebar">
            <div class="logo-area">
                <h2>🌐 Global Core</h2>
            </div>
            <div class="nav-menu">
                <div class="nav-item active">Overview</div>
                <div class="nav-item">Network Analytics</div>
                <div class="nav-item">Threat Intelligence</div>
                <div class="nav-item">System Settings</div>
            </div>
        </div>
        
        <div class="main-content">
            <div class="header">
                <div class="header-left">
                    <h1>System Architecture Dashboard</h1>
                    <p style="color: var(--text-muted); margin-top: 5px;">Today is Saturday | SentinelEdge Authorization Active</p>
                </div>
                <div class="sys-info">
                    <span class="pulse-dot"></span> Secure Connection Verified
                </div>
            </div>
            
            <div class="grid">
                <div class="card">
                    <div class="card-title">Sequence Patterns Scanned</div>
                    <div class="card-value">83</div>
                    <div class="card-subtext">✔ All sequences optimal</div>
                </div>
                <div class="card" style="border-left-color: #f59e0b;">
                    <div class="card-title">Active Security Nodes</div>
                    <div class="card-value">38</div>
                    <div class="card-subtext" style="color: #f59e0b;">Monitoring dynamic traffic</div>
                </div>
                <div class="card" style="border-left-color: var(--accent-green);">
                    <div class="card-title">Threats Bypassed</div>
                    <div class="card-value">0</div>
                    <div class="card-subtext">Zero-friction routing flawless</div>
                </div>
            </div>
            
            <h3 style="color: var(--text-muted); font-weight: 500; margin-bottom: 15px;">Live Gateway Logs</h3>
            <div class="terminal">
                <div class="term-line">[SYS] Initializing enterprise connection... <span class="term-success">OK</span></div>
                <div class="term-line">[SYS] Verifying user clearance level... <span class="term-success">CLEARED</span></div>
                <div class="term-line">[NET] Routing traffic through SentinelEdge Node-01... <span class="term-success">CONNECTED</span></div>
                <div class="term-line" style="color: #fff;">> Waiting for new events...</div>
            </div>
        </div>
    </body>
    </html>
    """
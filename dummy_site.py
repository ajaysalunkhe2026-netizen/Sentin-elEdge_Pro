from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/{path:path}", response_class=HTMLResponse)
@app.post("/{path:path}", response_class=HTMLResponse)
async def fake_admin_portal(request: Request, path: str):
    # Backend Logging: Hacker ke IP aur target path ko record karna
    client_ip = request.client.host
    print(f"[HONEYPOT TRAP] Intrusion Detected! IP: {client_ip} | Target: /{path}")
    
    # Premium Fake SecureBank Admin Portal (The Tarpit)
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SecureBank Intranet - Restricted Access</title>
        <style>
            :root {
                --bg-color: #f3f4f6;
                --primary: #1e3a8a;
                --danger: #ef4444;
                --border: #d1d5db;
                --text-dark: #1f2937;
                --text-light: #6b7280;
            }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                background-color: var(--bg-color); 
                display: flex; 
                justify-content: center; 
                align-items: center; 
                height: 100vh; 
                margin: 0; 
            }
            .login-container { 
                background: white; 
                padding: 40px; 
                border-radius: 8px; 
                box-shadow: 0 10px 25px rgba(0,0,0,0.1); 
                width: 100%; 
                max-width: 420px; 
                border-top: 5px solid var(--primary);
                position: relative;
            }
            .lock-icon {
                font-size: 40px;
                text-align: center;
                margin-bottom: 10px;
                color: var(--primary);
            }
            .login-container h2 { 
                color: var(--primary); 
                text-align: center; 
                margin: 0 0 5px 0; 
                font-weight: 600; 
                letter-spacing: -0.5px;
            }
            .subtitle {
                color: var(--text-light);
                text-align: center;
                font-size: 14px;
                margin-bottom: 30px;
            }
            .input-group { 
                margin-bottom: 20px; 
                text-align: left; 
            }
            .input-group label { 
                display: block; 
                font-size: 13px; 
                color: var(--text-dark); 
                margin-bottom: 6px; 
                font-weight: 500;
            }
            .input-group input { 
                width: 100%; 
                padding: 12px; 
                border: 1px solid var(--border); 
                border-radius: 4px; 
                box-sizing: border-box; 
                font-size: 14px;
                transition: border-color 0.3s;
            }
            .input-group input:focus {
                outline: none;
                border-color: var(--primary);
                box-shadow: 0 0 0 3px rgba(30, 58, 138, 0.1);
            }
            .login-btn { 
                background-color: var(--primary); 
                color: white; 
                border: none; 
                padding: 14px; 
                width: 100%; 
                border-radius: 4px; 
                cursor: pointer; 
                font-size: 16px; 
                font-weight: 600; 
                transition: background 0.3s; 
                margin-top: 10px;
            }
            .login-btn:hover { 
                background-color: #172554; 
            }
            .login-btn:disabled {
                background-color: #9ca3af;
                cursor: not-allowed;
            }
            .error-box {
                background-color: #fef2f2;
                border-left: 4px solid var(--danger);
                color: #b91c1c;
                padding: 12px;
                font-size: 13px;
                margin-top: 20px;
                border-radius: 4px;
                display: none;
            }
            .footer { 
                margin-top: 30px; 
                font-size: 11px; 
                color: #9ca3af; 
                text-align: center;
                border-top: 1px solid #f3f4f6;
                padding-top: 15px;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <div class="lock-icon">🔒</div>
            <h2>SecureBank Intranet</h2>
            <div class="subtitle">Level 4 Authorized Personnel Only</div>
            
            <form id="honeypot-form">
                <div class="input-group">
                    <label for="admin_id">Administrator ID</label>
                    <input type="text" id="admin_id" required placeholder="e.g., ADM-XXXX">
                </div>
                <div class="input-group">
                    <label for="password">System Password</label>
                    <input type="password" id="password" required placeholder="Enter secure password">
                </div>
                <button type="submit" class="login-btn" id="submit-btn">Authenticate</button>
            </form>
            
            <div class="error-box" id="error-msg">
                <strong>Authentication Failed:</strong> Invalid credentials provided. This attempt has been logged.
            </div>
            
            <div class="footer">
                &copy; 2026 SecureBank Enterprise Systems.<br>
                Unauthorized access is strictly prohibited and monitored.
            </div>
        </div>
        
        <script>
            // Fake authentication delay to waste hacker's time (Tarpitting)
            document.getElementById("honeypot-form").addEventListener("submit", function(e) {
                e.preventDefault();
                
                const btn = document.getElementById("submit-btn");
                const errorBox = document.getElementById("error-msg");
                
                // Hide previous error
                errorBox.style.display = "none";
                
                // UI changes for fake loading
                btn.innerText = "Verifying Database...";
                btn.disabled = true;
                
                // Wait 2.5 seconds before showing the error
                setTimeout(function() {
                    errorBox.style.display = "block";
                    btn.innerText = "Authenticate";
                    btn.disabled = false;
                    
                    // Clear inputs for the next fake attempt
                    document.getElementById("password").value = '';
                }, 2500);
            });
        </script>
    </body>
    </html>
    """
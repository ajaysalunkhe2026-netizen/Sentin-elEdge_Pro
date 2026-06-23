# SentinelEdge: Enterprise-Grade Defensive Gateway

SentinelEdge ek advanced cybersecurity framework hai jo Deception-based Defense (Honeypot) technique ka use karta hai. Yeh system attackers ko identify karke unhe real application ke bajaye ek controlled 'trap' environment mein redirect karta hai, jisse attacker ko lagta hai ki woh system hack kar raha hai, jabki woh ek surveillance trap mein hota hai.

## 🚀 Key Features
* **Transparent Proxy Deception:** Redirects ka use nahi karta. Attacker ko URL badalne ka pata nahi chalta.
* **Malicious Signature Detection:** SQL Injection, XSS, aur automated scanning attempts ko real-time mein detect karta hai.
* **Stealth Logs:** Attackers ke har activity ko `enterprise_audit.json` file mein log karta hai for forensic analysis.
* **Zero-Friction Routing:** Legitimate users ko bina kisi rukawat ke real dashboard tak route karta hai.

## 🛠️ Architecture


- **Gateway (`main.py`):** Traffic ka entry point jo har request ko inspect karta hai.
- **Real App (`real_site.py`):** Verified users ke liye corporate-grade secure dashboard.
- **Honeypot (`dummy_site.py`):** Intruder ke liye trap (fake login portal).

## ⚙️ Installation & Usage
1. **Prerequisites:**
   Ensure Python and pip are installed. Install required libraries:
   `pip install fastapi uvicorn httpx`

2. **Run System Modules (Open 3 separate terminals):**
   - **Terminal 1 (Real App):** `uvicorn real_site:app --port 3000`
   - **Terminal 2 (Honeypot):** `uvicorn dummy_site:app --port 4000`
   - **Terminal 3 (Gateway):** `uvicorn main:app --port 8080`

3. **Access the System:**
   - **Legitimate:** Visit `http://127.0.0.1:8080`
   - **Malicious:** Visit `http://127.0.0.1:8080/login?user=1=1` (Trap triggered)

## 🤝 Contributing
- Fork the project and create a feature branch.
- Follow coding standards and add comments for new features.
- Submit a Pull Request for review.

## 🛡️ Security Policy
- Vulnerabilities ko public na karein.
- Security flaws milne par seedha report karein.
- Updates ke liye repository check karte rahein.

---
*Developed by Ajay Salunke | Secure Enterprise Solutions*
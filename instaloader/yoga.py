import instaloader
import pandas as pd
import time

USERNAME = "rudranshupreti"  # same as session file
HASHTAG = "yogainfluencer"  # change to your niche hashtag
LIMIT = 50                  # how many profiles to scrape
DELAY_SEC = 5               # delay between requests (seconds)

L = instaloader.Instaloader()

# ✅ Load saved session
try:
    L.load_session_from_file(USERNAME)
    print(f"✅ Session loaded for @{USERNAME}")
except Exception as e:
    print(f"❌ Session load failed: {e}")
    exit()

# ✅ Load hashtag posts
try:
    print(f"🔍 Scraping #{HASHTAG}...")
    posts = instaloader.Hashtag.from_name(L.context, HASHTAG).get_posts()
except Exception as e:
    print(f"❌ Failed to load hashtag: {e}")
    exit()

results = []
scraped = 0

for post in posts:
    try:
        profile = post.owner_profile

        # ✅ Custom filter logic (followers + niche)
        if (
            profile.followers > 1000 and profile.followers < 100000 and
            (
                'yoga' in profile.username.lower() or
                'fitness' in profile.username.lower() or
                'gym' in profile.username.lower() or
                'yoga' in profile.biography.lower()
            )
        ):
            results.append({
                'Username': profile.username,
                'Full Name': profile.full_name,
                'Followers': profile.followers,
                'Bio': profile.biography,
                'External URL': profile.external_url,
                'Verified': profile.is_verified
            })
            scraped += 1
            print(f"✅ {scraped}. {profile.username} ({profile.followers} followers)")

        if scraped >= LIMIT:
            break

        time.sleep(DELAY_SEC)

    except Exception as e:
        print(f"⚠️ Error: {e}")
        time.sleep(10)

# ✅ Save to CSV
df = pd.DataFrame(results)
filename = f"{HASHTAG}_influencers.csv"
df.to_csv(filename, index=False)
print(f"\n🎉 Done! {scraped} profiles saved to {filename}")

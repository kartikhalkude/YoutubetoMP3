from flask import Flask, render_template, request, jsonify
import os
import yt_dlp
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# Function to download MP3
def download_audio(url):
    save_path = "downloads"
    os.makedirs(save_path, exist_ok=True)

    options = {
        'format': 'bestaudio/best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        return f"✅ {url} — Download complete!"
    except Exception as e:
        return f"❗ Error with {url}: {e}"

# Route to load the web page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle downloads
@app.route('/download', methods=['POST'])
def download():
    urls = request.form.get("urls")
    if not urls:
        return jsonify({"status": "error", "message": "Please provide at least one URL!"})

    url_list = [url.strip() for url in urls.split("\n") if url.strip()]
    results = []

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_audio, url) for url in url_list]
        for future in futures:
            results.append(future.result())

    return jsonify({"status": "success", "message": results})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


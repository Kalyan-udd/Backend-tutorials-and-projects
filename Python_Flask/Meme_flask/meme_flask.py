from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_meme():
    # Updated to a working public Meme API
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url).json()
        # 'preview' is a list of image URLs in different resolutions
        meme_large = response["preview"][-1] 
        subreddit = response["subreddit"]
        return meme_large, subreddit
    except Exception as e:
        print(f"Error fetching meme: {e}")
        return "https://via.placeholder.com/500", "error"

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  
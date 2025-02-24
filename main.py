from flask import Flask, render_template, request, send_from_directory, jsonify
import os

app = Flask(__name__)
MEME_FOLDER = "static/memes"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# Erstelle das Upload-Verzeichnis, falls es nicht existiert
os.makedirs(MEME_FOLDER, exist_ok=True)
app.config["MEME_FOLDER"] = MEME_FOLDER
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    meme_folder = "static/memes"
    memes = sorted(os.listdir(meme_folder), key=lambda x: os.path.getctime(os.path.join(meme_folder, x)), reverse=True)
    return render_template("index.html", memes=memes)

def file_exists(filename):
    return os.path.exists(os.path.join(app.config['MEME_FOLDER'], filename))


@app.route('/download', methods=['POST'])
def download_file():
    if 'file' not in request.files:
        return jsonify({"error": "Keine Datei gefunden"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Keine Datei ausgewählt"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Ungültiger Dateityp! Erlaubt sind nur .jpg, .jpeg, .png und .gif"}), 400

        # Prüfen, ob die Datei bereits existiert
    if file_exists(file.filename):
        return jsonify({"success": False, "message": "Datei existiert bereits!"}), 400
    # Speichert die Datei im Meme-Ordner
    file.save(os.path.join(app.config['MEME_FOLDER'], file.filename))




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


# Ensure static folder exists
if not os.path.exists(MEME_FOLDER):
    os.makedirs(MEME_FOLDER)

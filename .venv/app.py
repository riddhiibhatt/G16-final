from flask import Flask, render_template, request, send_from_directory
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/page2')
def index2():
    return render_template('index2.html')

@app.route('/page3')
def index3():
    return render_template('index3.html')

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    audio_file = request.files['audio']

    # Use a fixed filename for audio
    audio_filename = 'recorded_audio.mp3'

    # Check if audio file is empty
    if audio_file:
        # Save audio to the audio folder
        audio_path = os.path.join(app.static_folder, 'audio', audio_filename)
        audio_file.save(audio_path)

        # Print a message to the console
        print(f"Audio file saved: {audio_filename}")
    else:
        print("No audio file provided.")

    return audio_filename  # You can modify this response as needed

@app.route('/upload_text', methods=['POST'])
def upload_text():
    text = request.form.get('text')

    # Use a fixed filename for text
    text_filename = 'text_file.txt'

    # Check if text is empty
    if text:
        # Save text to the text folder
        text_path = os.path.join(app.static_folder, 'text', text_filename)
        with open(text_path, 'w') as text_file:
            text_file.write(text)

        # Print a message to the console
        print(f"Text file saved: {text_filename}")
    else:
        print("No text provided.")

    return text_filename  # You can modify this response as needed

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory(os.path.join(app.static_folder, 'audio'), filename)

@app.route('/text/<filename>')
def serve_text(filename):
    return send_from_directory(os.path.join(app.static_folder, 'text'), filename)

app.static_folder = 'static'
if __name__ == '__main__':
    app.run(debug=True)

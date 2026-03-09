from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion = emotion_detector(text_to_analyze)

    details = ", ".join(
        f"'{k}': {emotion[k]}"
        for k in sorted(emotion)
        if k != "dominant_emotion"
    )

    return (
        f"For the given statement, the system response is "
        f"{details}. The dominant emotion is <b>{emotion['dominant_emotion']}</b>."
    )
@app.route("/")
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(host='localhost', port='5000')
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=['GET'])
def emo_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if 'emotionPredictions' exists in the response
    if 'emotionPredictions' in response:
        emotion_scores = response['emotionPredictions'][0]['emotion']

        # Extract scores
        anger_score = emotion_scores['anger']
        disgust_score = emotion_scores['disgust']
        fear_score = emotion_scores['fear']
        joy_score = emotion_scores['joy']
        sadness_score = emotion_scores['sadness']

        # Determine the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Create a formatted response and return it
        return (
            "For the given statement, the system response is "
            f"'anger': {anger_score}, "
            f"'disgust': {disgust_score}, "
            f"'fear': {fear_score}, "
            f"'joy': {joy_score}, and "
            f"'sadness': {sadness_score}. "
            f"The dominant emotion is {dominant_emotion}."
        )
    else:
        return "Error: No emotion predictions found.", 500

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

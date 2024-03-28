# Text summarization using HuggingFace's inference API

This Flask-based web application allows users to input a large body of text and receive a summarized version of it. It utilizes the Hugging Face Inference API to generate the summary.

## Features

- Users can input any large text.
- Users can set the desired length for the summary.
- The summary is generated using a pre-trained model from the Hugging Face Inference API.
- It is possible for the user to select any summarization model from the Hugging Face website and get different results.
![image](https://github.com/AnasNasim12/HuggingFaceNLP/assets/106335309/d649bc91-5cfe-4f6e-86e8-7ce65e483790)

## Installation

Before running the application, ensure you have Python and Flask installed.

1. Clone the repository to your local machine.
2. Install the necessary packages using:
```
pip install -r requirements.txt
```
3. Run the Flask app:
```
python app.py
```
![image](https://github.com/AnasNasim12/HuggingFaceNLP/assets/106335309/09f2ba75-3bd1-4d34-bb2b-530769dec46f)

## Usage

1. Go to the web page provided by Flask.
2. Enter the text you want to summarize in the text area.
3. Adjust the slider to select the length of the summary.
4. Click 'Submit' to get the summary of the text.
5. Use the 'Copy text' button to copy the summary to the clipboard.

## Credits

This application was built using the [Hugging Face Inference API](https://huggingface.co/inference-api).


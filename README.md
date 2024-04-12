# Fake News Detection System

This repository contains the implementation of a Fake News Detection System developed as a final project for IST4900. The system utilizes machine learning techniques to classify news articles as either real or fake based on their content.

## Overview

The Fake News Detection System leverages Natural Language Processing (NLP) and machine learning algorithms to analyze news articles and determine their authenticity. The system is capable of processing news articles from both a pre-existing dataset and live web scraping, allowing for real-time detection of fake news.

## Key Features

- Utilizes a Passive-Aggressive classifier and TF-IDF vectorization for text classification.
- Provides a user-friendly web interface for users to input news articles and receive classification results.
- Supports integration with web scraping to fetch news articles from various sources for analysis.
- Implements continuous learning and feedback mechanisms to improve accuracy over time.

## Installation

1. Clone the repository:

   git clone https://github.com/yourusername/fake-news-detection.git

2. Install the required dependencies:

   pip install -r requirements.txt

## Usage

1. Start the Flask application:

   python fake_news_OG.py

2. Access the application in your web browser at `http://localhost:5000`.

3. Enter a news article or select the option to scrape news from the web.

## Contributors

- Elvir Ninteretse - 662638

## Acknowledgements

We would like to express our sincere gratitude to Prof. CEH Chrispus Alukwe for his invaluable guidance and support throughout the development of this project. Special thanks to our families and partners for their unwavering encouragement and understanding.

## License

This project is licensed under the [USIU License](LICENSE).

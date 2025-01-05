bash[README.md](https://github.com/user-attachments/files/18310121/README.md)
# Enhancing Ticket Buying Experience with Real-time Aggregation and Conversational AI

This project is a conversational AI chatbot built using the Rasa framework to streamline the event ticket purchasing experience. The chatbot processes user queries, classifies intents, extracts relevant entities, and interacts with external APIs to provide real-time event information. It also integrates **Retrieval-Augmented Generation (RAG)** and **Large Language Models (LLMs)** to enhance query understanding and improve response accuracy.

## Features
- **Intent Classification**: Powered by the DIETClassifier for accurate detection of user intents such as searching for events or tickets.
- **Entity Extraction**: Recognizes key entities like event names, locations, dates, and price ranges using Rasa NLU and Conditional Random Fields (CRF).
- **Real-time Data Aggregation**: Fetches and updates event details from the Ticketmaster API.
- **Interactive Conversations**: Maintains context across multi-turn dialogues for seamless user interaction.
- **Scalability**: Designed for future expansion, including cloud deployment and additional API integrations.
- **RAG Integration**: Uses a retrieval-augmented approach to fetch accurate and up-to-date event information, ensuring users receive reliable responses.
- **LLM Integration**: Incorporates GPT-4 for handling complex user queries, improving query understanding, and delivering context-aware responses.

## Requirements
- Python 3.8 or 3.9
- Virtual environment (optional)
- Libraries specified in `requirements.txt`

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd path/to/project
   ```
3. Set up the Python environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   pip install -r requirements.txt
   ```

## Usage
1. Train the Rasa model:
   ```bash
   rasa train
   ```
2. Run the action server (with RAG and GPT-4 integration):
   ```bash
   rasa run actions
   ```
3. Start the chatbot:
   ```bash
   rasa shell
   ```
4. Optionally, run the Rasa server with API enabled:
   ```bash
   rasa run -m models --enable-api --cors "*" --debug
   ```

## Key Technologies
- **Rasa Framework**: For intent classification, entity extraction, and dialogue management.
- **Retrieval-Augmented Generation (RAG)**: Enhances real-time data aggregation by retrieving relevant event information from external sources.
- **GPT-4 Integration**: Handles nuanced and complex user queries, ensuring accurate and context-sensitive responses.
- **Conditional Random Fields (CRF)**: For efficient entity recognition and extraction.
- **DIETClassifier**: Ensures high accuracy in intent detection and classification.

## Features to Improve
- Integration with other ticketing platforms (e.g., StubHub, Vivid Seats).
- Deployment to cloud platforms like AWS or Azure.
- Addition of secure payment gateway for complete ticket purchasing.
- Handling ambiguous and erroneous inputs using spell-check and enhanced NLP techniques.

## Future Plans
- Multilingual support.
- Integration with additional services like event reminders and travel accommodations.
- User feedback integration for continuous improvement.

## Acknowledgments
Special thanks to:
- **Dr. Safdar Khan**, for guidance and support.
- Family and friends for their encouragement.
- Allah Almighty for strength and perseverance.



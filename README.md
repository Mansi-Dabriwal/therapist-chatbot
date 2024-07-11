# Therapist Chatbot with Vector Embeddings and Pinecone

## Overview
This project implements a chatbot designed to assist therapists by storing therapist-patient conversations as vector embeddings in Pinecone for efficient retrieval. The chatbot leverages OpenAI's text-embedding-ada-002 model for embedding generation and utilizes Retrieval-Augmented Generation (RAG) for generating contextually accurate responses based on user queries.

## Features
Data Handling: Processes therapist-patient conversations from a CSV file, cleans and preprocesses the data for embedding generation.
Embedding Generation: Utilizes OpenAI's text-embedding-ada-002 model to convert conversations into vector embeddings.
Storage: Stores embeddings in Pinecone for efficient retrieval based on semantic similarity.
Querying: Implements a function to query Pinecone, retrieve relevant conversations, and generate responses using OpenAI's RAG model.
User Interface: Provides an interactive web interface using Streamlit for therapists to input queries and receive responses.

## Demo
YouTube link: [Therapist ChatBot](https://youtu.be/wbiaXNjdlJw)

## Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/your-username/therapist-chatbot.git
    cd therapist-chatbot
    ```

2. **Install Dependencies:**
    Make sure you have Python and pip installed. Then run:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up OpenAI API Key:**
    - Get your API key from OpenAI.
    - Create a file named `.env` in the project root and add your API key:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Run the Application:**
    ```sh
    streamlit run app.py
    ```

## Usage
1. Open the application in your browser (usually at `http://localhost:8501`).
2. Select the type of query from the dropdown menu.
3. Enter your query in the text area.
4. Click the "Submit" button to get a response.

## Error Handling and Troubleshooting

### Common Issues:
- **RateLimitError:** You have exceeded your current quota. Please check your plan and billing details.
- **InvalidRequestError:** There was an issue with your request, likely due to invalid parameters or incorrect API key.
- **Network Issues:** Ensure you have a stable internet connection.

### Solutions:
- **Retry Logic:** The application has built-in retry logic for handling temporary rate limits. If the error persists, consider checking your OpenAI plan and usage.
- **API Key:** Ensure your API key is correct and has the necessary permissions.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For any questions or support, please open an issue in the repository or contact the project maintainer at dabriwal.m@northeastern.edu

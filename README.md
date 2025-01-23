# Cold Email Generator

This project is a Cold Email Generator that uses machine learning to extract job postings from a given URL and generate a cold email tailored to the job description. The project leverages the `langchain_groq` library for natural language processing and `chromadb` for vector storage.

## Features

- Extracts job postings from a given URL.
- Cleans and processes the extracted text.
- Generates a cold email tailored to the job description.
- Uses a vector database to store and query relevant portfolio links.

## Requirements

- Python 3.12
- `langchain_groq`
- `chromadb`
- `streamlit`
- `pandas`
- `uuid`
- `dotenv`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/cold-email-generator.git
    cd cold-email-generator
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    - Create a `.env` file in the root directory.
    - Add your Groq API key to the `.env` file:
        ```
        GROQ_API_KEY='your_groq_api_key'
        ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app/main.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the URL of the job posting and click "Submit".

4. The generated cold email will be displayed on the page.

## Extending the Project

### Adding New Features

1. **Extracting Additional Information**:
    - Modify the `extract_jobs` method in `chains.py` to include additional keys in the JSON output.
    - Update the prompt template to include instructions for extracting the new information.

2. **Improving Email Generation**:
    - Modify the `write_mail` method in `chains.py` to include additional details in the email.
    - Update the prompt template to include instructions for generating a more detailed email.

3. **Enhancing the Vector Database**:
    - Add more documents to the vector database by updating the `my_portfolio.csv` file.
    - Modify the `load_portfolio` method in `portfolio.py` to handle additional data.

### Customizing the UI

1. **Updating the Streamlit Interface**:
    - Modify `app/main.py` to add new input fields or change the layout.
    - Use Streamlit's documentation to explore additional UI components.

## Project Structure

- `app/`: Contains the main application files.
  - `main.py`: The main Streamlit app.
  - `chains.py`: Contains the logic for extracting job postings and generating emails.
  - `portfolio.py`: Manages the portfolio data and vector database.
  - `utils.py`: Utility functions for cleaning text.
  - `resources/`: Contains resource files like `my_portfolio.csv`.
  - `vectorstore/`: Contains the vector database files.
- `.env`: Environment variables file.
- `requirements.txt`: List of required Python packages.

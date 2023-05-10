# INK (Intelligent Narrative Keeper)

This code provides an assistant called INK (Intelligent Narrative Keeper) that can generate various types of documents in different formats based on user input. It utilizes OpenAI's text-davinci-003 model for document generation and integrates with external libraries and APIs for additional functionalities.

Motivation
INK was created as a personal project to explore the capabilities of OpenAI’s text-davinci-003 engine and to demonstrate how natural language processing can be used to create documents.

## Prerequisites
- Python 3.x
- `dotenv` library
- `openai` library
- `prompt_toolkit` library
- `click` library
- `requests` library
- `reportlab` library
- `python-docx` library
- `pptx` library
- `docx2pdf` library
- `colormath` library

You can install using pip:

pip install -r requirements.txt


## Setup
1. Install the required libraries mentioned above.
2. Set up environment variables:
   - Fill the file named `.env` and set `OPENAI_API_KEY` variable to your OpenAI API key.
   - Fill the file named `un.env` and set `UNSPLASH_API_KEY` variable to your Unsplash API key.

## Usage
1. Imports the necessary modules and libraries.
2. Loads the environment variables using `load_dotenv()` function.
3. Sets the OpenAI API key using `openai.api_key`.
4. Implements the `px_to_emu()` function to convert pixels to EMU (English Metric Unit) for PowerPoint slide measurements.
5. Defines the `generate_response()` function that takes a prompt, previous response (optional), filename (optional), and save_to_file flag (optional) as inputs. This function uses the OpenAI API to generate a document based on the prompt. It also allows saving the generated document to a file in various formats (PDF, DOCX, PPTX, or plain text).
6. Implements the `exit_chat()` function to gracefully stop the assistant.
7. Uses a while loop to continuously interact with the user.
   - Prompts the user for input using `prompt_toolkit.prompt()`.
   - If the user enters "exit", "quit", "bye", or "goodbye", call the `exit_chat()` function and break the loop.
   - If the user input contains the word "write", set the `save_to_file` flag to `True`.
   - Calls the `generate_response()` function with the user input, filename (if applicable), and save_to_file flag.
   - If saving to a file, update the filename with the response.
   - If not saving to a file, display the response to the user using `click.echo()`.
   - Reset the `save_to_file` flag to `False`.

To run INK, simply execute the script:

python ink.py
Copy
You will see a prompt that says User:. You can type your request for a document in natural language. For example:

User: Write me a summary of the book "The Catcher in the Rye"
Copy
INK will respond with a generated document in plain text. For example:

INK: The Catcher in the Rye is a novel by J.D. Salinger, first published in 1951. It follows the story of Holden Caulfield, a 16-year-old boy who has been expelled from his prep school and decides to wander around New York City for three days before going home. Along the way, he encounters various people and situations that reveal his alienation, cynicism, and disillusionment with the world. He also struggles with his own identity, sexuality, and mental health. The novel is widely regarded as a classic of American literature and a defining work of the post-war era. It has been praised for its realistic portrayal of adolescence and its critique of social hypocrisy, but also criticized for its vulgar language and controversial themes.
Copy
If you want to save the generated document to a file, you can add write at the beginning of your request and specify the file extension. For example:

User: Write me a resume in pdf format
INK will ask you to enter the filename to save to (without extension) and then create a PDF file with the generated document. For example:

Enter the filename to save to (without extension): resume
Enter file extension (e.g. .txt, .pdf, .docx, .pptx): .pdf
INK: resume.pdf saved
You can also use INK to create presentations in PPTX format. INK will use capitalized words from your request as keywords to search for images on Unsplash and use them as backgrounds for the slides. For example:

User: Write me a presentation about climate change in pptx format
INK will create a PPTX file with slides that have images related to climate change as backgrounds and text that summarizes the topic. For example:

Enter the filename to save to (without extension): climate_change
Enter file extension (e.g. .txt, .pdf, .docx, .pptx): .pptx
INK: climate_change.pptx created successfully!
To exit INK, you can type exit, quit, bye, or goodbye.

**Note**: Ensure that the environment variables are correctly set before running the code.

## Additional Notes
- The code utilizes the `text-davinci-003` engine from OpenAI for generating documents. Modify the engine selection if needed.
- The code uses the Unsplash API to retrieve a random image based on capitalized words in the user prompt when generating PPTX files. Ensure that the `UNSPLASH_API_KEY` environment variable is set correctly.
- The code supports saving documents in multiple formats (PDF, DOCX, PPTX, or plain text) based on the file extension provided by the user when prompted.
- For PDF and DOCX files, the code uses `python-docx` library to create the document and `docx2pdf` library to convert the DOCX file to PDF.
- For PPTX files, the code uses `python-pptx` library to create the slides and sets a random Unsplash image as the background for each slide.
- For other file types, the code simply writes the response to a file with the specified extension.
- The generated documents include a section titled "Output"

## License

This project is licensed under the [MIT License](LICENSE).

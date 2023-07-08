# Voice Assistant

This code snippet demonstrates a Voice Assistant using Python. It can perform various tasks such as searching the web, opening applications, sending emails, telling jokes, providing weather information, taking photos, and more.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/deep663/AI_assistant.git
   ```

2. Install the required libraries:

   ```bash
   pip install speechrecognition pyttsx3 pyjokes opencv-python requests
   ```
3. API Keys

This code uses API keys for certain functionalities. Make sure to obtain the necessary API keys before running the code.

Open the script file voice_assistant.py in a text editor.

Weather API: To get weather information, you need to obtain an API key from OpenWeather and replace 'api_key' with your actual API key in the following line:
   ```bash
   api_key = 'api_key'
   ```
4. Set up email configuration (for sending emails):

   - Open the script file `voice_assistant.py` in a text editor.
   - Replace `'your email id'` with your actual email address.
   - Replace `'your email password'` with your actual email password.

5. Run the script:

   ```bash
   python voice_assistant.py
   ```

## Usage

Once the script is running, you can interact with the voice assistant by speaking commands or questions. Here are some examples:

- **Search the web:** Say "Search for cats on YouTube" to open a YouTube search for cats.

- **Open applications:** Say "Open Chrome" to launch Google Chrome.

- **Get the time:** Say "What's the time now?" to hear the current time.

- **Send an email:** Say "Send an email" to compose and send an email.

- **Tell a joke:** Say "Tell me a joke" to hear a random joke.

- **Get weather information:** Say "What's the weather like in New York?" to get the current weather in New York.

- **Take a photo:** Say "Take a photo" to capture a photo using the webcam.

- **And more:** The voice assistant can perform additional tasks such as changing the background, shutting down the system, locking the window, writing notes, and more.

## Customization

You can customize the voice assistant by modifying the `process_text()` function in the script. This function processes the user's input and performs the corresponding actions. You can add new commands or modify the existing ones to fit your needs.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

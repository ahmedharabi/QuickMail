# QuickMail
# Mail Sending Python App

This Python application allows users to send emails using Gmail and provides a convenient way to save and access the email addresses of teachers without the need to remember them each time.

## Features

- **Sending Emails:** Utilizes Gmail's SMTP server to send emails programmatically.
- **Saving Teacher Emails:** Saves the email addresses of teachers for easy retrieval.
- **User-Friendly Interface:** Provides a simple interface for managing and sending emails efficiently.

## Requirements

- Python 3.x
- Google account with access to Gmail
- Enable "less secure apps" in your Gmail settings (temporarily, for this application)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/mail-sending-app.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Obtain Google API credentials:
    - Go to the Google Developers Console (https://console.developers.google.com/).
    - Create a new project and enable the Gmail API.
    - Create OAuth2 credentials and download the `credentials.json` file.

2. Place the downloaded `credentials.json` file in the root directory of the application.

## Usage

1. Run the application:

    ```bash
    python app.py
    ```

2. Follow the on-screen prompts to send emails and manage teacher email addresses.

### Usage Examples



1. Run the application.
2. Choose the option to send an email.
3. Enter the recipient's email address (you can choose a saved teacher's email).
4. Compose the email content and send.

### Managing Teacher Emails

1. Run the application.
2. Choose the option to manage teacher emails.
3. Add, delete, or view the list of saved teacher emails.

## Disclaimer

- **Security Warning:** Enabling "less secure apps" in your Gmail settings may pose a security risk. Consider creating a separate Gmail account for testing purposes or use caution when enabling this option.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality of this application.

## License

This project is licensed under the [MIT License](LICENSE).

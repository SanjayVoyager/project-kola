# Video Downloader Telegram Bot

This is a Telegram bot that allows users to download videos from various platforms. The bot takes a video URL as input, downloads the video, and sends it back to the user.

## Features

- Download videos from supported platforms using `yt-dlp`.
- Send the downloaded video back to the user directly in the Telegram chat.

## Prerequisites

- Python 3.7 or higher
- Telegram bot token (Create a bot using [BotFather](https://core.telegram.org/bots#botfather) if you don't have one)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/video_downloader_bot.git
    cd video_downloader_bot
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add your Telegram bot token:

    ```plaintext
    TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
    ```

## Usage

1. **Run the bot:**

    ```sh
    python main.py
    ```

2. **Interact with the bot:**

    - Open your Telegram app and find your bot.
    - Send the bot a video URL from any supported platform.
    - The bot will download the video and send it back to you.

### `requirements.txt`

This file lists all the dependencies required for the project.

## Dependencies

- `python-telegram-bot`: A Python wrapper for the Telegram Bot API.
- `yt-dlp`: A youtube-dl fork with additional features and fixes.
- `python-dotenv`: Read environment variables from a `.env` file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [python-dotenv](https://github.com/theskumar/python-dotenv)


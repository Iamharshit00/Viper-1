# Viper-1

Viper-1 is a local AI chat application that runs completely on your computer using a locally stored Large Language Model (LLM). No internet connection is required after the model and dependencies have been installed.

## Features

* Runs completely offline
* Uses a local LLM model
* Simple Python-based interface
* Easy one-click launcher (`run_chat.bat`)
* Uses a Python virtual environment automatically
* Open source and easy to modify

---

## Project Structure

```
Viper-1/
│
├── LLM/
│   ├── model files
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   ├── config.json
│   ├── generation_config.json
│   └── other model files
│
├── chat.py
├── requirements.txt
├── run_chat.bat
└── README.md
```

---

## Requirements

Before running the project, make sure you have:

* Windows 10 or Windows 11
* Python 3.13 installed
* At least 8 GB RAM (16 GB recommended)
* Sufficient free disk space for the model

---

## Installation

### 1. Download the Repository

Download or clone this repository to your computer.

### 2. Install Python

Install **Python 3.13** from the official Python website.

During installation, make sure to enable:

* ✅ Add Python to PATH

---

## Running the Project

Simply double-click:

```
run_chat.bat
```

The launcher will automatically:

* Check whether Python 3.13 is available.
* Create a virtual environment (only the first time).
* Install all required Python packages from `requirements.txt`.
* Launch `chat.py`.

After the first setup, future launches are much faster because the virtual environment is reused.

---

## The LLM Folder

The `LLM` directory contains everything required for the AI model.

Typical files include:

* Model weights
* `config.json`
* `tokenizer.json`
* `tokenizer_config.json`
* `generation_config.json`
* Other model-specific files

Do **not** rename or delete these files unless you know exactly what you are doing.

---

## Updating Dependencies

If new packages are added to `requirements.txt`, simply run `run_chat.bat` again. It will install any missing dependencies automatically.

---

## Troubleshooting

### Python Not Found

Install Python 3.13 and ensure **Add Python to PATH** was enabled during installation.

---

### Missing Packages

Run `run_chat.bat` again. It will automatically install any missing dependencies.

---

### Model Not Loading

Verify that the entire `LLM` folder exists and contains all required model files.

---

## License

This project is provided for educational and personal use.

---

## Credits

Developed by **Harshit Singh Chauhan**.

If you find this project useful, consider giving it a ⭐ on GitHub.

## ⚠️ Disclaimer

This project is **very, very, very dumb** right now 😄.

Viper-1 is an early-stage local AI project that is still under development. Don't expect responses anywhere close to ChatGPT or other large commercial AI assistants.

Current limitations include:

* 🧠 Limited reasoning ability
* 🤖 Can make incorrect or nonsensical responses
* 💬 Small vocabulary and understanding compared to larger models
* 🚧 Many features are still work in progress
* ⚡ Performance depends on your hardware and the model being used

The goal of this project is to learn, experiment, and improve over time. Every update will make Viper-1 smarter than before.

If you encounter bugs or strange responses, feel free to open an issue or contribute to the project!

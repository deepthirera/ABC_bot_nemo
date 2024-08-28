
# Bot With Nemo GuardRails
This is an example LLM-based conversational application with guardrails build using NVIDIA's NemoGuardRails. The application uses llama3 LLM for implementing the chat.

Steps to run the app
- Install [ollama](https://ollama.com/download) in your local.
- `ollama run llama3:latest` to pull this llama3 to your local. All of your local models are automatically served on localhost:11434.
- Clone this app 
	- `git clone https://github.com/deepthirera/ABC_bot_nemo.git`
	- `cd ABC_bot_nemo`
- Following steps are for setting up python environment.
	- `python3 -m venv venv`
	- `source venv/bin/activate`
- Install the dependencies
	- `pip3 install -r requirements.txt`
- Presidio setup for PII masking 
	- `python3 -m spacy download en_core_web_lg`
- Run the app `nemoguardrails server`. Access it at http://0.0.0.0:8000/












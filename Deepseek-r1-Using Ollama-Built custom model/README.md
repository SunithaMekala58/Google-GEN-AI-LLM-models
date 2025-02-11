# Built Custom Model using Ollama - Deepseek-r1 LLM model:

## Using ollama to Run deepseek-r1:
## Prerequisites:
* Ensure you have ollama installed on your system. If not, you can install it by following the instructions on the official website.

## Check ollama Installation: (Run in Command Prompt)
* To verify that ollama is installed and working correctly, run:

ollama --version

* This should output the installed version of ollama. For example:
  
ollama version is 0.5.7

## Pull the deepseek-r1 Model:
* To download the deepseek-r1 model, execute:

ollama pull deepseek-r1

* This will retrieve the model from the registry, which may take some time depending on your internet speed.

## Run the deepseek-r1 Model:
* Once the model is pulled successfully, you can run it using:

ollama run deepseek-r1

* This will start the model and allow you to interact with it.

## Additional Commands:
* For more information on available commands, use:

ollama --help

## To list all installed models:

ollama list

## To remove a model:

ollama rm deepseek-r1

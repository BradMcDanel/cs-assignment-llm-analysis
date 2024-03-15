# Can LLMs Do My Homework?

## Requirements:
- Need an API key from OpenAI. Set your API key as an environment variable `OPENAI_API_KEY`.

## Usage:
- Example: `python main.py --assignment-folder assignments/food-webs/ --output-folder results/food-webs --model gpt-4-turbo-preview`

## TODO:
1. Switch to a diffing approach instead of asking the model to generate all files each generation
  - Not sure this is a good idea any more. Seems like its better to just retry multiple times rather than trying to fix the output.


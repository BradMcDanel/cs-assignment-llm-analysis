# Can LLMs Do My Homework?

## Requirements:
- Need an API key from OpenAI. Set your API key as an environment variable `OPENAI_API_KEY`.
  - Currently, the hardcoded model is gpt-4-turbo. I have yet to test it with other models.

## Usage:
- I ran `python main.py --assignment-folder assignments/food-webs/ --output-folder results/food-webs` to get current results. The output failed twice and then the third time it passed all tests without further generation.

## TODO:
1. Switch to a diffing approach instead of asking the model to generate all files each generation
  - Not sure this is a good idea any more. Seems like its better to just retry multiple times rather than trying to fix the output.


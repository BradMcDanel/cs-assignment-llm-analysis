#!/bin/bash

# Define the settings
NUM_EVALUATIONS=5
MODELS=("gpt-3.5-turbo" "gpt-4o" "claude-3-5-sonnet-20240620")
PROMPT_FILES=("prompts/level2.txt" "prompts/level4.txt")
EXCLUDE_NON_PDF=("true" "false")
EXCLUDE_TESTS=("true" "false")
INPUT_DIRS=("assignments/enigma" "assignments/food-webs" "assignments/spelling-bee" "assignments/wordle" "assignments/dna" "assignments/police-shootings")
BASE_OUTPUT_DIR="results"
SILENT=false

# Build the arguments string
MODELS_ARG=$(printf " %s" "${MODELS[@]}")
PROMPT_FILES_ARG=$(printf " %s" "${PROMPT_FILES[@]}")
EXCLUDE_NON_PDF_ARG=$(printf " %s" "${EXCLUDE_NON_PDF[@]}")
EXCLUDE_TESTS_ARG=$(printf " %s" "${EXCLUDE_TESTS[@]}")
INPUT_DIRS_ARG=$(printf " %s" "${INPUT_DIRS[@]}")

# Build the silent argument
SILENT_ARG=""
if [ "$SILENT" = true ]; then
  SILENT_ARG="--silent"
fi

# Run the batch_eval.py script with the specified settings
python batch_eval.py --num-evaluations $NUM_EVALUATIONS \
                     --models $MODELS_ARG \
                     --prompt-files $PROMPT_FILES_ARG \
                     --exclude-non-pdf $EXCLUDE_NON_PDF_ARG \
		     --exclude-tests $EXCLUDE_TESTS_ARG \
                     --input-dirs $INPUT_DIRS_ARG \
                     --base-output-dir $BASE_OUTPUT_DIR \
                     $SILENT_ARG


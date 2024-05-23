#!/bin/bash

# Define the settings
NUM_EVALUATIONS=3
MODELS=("gpt-3.5-turbo" "gpt-4o")
PROMPT_FILES=("prompts/level1.txt" "prompts/level4.txt")
EXCLUDE_NON_PDF=("false" "true")
INPUT_DIRS=("assignments/dna" "assignments/fatal-police-shootings" "assignments/food-webs" "assignments/spelling-bee" "assignments/wordle")
BASE_OUTPUT_DIR="results"
SILENT=false

# Build the arguments string
MODELS_ARG=$(printf " %s" "${MODELS[@]}")
PROMPT_FILES_ARG=$(printf " %s" "${PROMPT_FILES[@]}")
EXCLUDE_NON_PDF_ARG=$(printf " %s" "${EXCLUDE_NON_PDF[@]}")
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
                     --input-dirs $INPUT_DIRS_ARG \
                     --base-output-dir $BASE_OUTPUT_DIR \
                     $SILENT_ARG


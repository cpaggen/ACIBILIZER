#!/bin/bash

# Define input and output file paths
input_file="aci-meta-5.3-2c.json"
temp_file="temp_filtered.json"
output_file="filtered_output.json"

# Regex pattern to match lines to be removed
regex='[Cc]loud.*[^{]$'

# First awk command to filter out lines matching regex and save to temp file
awk '!$0 ~ regex' "$input_file" > "$temp_file"

# Second awk command to remove trailing commas before single }
awk '{
    if (NR > 1 && prev_line ~ /,$/ && $0 ~ /^}$/) {
        sub(/,$/, "", prev_line)
        printf "%s\n", prev_line
    } else {
        print
    }
    prev_line = $0
}' "$temp_file" > "$output_file"

# Clean up temporary file
rm "$temp_file"

echo "Filtered JSON saved to $output_file"

import re
import os
import sys

print("Starting build of master 34-topologies diagram engine...")

# Read existing senior-dotnet-interview-portal.html to get existing 19 custom layouts
with open('senior-dotnet-interview-portal.html', 'r', encoding='utf-8') as f:
    portal_content = f.read()

# Verify questions count
q_start = portal_content.find('const QUESTION_BANK = [')
print(f"Found QUESTION_BANK at index {q_start}")


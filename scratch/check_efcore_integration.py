import re
import os

with open('senior-dotnet-interview-portal.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Read portal file: {len(content)} characters, {len(content)/(1024*1024):.2f} MB")

# Check explorer-header location
idx_hdr = content.find('class="explorer-header"')
print(f"explorer-header found at: {idx_hdr}")

# Check mockCategorySelect
idx_mock = content.find('id="mockCategorySelect"')
print(f"mockCategorySelect found at: {idx_mock}")

# Check initCategoryNav
idx_nav = content.find('function initCategoryNav()')
print(f"initCategoryNav found at: {idx_nav}")

# Check applyFilters
idx_filter = content.find('function applyFilters()')
print(f"applyFilters found at: {idx_filter}")


import re
import os
import sys

print("Assembling complete 34-topologies diagram engine...")

with open('senior-dotnet-interview-portal.html', 'r', encoding='utf-8') as f:
    portal = f.read()

# Load batches 1, 2, 3
with open('scratch/test_batch1.js', 'r', encoding='utf-8') as f:
    batch1 = f.read()

with open('scratch/test_batch2.js', 'r', encoding='utf-8') as f:
    batch2 = f.read()

with open('scratch/test_batch3.js', 'r', encoding='utf-8') as f:
    batch3 = f.read()

# Extract the 19 existing custom layouts from portal
existing_funcs = [
  'renderOopClassLayout', 'renderEfCoreLayout', 'renderSqlEngineLayout', 'renderBTreeLayout',
  'renderAiRagLayout', 'renderCloudInfraLayout', 'renderDistributedLayout', 'renderPubSubLayout',
  'renderCacheTierLayout', 'renderMiddlewareLayout', 'renderSecurityLayout', 'renderTestingLayout',
  'renderJsRuntimeLayout', 'renderCycleLayout', 'renderMemoryLayout', 'renderBranchLayout',
  'renderFiberLayout', 'renderRibbonLayout', 'renderSdlcLayout'
]

extracted_layouts = []
for fn in existing_funcs:
    start_str = f"function {fn}("
    start = portal.find(start_str)
    if start == -1:
        print(f"Error: {fn} not found in portal!")
        sys.exit(1)
    next_fn = portal.find("\n    function ", start + 10)
    if next_fn == -1:
        print(f"Error: could not find end of {fn}")
        sys.exit(1)
    fn_code = portal[start:next_fn].strip()
    extracted_layouts.append(fn_code)

print(f"Extracted {len(extracted_layouts)} existing custom layouts.")

# Load header and renderPortalSVG
with open('scratch/build_comprehensive_diagram_engine.py', 'r', encoding='utf-8') as f:
    comp_py = f.read()

start_engine = comp_py.find("engine_code = r'''") + len("engine_code = r'''")
end_engine = comp_py.find("'''", start_engine)
header_and_classifier = comp_py[start_engine:end_engine].strip()

# Combine everything
full_engine_js = header_and_classifier + "\n\n"
full_engine_js += batch1 + "\n\n"
full_engine_js += batch2 + "\n\n"
full_engine_js += batch3 + "\n\n"

for ext in extracted_layouts:
    full_engine_js += "    " + ext + "\n\n"

full_engine_js += r'''
    QUESTION_BANK.forEach(q => {
      if (!q.diagram && q.diagramSteps) {
        q.diagram = renderPortalSVG(q);
      }
    });
'''

# Find boundaries in portal
marker_start = portal.find("    function escSvg(s) {")
marker_end = portal.find("    // User State stored in LocalStorage")

if marker_start == -1 or marker_end == -1:
    print(f"Could not find markers: marker_start={marker_start}, marker_end={marker_end}")
    sys.exit(1)

print(f"Replacing engine from {marker_start} to {marker_end} (length: {marker_end - marker_start})")

new_portal = portal[:marker_start] + full_engine_js + "\n    " + portal[marker_end:]

output_file = 'senior-dotnet-interview-portal.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(new_portal)

size_mb = os.path.getsize(output_file) / (1024 * 1024)
print(f"Successfully wrote {output_file} ({size_mb:.2f} MB)")


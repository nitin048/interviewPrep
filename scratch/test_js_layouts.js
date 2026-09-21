function esc(s) {
  if (!s) return '';
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// Let's test building the complete renderPortalSVG function
const testQ_memory = {
  id: 2706,
  q: "What is Boxing and Unboxing in C# and what happens in memory during boxing?",
  category: "csharp",
  categoryLabel: "C# Core",
  diagramTitle: "Boxing & Unboxing Memory Transition (Stack ➔ Heap)",
  diagramSteps: [
    ["STACK", "Value Type on Stack", "Primitive struct on stack frame"],
    ["ALLOC", "Heap Allocation", "box opcode allocates 16B on GC heap"],
    ["COPY", "Payload Byte Copy", "Copies bytes to heap payload field"],
    ["REF", "Heap Object Reference", "Stack holds reference pointer to boxed object"],
    ["UNBOX", "unbox.any & Restore", "Verifies type token and copies value back to Stack"]
  ]
};

const testQ_btree = {
  id: 3200,
  q: "What is a Clustered Index and how does the B-Tree leaf level store data?",
  category: "sql",
  categoryLabel: "SQL Server",
  diagramTitle: "B-Tree Clustered Index Topology & Page Allocation",
  diagramSteps: [
    ["ROOT", "Root Index Page", "Evaluates search key against root pointers"],
    ["BRANCH", "Intermediate Branch", "Navigates branch navigation pointers"],
    ["LEAF", "Leaf Level Node", "Locates exact row in clustered leaf data page"],
    ["BUFFER", "Buffer Pool Hit", "Reads 8KB page directly in RAM cache"]
  ]
};

console.log("Test question objects defined.");

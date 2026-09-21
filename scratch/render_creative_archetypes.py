import html

def esc(s):
    return html.escape(str(s or ''))

# 1. ARCH_MEMORY_STACK_HEAP
def render_memory_layout(title, cat_label, q):
    return f'''
    <svg viewBox="0 0 880 250" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0d131f; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(56, 189, 248, 0.25);">
      <defs>
        <linearGradient id="stackGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#0284c7" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="#0f172a" stop-opacity="0.85"/>
        </linearGradient>
        <linearGradient id="heapGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="#0f172a" stop-opacity="0.85"/>
        </linearGradient>
        <marker id="memArr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#38bdf8"/>
        </marker>
      </defs>
      
      <!-- Top Header -->
      <rect x="24" y="14" width="160" height="20" rx="4" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="1"/>
      <text x="104" y="28" text-anchor="middle" font-size="9" font-weight="800" fill="#38bdf8" font-family="monospace">💾 CLR MEMORY BLUEPRINT</text>
      <text x="196" y="29" font-size="12.5" font-weight="700" fill="#f8fafc" class="svg-title">{esc(title)}</text>
      
      <!-- LEFT PANEL: THREAD STACK -->
      <g transform="translate(24, 46)">
        <rect width="320" height="158" rx="8" fill="url(#stackGrad)" stroke="#38bdf8" stroke-width="1.4"/>
        <rect width="320" height="26" rx="8" fill="rgba(56, 189, 248, 0.15)"/>
        <text x="16" y="17" font-size="10" font-weight="800" fill="#38bdf8" font-family="system-ui">THREAD CALL STACK (Fast LIFO Frames)</text>
        <text x="304" y="17" text-anchor="end" font-size="8.5" fill="#94a3b8" font-family="monospace">0x7FFE_04A0</text>
        
        <!-- Stack Slot 1 -->
        <g transform="translate(14, 36)">
          <rect width="292" height="32" rx="5" fill="rgba(15, 23, 42, 0.75)" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1"/>
          <text x="12" y="20" font-size="9.5" font-weight="700" fill="#f8fafc">Local Frame: Value Types</text>
          <text x="150" y="20" font-size="8.5" fill="#94a3b8">Inline struct data</text>
          <text x="280" y="20" text-anchor="end" font-size="8.5" fill="#38bdf8" font-family="monospace">[4 / 8 Bytes]</text>
        </g>
        <!-- Stack Slot 2 (Reference Pointer) -->
        <g transform="translate(14, 76)">
          <rect width="292" height="34" rx="5" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1.3"/>
          <circle cx="20" cy="17" r="4" fill="#38bdf8"/>
          <text x="32" y="21" font-size="10" font-weight="800" fill="#38bdf8" font-family="monospace">ObjRef: 0x028A_FF10</text>
          <text x="280" y="21" text-anchor="end" font-size="8.5" fill="#94a3b8">64-bit Heap Ptr</text>
        </g>
        <!-- Stack Register Info -->
        <g transform="translate(14, 118)">
          <rect width="292" height="28" rx="4" fill="rgba(0, 0, 0, 0.3)"/>
          <text x="146" y="18" text-anchor="middle" font-size="8.5" fill="#94a3b8">Registers: <tspan fill="#38bdf8">RBP (Base Ptr)</tspan> | <tspan fill="#38bdf8">RSP (Stack Ptr)</tspan> — Zero GC Overhead</text>
        </g>
      </g>
      
      <!-- CENTER: POINTER CONNECTOR -->
      <path d="M 344 139 C 400 139, 440 95, 520 95" fill="none" stroke="#38bdf8" stroke-width="2.2" stroke-dasharray="4 3" marker-end="url(#memArr)"/>
      <rect x="388" y="104" width="88" height="20" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="432" y="117" text-anchor="middle" font-size="8" font-weight="800" fill="#38bdf8" font-family="monospace">HEAP REF</text>

      <!-- RIGHT PANEL: MANAGED HEAP -->
      <g transform="translate(520, 46)">
        <rect width="336" height="158" rx="8" fill="url(#heapGrad)" stroke="#8b5cf6" stroke-width="1.4"/>
        <rect width="336" height="26" rx="8" fill="rgba(139, 92, 246, 0.15)"/>
        <text x="16" y="17" font-size="10" font-weight="800" fill="#c084fc" font-family="system-ui">MANAGED GC HEAP (Tenured Allocations)</text>
        <text x="320" y="17" text-anchor="end" font-size="8.5" fill="#c084fc" font-family="monospace">GEN 0 / 1 / 2</text>
        
        <!-- Heap Object Header -->
        <g transform="translate(14, 36)">
          <rect width="308" height="66" rx="5" fill="rgba(15, 23, 42, 0.85)" stroke="#8b5cf6" stroke-width="1.2"/>
          <rect x="8" y="8" width="138" height="22" rx="3" fill="rgba(139, 92, 246, 0.2)"/>
          <text x="77" y="22" text-anchor="middle" font-size="8.5" font-weight="700" fill="#c084fc" font-family="monospace">SyncBlock (4B)</text>
          <rect x="154" y="8" width="146" height="22" rx="3" fill="rgba(56, 189, 248, 0.2)"/>
          <text x="227" y="22" text-anchor="middle" font-size="8.5" font-weight="700" fill="#38bdf8" font-family="monospace">TypeHandle (8B)</text>
          
          <text x="154" y="50" text-anchor="middle" font-size="9" fill="#f8fafc">Instance Fields &amp; Payload Bytes in RAM</text>
        </g>
        <!-- GC Generation Indicator -->
        <g transform="translate(14, 110)">
          <rect width="308" height="36" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="14" y="16" font-size="8" font-weight="700" fill="#94a3b8">GC ALLOCATION ZONE:</text>
          <rect x="14" y="22" width="70" height="8" rx="2" fill="#10b981"/>
          <rect x="90" y="22" width="70" height="8" rx="2" fill="#38bdf8"/>
          <rect x="166" y="22" width="70" height="8" rx="2" fill="#8b5cf6"/>
          <rect x="242" y="22" width="56" height="8" rx="2" fill="#f59e0b"/>
          <text x="154" y="32" text-anchor="middle" font-size="6.5" fill="#f8fafc" font-family="monospace">Gen 0 (Ephemeral) ➔ Gen 1 (Survivor) ➔ Gen 2 (Tenured) ➔ LOH</text>
        </g>
      </g>
      
      <!-- Footer Note -->
      <g transform="translate(24, 214)">
        <rect width="832" height="24" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="416" y="16" text-anchor="middle" font-size="9" fill="#38bdf8" font-family="system-ui">
          🧠 Memory Invariant: Value types store state directly on stack; Reference types allocate 24B+ heap header with 8-byte pointer reference.
        </text>
      </g>
    </svg>
    '''

print("Sample memory layout rendered.")

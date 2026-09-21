function esc(s) {
  if (!s) return '';
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function renderPortalSVG(q) {
  if (!q) return '';
  const title = q.diagramTitle || (q.categoryLabel ? `${q.categoryLabel}: ${q.q}` : q.q);
  const steps = q.diagramSteps || [];
  const tLow = (q.q || '').toLowerCase();
  const cat = (q.category || '').toLowerCase();
  const cleanTitle = esc(title);

  // Determine Creative Architectural Layout
  let layout = 'enterprise';
  
  if (anyIn(tLow, ['box', 'unbox', 'stack vs heap', 'stack and heap', 'value type', 'reference type', 'garbage collector', 'gc', 'generation', 'gen 0', 'gen 1', 'gen 2', 'loh', 'poh', 'managed code', 'unmanaged', 'span<t>', 'ref struct', 'stringbuilder', 'immutab', 'memory layout'])) {
    layout = 'memory';
  } else if (anyIn(tLow, ['b-tree', 'clustered index', 'non-clustered', 'index seek', 'index scan', 'page split', 'fill factor', 'expression tree', 'ast '])) {
    layout = 'btree';
  } else if (anyIn(tLow, ['middleware', 'pipeline', 'kestrel', 'action filter', 'request delegate', 'http request', 'routing'])) {
    layout = 'middleware';
  } else if (cat === 'redux' || anyIn(tLow, ['redux', 'event loop', 'microtask', 'unidirectional', 'tdd', 'cycle', 'circular'])) {
    layout = 'cycle';
  } else if (anyIn(tLow, ['microservice', 'outbox', 'kafka', 'rabbitmq', 'cdc', 'debezium', 'cqrs', 'event sourcing', 'saga', 'distributed'])) {
    layout = 'distributed';
  } else if (cat === 'async' || anyIn(tLow, ['async', 'await', 'state machine', 'task', 'movenext', 'threadpool', 'channel', 'cancellation'])) {
    layout = 'async';
  } else if (anyIn(tLow, ['cache', 'redis', 'circuit breaker', 'tryparse', 'deadlock', 'branch', 'polly', 'if/else', 'switch', 'fallback'])) {
    layout = 'branch';
  } else if (cat === 'react' || anyIn(tLow, ['fiber', 'virtual dom', 'reconciliation', 'reconcil', 'react', 'hooks', 'useeffect'])) {
    layout = 'fiber';
  } else if (cat === 'coding' || anyIn(tLow, ['pointer', 'binary search', 'sliding window', 'array', 'subsequence', 'two sum', 'leetcode'])) {
    layout = 'ribbon';
  }

  const w = 880;
  const h = 250;

  // Render specific layout
  if (layout === 'memory') return renderMemoryLayout(q, cleanTitle, steps, w, h);
  if (layout === 'btree') return renderBTreeLayout(q, cleanTitle, steps, w, h);
  if (layout === 'middleware') return renderMiddlewareLayout(q, cleanTitle, steps, w, h);
  if (layout === 'cycle') return renderCycleLayout(q, cleanTitle, steps, w, h);
  if (layout === 'distributed') return renderDistributedLayout(q, cleanTitle, steps, w, h);
  if (layout === 'async') return renderAsyncLayout(q, cleanTitle, steps, w, h);
  if (layout === 'branch') return renderBranchLayout(q, cleanTitle, steps, w, h);
  if (layout === 'fiber') return renderFiberLayout(q, cleanTitle, steps, w, h);
  if (layout === 'ribbon') return renderRibbonLayout(q, cleanTitle, steps, w, h);
  return renderEnterpriseLayout(q, cleanTitle, steps, w, h);
}

function anyIn(text, terms) {
  for (let i = 0; i < terms.length; i++) {
    if (text.includes(terms[i])) return true;
  }
  return false;
}

// 1. MEMORY LAYOUT (Stack vs Heap Blueprint)
function renderMemoryLayout(q, title, steps, w, h) {
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(56, 189, 248, 0.3);">
      <defs>
        <linearGradient id="memStackGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#0284c7" stop-opacity="0.28"/>
          <stop offset="100%" stop-color="#0f172a" stop-opacity="0.95"/>
        </linearGradient>
        <linearGradient id="memHeapGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.28"/>
          <stop offset="100%" stop-color="#0f172a" stop-opacity="0.95"/>
        </linearGradient>
        <marker id="memPtrArr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#38bdf8"/>
        </marker>
      </defs>
      
      <!-- Top Header -->
      <rect x="24" y="14" width="165" height="22" rx="4" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="106" y="29" text-anchor="middle" font-size="9" font-weight="800" fill="#38bdf8" font-family="monospace">💾 CLR MEMORY BLUEPRINT</text>
      <text x="202" y="30" font-size="13" font-weight="700" fill="#f8fafc" class="svg-title">${title}</text>
      
      <!-- LEFT PANEL: THREAD STACK -->
      <g transform="translate(24, 48)">
        <rect width="330" height="155" rx="8" fill="url(#memStackGrad)" stroke="#38bdf8" stroke-width="1.4"/>
        <rect width="330" height="26" rx="8" fill="rgba(56, 189, 248, 0.15)"/>
        <text x="14" y="18" font-size="10" font-weight="800" fill="#38bdf8" font-family="system-ui">THREAD CALL STACK (Fast LIFO Frames)</text>
        <text x="316" y="18" text-anchor="end" font-size="8.5" fill="#94a3b8" font-family="monospace">0x7FFE_04A0</text>
        
        <g transform="translate(12, 36)">
          <rect width="306" height="32" rx="5" fill="rgba(15, 23, 42, 0.75)" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1"/>
          <text x="12" y="20" font-size="10" font-weight="700" fill="#f8fafc">Local Frame: Value Types</text>
          <text x="175" y="20" font-size="9" fill="#94a3b8">Inline struct data</text>
          <text x="296" y="20" text-anchor="end" font-size="9" fill="#38bdf8" font-family="monospace">[4 / 8 B]</text>
        </g>
        
        <g transform="translate(12, 76)">
          <rect width="306" height="34" rx="5" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1.3"/>
          <circle cx="20" cy="17" r="4" fill="#38bdf8"/>
          <text x="32" y="21" font-size="10" font-weight="800" fill="#38bdf8" font-family="monospace">ObjRef: 0x028A_FF10</text>
          <text x="296" y="21" text-anchor="end" font-size="9" fill="#94a3b8">64-bit Heap Ptr</text>
        </g>
        
        <g transform="translate(12, 118)">
          <rect width="306" height="26" rx="4" fill="rgba(0, 0, 0, 0.35)"/>
          <text x="153" y="17" text-anchor="middle" font-size="8.5" fill="#94a3b8">Registers: <tspan fill="#38bdf8" font-weight="700">RBP (Base Ptr)</tspan> | <tspan fill="#38bdf8" font-weight="700">RSP (Stack Ptr)</tspan> — Zero GC Overhead</text>
        </g>
      </g>
      
      <!-- CENTER: POINTER CONNECTOR -->
      <path d="M 354 142 C 410 142, 450 96, 524 96" fill="none" stroke="#38bdf8" stroke-width="2.2" stroke-dasharray="4 3" marker-end="url(#memPtrArr)"/>
      <rect x="400" y="106" width="80" height="20" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="440" y="119" text-anchor="middle" font-size="8" font-weight="800" fill="#38bdf8" font-family="monospace">HEAP REF</text>

      <!-- RIGHT PANEL: MANAGED HEAP -->
      <g transform="translate(524, 48)">
        <rect width="332" height="155" rx="8" fill="url(#memHeapGrad)" stroke="#8b5cf6" stroke-width="1.4"/>
        <rect width="332" height="26" rx="8" fill="rgba(139, 92, 246, 0.15)"/>
        <text x="14" y="18" font-size="10" font-weight="800" fill="#c084fc" font-family="system-ui">MANAGED GC HEAP (Tenured Allocations)</text>
        <text x="318" y="18" text-anchor="end" font-size="8.5" fill="#c084fc" font-family="monospace">GEN 0 / 1 / 2</text>
        
        <g transform="translate(12, 36)">
          <rect width="308" height="66" rx="5" fill="rgba(15, 23, 42, 0.85)" stroke="#8b5cf6" stroke-width="1.2"/>
          <rect x="8" y="8" width="138" height="22" rx="3" fill="rgba(139, 92, 246, 0.2)"/>
          <text x="77" y="22" text-anchor="middle" font-size="9" font-weight="700" fill="#c084fc" font-family="monospace">SyncBlock (4B)</text>
          <rect x="154" y="8" width="146" height="22" rx="3" fill="rgba(56, 189, 248, 0.2)"/>
          <text x="227" y="22" text-anchor="middle" font-size="9" font-weight="700" fill="#38bdf8" font-family="monospace">TypeHandle (8B)</text>
          <text x="154" y="50" text-anchor="middle" font-size="9.5" fill="#f8fafc">Instance Fields &amp; Payload Bytes in RAM</text>
        </g>
        
        <g transform="translate(12, 110)">
          <rect width="308" height="34" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="14" y="14" font-size="8" font-weight="700" fill="#94a3b8">GC ALLOCATION ZONE:</text>
          <rect x="14" y="20" width="70" height="8" rx="2" fill="#10b981"/>
          <rect x="90" y="20" width="70" height="8" rx="2" fill="#38bdf8"/>
          <rect x="166" y="20" width="70" height="8" rx="2" fill="#8b5cf6"/>
          <rect x="242" y="20" width="56" height="8" rx="2" fill="#f59e0b"/>
          <text x="154" y="30" text-anchor="middle" font-size="6.5" fill="#f8fafc" font-family="monospace">Gen 0 (Ephemeral) ➔ Gen 1 (Survivor) ➔ Gen 2 (Tenured) ➔ LOH</text>
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
  `;
}

// 2. BTREE LAYOUT (Hierarchical Index Topology)
function renderBTreeLayout(q, title, steps, w, h) {
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(16, 185, 129, 0.3);">
      <defs>
        <linearGradient id="btreeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#059669" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="#0f172a" stop-opacity="0.95"/>
        </linearGradient>
      </defs>
      
      <!-- Top Header -->
      <rect x="24" y="14" width="165" height="22" rx="4" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1.2"/>
      <text x="106" y="29" text-anchor="middle" font-size="9" font-weight="800" fill="#10b981" font-family="monospace">🗄️ B-TREE INDEX TOPOLOGY</text>
      <text x="202" y="30" font-size="13" font-weight="700" fill="#f8fafc" class="svg-title">${title}</text>
      
      <!-- LEVEL 1: ROOT NODE -->
      <g transform="translate(300, 48)">
        <rect width="280" height="42" rx="6" fill="url(#btreeGrad)" stroke="#10b981" stroke-width="1.4"/>
        <text x="14" y="17" font-size="8.5" font-weight="800" fill="#10b981" font-family="monospace">ROOT INDEX NODE (Page #102)</text>
        <rect x="12" y="22" width="80" height="15" rx="3" fill="rgba(0,0,0,0.4)"/>
        <text x="52" y="33" text-anchor="middle" font-size="8.5" fill="#38bdf8" font-family="monospace">Key &lt; 100</text>
        <rect x="100" y="22" width="80" height="15" rx="3" fill="rgba(0,0,0,0.4)"/>
        <text x="140" y="33" text-anchor="middle" font-size="8.5" fill="#10b981" font-family="monospace">100..499</text>
        <rect x="188" y="22" width="80" height="15" rx="3" fill="rgba(0,0,0,0.4)"/>
        <text x="228" y="33" text-anchor="middle" font-size="8.5" fill="#f59e0b" font-family="monospace">Key &gt;= 500</text>
      </g>
      
      <!-- Connectors: Root to Branches -->
      <line x1="390" y1="90" x2="260" y2="108" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 2"/>
      <line x1="490" y1="90" x2="620" y2="108" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 2"/>

      <!-- LEVEL 2: INTERMEDIATE BRANCHES -->
      <g transform="translate(140, 108)">
        <rect width="240" height="40" rx="6" fill="rgba(15, 23, 42, 0.85)" stroke="#10b981" stroke-width="1.2"/>
        <text x="12" y="16" font-size="8" font-weight="800" fill="#10b981" font-family="monospace">BRANCH (Page #204) [Keys 10..99]</text>
        <text x="120" y="32" text-anchor="middle" font-size="8.5" fill="#94a3b8">Branch Page Pointers ➔ Child Ptrs</text>
      </g>
      
      <g transform="translate(500, 108)">
        <rect width="240" height="40" rx="6" fill="rgba(15, 23, 42, 0.85)" stroke="#10b981" stroke-width="1.2"/>
        <text x="12" y="16" font-size="8" font-weight="800" fill="#10b981" font-family="monospace">BRANCH (Page #205) [Keys 100..499]</text>
        <text x="120" y="32" text-anchor="middle" font-size="8.5" fill="#94a3b8">Branch Page Pointers ➔ Child Ptrs</text>
      </g>
      
      <!-- Connectors: Branches to Leaves -->
      <line x1="200" y1="148" x2="140" y2="164" stroke="#10b981" stroke-width="1.2"/>
      <line x1="320" y1="148" x2="380" y2="164" stroke="#10b981" stroke-width="1.2"/>
      <line x1="560" y1="148" x2="520" y2="164" stroke="#10b981" stroke-width="1.2"/>
      <line x1="680" y1="148" x2="740" y2="164" stroke="#10b981" stroke-width="1.2"/>

      <!-- LEVEL 3: LEAF LEVEL DATA PAGES -->
      <g transform="translate(40, 164)">
        <rect width="220" height="42" rx="5" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1.2"/>
        <text x="10" y="16" font-size="8" font-weight="800" fill="#38bdf8" font-family="monospace">LEAF PAGE #801 [Keys 10..49]</text>
        <text x="110" y="32" text-anchor="middle" font-size="8" fill="#f8fafc">8KB Page: Rows / Bookmark RID</text>
      </g>
      
      <g transform="translate(280, 164)">
        <rect width="200" height="42" rx="5" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1.2"/>
        <text x="10" y="16" font-size="8" font-weight="800" fill="#38bdf8" font-family="monospace">LEAF PAGE #802 [Keys 50..99]</text>
        <text x="100" y="32" text-anchor="middle" font-size="8" fill="#f8fafc">8KB Page: Rows / Bookmark RID</text>
      </g>
      
      <g transform="translate(500, 164)">
        <rect width="200" height="42" rx="5" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1.2"/>
        <text x="10" y="16" font-size="8" font-weight="800" fill="#38bdf8" font-family="monospace">LEAF PAGE #803 [Keys 100..299]</text>
        <text x="100" y="32" text-anchor="middle" font-size="8" fill="#f8fafc">8KB Page: Rows / Bookmark RID</text>
      </g>
      
      <!-- Right: Buffer Pool Callout -->
      <g transform="translate(720, 164)">
        <rect width="136" height="42" rx="5" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1.2"/>
        <text x="68" y="18" text-anchor="middle" font-size="8" font-weight="800" fill="#10b981" font-family="monospace">BUFFER POOL</text>
        <text x="68" y="32" text-anchor="middle" font-size="8.5" fill="#34d399">RAM Cache HIT 99.8%</text>
      </g>

      <!-- Footer Invariant -->
      <g transform="translate(24, 218)">
        <rect width="832" height="22" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="416" y="15" text-anchor="middle" font-size="9" fill="#10b981" font-family="system-ui">
          ⚡ Storage Invariant: Clustered Index Leaf IS the Data; Non-Clustered Index Leaf stores Bookmark pointer to Heap or Clustered Key.
        </text>
      </g>
    </svg>
  `;
}

// 3. MIDDLEWARE PIPELINE (Bidirectional Russian-Doll Onion Pipeline)
function renderMiddlewareLayout(q, title, steps, w, h) {
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(6, 182, 212, 0.3);">
      <defs>
        <marker id="pipeArrFwd" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#06b6d4"/>
        </marker>
        <marker id="pipeArrBack" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#10b981"/>
        </marker>
      </defs>
      
      <!-- Top Header -->
      <rect x="24" y="14" width="180" height="22" rx="4" fill="rgba(6, 182, 212, 0.15)" stroke="#06b6d4" stroke-width="1.2"/>
      <text x="114" y="29" text-anchor="middle" font-size="9" font-weight="800" fill="#06b6d4" font-family="monospace">⚡ HTTP MIDDLEWARE PIPELINE</text>
      <text x="216" y="30" font-size="13" font-weight="700" fill="#f8fafc" class="svg-title">${title}</text>
      
      <!-- INBOUND FLOW LABEL -->
      <text x="36" y="58" font-size="9" font-weight="800" fill="#06b6d4" font-family="monospace">➔ INBOUND HTTP REQUEST FLOW</text>
      
      <!-- 4 Layered Middleware Cards in a Pipeline -->
      <g transform="translate(24, 68)">
        <!-- Layer 1: Exception / Diagnostics -->
        <g transform="translate(0, 0)">
          <rect width="190" height="88" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#06b6d4" stroke-width="1.3"/>
          <rect width="190" height="20" rx="7" fill="rgba(6, 182, 212, 0.15)"/>
          <text x="10" y="14" font-size="8.5" font-weight="800" fill="#06b6d4" font-family="monospace">01: EXCEPTION / DIAG</text>
          <text x="95" y="38" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">ExceptionHandler</text>
          <text x="95" y="54" text-anchor="middle" font-size="8.5" fill="#94a3b8">ProblemDetails RFC 7807</text>
          <text x="95" y="72" text-anchor="middle" font-size="8" fill="#06b6d4" font-family="monospace">next(context)</text>
        </g>
        <line x1="192" y1="44" x2="212" y2="44" stroke="#06b6d4" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#pipeArrFwd)"/>

        <!-- Layer 2: Auth & Security -->
        <g transform="translate(214, 0)">
          <rect width="190" height="88" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1.3"/>
          <rect width="190" height="20" rx="7" fill="rgba(56, 189, 248, 0.15)"/>
          <text x="10" y="14" font-size="8.5" font-weight="800" fill="#38bdf8" font-family="monospace">02: AUTH &amp; SECURITY</text>
          <text x="95" y="38" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">Authentication / CORS</text>
          <text x="95" y="54" text-anchor="middle" font-size="8.5" fill="#94a3b8">Validates JWT Bearer Token</text>
          <text x="95" y="72" text-anchor="middle" font-size="8" fill="#38bdf8" font-family="monospace">ClaimsPrincipal</text>
        </g>
        <line x1="406" y1="44" x2="426" y2="44" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#pipeArrFwd)"/>

        <!-- Layer 3: Routing & Filters -->
        <g transform="translate(428, 0)">
          <rect width="190" height="88" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#8b5cf6" stroke-width="1.3"/>
          <rect width="190" height="20" rx="7" fill="rgba(139, 92, 246, 0.15)"/>
          <text x="10" y="14" font-size="8.5" font-weight="800" fill="#c084fc" font-family="monospace">03: ROUTING &amp; FILTERS</text>
          <text x="95" y="38" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">Endpoint Routing</text>
          <text x="95" y="54" text-anchor="middle" font-size="8.5" fill="#94a3b8">Action Filters &amp; Binding</text>
          <text x="95" y="72" text-anchor="middle" font-size="8" fill="#c084fc" font-family="monospace">ModelState.IsValid</text>
        </g>
        <line x1="620" y1="44" x2="640" y2="44" stroke="#8b5cf6" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#pipeArrFwd)"/>

        <!-- Layer 4: Action Execution / Minimal API -->
        <g transform="translate(642, 0)">
          <rect width="190" height="88" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#10b981" stroke-width="1.4"/>
          <rect width="190" height="20" rx="7" fill="rgba(16, 185, 129, 0.15)"/>
          <text x="10" y="14" font-size="8.5" font-weight="800" fill="#10b981" font-family="monospace">04: ENDPOINT EXECUTION</text>
          <text x="95" y="38" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">Controller / MapGet</text>
          <text x="95" y="54" text-anchor="middle" font-size="8.5" fill="#94a3b8">Business Logic Execution</text>
          <text x="95" y="72" text-anchor="middle" font-size="8" fill="#10b981" font-family="monospace">Results.Ok(DTO)</text>
        </g>
      </g>
      
      <!-- OUTBOUND RETURN ARROW (Reverse Unwind) -->
      <g transform="translate(24, 172)">
        <rect width="832" height="34" rx="6" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1"/>
        <line x1="790" y1="17" x2="40" y2="17" stroke="#10b981" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#pipeArrBack)"/>
        <text x="416" y="21" text-anchor="middle" font-size="9" font-weight="800" fill="#10b981" font-family="system-ui">
          ⬅ OUTBOUND RESPONSE UNWIND (HTTP 200 OK — Formatters, Compression &amp; Socket Streaming)
        </text>
      </g>
      
      <!-- Footer Invariant -->
      <g transform="translate(24, 218)">
        <rect width="832" height="22" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="416" y="15" text-anchor="middle" font-size="9" fill="#06b6d4" font-family="system-ui">
          🔄 Pipeline Invariant: Middlewares execute in registered order on Request, and in exact REVERSE order on Response.
        </text>
      </g>
    </svg>
  `;
}

// 4. CYCLOTRON / UNIDIRECTIONAL LOOP (Redux & Event Loop)
function renderCycleLayout(q, title, steps, w, h) {
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(139, 92, 246, 0.3);">
      <defs>
        <marker id="cycleArr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#c084fc"/>
        </marker>
      </defs>
      
      <!-- Top Header -->
      <rect x="24" y="14" width="185" height="22" rx="4" fill="rgba(139, 92, 246, 0.15)" stroke="#8b5cf6" stroke-width="1.2"/>
      <text x="116" y="29" text-anchor="middle" font-size="9" font-weight="800" fill="#c084fc" font-family="monospace">🔄 UNIDIRECTIONAL STATE CYCLE</text>
      <text x="220" y="30" font-size="13" font-weight="700" fill="#f8fafc" class="svg-title">${title}</text>
      
      <!-- 4 Orbital Stations -->
      <!-- Station 1: VIEW (Top Center) -->
      <g transform="translate(340, 48)">
        <rect width="200" height="42" rx="6" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1.3"/>
        <text x="100" y="18" text-anchor="middle" font-size="9" font-weight="800" fill="#38bdf8" font-family="monospace">1. UI VIEW COMPONENT</text>
        <text x="100" y="33" text-anchor="middle" font-size="8.5" fill="#f8fafc">User Action triggers dispatch()</text>
      </g>
      
      <!-- Curve 1: View to Action -->
      <path d="M 540 69 C 640 69, 700 90, 700 120" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#cycleArr)"/>

      <!-- Station 2: ACTION & MIDDLEWARE (Right) -->
      <g transform="translate(600, 110)">
        <rect width="200" height="44" rx="6" fill="rgba(15, 23, 42, 0.85)" stroke="#8b5cf6" stroke-width="1.3"/>
        <text x="100" y="18" text-anchor="middle" font-size="9" font-weight="800" fill="#c084fc" font-family="monospace">2. ACTION &amp; THUNK</text>
        <text x="100" y="33" text-anchor="middle" font-size="8.5" fill="#f8fafc">{ type: 'ORDER_SUBMIT' }</text>
      </g>
      
      <!-- Curve 2: Action to Reducer -->
      <path d="M 700 154 C 700 185, 620 195, 540 195" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#cycleArr)"/>

      <!-- Station 3: REDUCER (Bottom Center) -->
      <g transform="translate(340, 168)">
        <rect width="200" height="42" rx="6" fill="rgba(15, 23, 42, 0.85)" stroke="#10b981" stroke-width="1.3"/>
        <text x="100" y="18" text-anchor="middle" font-size="9" font-weight="800" fill="#10b981" font-family="monospace">3. PURE REDUCER</text>
        <text x="100" y="33" text-anchor="middle" font-size="8.5" fill="#f8fafc">(prevState, action) ➔ nextState</text>
      </g>
      
      <!-- Curve 3: Reducer to Store -->
      <path d="M 340 195 C 260 195, 180 185, 180 154" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#cycleArr)"/>

      <!-- Station 4: STORE (Left) -->
      <g transform="translate(80, 110)">
        <rect width="200" height="44" rx="6" fill="rgba(15, 23, 42, 0.85)" stroke="#f59e0b" stroke-width="1.3"/>
        <text x="100" y="18" text-anchor="middle" font-size="9" font-weight="800" fill="#fbbf24" font-family="monospace">4. IMMUTABLE STORE</text>
        <text x="100" y="33" text-anchor="middle" font-size="8.5" fill="#f8fafc">Single Source of Truth</text>
      </g>
      
      <!-- Curve 4: Store to View -->
      <path d="M 180 110 C 180 80, 240 69, 340 69" fill="none" stroke="#c084fc" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#cycleArr)"/>

      <!-- Central Orb -->
      <circle cx="440" cy="132" r="30" fill="rgba(139, 92, 246, 0.12)" stroke="#8b5cf6" stroke-width="1.5"/>
      <text x="440" y="132" text-anchor="middle" font-size="7.5" font-weight="800" fill="#c084fc" font-family="monospace">REDUX</text>
      <text x="440" y="142" text-anchor="middle" font-size="6.5" fill="#94a3b8">HUB</text>

      <!-- Footer Invariant -->
      <g transform="translate(24, 218)">
        <rect width="832" height="22" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="416" y="15" text-anchor="middle" font-size="9" fill="#c084fc" font-family="system-ui">
          🔄 Unidirectional Invariant: State is strictly read-only; components never mutate store directly, eliminating race conditions.
        </text>
      </g>
    </svg>
  `;
}

// 5. DISTRIBUTED MICROSERVICES & OUTBOX (Multi-Lane Event Streaming)
function renderDistributedLayout(q, title, steps, w, h) {
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(168, 85, 247, 0.3);">
      <defs>
        <marker id="distArr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#a855f7"/>
        </marker>
      </defs>
      
      <rect x="24" y="14" width="185" height="22" rx="4" fill="rgba(168, 85, 247, 0.15)" stroke="#a855f7" stroke-width="1.2"/>
      <text x="116" y="29" text-anchor="middle" font-size="9" font-weight="800" fill="#c084fc" font-family="monospace">📦 DISTRIBUTED EVENT STREAM</text>
      <text x="220" y="30" font-size="13" font-weight="700" fill="#f8fafc" class="svg-title">${title}</text>
      
      <!-- 4 Distributed Nodes -->
      <g transform="translate(24, 60)">
        <!-- Node 1: Publisher Service -->
        <g transform="translate(0, 0)">
          <rect width="180" height="142" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1.3"/>
          <rect width="180" height="24" rx="7" fill="rgba(56, 189, 248, 0.15)"/>
          <text x="10" y="16" font-size="8.5" font-weight="800" fill="#38bdf8" font-family="monospace">SERVICE A (PUBLISHER)</text>
          <text x="90" y="48" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">Order Management</text>
          <text x="90" y="66" text-anchor="middle" font-size="8.5" fill="#94a3b8">Executes Command</text>
          <rect x="15" y="80" width="150" height="26" rx="4" fill="rgba(0,0,0,0.3)"/>
          <text x="90" y="96" text-anchor="middle" font-size="8" fill="#38bdf8" font-family="monospace">Local DB Tx Commit</text>
          <rect x="15" y="112" width="150" height="20" rx="3" fill="rgba(56, 189, 248, 0.1)"/>
          <text x="90" y="125" text-anchor="middle" font-size="7.5" fill="#38bdf8">Outbox Pattern Record</text>
        </g>
        <line x1="182" y1="71" x2="214" y2="71" stroke="#a855f7" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#distArr)"/>

        <!-- Node 2: Outbox & CDC Relay -->
        <g transform="translate(218, 0)">
          <rect width="185" height="142" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#a855f7" stroke-width="1.3"/>
          <rect width="185" height="24" rx="7" fill="rgba(168, 85, 247, 0.15)"/>
          <text x="10" y="16" font-size="8.5" font-weight="800" fill="#c084fc" font-family="monospace">CDC LOG MINER</text>
          <text x="92" y="48" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">Debezium / Outbox</text>
          <text x="92" y="66" text-anchor="middle" font-size="8.5" fill="#94a3b8">Reads DB WAL Log</text>
          <rect x="15" y="80" width="155" height="26" rx="4" fill="rgba(0,0,0,0.3)"/>
          <text x="92" y="96" text-anchor="middle" font-size="8" fill="#c084fc" font-family="monospace">Zero-Lag Polling</text>
          <rect x="15" y="112" width="155" height="20" rx="3" fill="rgba(168, 85, 247, 0.1)"/>
          <text x="92" y="125" text-anchor="middle" font-size="7.5" fill="#c084fc">Guarantees At-Least-Once</text>
        </g>
        <line x1="405" y1="71" x2="437" y2="71" stroke="#a855f7" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#distArr)"/>

        <!-- Node 3: Kafka Message Broker -->
        <g transform="translate(441, 0)">
          <rect width="190" height="142" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#ec4899" stroke-width="1.3"/>
          <rect width="190" height="24" rx="7" fill="rgba(236, 72, 153, 0.15)"/>
          <text x="10" y="16" font-size="8.5" font-weight="800" fill="#f472b6" font-family="monospace">KAFKA EVENT BROKER</text>
          <text x="95" y="48" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">Topic: order-events</text>
          <text x="95" y="66" text-anchor="middle" font-size="8.5" fill="#94a3b8">Partitioned High IOPS</text>
          <rect x="15" y="80" width="160" height="26" rx="4" fill="rgba(0,0,0,0.3)"/>
          <text x="95" y="96" text-anchor="middle" font-size="8" fill="#f472b6" font-family="monospace">[P0: 1042] [P1: 981]</text>
          <rect x="15" y="112" width="160" height="20" rx="3" fill="rgba(236, 72, 153, 0.1)"/>
          <text x="95" y="125" text-anchor="middle" font-size="7.5" fill="#f472b6">Ordered Partition Stream</text>
        </g>
        <line x1="633" y1="71" x2="665" y2="71" stroke="#a855f7" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#distArr)"/>

        <!-- Node 4: Consumer Service -->
        <g transform="translate(669, 0)">
          <rect width="163" height="142" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#10b981" stroke-width="1.3"/>
          <rect width="163" height="24" rx="7" fill="rgba(16, 185, 129, 0.15)"/>
          <text x="10" y="16" font-size="8.5" font-weight="800" fill="#10b981" font-family="monospace">CONSUMER B</text>
          <text x="81" y="48" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">Payment Service</text>
          <text x="81" y="66" text-anchor="middle" font-size="8.5" fill="#94a3b8">Consumer Group</text>
          <rect x="12" y="80" width="139" height="26" rx="4" fill="rgba(0,0,0,0.3)"/>
          <text x="81" y="96" text-anchor="middle" font-size="8" fill="#10b981" font-family="monospace">Idempotent Process</text>
          <rect x="12" y="112" width="139" height="20" rx="3" fill="rgba(16, 185, 129, 0.1)"/>
          <text x="81" y="125" text-anchor="middle" font-size="7.5" fill="#10b981">Commit Offset Ack</text>
        </g>
      </g>
      
      <!-- Footer Invariant -->
      <g transform="translate(24, 218)">
        <rect width="832" height="22" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="416" y="15" text-anchor="middle" font-size="9" fill="#a855f7" font-family="system-ui">
          📦 Distributed Invariant: Transactional Outbox eliminates dual-write failures; CDC guarantees event publication even during crashes.
        </text>
      </g>
    </svg>
  `;
}

// 6. ASYNC STATE MACHINE
function renderAsyncLayout(q, title, steps, w, h) {
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(245, 158, 11, 0.3);">
      <defs>
        <marker id="asyncArr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#f59e0b"/>
        </marker>
      </defs>
      
      <rect x="24" y="14" width="195" height="22" rx="4" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="1.2"/>
      <text x="121" y="29" text-anchor="middle" font-size="9" font-weight="800" fill="#fbbf24" font-family="monospace">⚡ ASYNC COMPILER STATE MACHINE</text>
      <text x="230" y="30" font-size="13" font-weight="700" fill="#f8fafc" class="svg-title">${title}</text>
      
      <!-- 4 State Machine Transition Cards -->
      <g transform="translate(24, 60)">
        <!-- Step 1: Initial Call -->
        <g transform="translate(0, 0)">
          <rect width="190" height="142" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1.3"/>
          <rect width="190" height="22" rx="7" fill="rgba(56, 189, 248, 0.15)"/>
          <text x="10" y="15" font-size="8.5" font-weight="800" fill="#38bdf8" font-family="monospace">STATE 0: INITIAL CALL</text>
          <text x="95" y="46" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">Caller Invocation</text>
          <text x="95" y="64" text-anchor="middle" font-size="8.5" fill="#94a3b8">Evaluates task.IsCompleted</text>
          <rect x="15" y="80" width="160" height="26" rx="4" fill="rgba(0,0,0,0.35)"/>
          <text x="95" y="96" text-anchor="middle" font-size="8" fill="#38bdf8" font-family="monospace">Fast Path (Synchronous)</text>
          <rect x="15" y="112" width="160" height="20" rx="3" fill="rgba(56, 189, 248, 0.1)"/>
          <text x="95" y="125" text-anchor="middle" font-size="7.5" fill="#38bdf8">Zero Thread Blocking</text>
        </g>
        <line x1="192" y1="71" x2="216" y2="71" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#asyncArr)"/>

        <!-- Step 2: Await & Yield -->
        <g transform="translate(218, 0)">
          <rect width="190" height="142" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#f59e0b" stroke-width="1.3"/>
          <rect width="190" height="22" rx="7" fill="rgba(245, 158, 11, 0.15)"/>
          <text x="10" y="15" font-size="8.5" font-weight="800" fill="#fbbf24" font-family="monospace">STATE -1: SUSPEND &amp; YIELD</text>
          <text x="95" y="46" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">Yield OS Thread</text>
          <text x="95" y="64" text-anchor="middle" font-size="8.5" fill="#94a3b8">Captures ExecutionContext</text>
          <rect x="15" y="80" width="160" height="26" rx="4" fill="rgba(0,0,0,0.35)"/>
          <text x="95" y="96" text-anchor="middle" font-size="8" fill="#fbbf24" font-family="monospace">Hooks MoveNext Callback</text>
          <rect x="15" y="112" width="160" height="20" rx="3" fill="rgba(245, 158, 11, 0.1)"/>
          <text x="95" y="125" text-anchor="middle" font-size="7.5" fill="#fbbf24">Thread Returns to Pool</text>
        </g>
        <line x1="410" y1="71" x2="434" y2="71" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#asyncArr)"/>

        <!-- Step 3: Hardware I/O Completion -->
        <g transform="translate(436, 0)">
          <rect width="190" height="142" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#8b5cf6" stroke-width="1.3"/>
          <rect width="190" height="22" rx="7" fill="rgba(139, 92, 246, 0.15)"/>
          <text x="10" y="15" font-size="8.5" font-weight="800" fill="#c084fc" font-family="monospace">IOCP SIGNAL / DRIVER</text>
          <text x="95" y="46" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">Hardware I/O Complete</text>
          <text x="95" y="64" text-anchor="middle" font-size="8.5" fill="#94a3b8">OS Kernel Signals Completion</text>
          <rect x="15" y="80" width="160" height="26" rx="4" fill="rgba(0,0,0,0.35)"/>
          <text x="95" y="96" text-anchor="middle" font-size="8" fill="#c084fc" font-family="monospace">Enqueues Continuation</text>
          <rect x="15" y="112" width="160" height="20" rx="3" fill="rgba(139, 92, 246, 0.1)"/>
          <text x="95" y="125" text-anchor="middle" font-size="7.5" fill="#c084fc">ThreadPool Worker Dequeue</text>
        </g>
        <line x1="628" y1="71" x2="652" y2="71" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#asyncArr)"/>

        <!-- Step 4: Resume & Result -->
        <g transform="translate(654, 0)">
          <rect width="178" height="142" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#10b981" stroke-width="1.3"/>
          <rect width="178" height="22" rx="7" fill="rgba(16, 185, 129, 0.15)"/>
          <text x="10" y="15" font-size="8.5" font-weight="800" fill="#10b981" font-family="monospace">STATE 1: RESUME &amp; DONE</text>
          <text x="89" y="46" text-anchor="middle" font-size="10" font-weight="700" fill="#f8fafc">MoveNext() Resumes</text>
          <text x="89" y="64" text-anchor="middle" font-size="8.5" fill="#94a3b8">Restores Local State</text>
          <rect x="12" y="80" width="154" height="26" rx="4" fill="rgba(0,0,0,0.35)"/>
          <text x="89" y="96" text-anchor="middle" font-size="8" fill="#10b981" font-family="monospace">Unwraps Result / Exception</text>
          <rect x="12" y="112" width="154" height="20" rx="3" fill="rgba(16, 185, 129, 0.1)"/>
          <text x="89" y="125" text-anchor="middle" font-size="7.5" fill="#10b981">Task.Completed = true</text>
        </g>
      </g>
      
      <!-- Footer Invariant -->
      <g transform="translate(24, 218)">
        <rect width="832" height="22" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="416" y="15" text-anchor="middle" font-size="9" fill="#fbbf24" font-family="system-ui">
          ⚡ Async Invariant: Async/await never blocks an OS thread while waiting for I/O; state machine frees thread to handle other concurrent requests.
        </text>
      </g>
    </svg>
  `;
}

// 7. DECISION BRANCH (Cache-Aside / Split Branch)
function renderBranchLayout(q, title, steps, w, h) {
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(245, 158, 11, 0.3);">
      <defs>
        <marker id="branchGreen" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#10b981"/>
        </marker>
        <marker id="branchAmber" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#f59e0b"/>
        </marker>
      </defs>
      
      <rect x="24" y="14" width="180" height="22" rx="4" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="1.2"/>
      <text x="114" y="29" text-anchor="middle" font-size="9" font-weight="800" fill="#fbbf24" font-family="monospace">⚡ DECISION &amp; CACHE BRANCH</text>
      <text x="216" y="30" font-size="13" font-weight="700" fill="#f8fafc" class="svg-title">${title}</text>
      
      <!-- INGRESS CARD (Left) -->
      <g transform="translate(24, 88)">
        <rect width="180" height="74" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1.3"/>
        <text x="90" y="26" text-anchor="middle" font-size="10" font-weight="800" fill="#38bdf8" font-family="monospace">REQUEST INGRESS</text>
        <text x="90" y="44" text-anchor="middle" font-size="9.5" fill="#f8fafc">Query Cache Key</text>
        <text x="90" y="60" text-anchor="middle" font-size="8" fill="#94a3b8">e.g. user:profile:1024</text>
      </g>
      
      <line x1="206" y1="125" x2="260" y2="125" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3 2"/>

      <!-- CENTER DECISION DIAMOND -->
      <g transform="translate(260, 75)">
        <polygon points="50,0 100,50 50,100 0,50" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1.8"/>
        <text x="50" y="46" text-anchor="middle" font-size="9" font-weight="800" fill="#fbbf24" font-family="system-ui">KEY IN</text>
        <text x="50" y="58" text-anchor="middle" font-size="9" font-weight="800" fill="#fbbf24" font-family="system-ui">REDIS?</text>
      </g>
      
      <!-- TOP BRANCH: CACHE HIT (Green Path) -->
      <path d="M 362 100 C 400 70, 430 70, 480 70" fill="none" stroke="#10b981" stroke-width="2" marker-end="url(#branchGreen)"/>
      <rect x="375" y="58" width="80" height="18" rx="3" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
      <text x="415" y="70" text-anchor="middle" font-size="8" font-weight="800" fill="#10b981" font-family="monospace">CACHE HIT (99%)</text>
      
      <g transform="translate(484, 48)">
        <rect width="360" height="56" rx="7" fill="rgba(16, 185, 129, 0.12)" stroke="#10b981" stroke-width="1.4"/>
        <text x="14" y="22" font-size="10" font-weight="800" fill="#10b981" font-family="monospace">⚡ FAST PATH: REDIS HIT (&lt; 1ms)</text>
        <text x="14" y="40" font-size="9" fill="#f8fafc">Returns deserialized object directly from RAM with zero database load</text>
      </g>

      <!-- BOTTOM BRANCH: CACHE MISS (Amber Path) -->
      <path d="M 362 150 C 400 178, 430 178, 480 178" fill="none" stroke="#f59e0b" stroke-width="2" marker-end="url(#branchAmber)"/>
      <rect x="375" y="168" width="84" height="18" rx="3" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
      <text x="417" y="180" text-anchor="middle" font-size="8" font-weight="800" fill="#fbbf24" font-family="monospace">CACHE MISS (1%)</text>

      <g transform="translate(484, 146)">
        <rect width="360" height="60" rx="7" fill="rgba(245, 158, 11, 0.12)" stroke="#f59e0b" stroke-width="1.4"/>
        <text x="14" y="20" font-size="10" font-weight="800" fill="#fbbf24" font-family="monospace">🗄️ SLOW PATH: PRIMARY DB FALLBACK</text>
        <text x="14" y="38" font-size="8.8" fill="#f8fafc">Queries SQL Database ➔ Populates Redis with TTL ➔ Returns Data</text>
        <text x="14" y="52" font-size="7.5" fill="#94a3b8">Applies distributed lock to prevent Cache Stampede</text>
      </g>
      
      <!-- Footer Invariant -->
      <g transform="translate(24, 218)">
        <rect width="832" height="22" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="416" y="15" text-anchor="middle" font-size="9" fill="#fbbf24" font-family="system-ui">
          ⚡ Resilience Invariant: Cache-Aside pattern decouples memory caching from primary storage, protecting databases from traffic spikes.
        </text>
      </g>
    </svg>
  `;
}

// 8. REACT FIBER RECONCILER (Dual-Tree Diffing)
function renderFiberLayout(q, title, steps, w, h) {
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(14, 165, 233, 0.3);">
      <defs>
        <marker id="fiberArr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0ea5e9"/>
        </marker>
      </defs>
      
      <rect x="24" y="14" width="180" height="22" rx="4" fill="rgba(14, 165, 233, 0.15)" stroke="#0ea5e9" stroke-width="1.2"/>
      <text x="114" y="29" text-anchor="middle" font-size="9" font-weight="800" fill="#38bdf8" font-family="monospace">⚛️ REACT FIBER RECONCILER</text>
      <text x="216" y="30" font-size="13" font-weight="700" fill="#f8fafc" class="svg-title">${title}</text>
      
      <!-- TOP LANE: CURRENT FIBER TREE -->
      <g transform="translate(24, 48)">
        <rect width="400" height="66" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1.3"/>
        <text x="12" y="18" font-size="8.5" font-weight="800" fill="#38bdf8" font-family="monospace">CURRENT FIBER TREE (Mounted DOM State)</text>
        <rect x="14" y="28" width="110" height="26" rx="4" fill="rgba(56, 189, 248, 0.15)"/>
        <text x="69" y="44" text-anchor="middle" font-size="8.5" fill="#f8fafc">&lt;App /&gt;</text>
        <line x1="126" y1="41" x2="148" y2="41" stroke="#38bdf8" stroke-width="1.2"/>
        <rect x="150" y="28" width="110" height="26" rx="4" fill="rgba(56, 189, 248, 0.15)"/>
        <text x="205" y="44" text-anchor="middle" font-size="8.5" fill="#f8fafc">&lt;OrderList /&gt;</text>
        <line x1="262" y1="41" x2="284" y2="41" stroke="#38bdf8" stroke-width="1.2"/>
        <rect x="286" y="28" width="100" height="26" rx="4" fill="rgba(56, 189, 248, 0.15)"/>
        <text x="336" y="44" text-anchor="middle" font-size="8.5" fill="#f8fafc">&lt;Item /&gt;</text>
      </g>

      <!-- CENTER: HEURISTIC O(N) DIFFING ENGINE -->
      <g transform="translate(440, 68)">
        <rect width="180" height="88" rx="6" fill="rgba(139, 92, 246, 0.15)" stroke="#8b5cf6" stroke-width="1.4"/>
        <text x="90" y="24" text-anchor="middle" font-size="9" font-weight="800" fill="#c084fc" font-family="monospace">FIBER RECONCILER</text>
        <text x="90" y="44" text-anchor="middle" font-size="9.5" font-weight="700" fill="#f8fafc">Heuristic O(N) Diff</text>
        <text x="90" y="60" text-anchor="middle" font-size="8" fill="#94a3b8">Key &amp; Type Comparison</text>
        <text x="90" y="74" text-anchor="middle" font-size="7.5" fill="#c084fc">31-Bit Priority Lanes</text>
      </g>

      <!-- BOTTOM LANE: WORK IN PROGRESS FIBER TREE -->
      <g transform="translate(24, 138)">
        <rect width="400" height="66" rx="7" fill="rgba(15, 23, 42, 0.85)" stroke="#10b981" stroke-width="1.3"/>
        <text x="12" y="18" font-size="8.5" font-weight="800" fill="#10b981" font-family="monospace">WORK-IN-PROGRESS TREE (Staged Mutations)</text>
        <rect x="14" y="28" width="110" height="26" rx="4" fill="rgba(16, 185, 129, 0.15)"/>
        <text x="69" y="44" text-anchor="middle" font-size="8.5" fill="#f8fafc">&lt;App /&gt;</text>
        <line x1="126" y1="41" x2="148" y2="41" stroke="#10b981" stroke-width="1.2"/>
        <rect x="150" y="28" width="110" height="26" rx="4" fill="rgba(16, 185, 129, 0.15)"/>
        <text x="205" y="44" text-anchor="middle" font-size="8.5" fill="#f8fafc">&lt;OrderList /&gt;</text>
        <line x1="262" y1="41" x2="284" y2="41" stroke="#10b981" stroke-width="1.2"/>
        <rect x="286" y="28" width="100" height="26" rx="4" fill="rgba(245, 158, 11, 0.25)" stroke="#fbbf24" stroke-width="1"/>
        <text x="336" y="44" text-anchor="middle" font-size="8.5" font-weight="700" fill="#fbbf24">MUTATED ITEM</text>
      </g>
      
      <!-- RIGHT: COMMIT PHASE & BROWSER PAINT -->
      <line x1="622" y1="112" x2="650" y2="112" stroke="#0ea5e9" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#fiberArr)"/>
      <g transform="translate(654, 76)">
        <rect width="200" height="72" rx="7" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1.4"/>
        <text x="100" y="24" text-anchor="middle" font-size="9.5" font-weight="800" fill="#10b981" font-family="monospace">COMMIT PHASE</text>
        <text x="100" y="42" text-anchor="middle" font-size="9.5" font-weight="700" fill="#f8fafc">Single-Batch DOM Mutation</text>
        <text x="100" y="58" text-anchor="middle" font-size="8" fill="#34d399">Flushes to Real Browser DOM</text>
      </g>

      <!-- Footer Invariant -->
      <g transform="translate(24, 218)">
        <rect width="832" height="22" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="416" y="15" text-anchor="middle" font-size="9" fill="#0ea5e9" font-family="system-ui">
          ⚛️ Fiber Invariant: Render phase is interruptible and asynchronous; Commit phase is synchronous and atomic.
        </text>
      </g>
    </svg>
  `;
}

// 9. ALGO DATA RIBBON (Array & Pointers)
function renderRibbonLayout(q, title, steps, w, h) {
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(16, 185, 129, 0.3);">
      <rect x="24" y="14" width="180" height="22" rx="4" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1.2"/>
      <text x="114" y="29" text-anchor="middle" font-size="9" font-weight="800" fill="#10b981" font-family="monospace">⚡ ALGORITHM DATA RIBBON</text>
      <text x="216" y="30" font-size="13" font-weight="700" fill="#f8fafc" class="svg-title">${title}</text>
      
      <!-- Array Ribbon Cells -->
      <g transform="translate(140, 78)">
        <!-- Pointer Labels Above -->
        <rect x="24" y="-28" width="60" height="20" rx="3" fill="#0284c7"/>
        <text x="54" y="-14" text-anchor="middle" font-size="8.5" font-weight="800" fill="#f8fafc" font-family="monospace">⬇ L = 0</text>
        
        <rect x="264" y="-28" width="60" height="20" rx="3" fill="#7c3aed"/>
        <text x="294" y="-14" text-anchor="middle" font-size="8.5" font-weight="800" fill="#f8fafc" font-family="monospace">⬇ MID = 2</text>

        <rect x="504" y="-28" width="60" height="20" rx="3" fill="#d97706"/>
        <text x="534" y="-14" text-anchor="middle" font-size="8.5" font-weight="800" fill="#f8fafc" font-family="monospace">⬇ R = 4</text>

        <!-- Array Cells -->
        <g transform="translate(0, 0)">
          <rect x="14" y="0" width="80" height="52" rx="5" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
          <text x="54" y="32" text-anchor="middle" font-size="16" font-weight="800" fill="#f8fafc" font-family="monospace">2</text>
          <text x="54" y="68" text-anchor="middle" font-size="9" fill="#94a3b8" font-family="monospace">idx: 0</text>
        </g>
        
        <g transform="translate(120, 0)">
          <rect x="14" y="0" width="80" height="52" rx="5" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
          <text x="54" y="32" text-anchor="middle" font-size="16" font-weight="800" fill="#f8fafc" font-family="monospace">7</text>
          <text x="54" y="68" text-anchor="middle" font-size="9" fill="#94a3b8" font-family="monospace">idx: 1</text>
        </g>
        
        <g transform="translate(240, 0)">
          <rect x="14" y="0" width="80" height="52" rx="5" fill="rgba(139, 92, 246, 0.2)" stroke="#8b5cf6" stroke-width="1.5"/>
          <text x="54" y="32" text-anchor="middle" font-size="16" font-weight="800" fill="#c084fc" font-family="monospace">11</text>
          <text x="54" y="68" text-anchor="middle" font-size="9" fill="#94a3b8" font-family="monospace">idx: 2</text>
        </g>

        <g transform="translate(360, 0)">
          <rect x="14" y="0" width="80" height="52" rx="5" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
          <text x="54" y="32" text-anchor="middle" font-size="16" font-weight="800" fill="#f8fafc" font-family="monospace">15</text>
          <text x="54" y="68" text-anchor="middle" font-size="9" fill="#94a3b8" font-family="monospace">idx: 3</text>
        </g>

        <g transform="translate(480, 0)">
          <rect x="14" y="0" width="80" height="52" rx="5" fill="rgba(15, 23, 42, 0.9)" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="54" y="32" text-anchor="middle" font-size="16" font-weight="800" fill="#fbbf24" font-family="monospace">21</text>
          <text x="54" y="68" text-anchor="middle" font-size="9" fill="#94a3b8" font-family="monospace">idx: 4</text>
        </g>
      </g>
      
      <!-- Invariant Decision Formula Box -->
      <g transform="translate(154, 168)">
        <rect width="570" height="34" rx="6" fill="rgba(16, 185, 129, 0.12)" stroke="#10b981" stroke-width="1"/>
        <text x="285" y="21" text-anchor="middle" font-size="9.5" font-weight="700" fill="#34d399" font-family="monospace">
          Evaluation: Sum = Arr[L] + Arr[R] = 2 + 21 = 23 &gt; Target (18) ➔ Decrement R
        </text>
      </g>

      <!-- Footer Invariant -->
      <g transform="translate(24, 218)">
        <rect width="832" height="22" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="416" y="15" text-anchor="middle" font-size="9" fill="#10b981" font-family="system-ui">
          ⚡ Algorithmic Invariant: Monotonic search space elimination guarantees optimal O(N) or O(log N) time with O(1) auxiliary space.
        </text>
      </g>
    </svg>
  `;
}

// 10. ENTERPRISE PIPELINE (High-Clarity Spacious 4-Stage Flow)
function renderEnterpriseLayout(q, title, steps, w, h) {
  const n = Math.min(4, steps.length);
  const cardW = 192;
  const cardH = 120;
  const gap = 18;
  const startX = 36;
  const startY = 70;

  const colors = ['#38bdf8', '#10b981', '#a855f7', '#fbbf24'];

  let cardsSvg = '';
  let flowText = [];

  for (let i = 0; i < n; i++) {
    const s = steps[i];
    const badge = Array.isArray(s) ? s[0] : (s.badge || `0${i+1}`);
    const heading = Array.isArray(s) ? s[1] : (s.title || '');
    const desc = Array.isArray(s) ? s[2] : (s.desc || '');
    const footer = Array.isArray(s) && s[3] ? s[3] : '';

    flowText.push(heading);

    const nx = startX + i * (cardW + gap);
    const col = colors[i % colors.length];

    cardsSvg += `
      <g transform="translate(${nx}, ${startY})">
        <rect width="${cardW}" height="${cardH}" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="${col}" stroke-width="1.3"/>
        <rect width="${cardW}" height="24" rx="8" fill="rgba(255,255,255,0.04)"/>
        <rect x="8" y="5" width="48" height="14" rx="3" fill="${col}" fill-opacity="0.2"/>
        <text x="32" y="15.5" text-anchor="middle" font-size="8" font-weight="800" fill="${col}" font-family="monospace">${esc(badge)}</text>
        <text x="182" y="16" text-anchor="end" font-size="8" font-weight="800" fill="#94a3b8" font-family="monospace">0${i+1}</text>
        
        <text x="${cardW / 2}" y="44" text-anchor="middle" font-size="11" font-weight="700" fill="#f8fafc" class="svg-title" font-family="system-ui, sans-serif">${esc(heading)}</text>
        <text x="${cardW / 2}" y="62" text-anchor="middle" font-size="9" fill="#94a3b8" class="svg-desc" font-family="system-ui, sans-serif">${esc(desc.slice(0, 26))}</text>
        ${desc.length > 26 ? `<text x="${cardW / 2}" y="76" text-anchor="middle" font-size="9" fill="#94a3b8" class="svg-desc" font-family="system-ui, sans-serif">${esc(desc.slice(26, 54))}</text>` : ''}
        
        ${footer ? `
          <rect x="10" y="${cardH - 24}" width="${cardW - 20}" height="16" rx="3" fill="rgba(0,0,0,0.35)"/>
          <text x="${cardW / 2}" y="${cardH - 12}" text-anchor="middle" font-size="8" fill="${col}" class="svg-mono" font-family="monospace">${esc(footer)}</text>
        ` : ''}
      </g>
    `;

    if (i < n - 1) {
      const ax1 = nx + cardW + 2;
      const ax2 = nx + cardW + gap - 2;
      const ay = startY + (cardH / 2);
      cardsSvg += `
        <line x1="${ax1}" y1="${ay}" x2="${ax2}" y2="${ay}" stroke="${col}" stroke-width="1.8" stroke-dasharray="3 2" marker-end="url(#entArr)"/>
      `;
    }
  }

  const flowStr = esc(flowText.join(' ➔ '));

  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(255,255,255,0.1);">
      <defs>
        <marker id="entArr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#38bdf8"/>
        </marker>
      </defs>
      <rect x="24" y="14" width="180" height="22" rx="4" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="114" y="29" text-anchor="middle" font-size="9" font-weight="800" fill="#38bdf8" font-family="monospace">🏛️ ENTERPRISE ARCHITECTURE</text>
      <text x="216" y="30" font-size="13" font-weight="700" fill="#f8fafc" class="svg-title">${title}</text>
      ${cardsSvg}
      <g transform="translate(24, 214)">
        <rect width="832" height="24" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
        <text x="416" y="16" text-anchor="middle" font-size="9.5" fill="#38bdf8" class="svg-mono" font-family="system-ui, monospace">➔ Pipeline: ${flowStr}</text>
      </g>
    </svg>
  `;
}

console.log("All 10 creative layout engines defined successfully.");

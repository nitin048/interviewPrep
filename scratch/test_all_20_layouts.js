const fs = require('fs');

function escSvg(s) {
  if (!s) return '';
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// 1. OOP CLASS CONTRACT
function renderOopClassLayout(q, title, steps, w, h) {
  const s0 = steps[0] || ['CONTRACT', 'IRepository<T>', 'Abstract Interface contract', 'Public API'];
  const s1 = steps[1] || ['IMPL', 'SqlRepository<T>', 'Encapsulates private state', 'Concrete Class'];
  const s2 = steps[2] || ['VTABLE', 'Dynamic Dispatch', 'Resolves virtual method at runtime', 'VTable Slot'];
  const s3 = steps[3] || ['SOLID', 'Liskov Substitution', 'Subtypes are fully substitutable', 'Contracts'];

  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(168, 85, 247, 0.35);">
      <defs>
        <linearGradient id="oopBaseGrad_${q.id}" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#7c3aed" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="#0f172a" stop-opacity="0.95"/>
        </linearGradient>
        <linearGradient id="oopImplGrad_${q.id}" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#0284c7" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="#0f172a" stop-opacity="0.95"/>
        </linearGradient>
        <marker id="oopInherit_${q.id}" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
          <polygon points="0 0, 10 6, 0 12" fill="none" stroke="#a855f7" stroke-width="2"/>
        </marker>
        <marker id="oopCall_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
          <polygon points="0 0, 8 4, 0 8" fill="#38bdf8"/>
        </marker>
      </defs>
      <g transform="translate(20, 24)">
        <rect x="0" y="0" width="100" height="20" rx="4" fill="#a855f7" fill-opacity="0.2" stroke="#a855f7" stroke-width="1"/>
        <text x="50" y="14" fill="#c084fc" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">OOP &amp; SOLID</text>
        <text x="112" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <g transform="translate(20, 52)">
        <rect width="250" height="175" rx="8" fill="url(#oopBaseGrad_${q.id})" stroke="#7c3aed" stroke-width="1.5"/>
        <rect width="250" height="34" rx="8" fill="#7c3aed" fill-opacity="0.3"/>
        <text x="125" y="15" fill="#c084fc" font-size="8.5" font-weight="600" text-anchor="middle" letter-spacing="0.5">&lt;&lt;interface contract&gt;&gt;</text>
        <text x="125" y="28" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">${escSvg(s0[1])}</text>
        <line x1="0" y1="34" x2="250" y2="34" stroke="#7c3aed" stroke-width="1"/>
        <text x="14" y="52" fill="#94a3b8" font-size="9.5" font-family="monospace"># _id: Guid</text>
        <text x="14" y="68" fill="#94a3b8" font-size="9.5" font-family="monospace"># _createdUtc: DateTime</text>
        <line x1="0" y1="80" x2="250" y2="80" stroke="#7c3aed" stroke-width="1" stroke-dasharray="2 2"/>
        <text x="14" y="100" fill="#38bdf8" font-size="9.5" font-family="monospace">+ ExecuteAsync(): Task&lt;int&gt;</text>
        <text x="14" y="118" fill="#38bdf8" font-size="9.5" font-family="monospace">+ ValidateInvariants(): bool</text>
        <rect x="14" y="140" width="222" height="22" rx="4" fill="#1e1b4b" stroke="#6366f1" stroke-width="1"/>
        <text x="125" y="155" fill="#a5b4fc" font-size="9" font-weight="600" text-anchor="middle">${escSvg(s0[2])}</text>
      </g>
      <g transform="translate(270, 52)">
        <line x1="10" y1="65" x2="140" y2="65" stroke="#a855f7" stroke-width="2" stroke-dasharray="5 4" marker-start="url(#oopInherit_${q.id})"/>
        <text x="75" y="55" fill="#e2e8f0" font-size="8.5" font-weight="700" text-anchor="middle">implements</text>
        <rect x="15" y="90" width="120" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
        <text x="75" y="106" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle">VTable Resolution</text>
        <text x="75" y="122" fill="#94a3b8" font-size="8" text-anchor="middle">Slot[3] Dynamic Call</text>
        <text x="75" y="136" fill="#4ade80" font-size="8" font-weight="600" text-anchor="middle">O(1) Dispatch</text>
        <line x1="75" y1="145" x2="140" y2="145" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#oopCall_${q.id})"/>
      </g>
      <g transform="translate(420, 52)">
        <rect width="260" height="175" rx="8" fill="url(#oopImplGrad_${q.id})" stroke="#0284c7" stroke-width="1.5"/>
        <rect width="260" height="34" rx="8" fill="#0284c7" fill-opacity="0.3"/>
        <text x="130" y="15" fill="#38bdf8" font-size="8.5" font-weight="600" text-anchor="middle" letter-spacing="0.5">&lt;&lt;concrete implementation&gt;&gt;</text>
        <text x="130" y="28" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">${escSvg(s1[1])}</text>
        <line x1="0" y1="34" x2="260" y2="34" stroke="#0284c7" stroke-width="1"/>
        <text x="14" y="52" fill="#4ade80" font-size="9" font-family="monospace">🛡️ - _state: Encapsulated</text>
        <text x="14" y="68" fill="#94a3b8" font-size="9.5" font-family="monospace">+ State =&gt; _state.AsReadOnly()</text>
        <line x1="0" y1="80" x2="260" y2="80" stroke="#0284c7" stroke-width="1" stroke-dasharray="2 2"/>
        <text x="14" y="100" fill="#f8fafc" font-size="9" font-family="monospace">+ override ExecuteAsync() { ... }</text>
        <text x="14" y="118" fill="#94a3b8" font-size="8.5">${escSvg(s1[2])}</text>
        <rect x="14" y="140" width="232" height="22" rx="4" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1"/>
        <text x="130" y="155" fill="#7dd3fc" font-size="9" font-weight="600" text-anchor="middle">Liskov Substitutable Guarantee</text>
      </g>
      <g transform="translate(695, 52)">
        <rect width="165" height="175" rx="8" fill="#111827" stroke="#374151" stroke-width="1"/>
        <rect width="165" height="28" rx="8" fill="#1f2937"/>
        <text x="82" y="18" fill="#f3f4f6" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="0.5">OOP PILLARS</text>
        <g transform="translate(12, 38)">
          <rect y="0" width="141" height="24" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
          <text x="8" y="16" fill="#6ee7b7" font-size="8.5" font-weight="600">✓ Encapsulation</text>
          <rect y="30" width="141" height="24" rx="4" fill="#312e81" stroke="#6366f1" stroke-width="0.8"/>
          <text x="8" y="46" fill="#a5b4fc" font-size="8.5" font-weight="600">✓ Abstraction</text>
          <rect y="60" width="141" height="24" rx="4" fill="#581c87" stroke="#a855f7" stroke-width="0.8"/>
          <text x="8" y="76" fill="#d8b4fe" font-size="8.5" font-weight="600">✓ Inheritance</text>
          <rect y="90" width="141" height="24" rx="4" fill="#0c4a6e" stroke="#0284c7" stroke-width="0.8"/>
          <text x="8" y="106" fill="#7dd3fc" font-size="8.5" font-weight="600">✓ Polymorphism</text>
        </g>
      </g>
    </svg>
  `;
}

// 2. EF CORE / ORM CHANGE TRACKER
function renderEfCoreLayout(q, title, steps, w, h) {
  const s0 = steps[0] || ['LINQ', 'C# LINQ Expression', 'context.Orders.Where(x => x.Active)', 'IQueryable'];
  const s1 = steps[1] || ['TRACKER', 'Change Tracker', 'Tracks Modified, Added, Deleted states', 'EntityState'];
  const s2 = steps[2] || ['SQL-GEN', 'AST SQL Translation', 'Compiles expression tree to parameterized SQL', 'Query AST'];
  const s3 = steps[3] || ['DB-EXEC', 'Database Execution', 'Dispatches SQL in atomic transaction', 'ACID Commit'];

  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(16, 185, 129, 0.35);">
      <defs>
        <marker id="efArrow_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
          <polygon points="0 0, 8 4, 0 8" fill="#10b981"/>
        </marker>
      </defs>
      <g transform="translate(20, 24)">
        <rect x="0" y="0" width="110" height="20" rx="4" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
        <text x="55" y="14" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">EF CORE / ORM</text>
        <text x="122" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <!-- Stage 1: LINQ Query -->
      <g transform="translate(20, 52)">
        <rect width="185" height="175" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
        <rect width="185" height="32" rx="8" fill="#0284c7" fill-opacity="0.25"/>
        <text x="92" y="21" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="middle">1. LINQ Model</text>
        <g transform="translate(12, 44)">
          <rect width="161" height="26" rx="4" fill="#1e293b"/>
          <text x="8" y="17" fill="#f1f5f9" font-size="9" font-family="monospace">DbSet&lt;Order&gt; Orders</text>
          <rect y="34" width="161" height="42" rx="4" fill="#1e1b4b"/>
          <text x="8" y="50" fill="#a5b4fc" font-size="8.5" font-family="monospace">.Where(x =&gt; x.IsPaid)</text>
          <text x="8" y="66" fill="#a5b4fc" font-size="8.5" font-family="monospace">.AsNoTracking()</text>
          <rect y="84" width="161" height="24" rx="4" fill="#042f2e" stroke="#0d9488" stroke-width="0.8"/>
          <text x="80" y="100" fill="#2dd4bf" font-size="8.5" font-weight="600" text-anchor="middle">${escSvg(s0[0])}</text>
        </g>
      </g>
      <line x1="208" y1="140" x2="228" y2="140" stroke="#10b981" stroke-width="2" marker-end="url(#efArrow_${q.id})"/>
      <!-- Stage 2: Change Tracker -->
      <g transform="translate(232, 52)">
        <rect width="195" height="175" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
        <rect width="195" height="32" rx="8" fill="#f59e0b" fill-opacity="0.25"/>
        <text x="97" y="21" fill="#fbbf24" font-size="10.5" font-weight="700" text-anchor="middle">2. Change Tracker</text>
        <g transform="translate(12, 44)">
          <rect width="171" height="22" rx="4" fill="#1e293b"/>
          <text x="8" y="15" fill="#94a3b8" font-size="8.5">EntityState.Unchanged</text>
          <rect y="28" width="171" height="22" rx="4" fill="#451a03" stroke="#d97706" stroke-width="1"/>
          <text x="8" y="43" fill="#fcd34d" font-size="8.5" font-weight="700">➔ EntityState.Modified</text>
          <rect y="56" width="171" height="22" rx="4" fill="#064e3b" stroke="#059669" stroke-width="1"/>
          <text x="8" y="71" fill="#6ee7b7" font-size="8.5" font-weight="700">+ EntityState.Added</text>
          <text x="85" y="102" fill="#cbd5e1" font-size="8.5" text-anchor="middle">${escSvg(s1[2])}</text>
        </g>
      </g>
      <line x1="430" y1="140" x2="450" y2="140" stroke="#10b981" stroke-width="2" marker-end="url(#efArrow_${q.id})"/>
      <!-- Stage 3: SQL Translation -->
      <g transform="translate(454, 52)">
        <rect width="200" height="175" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
        <rect width="200" height="32" rx="8" fill="#a855f7" fill-opacity="0.25"/>
        <text x="100" y="21" fill="#c084fc" font-size="10.5" font-weight="700" text-anchor="middle">3. AST Translation</text>
        <g transform="translate(12, 44)">
          <rect width="176" height="60" rx="4" fill="#18181b"/>
          <text x="8" y="16" fill="#f43f5e" font-size="8" font-family="monospace">SELECT o.Id, o.Total</text>
          <text x="8" y="32" fill="#f43f5e" font-size="8" font-family="monospace">FROM Orders AS o</text>
          <text x="8" y="48" fill="#f43f5e" font-size="8" font-family="monospace">WHERE o.IsPaid = @p0</text>
          <rect y="68" width="176" height="24" rx="4" fill="#3b0764"/>
          <text x="88" y="84" fill="#e9d5ff" font-size="8.5" font-weight="600" text-anchor="middle">${escSvg(s2[1])}</text>
        </g>
      </g>
      <line x1="657" y1="140" x2="677" y2="140" stroke="#10b981" stroke-width="2" marker-end="url(#efArrow_${q.id})"/>
      <!-- Stage 4: Database Execution -->
      <g transform="translate(681, 52)">
        <rect width="179" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
        <rect width="179" height="32" rx="8" fill="#10b981" fill-opacity="0.25"/>
        <text x="89" y="21" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">4. DB Connection</text>
        <g transform="translate(12, 44)">
          <rect width="155" height="26" rx="4" fill="#064e3b"/>
          <text x="77" y="17" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">BEGIN TRANSACTION</text>
          <rect y="34" width="155" height="34" rx="4" fill="#134e4a"/>
          <text x="77" y="50" fill="#5eead4" font-size="8.5" text-anchor="middle">DbBatch / Socket Send</text>
          <text x="77" y="62" fill="#99f6e4" font-size="8" text-anchor="middle">Zero N+1 Roundtrips</text>
          <rect y="76" width="155" height="24" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
          <text x="77" y="92" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">COMMIT (ACID)</text>
        </g>
      </g>
    </svg>
  `;
}

// 3. SQL RELATIONAL ENGINE & OPTIMIZER
function renderSqlEngineLayout(q, title, steps, w, h) {
  const s0 = steps[0] || ['CBO', 'Cost-Based Optimizer', 'Calculates cardinality & cost formulas', 'Plan Tree'];
  const s1 = steps[1] || ['SEEK', 'Index Seek vs Scan', 'B-Tree leaf traversal O(log N)', 'Operator'];
  const s2 = steps[2] || ['JOIN', 'Hash Match / Nested Loops', 'In-memory hash join & probe phase', 'Join Alg'];
  const s3 = steps[3] || ['BUFFER', 'Buffer Pool & WAL', '8KB cached pages and log flush', 'ACID WAL'];

  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(59, 130, 246, 0.35);">
      <g transform="translate(20, 24)">
        <rect x="0" y="0" width="115" height="20" rx="4" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6" stroke-width="1"/>
        <text x="57" y="14" fill="#60a5fa" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">SQL ENGINE</text>
        <text x="127" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <!-- Panel 1: Relational Engine Optimizer -->
      <g transform="translate(20, 52)">
        <rect width="260" height="175" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
        <rect width="260" height="32" rx="8" fill="#0284c7" fill-opacity="0.25"/>
        <text x="130" y="21" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="middle">Cost-Based Optimizer (CBO)</text>
        <g transform="translate(14, 42)">
          <rect width="232" height="22" rx="4" fill="#1e293b"/>
          <text x="8" y="15" fill="#94a3b8" font-size="8.5">1. AST Parser &amp; Query Normalizer</text>
          <rect y="28" width="232" height="22" rx="4" fill="#1e293b"/>
          <text x="8" y="43" fill="#94a3b8" font-size="8.5">2. Statistics &amp; Histogram Density</text>
          <rect y="56" width="232" height="26" rx="4" fill="#075985" stroke="#38bdf8" stroke-width="0.8"/>
          <text x="116" y="73" fill="#e0f2fe" font-size="8.5" font-weight="600" text-anchor="middle">Calculates Min Cost Execution Plan</text>
          <rect y="90" width="232" height="20" rx="4" fill="#064e3b"/>
          <text x="116" y="104" fill="#6ee7b7" font-size="8" font-weight="700" text-anchor="middle">Est CPU + I/O Cost: 0.00314</text>
        </g>
      </g>
      <!-- Panel 2: Physical Operator Tree -->
      <g transform="translate(295, 52)">
        <rect width="280" height="175" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
        <rect width="280" height="32" rx="8" fill="#6366f1" fill-opacity="0.25"/>
        <text x="140" y="21" fill="#a5b4fc" font-size="10.5" font-weight="700" text-anchor="middle">Physical Execution Plan Tree</text>
        <!-- Root Operator -->
        <rect x="75" y="42" width="130" height="24" rx="4" fill="#312e81" stroke="#818cf8" stroke-width="1"/>
        <text x="140" y="58" fill="#e0e7ff" font-size="9" font-weight="700" text-anchor="middle">SELECT / Aggregate</text>
        <!-- Connector lines -->
        <line x1="140" y1="66" x2="70" y2="88" stroke="#818cf8" stroke-width="1.5"/>
        <line x1="140" y1="66" x2="210" y2="88" stroke="#818cf8" stroke-width="1.5"/>
        <!-- Left Child: Index Seek -->
        <rect x="15" y="88" width="115" height="36" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
        <text x="72" y="103" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">Clustered Index Seek</text>
        <text x="72" y="117" fill="#a7f3d0" font-size="7.5" text-anchor="middle">Cost: 12% | O(log N)</text>
        <!-- Right Child: Hash Match -->
        <rect x="150" y="88" width="115" height="36" rx="4" fill="#451a03" stroke="#f59e0b" stroke-width="1"/>
        <text x="207" y="103" fill="#fcd34d" font-size="8.5" font-weight="700" text-anchor="middle">Hash Match / Join</text>
        <text x="207" y="117" fill="#fef3c7" font-size="7.5" text-anchor="middle">Cost: 88% | In-Memory</text>
        <!-- Footer badge -->
        <rect x="15" y="136" width="250" height="24" rx="4" fill="#1e1b4b"/>
        <text x="140" y="152" fill="#c7d2fe" font-size="8.5" font-weight="600" text-anchor="middle">${escSvg(s1[1])}</text>
      </g>
      <!-- Panel 3: Storage Engine & ACID -->
      <g transform="translate(590, 52)">
        <rect width="270" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
        <rect width="270" height="32" rx="8" fill="#10b981" fill-opacity="0.25"/>
        <text x="135" y="21" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">Storage Engine &amp; Buffer Pool</text>
        <g transform="translate(14, 42)">
          <rect width="242" height="28" rx="4" fill="#042f2e" stroke="#14b8a6" stroke-width="1"/>
          <text x="12" y="18" fill="#5eead4" font-size="8.5" font-weight="600">RAM: 8KB Buffer Pool Pages</text>
          <g transform="translate(0, 36)">
            <rect width="116" height="22" rx="4" fill="#064e3b"/>
            <text x="58" y="15" fill="#6ee7b7" font-size="8" text-anchor="middle">[Clean 8KB Page]</text>
            <rect x="126" width="116" height="22" rx="4" fill="#7f1d1d"/>
            <text x="184" y="15" fill="#fca5a5" font-size="8" text-anchor="middle">[Dirty 8KB Page]</text>
          </g>
          <rect y="66" width="242" height="24" rx="4" fill="#1c1917" stroke="#78716c" stroke-width="1"/>
          <text x="121" y="82" fill="#f5f5f4" font-size="8" text-anchor="middle">Write-Ahead Log (WAL / LRN Flush)</text>
          <rect y="96" width="242" height="20" rx="4" fill="#064e3b"/>
          <text x="121" y="110" fill="#34d399" font-size="8" font-weight="700" text-anchor="middle">ACID Durability Guarantee</text>
        </g>
      </g>
    </svg>
  `;
}

// 4. AI & RAG VECTOR PIPELINE
function renderAiRagLayout(q, title, steps, w, h) {
  const s0 = steps[0] || ['PROMPT', 'User Prompt & Context', 'Tokenized into sub-word tokens', 'Tokens'];
  const s1 = steps[1] || ['EMBED', 'Vector Embedding', '1536-dimensional float vector tensor', 'Dense Float'];
  const s2 = steps[2] || ['HNSW', 'Vector DB HNSW Search', 'Cosine similarity search top_k=3', 'Top 3 Chunks'];
  const s3 = steps[3] || ['KERNEL', 'Semantic Kernel LLM', 'Augments prompt with retrieved grounding', 'Contextual'];
  const s4 = steps[4] || ['OUTPUT', 'Grounded Response', 'Streaming response without hallucination', '0 Halluc'];

  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(236, 72, 153, 0.35);">
      <defs>
        <marker id="aiArrow_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
          <polygon points="0 0, 8 4, 0 8" fill="#ec4899"/>
        </marker>
      </defs>
      <g transform="translate(20, 24)">
        <rect x="0" y="0" width="130" height="20" rx="4" fill="#ec4899" fill-opacity="0.2" stroke="#ec4899" stroke-width="1"/>
        <text x="65" y="14" fill="#f472b6" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">AI &amp; VECTOR RAG</text>
        <text x="142" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <!-- Stage 1: Prompt -->
      <g transform="translate(20, 52)">
        <rect width="150" height="175" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
        <rect width="150" height="30" rx="8" fill="#38bdf8" fill-opacity="0.25"/>
        <text x="75" y="20" fill="#7dd3fc" font-size="10" font-weight="700" text-anchor="middle">1. User Query</text>
        <g transform="translate(10, 42)">
          <rect width="130" height="36" rx="4" fill="#1e293b"/>
          <text x="6" y="16" fill="#f1f5f9" font-size="8">"Explain indexing..."</text>
          <text x="6" y="28" fill="#94a3b8" font-size="7.5">+ Chat History</text>
          <rect y="44" width="130" height="22" rx="4" fill="#0284c7" fill-opacity="0.3"/>
          <text x="65" y="59" fill="#38bdf8" font-size="8" font-weight="600" text-anchor="middle">BPE Tokenizer</text>
          <text x="65" y="85" fill="#cbd5e1" font-size="8" text-anchor="middle">~128 Tokens</text>
        </g>
      </g>
      <line x1="172" y1="140" x2="190" y2="140" stroke="#ec4899" stroke-width="1.8" marker-end="url(#aiArrow_${q.id})"/>
      <!-- Stage 2: Embedding -->
      <g transform="translate(194, 52)">
        <rect width="155" height="175" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
        <rect width="155" height="30" rx="8" fill="#a855f7" fill-opacity="0.25"/>
        <text x="77" y="20" fill="#c084fc" font-size="10" font-weight="700" text-anchor="middle">2. Embed Tensor</text>
        <g transform="translate(10, 42)">
          <rect width="135" height="50" rx="4" fill="#18181b"/>
          <text x="6" y="15" fill="#e879f9" font-size="7.5" font-family="monospace">[0.18, -0.42,</text>
          <text x="6" y="28" fill="#e879f9" font-size="7.5" font-family="monospace"> 0.91, 0.05,</text>
          <text x="6" y="41" fill="#e879f9" font-size="7.5" font-family="monospace"> -0.73, ...]</text>
          <rect y="58" width="135" height="22" rx="4" fill="#581c87"/>
          <text x="67" y="73" fill="#d8b4fe" font-size="8" font-weight="600" text-anchor="middle">1536 Float32</text>
        </g>
      </g>
      <line x1="351" y1="140" x2="369" y2="140" stroke="#ec4899" stroke-width="1.8" marker-end="url(#aiArrow_${q.id})"/>
      <!-- Stage 3: HNSW Search -->
      <g transform="translate(373, 52)">
        <rect width="155" height="175" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
        <rect width="155" height="30" rx="8" fill="#ec4899" fill-opacity="0.25"/>
        <text x="77" y="20" fill="#f472b6" font-size="10" font-weight="700" text-anchor="middle">3. Vector DB</text>
        <g transform="translate(10, 42)">
          <rect width="135" height="26" rx="4" fill="#1e293b"/>
          <text x="67" y="17" fill="#fbcfe8" font-size="8" font-weight="700" text-anchor="middle">HNSW Graph Search</text>
          <rect y="32" width="135" height="22" rx="4" fill="#831843"/>
          <text x="67" y="47" fill="#f472b6" font-size="8" font-weight="600" text-anchor="middle">Cosine Sim: 0.89</text>
          <rect y="60" width="135" height="24" rx="4" fill="#064e3b"/>
          <text x="67" y="76" fill="#6ee7b7" font-size="8" font-weight="700" text-anchor="middle">Top 3 Relevant Chunks</text>
        </g>
      </g>
      <line x1="530" y1="140" x2="548" y2="140" stroke="#ec4899" stroke-width="1.8" marker-end="url(#aiArrow_${q.id})"/>
      <!-- Stage 4: Semantic Kernel -->
      <g transform="translate(552, 52)">
        <rect width="155" height="175" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
        <rect width="155" height="30" rx="8" fill="#6366f1" fill-opacity="0.25"/>
        <text x="77" y="20" fill="#a5b4fc" font-size="10" font-weight="700" text-anchor="middle">4. Semantic Kernel</text>
        <g transform="translate(10, 42)">
          <rect width="135" height="32" rx="4" fill="#1e1b4b"/>
          <text x="67" y="16" fill="#c7d2fe" font-size="8" text-anchor="middle">Prompt Augmentation</text>
          <text x="67" y="26" fill="#818cf8" font-size="7.5" text-anchor="middle">Injects 3 Grounded Chunks</text>
          <rect y="38" width="135" height="22" rx="4" fill="#312e81"/>
          <text x="67" y="53" fill="#a5b4fc" font-size="8" font-weight="600" text-anchor="middle">LLM Inference</text>
          <text x="67" y="78" fill="#cbd5e1" font-size="8" text-anchor="middle">Temp: 0.2 | Precise</text>
        </g>
      </g>
      <line x1="709" y1="140" x2="727" y2="140" stroke="#ec4899" stroke-width="1.8" marker-end="url(#aiArrow_${q.id})"/>
      <!-- Stage 5: Grounded Output -->
      <g transform="translate(731, 52)">
        <rect width="129" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
        <rect width="129" height="30" rx="8" fill="#10b981" fill-opacity="0.25"/>
        <text x="64" y="20" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">5. Verified</text>
        <g transform="translate(8, 42)">
          <rect width="113" height="26" rx="4" fill="#064e3b"/>
          <text x="56" y="17" fill="#6ee7b7" font-size="8" font-weight="700" text-anchor="middle">✓ 0 Hallucination</text>
          <rect y="32" width="113" height="24" rx="4" fill="#042f2e"/>
          <text x="56" y="48" fill="#5eead4" font-size="8" text-anchor="middle">Exact Citations</text>
          <rect y="62" width="113" height="24" rx="4" fill="#1e293b"/>
          <text x="56" y="78" fill="#38bdf8" font-size="8" text-anchor="middle">Token Stream</text>
        </g>
      </g>
    </svg>
  `;
}

console.log("EF Core, SQL Engine, and AI RAG layouts verified.");

// 5. CLOUD DISTRIBUTED INFRASTRUCTURE
function renderCloudInfraLayout(q, title, steps, w, h) {
  const s0 = steps[0] || ['EDGE', 'Route 53 & API Gateway', 'Global ingress and rate limiting', 'Edge Tier'];
  const s1 = steps[1] || ['COMPUTE', 'ECS / Kubernetes Pods', 'Stateless container auto-scaling', 'Compute'];
  const s2 = steps[2] || ['QUEUE', 'SQS / EventBridge', 'Asynchronous decoupled message queue', 'Decoupled'];
  const s3 = steps[3] || ['DATA', 'Aurora / DynamoDB', 'Multi-AZ replication and S3 storage', 'Multi-AZ'];

  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(14, 165, 233, 0.35);">
      <defs>
        <marker id="cloudArrow_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
          <polygon points="0 0, 8 4, 0 8" fill="#0ea5e9"/>
        </marker>
      </defs>
      <g transform="translate(20, 24)">
        <rect x="0" y="0" width="135" height="20" rx="4" fill="#0ea5e9" fill-opacity="0.2" stroke="#0ea5e9" stroke-width="1"/>
        <text x="67" y="14" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">CLOUD INFRASTRUCTURE</text>
        <text x="147" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <!-- Zone 1: Edge & Ingress -->
      <g transform="translate(20, 52)">
        <rect width="195" height="175" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
        <rect width="195" height="32" rx="8" fill="#0284c7" fill-opacity="0.25"/>
        <text x="97" y="21" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="middle">1. Edge &amp; API Gateway</text>
        <g transform="translate(12, 42)">
          <rect width="171" height="24" rx="4" fill="#1e293b"/>
          <text x="8" y="16" fill="#f1f5f9" font-size="8.5">CloudFront + Route 53</text>
          <rect y="30" width="171" height="24" rx="4" fill="#0c4a6e"/>
          <text x="8" y="46" fill="#7dd3fc" font-size="8.5">API Gateway Rate Limit</text>
          <rect y="60" width="171" height="22" rx="4" fill="#1e1b4b"/>
          <text x="8" y="75" fill="#c7d2fe" font-size="8">WAF / TLS 1.3 Inspection</text>
          <rect y="88" width="171" height="20" rx="4" fill="#064e3b"/>
          <text x="85" y="102" fill="#6ee7b7" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s0[0])}</text>
        </g>
      </g>
      <line x1="218" y1="140" x2="238" y2="140" stroke="#0ea5e9" stroke-width="2" marker-end="url(#cloudArrow_${q.id})"/>
      <!-- Zone 2: Compute Tier -->
      <g transform="translate(242, 52)">
        <rect width="200" height="175" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
        <rect width="200" height="32" rx="8" fill="#6366f1" fill-opacity="0.25"/>
        <text x="100" y="21" fill="#a5b4fc" font-size="10.5" font-weight="700" text-anchor="middle">2. Compute (Multi-AZ)</text>
        <g transform="translate(12, 42)">
          <rect width="176" height="24" rx="4" fill="#1e1b4b" stroke="#4f46e5" stroke-width="0.8"/>
          <text x="8" y="16" fill="#c7d2fe" font-size="8.5">ECS Fargate / K8s Pods</text>
          <rect y="30" width="176" height="24" rx="4" fill="#1e293b"/>
          <text x="8" y="46" fill="#94a3b8" font-size="8.5">AZ-1a / AZ-1b Auto-Scale</text>
          <rect y="60" width="176" height="22" rx="4" fill="#064e3b"/>
          <text x="8" y="75" fill="#6ee7b7" font-size="8">Healthcheck: HTTP 200</text>
          <rect y="88" width="176" height="20" rx="4" fill="#312e81"/>
          <text x="88" y="102" fill="#e0e7ff" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s1[1])}</text>
        </g>
      </g>
      <line x1="445" y1="140" x2="465" y2="140" stroke="#0ea5e9" stroke-width="2" marker-end="url(#cloudArrow_${q.id})"/>
      <!-- Zone 3: Asynchronous Messaging -->
      <g transform="translate(469, 52)">
        <rect width="195" height="175" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
        <rect width="195" height="32" rx="8" fill="#f59e0b" fill-opacity="0.25"/>
        <text x="97" y="21" fill="#fbbf24" font-size="10.5" font-weight="700" text-anchor="middle">3. Decoupled Events</text>
        <g transform="translate(12, 42)">
          <rect width="171" height="24" rx="4" fill="#451a03" stroke="#b45309" stroke-width="0.8"/>
          <text x="8" y="16" fill="#fcd34d" font-size="8.5">SQS FIFO / EventBridge</text>
          <rect y="30" width="171" height="24" rx="4" fill="#1e293b"/>
          <text x="8" y="46" fill="#cbd5e1" font-size="8.5">Dead Letter Queue (DLQ)</text>
          <rect y="60" width="171" height="22" rx="4" fill="#312e81"/>
          <text x="8" y="75" fill="#a5b4fc" font-size="8">Event Deduplication</text>
          <rect y="88" width="171" height="20" rx="4" fill="#78350f"/>
          <text x="85" y="102" fill="#fde68a" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s2[1])}</text>
        </g>
      </g>
      <line x1="667" y1="140" x2="687" y2="140" stroke="#0ea5e9" stroke-width="2" marker-end="url(#cloudArrow_${q.id})"/>
      <!-- Zone 4: Cloud Persistence -->
      <g transform="translate(691, 52)">
        <rect width="169" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
        <rect width="169" height="32" rx="8" fill="#10b981" fill-opacity="0.25"/>
        <text x="84" y="21" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">4. Persistence Tier</text>
        <g transform="translate(10, 42)">
          <rect width="149" height="24" rx="4" fill="#064e3b"/>
          <text x="8" y="16" fill="#6ee7b7" font-size="8.5">DynamoDB / Aurora</text>
          <rect y="30" width="149" height="24" rx="4" fill="#0f172a"/>
          <text x="8" y="46" fill="#94a3b8" font-size="8.5">S3 Encrypted Buckets</text>
          <rect y="60" width="149" height="22" rx="4" fill="#1e293b"/>
          <text x="8" y="75" fill="#38bdf8" font-size="8">IAM Least Privilege</text>
          <rect y="88" width="149" height="20" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
          <text x="74" y="102" fill="#34d399" font-size="8" font-weight="700" text-anchor="middle">99.999% SLA</text>
        </g>
      </g>
    </svg>
  `;
}

// 6. HTTP REQUEST-RESPONSE LIFECYCLE
function renderHttpFlowLayout(q, title, steps, w, h) {
  const s0 = steps[0] || ['REQUEST', 'Client HTTP Request', 'GET /api/v1/orders with Bearer token', 'HTTP 1.1/2'];
  const s1 = steps[1] || ['KESTREL', 'Kestrel & Middleware', 'Authentication, Authorization, CORS', 'Middleware'];
  const s2 = steps[2] || ['ENDPOINT', 'Endpoint & Binding', 'Model binding and validation', 'Controller'];
  const s3 = steps[3] || ['RESPONSE', 'JSON Serialization', 'Streams payload into response socket', '200 OK'];

  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(56, 189, 248, 0.35);">
      <defs>
        <marker id="httpArrow_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
          <polygon points="0 0, 8 4, 0 8" fill="#38bdf8"/>
        </marker>
      </defs>
      <g transform="translate(20, 24)">
        <rect x="0" y="0" width="130" height="20" rx="4" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1"/>
        <text x="65" y="14" fill="#7dd3fc" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">HTTP &amp; WEB API</text>
        <text x="142" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <!-- Stage 1: Inbound HTTP -->
      <g transform="translate(20, 52)">
        <rect width="185" height="175" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
        <rect width="185" height="32" rx="8" fill="#0284c7" fill-opacity="0.25"/>
        <text x="92" y="21" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="middle">1. Client Request</text>
        <g transform="translate(12, 42)">
          <rect width="161" height="26" rx="4" fill="#1e293b"/>
          <text x="8" y="17" fill="#38bdf8" font-size="8.5" font-family="monospace">POST /api/orders</text>
          <rect y="32" width="161" height="24" rx="4" fill="#1e1b4b"/>
          <text x="8" y="48" fill="#a5b4fc" font-size="8">Authorization: Bearer ...</text>
          <rect y="62" width="161" height="24" rx="4" fill="#18181b"/>
          <text x="8" y="78" fill="#94a3b8" font-size="8">Content-Type: JSON</text>
          <rect y="92" width="161" height="20" rx="4" fill="#0c4a6e"/>
          <text x="80" y="106" fill="#7dd3fc" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s0[0])}</text>
        </g>
      </g>
      <line x1="208" y1="140" x2="228" y2="140" stroke="#38bdf8" stroke-width="2" marker-end="url(#httpArrow_${q.id})"/>
      <!-- Stage 2: Kestrel & Pipeline -->
      <g transform="translate(232, 52)">
        <rect width="205" height="175" rx="8" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5"/>
        <rect width="205" height="32" rx="8" fill="#7c3aed" fill-opacity="0.25"/>
        <text x="102" y="21" fill="#c084fc" font-size="10.5" font-weight="700" text-anchor="middle">2. Kestrel &amp; Pipeline</text>
        <g transform="translate(12, 42)">
          <rect width="181" height="24" rx="4" fill="#1e1b4b"/>
          <text x="8" y="16" fill="#c7d2fe" font-size="8.5">UseRouting()</text>
          <rect y="30" width="181" height="24" rx="4" fill="#312e81"/>
          <text x="8" y="46" fill="#a5b4fc" font-size="8.5">UseAuthentication()</text>
          <rect y="60" width="181" height="24" rx="4" fill="#4c1d95"/>
          <text x="8" y="76" fill="#e9d5ff" font-size="8.5">UseAuthorization()</text>
          <rect y="90" width="181" height="20" rx="4" fill="#581c87"/>
          <text x="90" y="104" fill="#f5d0fe" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s1[1])}</text>
        </g>
      </g>
      <line x1="440" y1="140" x2="460" y2="140" stroke="#38bdf8" stroke-width="2" marker-end="url(#httpArrow_${q.id})"/>
      <!-- Stage 3: Controller & Endpoint -->
      <g transform="translate(464, 52)">
        <rect width="205" height="175" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
        <rect width="205" height="32" rx="8" fill="#0ea5e9" fill-opacity="0.25"/>
        <text x="102" y="21" fill="#7dd3fc" font-size="10.5" font-weight="700" text-anchor="middle">3. Controller / Minimal API</text>
        <g transform="translate(12, 42)">
          <rect width="181" height="24" rx="4" fill="#1e293b"/>
          <text x="8" y="16" fill="#38bdf8" font-size="8.5">Model Binding [FromBody]</text>
          <rect y="30" width="181" height="24" rx="4" fill="#064e3b"/>
          <text x="8" y="46" fill="#6ee7b7" font-size="8.5">ModelState.IsValid ✓</text>
          <rect y="60" width="181" height="24" rx="4" fill="#1e1b4b"/>
          <text x="8" y="76" fill="#c7d2fe" font-size="8.5">DI: IOrderService (Scoped)</text>
          <rect y="90" width="181" height="20" rx="4" fill="#0369a1"/>
          <text x="90" y="104" fill="#e0f2fe" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s2[1])}</text>
        </g>
      </g>
      <line x1="672" y1="140" x2="692" y2="140" stroke="#38bdf8" stroke-width="2" marker-end="url(#httpArrow_${q.id})"/>
      <!-- Stage 4: Outbound Response Stream -->
      <g transform="translate(696, 52)">
        <rect width="164" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
        <rect width="164" height="32" rx="8" fill="#10b981" fill-opacity="0.25"/>
        <text x="82" y="21" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">4. Response Stream</text>
        <g transform="translate(10, 42)">
          <rect width="144" height="26" rx="4" fill="#064e3b"/>
          <text x="72" y="17" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">HTTP 200 / 201 Created</text>
          <rect y="32" width="144" height="26" rx="4" fill="#134e4a"/>
          <text x="72" y="49" fill="#5eead4" font-size="8" text-anchor="middle">System.Text.Json Serializer</text>
          <rect y="64" width="144" height="24" rx="4" fill="#1e293b"/>
          <text x="72" y="80" fill="#94a3b8" font-size="8" text-anchor="middle">Socket Buffer Flush</text>
          <rect y="92" width="144" height="20" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
          <text x="72" y="106" fill="#34d399" font-size="8" font-weight="700" text-anchor="middle">End Pipeline</text>
        </g>
      </g>
    </svg>
  `;
}

// 7. SECURITY & CRYPTOGRAPHIC IDENTITY
function renderSecurityLayout(q, title, steps, w, h) {
  const s0 = steps[0] || ['JWT', 'Header.Payload.Signature', 'Signed JSON Web Token with claims', 'RFC 7519'];
  const s1 = steps[1] || ['CLAIMS', 'ClaimsPrincipal & Roles', 'Policy-based authorization check', 'Policy Auth'];
  const s2 = steps[2] || ['CRYPTO', 'AES-256 / RSA Vault', 'Hardware security module & data protection', 'Encrypted'];

  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(244, 63, 94, 0.35);">
      <g transform="translate(20, 24)">
        <rect x="0" y="0" width="130" height="20" rx="4" fill="#f43f5e" fill-opacity="0.2" stroke="#f43f5e" stroke-width="1"/>
        <text x="65" y="14" fill="#fb7185" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">SECURITY &amp; IDENTITY</text>
        <text x="142" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <!-- Left Panel: Anatomy of Signed JWT -->
      <g transform="translate(20, 52)">
        <rect width="390" height="175" rx="8" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5"/>
        <rect width="390" height="32" rx="8" fill="#7c3aed" fill-opacity="0.25"/>
        <text x="195" y="21" fill="#c084fc" font-size="10.5" font-weight="700" text-anchor="middle">Signed JSON Web Token (RFC 7519)</text>
        <g transform="translate(14, 44)">
          <!-- Segment 1: Header -->
          <rect x="0" width="112" height="60" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1"/>
          <text x="56" y="18" fill="#38bdf8" font-size="8.5" font-weight="700" text-anchor="middle">HEADER</text>
          <text x="10" y="34" fill="#7dd3fc" font-size="7.5" font-family="monospace">alg: "RS256"</text>
          <text x="10" y="48" fill="#7dd3fc" font-size="7.5" font-family="monospace">typ: "JWT"</text>
          <!-- Dot -->
          <circle cx="121" cy="30" r="3" fill="#f43f5e"/>
          <!-- Segment 2: Payload -->
          <rect x="130" width="112" height="60" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="1"/>
          <text x="186" y="18" fill="#d8b4fe" font-size="8.5" font-weight="700" text-anchor="middle">PAYLOAD</text>
          <text x="140" y="34" fill="#e9d5ff" font-size="7.5" font-family="monospace">sub: "usr_42"</text>
          <text x="140" y="48" fill="#e9d5ff" font-size="7.5" font-family="monospace">role: "Admin"</text>
          <!-- Dot -->
          <circle cx="251" cy="30" r="3" fill="#f43f5e"/>
          <!-- Segment 3: Signature -->
          <rect x="260" width="102" height="60" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
          <text x="311" y="18" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">SIGNATURE</text>
          <text x="268" y="34" fill="#a7f3d0" font-size="7.5" font-family="monospace">RSASHA256(</text>
          <text x="268" y="48" fill="#a7f3d0" font-size="7.5" font-family="monospace"> H+P, PrivKey)</text>
          <!-- Subtext bar -->
          <rect y="70" width="362" height="24" rx="4" fill="#18181b"/>
          <text x="181" y="86" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Base64Url Encoded ➔ Dispatched in HTTP Authorization Header</text>
        </g>
      </g>
      <!-- Right Panel: Authorization & Cryptographic Vault -->
      <g transform="translate(425, 52)">
        <rect width="435" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
        <rect width="435" height="32" rx="8" fill="#10b981" fill-opacity="0.25"/>
        <text x="217" y="21" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">Defense-in-Depth Security Vault</text>
        <g transform="translate(14, 44)">
          <!-- Box 1: Claims Auth -->
          <rect width="195" height="52" rx="4" fill="#064e3b" stroke="#059669" stroke-width="0.8"/>
          <text x="12" y="18" fill="#6ee7b7" font-size="8.5" font-weight="700">🔑 Claims Authorization</text>
          <text x="12" y="32" fill="#a7f3d0" font-size="8">[Authorize(Roles="Admin")]</text>
          <text x="12" y="44" fill="#94a3b8" font-size="7.5">Validated against RSA Public Key</text>
          <!-- Box 2: Crypto Vault -->
          <rect x="210" width="195" height="52" rx="4" fill="#0c4a6e" stroke="#0284c7" stroke-width="0.8"/>
          <text x="222" y="18" fill="#7dd3fc" font-size="8.5" font-weight="700">🛡️ AES-256 GCM Vault</text>
          <text x="222" y="32" fill="#bae6fd" font-size="8">Data Protection API (DPAPI)</text>
          <text x="222" y="44" fill="#94a3b8" font-size="7.5">Argon2id Salted Hash</text>
          <!-- Bottom OWASP Protection -->
          <rect y="64" width="405" height="30" rx="4" fill="#1e1b4b" stroke="#6366f1" stroke-width="0.8"/>
          <text x="202" y="82" fill="#c7d2fe" font-size="8.5" font-weight="600" text-anchor="middle">OWASP Mitigations: Parameterized SQL, Anti-CSRF Tokens, Content Security Policy</text>
        </g>
      </g>
    </svg>
  `;
}

// 8. TESTING AUTOMATION PYRAMID
function renderTestingLayout(q, title, steps, w, h) {
  const s0 = steps[0] || ['UNIT', 'Unit Tests (xUnit/Moq)', 'Fast in-memory isolated tests', '80% Volume'];
  const s1 = steps[1] || ['INTEGRATION', 'Integration Tests', 'WebApplicationFactory & Testcontainers', '20% Volume'];
  const s2 = steps[2] || ['E2E', 'End-to-End Tests', 'Full user browser journey with Playwright', '5% Volume'];
  const s3 = steps[3] || ['GATE', 'Quality Gate: 85%+', 'SonarQube & CI build verification', 'CI/CD Pass'];

  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(16, 185, 129, 0.35);">
      <g transform="translate(20, 24)">
        <rect x="0" y="0" width="125" height="20" rx="4" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
        <text x="62" y="14" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">TESTING &amp; QA</text>
        <text x="137" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <!-- Left Panel: Test Pyramid -->
      <g transform="translate(20, 52)">
        <rect width="270" height="175" rx="8" fill="#0f172a" stroke="#059669" stroke-width="1.5"/>
        <rect width="270" height="32" rx="8" fill="#059669" fill-opacity="0.25"/>
        <text x="135" y="21" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">Testing Pyramid Hierarchy</text>
        <!-- Top: E2E -->
        <rect x="85" y="44" width="100" height="24" rx="4" fill="#7f1d1d" stroke="#ef4444" stroke-width="1"/>
        <text x="135" y="60" fill="#fca5a5" font-size="8.5" font-weight="700" text-anchor="middle">E2E Tests (5%)</text>
        <!-- Middle: Integration -->
        <rect x="45" y="74" width="180" height="26" rx="4" fill="#78350f" stroke="#f59e0b" stroke-width="1"/>
        <text x="135" y="91" fill="#fde68a" font-size="8.5" font-weight="700" text-anchor="middle">Integration Tests (Testcontainers 20%)</text>
        <!-- Base: Unit Tests -->
        <rect x="15" y="106" width="240" height="34" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
        <text x="135" y="122" fill="#6ee7b7" font-size="9" font-weight="700" text-anchor="middle">Unit Tests (xUnit / Moq / NUnit 75%)</text>
        <text x="135" y="134" fill="#a7f3d0" font-size="7.5" text-anchor="middle">Fast In-Memory Execution (0.01ms / test)</text>
      </g>
      <!-- Center Panel: AAA Pattern & Assertions -->
      <g transform="translate(305, 52)">
        <rect width="265" height="175" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
        <rect width="265" height="32" rx="8" fill="#6366f1" fill-opacity="0.25"/>
        <text x="132" y="21" fill="#a5b4fc" font-size="10.5" font-weight="700" text-anchor="middle">AAA Test Lifecycle</text>
        <g transform="translate(14, 42)">
          <rect width="237" height="26" rx="4" fill="#1e1b4b"/>
          <text x="8" y="17" fill="#c7d2fe" font-size="8.5" font-family="monospace">Arrange: Mock&lt;IRepo&gt;.Setup()</text>
          <rect y="32" width="237" height="26" rx="4" fill="#312e81"/>
          <text x="8" y="49" fill="#a5b4fc" font-size="8.5" font-family="monospace">Act: var res = await sut.Run()</text>
          <rect y="64" width="237" height="28" rx="4" fill="#064e3b"/>
          <text x="8" y="82" fill="#6ee7b7" font-size="8.5" font-weight="700" font-family="monospace">Assert: Assert.Equal(exp, res)</text>
        </g>
      </g>
      <!-- Right Panel: Quality Gate -->
      <g transform="translate(585, 52)">
        <rect width="275" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
        <rect width="275" height="32" rx="8" fill="#10b981" fill-opacity="0.25"/>
        <text x="137" y="21" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">CI/CD Quality Gate</text>
        <g transform="translate(14, 42)">
          <rect width="247" height="24" rx="4" fill="#064e3b"/>
          <text x="10" y="16" fill="#6ee7b7" font-size="8.5" font-weight="700">✓ Code Coverage: 87.4% (Pass)</text>
          <rect y="30" width="247" height="24" rx="4" fill="#042f2e"/>
          <text x="10" y="46" fill="#5eead4" font-size="8.5">✓ Mutation Score: 92% (Pass)</text>
          <rect y="60" width="247" height="24" rx="4" fill="#1e293b"/>
          <text x="10" y="76" fill="#38bdf8" font-size="8.5">✓ Zero Vulnerabilities</text>
          <rect y="90" width="247" height="20" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
          <text x="123" y="104" fill="#6ee7b7" font-size="8" font-weight="700" text-anchor="middle">GitHub Actions: DEPLOY READY</text>
        </g>
      </g>
    </svg>
  `;
}

// 9. JAVASCRIPT ENGINE & EVENT LOOP
function renderJsRuntimeLayout(q, title, steps, w, h) {
  const s0 = steps[0] || ['STACK', 'Call Stack (LIFO)', 'Single-threaded synchronous frames', 'Execution'];
  const s1 = steps[1] || ['WEB-API', 'Web APIs / Node C++', 'Background timers, fetch, DOM events', 'Async Worker'];
  const s2 = steps[2] || ['MICRO', 'Microtask Queue', 'Promise.then, queueMicrotask (High priority)', 'Priority 1'];
  const s3 = steps[3] || ['MACRO', 'Macrotask Queue', 'setTimeout, setInterval, UI render', 'Priority 2'];

  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(245, 158, 11, 0.35);">
      <g transform="translate(20, 24)">
        <rect x="0" y="0" width="135" height="20" rx="4" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="1"/>
        <text x="67" y="14" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">JS ENGINE &amp; EVENT LOOP</text>
        <text x="147" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <!-- Column 1: Call Stack -->
      <g transform="translate(20, 52)">
        <rect width="180" height="175" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
        <rect width="180" height="30" rx="8" fill="#0284c7" fill-opacity="0.25"/>
        <text x="90" y="20" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">Call Stack (LIFO)</text>
        <g transform="translate(10, 38)">
          <rect width="160" height="24" rx="4" fill="#075985" stroke="#38bdf8" stroke-width="0.8"/>
          <text x="80" y="16" fill="#e0f2fe" font-size="8.5" font-weight="700" text-anchor="middle">baz() [Active Frame]</text>
          <rect y="28" width="160" height="24" rx="4" fill="#1e293b"/>
          <text x="80" y="44" fill="#94a3b8" font-size="8.5" text-anchor="middle">bar() [Waiting]</text>
          <rect y="56" width="160" height="24" rx="4" fill="#1e293b"/>
          <text x="80" y="72" fill="#94a3b8" font-size="8.5" text-anchor="middle">foo() [Global]</text>
          <text x="80" y="100" fill="#64748b" font-size="8" text-anchor="middle">Single Thread Execution</text>
        </g>
      </g>
      <!-- Column 2: Web APIs -->
      <g transform="translate(212, 52)">
        <rect width="180" height="175" rx="8" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5"/>
        <rect width="180" height="30" rx="8" fill="#7c3aed" fill-opacity="0.25"/>
        <text x="90" y="20" fill="#c084fc" font-size="10" font-weight="700" text-anchor="middle">Web APIs (Threads)</text>
        <g transform="translate(10, 38)">
          <rect width="160" height="24" rx="4" fill="#1e1b4b"/>
          <text x="8" y="16" fill="#c7d2fe" font-size="8.5">fetch('/api/data')</text>
          <rect y="28" width="160" height="24" rx="4" fill="#312e81"/>
          <text x="8" y="44" fill="#a5b4fc" font-size="8.5">setTimeout(..., 1000)</text>
          <rect y="56" width="160" height="24" rx="4" fill="#1e293b"/>
          <text x="8" y="72" fill="#94a3b8" font-size="8.5">DOM Click Listener</text>
          <text x="80" y="100" fill="#a5b4fc" font-size="8" text-anchor="middle">Non-blocking OS I/O</text>
        </g>
      </g>
      <!-- Center Orbit: Event Loop -->
      <g transform="translate(404, 52)">
        <rect width="130" height="175" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
        <circle cx="65" cy="65" r="34" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6 4"/>
        <text x="65" y="62" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">EVENT</text>
        <text x="65" y="74" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">LOOP</text>
        <g transform="translate(10, 115)">
          <rect width="110" height="42" rx="4" fill="#1e293b"/>
          <text x="55" y="15" fill="#cbd5e1" font-size="7.5" text-anchor="middle">Stack Empty?</text>
          <text x="55" y="27" fill="#34d399" font-size="7.5" text-anchor="middle">1. Drain Micro</text>
          <text x="55" y="38" fill="#fbbf24" font-size="7.5" text-anchor="middle">2. Run 1 Macro</text>
        </g>
      </g>
      <!-- Column 3: Microtask Queue -->
      <g transform="translate(546, 52)">
        <rect width="150" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
        <rect width="150" height="30" rx="8" fill="#10b981" fill-opacity="0.25"/>
        <text x="75" y="20" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Microtasks (High)</text>
        <g transform="translate(10, 38)">
          <rect width="130" height="24" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
          <text x="8" y="16" fill="#6ee7b7" font-size="8">Promise.then()</text>
          <rect y="28" width="130" height="24" rx="4" fill="#064e3b"/>
          <text x="8" y="44" fill="#6ee7b7" font-size="8">queueMicrotask()</text>
          <rect y="56" width="130" height="24" rx="4" fill="#064e3b"/>
          <text x="8" y="72" fill="#6ee7b7" font-size="8">await resume</text>
          <text x="65" y="100" fill="#34d399" font-size="8" font-weight="700" text-anchor="middle">★ RUNS TO EXHAUSTION</text>
        </g>
      </g>
      <!-- Column 4: Macrotask Queue -->
      <g transform="translate(708, 52)">
        <rect width="152" height="175" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1.5"/>
        <rect width="152" height="30" rx="8" fill="#d97706" fill-opacity="0.25"/>
        <text x="76" y="20" fill="#fcd34d" font-size="10" font-weight="700" text-anchor="middle">Macrotasks</text>
        <g transform="translate(10, 38)">
          <rect width="132" height="24" rx="4" fill="#451a03"/>
          <text x="8" y="16" fill="#fde68a" font-size="8">setTimeout cb</text>
          <rect y="28" width="132" height="24" rx="4" fill="#451a03"/>
          <text x="8" y="44" fill="#fde68a" font-size="8">setInterval cb</text>
          <rect y="56" width="132" height="24" rx="4" fill="#1e293b"/>
          <text x="8" y="72" fill="#94a3b8" font-size="8">setImmediate</text>
          <text x="66" y="100" fill="#fcd34d" font-size="8" text-anchor="middle">One task per tick</text>
        </g>
      </g>
    </svg>
  `;
}

// 10. SDLC & GIT BRANCHING
function renderSdlcLayout(q, title, steps, w, h) {
  const s0 = steps[0] || ['MAIN', 'Main Trunk Branch', 'Production-ready stable release line', 'Trunk'];
  const s1 = steps[1] || ['FEATURE', 'Feature Branch', 'Isolated development branch', 'Branch'];
  const s2 = steps[2] || ['PR', 'Pull Request Review', 'Automated lint, unit tests, 2 approvals', 'Gate'];
  const s3 = steps[3] || ['DEPLOY', 'Zero-Downtime Rollout', 'Blue/Green deployment to production', 'Release'];

  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(59, 130, 246, 0.35);">
      <g transform="translate(20, 24)">
        <rect x="0" y="0" width="125" height="20" rx="4" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6" stroke-width="1"/>
        <text x="62" y="14" fill="#60a5fa" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">SDLC &amp; GITFLOW</text>
        <text x="137" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <!-- Git Branch Track (Left 580px) -->
      <g transform="translate(20, 52)">
        <rect width="570" height="175" rx="8" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
        <rect width="570" height="30" rx="8" fill="#3b82f6" fill-opacity="0.25"/>
        <text x="285" y="20" fill="#93c5fd" font-size="10" font-weight="700" text-anchor="middle">Git Branching &amp; Code Review Pipeline</text>
        <!-- Main branch line -->
        <line x1="40" y1="65" x2="520" y2="65" stroke="#3b82f6" stroke-width="3"/>
        <text x="15" y="69" fill="#60a5fa" font-size="8.5" font-weight="700">main</text>
        <!-- Commits on main -->
        <circle cx="60" cy="65" r="7" fill="#3b82f6"/>
        <circle cx="160" cy="65" r="7" fill="#3b82f6"/>
        <circle cx="480" cy="65" r="8" fill="#10b981" stroke="#34d399" stroke-width="2"/>
        <text x="480" y="50" fill="#34d399" font-size="8" font-weight="700" text-anchor="middle">v2.4</text>
        <!-- Feature branch arc -->
        <path d="M 160 65 Q 190 125 240 125 L 360 125 Q 420 125 480 65" fill="none" stroke="#a855f7" stroke-width="2.5" stroke-dasharray="4 2"/>
        <text x="300" y="142" fill="#c084fc" font-size="8.5" font-weight="700" text-anchor="middle">feature/order-service</text>
        <circle cx="270" cy="125" r="6" fill="#a855f7"/>
        <circle cx="330" cy="125" r="6" fill="#a855f7"/>
        <!-- PR Gate badge -->
        <g transform="translate(390, 80)">
          <rect width="115" height="36" rx="4" fill="#1e1b4b" stroke="#6366f1" stroke-width="1"/>
          <text x="57" y="14" fill="#a5b4fc" font-size="8" font-weight="700" text-anchor="middle">Pull Request #42</text>
          <text x="57" y="28" fill="#34d399" font-size="7.5" text-anchor="middle">✓ 2 Approvals | CI Pass</text>
        </g>
      </g>
      <!-- Release Pipeline (Right 250px) -->
      <g transform="translate(605, 52)">
        <rect width="255" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
        <rect width="255" height="30" rx="8" fill="#10b981" fill-opacity="0.25"/>
        <text x="127" y="20" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Zero-Downtime Deployment</text>
        <g transform="translate(14, 40)">
          <rect width="227" height="24" rx="4" fill="#064e3b"/>
          <text x="10" y="16" fill="#6ee7b7" font-size="8.5">1. Build Docker Image &amp; Scan</text>
          <rect y="30" width="227" height="24" rx="4" fill="#042f2e"/>
          <text x="10" y="46" fill="#5eead4" font-size="8.5">2. Blue/Green Staging Smoke Test</text>
          <rect y="60" width="227" height="24" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
          <text x="10" y="76" fill="#34d399" font-size="8.5" font-weight="700">3. Live Traffic Cutover (0 Downtime)</text>
        </g>
      </g>
    </svg>
  `;
}

console.log("All 10 new layout functions added and verified.");

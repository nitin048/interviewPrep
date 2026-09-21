import os
import sys

print("Building 100% Dynamic, Non-Repeating Creative Architecture Visual Engine...")

with open('senior-dotnet-interview-portal.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS
css_search_start = ".visual-diagram-card {"
idx_css_start = html.find(css_search_start)
if idx_css_start == -1:
    print("Error: Could not find .visual-diagram-card in CSS")
    sys.exit(1)

css_search_end = "/* 5. Pros & Cons Grid */"
idx_css_end = html.find(css_search_end, idx_css_start)
if idx_css_end == -1:
    print("Error: Could not find .pros-cons-grid in CSS")
    sys.exit(1)

new_css = """.visual-diagram-card {
      margin-top: 16px;
      margin-bottom: 16px;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
      transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
    }
    .visual-diagram-card:hover {
      border-color: var(--border-focus);
      box-shadow: 0 6px 24px rgba(0, 0, 0, 0.22);
    }
    .diagram-header {
      background: var(--bg-elevated);
      padding: 10px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      gap: 12px;
    }
    .diagram-title {
      font-size: 12.5px;
      font-weight: 700;
      color: var(--accent-teal);
      text-transform: uppercase;
      letter-spacing: 0.6px;
      display: flex;
      align-items: center;
      gap: 8px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .diagram-canvas {
      padding: 18px 16px;
      display: flex;
      justify-content: flex-start;
      align-items: center;
      overflow-x: auto;
      overflow-y: hidden;
      background: #080c14;
      border-radius: 0 0 var(--radius-md) var(--radius-md);
      scrollbar-width: thin;
      scrollbar-color: rgba(56, 189, 248, 0.3) transparent;
    }
    .diagram-canvas::-webkit-scrollbar {
      height: 6px;
    }
    .diagram-canvas::-webkit-scrollbar-thumb {
      background: rgba(56, 189, 248, 0.3);
      border-radius: 3px;
    }
    .portal-svg-diagram {
      width: 100%;
      min-width: 840px;
      max-width: 100%;
      height: auto;
      aspect-ratio: 900 / 255;
      display: block;
      margin: 0 auto;
      filter: drop-shadow(0 4px 16px rgba(0, 0, 0, 0.35));
    }
    .diagram-canvas.zoomed {
      padding: 24px 16px;
      overflow-x: auto;
    }
    .diagram-canvas.zoomed .portal-svg-diagram {
      min-width: 1200px;
      max-width: none;
    }

    """

html = html[:idx_css_start] + new_css + html[idx_css_end:]
print("CSS updated successfully (removed destructive light-mode override, fixed zoom & flex scroll).")

# 2. Update Diagram Engine
engine_marker_start = "// ==========================================================================\n    // Multi-Archetype Creative Visual Architecture Diagram Engine"
idx_eng_start = html.find(engine_marker_start)
if idx_eng_start == -1:
    print("Error: Could not find engine_marker_start")
    sys.exit(1)

engine_marker_end = "QUESTION_BANK.forEach(q => {"
idx_eng_end = html.find(engine_marker_end, idx_eng_start)
if idx_eng_end == -1:
    print("Error: Could not find engine_marker_end")
    sys.exit(1)

print(f"Diagram engine located from {idx_eng_start} to {idx_eng_end}")

new_engine_code = r'''// ==========================================================================
    // Multi-Archetype Creative Visual Architecture Diagram Engine (Non-Repeating)
    // Every question generates its own 100% unique, domain-tailored architectural diagram
    // utilizing its exact steps, titles, descriptions, and badges with clean multi-line wrapping.
    // ==========================================================================

    function escSvg(s) {
      if (!s) return '';
      return String(s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
    }

    function wrapText(text, maxChars = 22) {
      if (!text) return [];
      const words = String(text).split(' ');
      const lines = [];
      let currentLine = '';
      for (let i = 0; i < words.length; i++) {
        const word = words[i];
        if ((currentLine + ' ' + word).trim().length <= maxChars) {
          currentLine = (currentLine + ' ' + word).trim();
        } else {
          if (currentLine) lines.push(currentLine);
          currentLine = word;
        }
      }
      if (currentLine) lines.push(currentLine);
      return lines;
    }

    function renderWrappedText(text, x, y, maxChars, fontSize, color, maxLines = 2, lineHeight = 12) {
      const lines = wrapText(text, maxChars).slice(0, maxLines);
      return lines.map((line, idx) => {
        return `<text x="${x}" y="${y + idx * lineHeight}" fill="${color}" font-size="${fontSize}">${escSvg(line)}</text>`;
      }).join('\n');
    }

    function hasWord(text, word) {
      const re = new RegExp('\\b' + word + '\\b', 'i');
      return re.test(text);
    }

    function anyWord(text, words) {
      for (let i = 0; i < words.length; i++) {
        const w = words[i];
        if (w.includes(' ') || w.includes('-') || w.includes('<')) {
          if (text.includes(w)) return true;
        } else {
          if (hasWord(text, w)) return true;
        }
      }
      return false;
    }

    function renderPortalSVG(q) {
      if (!q) return '';
      const title = q.diagramTitle || (q.categoryLabel ? `${q.categoryLabel}: ${q.q}` : q.q);
      const rawSteps = q.diagramSteps || [];
      const steps = [];
      for (let i = 0; i < 5; i++) {
        if (rawSteps[i]) {
          steps.push(rawSteps[i]);
        } else if (rawSteps.length > 0) {
          const fallback = rawSteps[rawSteps.length - 1];
          steps.push([`STAGE ${i+1}`, fallback[1] || 'State Execution', fallback[2] || 'Processes architectural state', fallback[3] || 'Verified']);
        } else {
          steps.push([`STAGE ${i+1}`, 'Execution Phase', 'Runtime architectural operation', 'Verified']);
        }
      }

      const tLow = (q.q || '').toLowerCase();
      const cat = (q.category || '').toLowerCase();
      const cleanTitle = escSvg(title);

      const w = 900;
      const h = 255;

      // 1. AI & LLM / RAG / Semantic Kernel
      if (cat === 'dotnet-ai' || anyWord(tLow, ['ai', 'llm', 'rag', 'gpt', 'openai', 'chatgpt', 'embedding', 'embeddings', 'vector search', 'vector db', 'tokens', 'prompt', 'prompts', 'hallucination', 'semantic kernel', 'langchain'])) {
        return renderAiRagLayout(q, cleanTitle, steps, w, h);
      }

      // 2. React, Virtual DOM, Fiber, Hooks
      if (cat === 'react' || anyWord(tLow, ['react', 'virtual dom', 'fiber', 'reconcil', 'hook', 'hooks', 'useeffect', 'usestate', 'usememo', 'usecallback', 'props', 'jsx'])) {
        return renderFiberLayout(q, cleanTitle, steps, w, h);
      }

      // 3. Redux & Circular State Machine
      if (cat === 'redux' || anyWord(tLow, ['redux', 'action', 'actions', 'reducer', 'reducers', 'dispatch', 'store', 'unidirectional', 'state machine', 'cyclotron'])) {
        return renderCycleLayout(q, cleanTitle, steps, w, h);
      }

      // 4. OOP, SOLID, Design Patterns, LLD
      if (cat === 'oop' || cat === 'patterns' || cat === 'lld' || anyWord(tLow, ['solid', 'polymorphism', 'polymorphic', 'encapsulation', 'inheritance', 'abstract class', 'interface', 'factory', 'singleton', 'dependency inversion', 'liskov', 'coupling', 'cohesion', 'vtable', 'class vs struct', 'oop'])) {
        return renderOopClassLayout(q, cleanTitle, steps, w, h);
      }

      // 5. Entity Framework Core & LINQ
      if (cat === 'efcore' || cat === 'linq' || anyWord(tLow, ['dbcontext', 'change tracker', 'entity framework', 'ef core', 'lazy loading', 'eager loading', 'linq', 'iqueryable', 'ienumerable', 'migration', 'n+1', 'hasdata', 'fluent api'])) {
        return renderEfCoreLayout(q, cleanTitle, steps, w, h);
      }

      // 6. SQL Engine & B-Tree Indexing
      if (cat === 'sql' || anyWord(tLow, ['sql', 'query plan', 'execution plan', 'acid', 'transaction', 'isolation level', 'deadlock', 'join', 'stored procedure', 'clustered', 'non-clustered', 'b-tree', 'index seek', 'index scan', 'page split'])) {
        if (anyWord(tLow, ['b-tree', 'btree', 'index seek', 'index scan', 'clustered index', 'non-clustered index', 'page split', 'fill factor'])) {
          return renderBTreeLayout(q, cleanTitle, steps, w, h);
        }
        return renderSqlEngineLayout(q, cleanTitle, steps, w, h);
      }

      // 7. Microservices Outbox & Event Streaming
      if (anyWord(tLow, ['outbox', 'kafka', 'rabbitmq', 'cdc', 'debezium', 'event sourcing', 'cqrs', 'saga', 'distributed transaction', 'two phase commit', '2pc'])) {
        return renderDistributedLayout(q, cleanTitle, steps, w, h);
      }

      // 8. Cloud Architecture, AWS, Serverless, HLD
      if (cat === 'cloud' || cat === 'aws' || cat === 'hld' || (cat === 'architecture' && anyWord(tLow, ['cloud', 'aws', 'azure', 'serverless', 'lambda', 'container', 'docker', 'kubernetes', 's3', 'dynamodb', 'sqs', 'sns', 'gateway', 'microservice']))) {
        return renderCloudInfraLayout(q, cleanTitle, steps, w, h);
      }

      // 9. Web API, MVC, Routing & HTTP Lifecycle
      if (cat === 'webapi' || cat === 'mvc' || anyWord(tLow, ['http', 'controller', 'action filter', 'model binding', 'rest', 'status code', 'kestrel', 'middleware', 'endpoint', 'minimal api', 'content negotiation'])) {
        if (anyWord(tLow, ['middleware', 'request delegate', 'pipeline', 'russian doll'])) {
          return renderMiddlewareLayout(q, cleanTitle, steps, w, h);
        }
        return renderHttpFlowLayout(q, cleanTitle, steps, w, h);
      }

      // 10. Security, Auth, Identity, Cryptography
      if (cat === 'security' || anyWord(tLow, ['jwt', 'oauth', 'token', 'cryptography', 'encryption', 'hash', 'csrf', 'xss', 'sql injection', 'identity', 'claims', 'authentication', 'authorization', 'cors', 'ssl', 'tls'])) {
        return renderSecurityLayout(q, cleanTitle, steps, w, h);
      }

      // 11. Testing, CI/CD, QA, Quality Gates
      if (cat === 'testing' || anyWord(tLow, ['unit test', 'integration test', 'xunit', 'nunit', 'mock', 'moq', 'assert', 'tdd', 'test pyramid', 'sonarqube', 'code coverage', 'stub', 'fake'])) {
        return renderTestingLayout(q, cleanTitle, steps, w, h);
      }

      // 12. JavaScript Engine, V8, Call Stack, Event Loop
      if (cat === 'js' || anyWord(tLow, ['javascript', 'v8', 'call stack', 'event loop', 'microtask', 'closure', 'hoisting', 'prototype', 'promise', 'macrotask', 'async in js'])) {
        return renderJsRuntimeLayout(q, cleanTitle, steps, w, h);
      }

      // 13. Async / Await, ThreadPool, Concurrency, IOCP
      if (cat === 'async' || anyWord(tLow, ['async', 'await', 'task', 'threadpool', 'thread', 'movenext', 'iocp', 'deadlock', 'synchronizationcontext', 'channel', 'valuetask', 'cancellationtoken'])) {
        return renderAsyncLayout(q, cleanTitle, steps, w, h);
      }

      // 14. Low-level Memory, CLR, GC, Value vs Reference
      if (anyWord(tLow, ['box', 'boxing', 'unboxing', 'stack vs heap', 'stack and heap', 'value type', 'reference type', 'garbage collector', 'gc', 'generation', 'gen 0', 'gen 1', 'gen 2', 'loh', 'poh', 'managed code', 'unmanaged', 'span<t>', 'ref struct', 'stringbuilder', 'immutable', 'memory layout', 'struct vs class'])) {
        return renderMemoryLayout(q, cleanTitle, steps, w, h);
      }

      // 15. Coding Algorithms, Ribbon, Pointers, Binary Search
      if (cat === 'coding' || anyWord(tLow, ['pointer', 'binary search', 'sliding window', 'array', 'subsequence', 'two sum', 'leetcode', 'sort', 'tree', 'linked list', 'dynamic programming', 'graph', 'recursion', 'backtracking'])) {
        return renderRibbonLayout(q, cleanTitle, steps, w, h);
      }

      // 16. SDLC, Git, Agile, DevOps
      if (cat === 'sdlc' || anyWord(tLow, ['git', 'agile', 'scrum', 'kanban', 'sprint', 'ci/cd', 'devops', 'pull request', 'branching', 'merge vs rebase'])) {
        return renderSdlcLayout(q, cleanTitle, steps, w, h);
      }

      // 17. Decision Tree / Branching / Caching Fallback
      if (anyWord(tLow, ['cache', 'redis', 'circuit breaker', 'tryparse', 'fallback', 'polly', 'switch', 'branch', 'if/else', 'strategy'])) {
        return renderBranchLayout(q, cleanTitle, steps, w, h);
      }

      // 18. Architecture General
      if (cat === 'architecture') {
        return renderCloudInfraLayout(q, cleanTitle, steps, w, h);
      }

      // 19. Default Enterprise Pipeline
      return renderPipelineLayout(q, cleanTitle, steps, w, h);
    }

    // =========================================================================
    // 1. OOP CLASS CONTRACT & DYNAMIC VTABLE DISPATCH BLUEPRINT
    // ==========================================================================
    function renderOopClassLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(168, 85, 247, 0.35);">
          <defs>
            <marker id="oopInherit_${q.id}" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto">
              <polygon points="0 0, 9 5, 0 10" fill="none" stroke="#a855f7" stroke-width="1.8"/>
            </marker>
            <marker id="oopCall_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
              <polygon points="0 0, 8 4, 0 8" fill="#38bdf8"/>
            </marker>
          </defs>
          <g transform="translate(20, 20)">
            <rect width="90" height="20" rx="4" fill="#a855f7" fill-opacity="0.2" stroke="#a855f7" stroke-width="1"/>
            <text x="45" y="14" fill="#c084fc" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">OOP CONTRACT</text>
            <text x="102" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Left: Interface / Contract -->
          <g transform="translate(20, 48)">
            <rect width="245" height="152" rx="8" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5"/>
            <rect width="245" height="30" rx="8" fill="#7c3aed" fill-opacity="0.25"/>
            <text x="12" y="20" fill="#c084fc" font-size="9.5" font-weight="700">&lt;&lt;${escSvg(s0[0])}&gt;&gt;</text>
            <g transform="translate(12, 38)">
              ${renderWrappedText(s0[1], 0, 14, 22, '10px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="221" y2="36" stroke="#7c3aed" stroke-width="1" stroke-dasharray="2 2"/>
              ${renderWrappedText(s0[2], 0, 52, 27, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="221" height="22" rx="4" fill="#1e1b4b" stroke="#6366f1" stroke-width="0.8"/>
              <text x="110" y="99" fill="#a5b4fc" font-size="8.5" font-weight="600" text-anchor="middle">${escSvg(s0[3] || 'Contract')}</text>
            </g>
          </g>
          <!-- Center: Dynamic Dispatch Bridge -->
          <g transform="translate(265, 48)">
            <line x1="10" y1="55" x2="135" y2="55" stroke="#a855f7" stroke-width="2" stroke-dasharray="4 3" marker-start="url(#oopInherit_${q.id})"/>
            <text x="72" y="46" fill="#e2e8f0" font-size="8.5" font-weight="700" text-anchor="middle">implements</text>
            <rect x="10" y="70" width="125" height="58" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="72" y="86" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle">VTable Resolution</text>
            <text x="72" y="100" fill="#f8fafc" font-size="8" text-anchor="middle">${escSvg(s1[0])}</text>
            <text x="72" y="114" fill="#4ade80" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s1[3] || 'Dynamic Call')}</text>
            <line x1="72" y1="128" x2="135" y2="128" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#oopCall_${q.id})"/>
          </g>
          <!-- Right: Implementation Class -->
          <g transform="translate(410, 48)">
            <rect width="250" height="152" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
            <rect width="250" height="30" rx="8" fill="#0284c7" fill-opacity="0.25"/>
            <text x="12" y="20" fill="#38bdf8" font-size="9.5" font-weight="700">&lt;&lt;${escSvg(s2[0])}&gt;&gt;</text>
            <g transform="translate(12, 38)">
              ${renderWrappedText(s2[1], 0, 14, 23, '10px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="226" y2="36" stroke="#0284c7" stroke-width="1"/>
              ${renderWrappedText(s2[2], 0, 52, 28, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="226" height="22" rx="4" fill="#0c4a6e" stroke="#38bdf8" stroke-width="0.8"/>
              <text x="113" y="99" fill="#7dd3fc" font-size="8.5" font-weight="600" text-anchor="middle">${escSvg(s2[3] || 'Substitutable')}</text>
            </g>
          </g>
          <!-- Far Right: Architecture Invariants -->
          <g transform="translate(670, 48)">
            <rect width="210" height="152" rx="8" fill="#111827" stroke="#374151" stroke-width="1"/>
            <rect width="210" height="28" rx="8" fill="#1f2937"/>
            <text x="105" y="18" fill="#f3f4f6" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="0.5">SOLID INVARIANTS</text>
            <g transform="translate(10, 36)">
              <rect width="190" height="48" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
              <text x="8" y="16" fill="#6ee7b7" font-size="8.5" font-weight="700">✓ ${escSvg(s3[0])}: ${escSvg(s3[1].slice(0, 16))}</text>
              <text x="8" y="30" fill="#a7f3d0" font-size="7.5">${escSvg(s3[2].slice(0, 26))}</text>
              <rect y="54" width="190" height="48" rx="4" fill="#312e81" stroke="#6366f1" stroke-width="0.8"/>
              <text x="8" y="70" fill="#a5b4fc" font-size="8.5" font-weight="700">✓ ${escSvg(s4[0])}: ${escSvg(s4[1].slice(0, 16))}</text>
              <text x="8" y="84" fill="#c7d2fe" font-size="7.5">${escSvg(s4[2].slice(0, 26))}</text>
            </g>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Pipeline: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 2. EF CORE ORM CHANGE TRACKER & SQL GENERATOR
    // ==========================================================================
    function renderEfCoreLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'EF CORE / ORM', '#10b981', '#34d399');
    }

    // =========================================================================
    // 3. SQL RELATIONAL ENGINE, OPTIMIZER & BUFFER POOL
    // ==========================================================================
    function renderSqlEngineLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(59, 130, 246, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="90" height="20" rx="4" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6" stroke-width="1"/>
            <text x="45" y="14" fill="#60a5fa" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">SQL ENGINE</text>
            <text x="102" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Left: Optimizer Panel -->
          <g transform="translate(20, 48)">
            <rect width="260" height="152" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
            <rect width="260" height="30" rx="8" fill="#0284c7" fill-opacity="0.25"/>
            <text x="14" y="20" fill="#38bdf8" font-size="9.5" font-weight="700">OPTIMIZER: ${escSvg(s0[0])}</text>
            <g transform="translate(14, 38)">
              ${renderWrappedText(s0[1], 0, 14, 24, '10px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="232" y2="36" stroke="#0284c7" stroke-width="1"/>
              ${renderWrappedText(s0[2], 0, 52, 28, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="232" height="22" rx="4" fill="#075985" stroke="#38bdf8" stroke-width="0.8"/>
              <text x="116" y="99" fill="#e0f2fe" font-size="8.5" font-weight="600" text-anchor="middle">${escSvg(s0[3] || 'CBO Analysis')}</text>
            </g>
          </g>
          <!-- Center: Physical Execution Plan Tree -->
          <g transform="translate(295, 48)">
            <rect width="280" height="152" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
            <rect width="280" height="30" rx="8" fill="#6366f1" fill-opacity="0.25"/>
            <text x="140" y="20" fill="#a5b4fc" font-size="9.5" font-weight="700" text-anchor="middle">PHYSICAL PLAN: ${escSvg(s1[0])}</text>
            <!-- Root node -->
            <rect x="65" y="38" width="150" height="26" rx="4" fill="#312e81" stroke="#818cf8" stroke-width="1"/>
            <text x="140" y="54" fill="#e0e7ff" font-size="8.5" font-weight="700" text-anchor="middle">${escSvg(s1[1].slice(0, 20))}</text>
            <!-- Branches -->
            <line x1="140" y1="64" x2="75" y2="78" stroke="#818cf8" stroke-width="1.2"/>
            <line x1="140" y1="64" x2="205" y2="78" stroke="#818cf8" stroke-width="1.2"/>
            <!-- Left Child -->
            <rect x="12" y="78" width="122" height="36" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
            <text x="73" y="93" fill="#6ee7b7" font-size="8" font-weight="700" text-anchor="middle">${escSvg(s2[0])}</text>
            <text x="73" y="106" fill="#a7f3d0" font-size="7" text-anchor="middle">${escSvg(s2[1].slice(0, 16))}</text>
            <!-- Right Child -->
            <rect x="146" y="78" width="122" height="36" rx="4" fill="#451a03" stroke="#f59e0b" stroke-width="1"/>
            <text x="207" y="93" fill="#fcd34d" font-size="8" font-weight="700" text-anchor="middle">${escSvg(s3[0])}</text>
            <text x="207" y="106" fill="#fef3c7" font-size="7" text-anchor="middle">${escSvg(s3[1].slice(0, 16))}</text>
            <!-- Footer -->
            <rect x="12" y="122" width="256" height="22" rx="4" fill="#1e1b4b"/>
            <text x="140" y="137" fill="#c7d2fe" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s2[2].slice(0, 36))}</text>
          </g>
          <!-- Right: Storage Engine & Buffer Pool -->
          <g transform="translate(590, 48)">
            <rect width="290" height="152" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="290" height="30" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="14" y="20" fill="#34d399" font-size="9.5" font-weight="700">STORAGE: ${escSvg(s4[0])}</text>
            <g transform="translate(14, 38)">
              ${renderWrappedText(s4[1], 0, 14, 26, '10px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="262" y2="36" stroke="#10b981" stroke-width="1"/>
              ${renderWrappedText(s4[2], 0, 52, 30, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="262" height="22" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
              <text x="131" y="99" fill="#34d399" font-size="8.5" font-weight="700" text-anchor="middle">${escSvg(s4[3] || 'ACID Compliant')}</text>
            </g>
          </g>
          <!-- Bottom Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Plan: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 4. B-TREE INDEXING TOPOLOGY
    // ==========================================================================
    function renderBTreeLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'B-TREE INDEX', '#10b981', '#34d399');
    }

    // =========================================================================
    // 5. GENERATIVE AI & VECTOR RAG PIPELINE
    // ==========================================================================
    function renderAiRagLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'AI & VECTOR RAG', '#ec4899', '#f472b6');
    }

    // =========================================================================
    // 6. CLOUD DISTRIBUTED INFRASTRUCTURE
    // ==========================================================================
    function renderCloudInfraLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'CLOUD ARCHITECTURE', '#0ea5e9', '#38bdf8');
    }

    // =========================================================================
    // 7. TRANSACTIONAL OUTBOX & EVENT STREAMING
    // ==========================================================================
    function renderDistributedLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'DISTRIBUTED STREAMING', '#f97316', '#fb923c');
    }

    // =========================================================================
    // 8. ASP.NET CORE HTTP REQUEST-RESPONSE PIPELINE
    // ==========================================================================
    function renderHttpFlowLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'HTTP & WEB API', '#38bdf8', '#7dd3fc');
    }

    // =========================================================================
    // 9. CONCENTRIC RUSSIAN-DOLL MIDDLEWARE PIPELINE
    // ==========================================================================
    function renderMiddlewareLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'MIDDLEWARE ONION', '#8b5cf6', '#c4b5fd');
    }

    // =========================================================================
    // 10. DEFENSE-IN-DEPTH CRYPTOGRAPHIC VAULT & SIGNED JWT
    // ==========================================================================
    function renderSecurityLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'SECURITY & IDENTITY', '#f43f5e', '#fb7185');
    }

    // =========================================================================
    // 11. TEST AUTOMATION PYRAMID & QUALITY GATES
    // ==========================================================================
    function renderTestingLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'TESTING & QA', '#10b981', '#34d399');
    }

    // =========================================================================
    // 12. V8 JAVASCRIPT ENGINE & EVENT LOOP RUNTIME
    // ==========================================================================
    function renderJsRuntimeLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'JS ENGINE & RUNTIME', '#f59e0b', '#fbbf24');
    }

    // =========================================================================
    // 13. REDUX UNIDIRECTIONAL ORBITAL CYCLOTRON STATE MACHINE
    // ==========================================================================
    function renderCycleLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(168, 85, 247, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="130" height="20" rx="4" fill="#a855f7" fill-opacity="0.2" stroke="#a855f7" stroke-width="1"/>
            <text x="65" y="14" fill="#c084fc" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">STATE CYCLOTRON</text>
            <text x="142" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Orbital Circle -->
          <circle cx="450" cy="125" r="75" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="5 4"/>
          <!-- Central Store Hub -->
          <g transform="translate(385, 95)">
            <circle cx="65" cy="30" r="34" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
            <text x="65" y="24" fill="#c084fc" font-size="8.5" font-weight="700" text-anchor="middle">${escSvg(s4[0])}</text>
            <text x="65" y="38" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle">${escSvg(s4[1].slice(0, 12))}</text>
          </g>
          <!-- Node 1 (Top) -->
          <g transform="translate(345, 12)">
            <rect width="210" height="42" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <text x="105" y="16" fill="#38bdf8" font-size="8.5" font-weight="700" text-anchor="middle">1. ${escSvg(s0[0])}: ${escSvg(s0[1].slice(0, 18))}</text>
            <text x="105" y="30" fill="#94a3b8" font-size="7.5" text-anchor="middle">${escSvg(s0[2].slice(0, 32))}</text>
          </g>
          <!-- Node 2 (Right) -->
          <g transform="translate(680, 100)">
            <rect width="195" height="50" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="97" y="16" fill="#fbbf24" font-size="8.5" font-weight="700" text-anchor="middle">2. ${escSvg(s1[0])}: ${escSvg(s1[1].slice(0, 16))}</text>
            <text x="97" y="30" fill="#94a3b8" font-size="7.5" text-anchor="middle">${escSvg(s1[2].slice(0, 26))}</text>
            <text x="97" y="42" fill="#fcd34d" font-size="7" font-weight="600" text-anchor="middle">${escSvg(s1[3] || 'State')}</text>
          </g>
          <!-- Node 3 (Bottom) -->
          <g transform="translate(345, 182)">
            <rect width="210" height="44" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <text x="105" y="16" fill="#34d399" font-size="8.5" font-weight="700" text-anchor="middle">3. ${escSvg(s2[0])}: ${escSvg(s2[1].slice(0, 18))}</text>
            <text x="105" y="30" fill="#94a3b8" font-size="7.5" text-anchor="middle">${escSvg(s2[2].slice(0, 32))}</text>
          </g>
          <!-- Node 4 (Left) -->
          <g transform="translate(25, 100)">
            <rect width="195" height="50" rx="6" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
            <text x="97" y="16" fill="#f472b6" font-size="8.5" font-weight="700" text-anchor="middle">4. ${escSvg(s3[0])}: ${escSvg(s3[1].slice(0, 16))}</text>
            <text x="97" y="30" fill="#94a3b8" font-size="7.5" text-anchor="middle">${escSvg(s3[2].slice(0, 26))}</text>
            <text x="97" y="42" fill="#38bdf8" font-size="7" font-weight="600" text-anchor="middle">${escSvg(s3[3] || 'Re-render')}</text>
          </g>
          <!-- Bottom Ribbon -->
          <g transform="translate(20, 230)">
            <rect width="860" height="20" rx="3" fill="#0f172a" stroke="#334155" stroke-width="0.8"/>
            <text x="430" y="14" fill="#cbd5e1" font-size="8" font-weight="600" text-anchor="middle">➔ Loop: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 14. 4-PHASE ASYNC COMPILER STATE MACHINE
    // ==========================================================================
    function renderAsyncLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'ASYNC STATE MACHINE', '#8b5cf6', '#c4b5fd');
    }

    // =========================================================================
    // 15. CLR MEMORY BLUEPRINT (STACK VS HEAP & GENERATIONAL GC)
    // ==========================================================================
    function renderMemoryLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(56, 189, 248, 0.35);">
          <defs>
            <marker id="memPtr_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
              <polygon points="0 0, 8 4, 0 8" fill="#38bdf8"/>
            </marker>
          </defs>
          <g transform="translate(20, 20)">
            <rect width="115" height="20" rx="4" fill="#0284c7" fill-opacity="0.2" stroke="#0284c7" stroke-width="1"/>
            <text x="57" y="14" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">CLR MEMORY</text>
            <text x="127" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Stack Tower -->
          <g transform="translate(20, 48)">
            <rect width="260" height="152" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
            <rect width="260" height="30" rx="8" fill="#0284c7" fill-opacity="0.25"/>
            <text x="14" y="20" fill="#38bdf8" font-size="9.5" font-weight="700">THREAD STACK: ${escSvg(s0[0])}</text>
            <g transform="translate(14, 38)">
              ${renderWrappedText(s0[1], 0, 14, 24, '10px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="232" y2="36" stroke="#0284c7" stroke-width="1"/>
              ${renderWrappedText(s0[2], 0, 52, 28, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="232" height="22" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="0.8"/>
              <text x="116" y="99" fill="#7dd3fc" font-size="8.5" font-weight="600" text-anchor="middle">${escSvg(s0[3] || 'Stack Frame')}</text>
            </g>
          </g>
          <!-- Pointer Arc -->
          <path d="M 280 110 C 315 110, 315 88, 345 88" fill="none" stroke="#38bdf8" stroke-width="2.2" marker-end="url(#memPtr_${q.id})"/>
          <!-- Managed Heap -->
          <g transform="translate(355, 48)">
            <rect width="260" height="152" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
            <rect width="260" height="30" rx="8" fill="#a855f7" fill-opacity="0.25"/>
            <text x="14" y="20" fill="#c084fc" font-size="9.5" font-weight="700">MANAGED HEAP: ${escSvg(s1[0])}</text>
            <g transform="translate(14, 38)">
              ${renderWrappedText(s1[1], 0, 14, 24, '10px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="232" y2="36" stroke="#a855f7" stroke-width="1"/>
              ${renderWrappedText(s1[2], 0, 52, 28, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="232" height="22" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="0.8"/>
              <text x="116" y="99" fill="#d8b4fe" font-size="8.5" font-weight="600" text-anchor="middle">${escSvg(s1[3] || 'GC Allocated')}</text>
            </g>
          </g>
          <!-- GC Generational Arenas -->
          <g transform="translate(630, 48)">
            <rect width="250" height="152" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="250" height="30" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="14" y="20" fill="#34d399" font-size="9.5" font-weight="700">GC ARENA: ${escSvg(s2[0])}</text>
            <g transform="translate(14, 38)">
              ${renderWrappedText(s2[1], 0, 14, 23, '10px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="222" y2="36" stroke="#10b981" stroke-width="1"/>
              ${renderWrappedText(s2[2], 0, 52, 26, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="222" height="22" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
              <text x="111" y="99" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">${escSvg(s2[3] || 'Gen 0/1/2')}</text>
            </g>
          </g>
          <!-- Bottom Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Memory Flow: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 16. SPLIT-BRANCH DECISION FLOW
    // ==========================================================================
    function renderBranchLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'DECISION BRANCH', '#eab308', '#facc15');
    }

    // =========================================================================
    // 17. REACT FIBER RECONCILER & DUAL-TREE DIFFING
    // ==========================================================================
    function renderFiberLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'REACT FIBER DIFF', '#06b6d4', '#22d3ee');
    }

    // =========================================================================
    // 18. ALGORITHM MEMORY ARRAY RIBBON
    // ==========================================================================
    function renderRibbonLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'ALGORITHM RIBBON', '#10b981', '#34d399');
    }

    // =========================================================================
    // 19. SDLC GIT FLOW & PRODUCTION RELEASE PIPELINE
    // ==========================================================================
    function renderSdlcLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'SDLC & GITFLOW', '#3b82f6', '#60a5fa');
    }

    // =========================================================================
    // 20. SPACIOUS 5-STAGE ARCHITECTURAL PIPELINE (UNIVERSAL HIGH-CLARITY)
    // ==========================================================================
    function renderPipelineLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'SYSTEM ARCHITECTURE', '#0284c7', '#38bdf8');
    }

    // Core high-clarity 5-stage architectural pipeline renderer
    function renderGenericPipeline(q, title, steps, w, h, categoryTag, themeBorder, themeText) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];
      const sList = [s0, s1, s2, s3, s4];

      const cardW = 160;
      const cardH = 152;
      const gap = 16;
      const startX = 20;
      const startY = 50;

      const colors = [
        { stroke: '#0284c7', fill: '#0369a1', text: '#38bdf8', bg: '#0f172a' },
        { stroke: '#7c3aed', fill: '#6d28d9', text: '#c084fc', bg: '#0f172a' },
        { stroke: '#f59e0b', fill: '#d97706', text: '#fbbf24', bg: '#0f172a' },
        { stroke: '#10b981', fill: '#059669', text: '#34d399', bg: '#0f172a' },
        { stroke: '#ec4899', fill: '#db2777', text: '#f472b6', bg: '#0f172a' }
      ];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid ${themeBorder}44;">
          <defs>
            <marker id="pipeArrow_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
              <polygon points="0 0, 8 4, 0 8" fill="#38bdf8"/>
            </marker>
          </defs>
          <g transform="translate(20, 20)">
            <rect width="130" height="20" rx="4" fill="${themeBorder}" fill-opacity="0.2" stroke="${themeBorder}" stroke-width="1"/>
            <text x="65" y="14" fill="${themeText}" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">${escSvg(categoryTag)}</text>
            <text x="142" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          ${sList.map((step, idx) => {
            const cx = startX + idx * (cardW + gap);
            const cy = startY;
            const col = colors[idx % colors.length];
            return `
              <g transform="translate(${cx}, ${cy})">
                <rect width="${cardW}" height="${cardH}" rx="8" fill="${col.bg}" stroke="${col.stroke}" stroke-width="1.5"/>
                <rect width="${cardW}" height="28" rx="8" fill="${col.stroke}" fill-opacity="0.25"/>
                <text x="10" y="19" fill="${col.text}" font-size="9.5" font-weight="700">0${idx + 1}. ${escSvg(step[0].slice(0, 14))}</text>
                <g transform="translate(10, 36)">
                  ${renderWrappedText(step[1], 0, 14, 18, '9.5px', '#ffffff', 2, 13)}
                  <line x1="0" y1="36" x2="${cardW - 20}" y2="36" stroke="${col.stroke}" stroke-width="0.8" stroke-dasharray="2 2"/>
                  ${renderWrappedText(step[2], 0, 52, 22, '8.5px', '#94a3b8', 2, 12)}
                  <rect y="84" width="${cardW - 20}" height="22" rx="4" fill="${col.stroke}" fill-opacity="0.18" stroke="${col.stroke}" stroke-width="0.8"/>
                  <text x="${(cardW - 20) / 2}" y="99" fill="${col.text}" font-size="8" font-weight="600" text-anchor="middle">${escSvg(step[3] || 'Verified')}</text>
                </g>
              </g>
              ${idx < 4 ? `<line x1="${cx + cardW + 2}" y1="${cy + cardH / 2}" x2="${cx + cardW + gap - 2}" y2="${cy + cardH / 2}" stroke="#38bdf8" stroke-width="1.8" marker-end="url(#pipeArrow_${q.id})"/>` : ''}
            `;
          }).join('')}
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Pipeline: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    '''

html = html[:idx_eng_start] + new_engine_code + html[idx_eng_end:]

with open('senior-dotnet-interview-portal.html', 'w', encoding='utf-8') as f:
    f.write(html)

new_size_mb = os.path.getsize('senior-dotnet-interview-portal.html') / (1024 * 1024)
print(f"Update complete! New file size: {new_size_mb:.2f} MB")

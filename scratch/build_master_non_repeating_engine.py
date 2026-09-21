import os
import sys

print("Building Master Non-Repeating Multi-Topology Architecture Visual Engine...")

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

# 2. Update Engine Code
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
    // Zero hardcoded mock text. Over 19 radically different geometric visual topologies.
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

    function renderWrappedText(text, x, y, maxChars, fontSize, color, maxLines = 2, lineHeight = 12, anchor = 'start') {
      const lines = wrapText(text, maxChars).slice(0, maxLines);
      return lines.map((line, idx) => {
        return `<text x="${x}" y="${y + idx * lineHeight}" fill="${color}" font-size="${fontSize}" text-anchor="${anchor}">${escSvg(line)}</text>`;
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

      // 1. AI & LLM / RAG / Semantic Kernel -> Neural Vector Circuit Topology
      if (cat === 'dotnet-ai' || anyWord(tLow, ['ai', 'llm', 'rag', 'gpt', 'openai', 'chatgpt', 'embedding', 'embeddings', 'vector search', 'vector db', 'tokens', 'prompt', 'prompts', 'hallucination', 'semantic kernel', 'langchain'])) {
        return renderAiRagLayout(q, cleanTitle, steps, w, h);
      }

      // 2. React, Virtual DOM, Fiber, Hooks -> Dual-Tree Reconciler Topology
      if (cat === 'react' || anyWord(tLow, ['react', 'virtual dom', 'fiber', 'reconcil', 'hook', 'hooks', 'useeffect', 'usestate', 'usememo', 'usecallback', 'props', 'jsx'])) {
        return renderFiberLayout(q, cleanTitle, steps, w, h);
      }

      // 3. Redux, Event Loop, Circular Cycles -> Orbital Cyclotron Topology
      if (cat === 'redux' || anyWord(tLow, ['redux', 'action', 'actions', 'reducer', 'reducers', 'dispatch', 'store', 'unidirectional', 'state machine', 'cyclotron'])) {
        return renderCycleLayout(q, cleanTitle, steps, w, h);
      }

      // 4. OOP, SOLID, Design Patterns, LLD -> UML Class Contract & VTable Dispatch Topology
      if (cat === 'oop' || cat === 'patterns' || cat === 'lld' || anyWord(tLow, ['solid', 'polymorphism', 'polymorphic', 'encapsulation', 'inheritance', 'abstract class', 'interface', 'factory', 'singleton', 'dependency inversion', 'liskov', 'coupling', 'cohesion', 'vtable', 'class vs struct', 'oop'])) {
        return renderOopClassLayout(q, cleanTitle, steps, w, h);
      }

      // 5. Entity Framework Core & LINQ -> 3-Tier ORM with Change Tracker State Bubbles
      if (cat === 'efcore' || cat === 'linq' || anyWord(tLow, ['dbcontext', 'change tracker', 'entity framework', 'ef core', 'lazy loading', 'eager loading', 'linq', 'iqueryable', 'ienumerable', 'migration', 'n+1', 'hasdata', 'fluent api'])) {
        return renderEfCoreLayout(q, cleanTitle, steps, w, h);
      }

      // 6. SQL Engine & B-Tree Indexing -> B-Tree Tree or Relational Plan Tree
      if (cat === 'sql' || anyWord(tLow, ['sql', 'query plan', 'execution plan', 'acid', 'transaction', 'isolation level', 'deadlock', 'join', 'stored procedure', 'clustered', 'non-clustered', 'b-tree', 'index seek', 'index scan', 'page split'])) {
        if (anyWord(tLow, ['b-tree', 'btree', 'index seek', 'index scan', 'clustered index', 'non-clustered index', 'page split', 'fill factor'])) {
          return renderBTreeLayout(q, cleanTitle, steps, w, h);
        }
        return renderSqlEngineLayout(q, cleanTitle, steps, w, h);
      }

      // 7. Microservices Outbox & Event Streaming -> Multi-Lane Swimlane Topology
      if (anyWord(tLow, ['outbox', 'kafka', 'rabbitmq', 'cdc', 'debezium', 'event sourcing', 'cqrs', 'saga', 'distributed transaction', 'two phase commit', '2pc'])) {
        return renderDistributedLayout(q, cleanTitle, steps, w, h);
      }

      // 8. Pub-Sub & Message Broker Fanout
      if (anyWord(tLow, ['pub/sub', 'pubsub', 'sns', 'eventbridge', 'fanout', 'topic', 'broker', 'message broker', 'exchange'])) {
        return renderPubSubLayout(q, cleanTitle, steps, w, h);
      }

      // 9. Multi-Tier Cache Hierarchy
      if (anyWord(tLow, ['multi-tier', 'cache-aside', 'two-tier', 'l1', 'l2', 'cache invalidation', 'distributed cache'])) {
        return renderCacheTierLayout(q, cleanTitle, steps, w, h);
      }

      // 10. Cloud Architecture, AWS, Serverless, HLD -> Multi-AZ Network Topology
      if (cat === 'cloud' || cat === 'aws' || cat === 'hld' || (cat === 'architecture' && anyWord(tLow, ['cloud', 'aws', 'azure', 'serverless', 'lambda', 'container', 'docker', 'kubernetes', 's3', 'dynamodb', 'sqs', 'sns', 'gateway', 'microservice']))) {
        return renderCloudInfraLayout(q, cleanTitle, steps, w, h);
      }

      // 11. Concentric Russian-Doll Middleware
      if (anyWord(tLow, ['middleware', 'request delegate', 'russian doll', 'concentric'])) {
        return renderMiddlewareLayout(q, cleanTitle, steps, w, h);
      }

      // 12. Web API, MVC, Routing -> Staggered Request-Response Flow
      if (cat === 'webapi' || cat === 'mvc' || anyWord(tLow, ['http', 'controller', 'action filter', 'model binding', 'rest', 'status code', 'kestrel', 'endpoint', 'minimal api', 'content negotiation'])) {
        return renderHttpFlowLayout(q, cleanTitle, steps, w, h);
      }

      // 13. Security, Auth, Identity, Cryptography -> 3-Part Token Anatomy & Crypto Vault
      if (cat === 'security' || anyWord(tLow, ['jwt', 'oauth', 'token', 'cryptography', 'encryption', 'hash', 'csrf', 'xss', 'sql injection', 'identity', 'claims', 'authentication', 'authorization', 'cors', 'ssl', 'tls'])) {
        return renderSecurityLayout(q, cleanTitle, steps, w, h);
      }

      // 14. Testing, CI/CD, QA -> Triangular Testing Pyramid Topology
      if (cat === 'testing' || anyWord(tLow, ['unit test', 'integration test', 'xunit', 'nunit', 'mock', 'moq', 'assert', 'tdd', 'test pyramid', 'sonarqube', 'code coverage', 'stub', 'fake'])) {
        return renderTestingLayout(q, cleanTitle, steps, w, h);
      }

      // 15. JavaScript Engine -> V8 Multi-Compartment Runtime
      if (cat === 'js' || anyWord(tLow, ['javascript', 'v8', 'call stack', 'event loop', 'microtask', 'closure', 'hoisting', 'prototype', 'promise', 'macrotask', 'async in js'])) {
        return renderJsRuntimeLayout(q, cleanTitle, steps, w, h);
      }

      // 16. Async / Await -> 4-Phase Compiler State Machine Flowchart
      if (cat === 'async' || anyWord(tLow, ['async', 'await', 'task', 'threadpool', 'thread', 'movenext', 'iocp', 'deadlock', 'synchronizationcontext', 'channel', 'valuetask', 'cancellationtoken'])) {
        return renderAsyncLayout(q, cleanTitle, steps, w, h);
      }

      // 17. Low-level Memory, CLR, GC -> Stack vs Heap Dual-Tower Blueprint
      if (anyWord(tLow, ['box', 'boxing', 'unboxing', 'stack vs heap', 'stack and heap', 'value type', 'reference type', 'garbage collector', 'gc', 'generation', 'gen 0', 'gen 1', 'gen 2', 'loh', 'poh', 'managed code', 'unmanaged', 'span<t>', 'ref struct', 'stringbuilder', 'immutable', 'memory layout', 'struct vs class'])) {
        return renderMemoryLayout(q, cleanTitle, steps, w, h);
      }

      // 18. Coding Algorithms -> Memory Array Ribbon & Pointer Tape
      if (cat === 'coding' || anyWord(tLow, ['pointer', 'binary search', 'sliding window', 'array', 'subsequence', 'two sum', 'leetcode', 'sort', 'tree', 'linked list', 'dynamic programming', 'graph', 'recursion', 'backtracking'])) {
        return renderRibbonLayout(q, cleanTitle, steps, w, h);
      }

      // 19. SDLC, Git, Agile, DevOps -> Git Branching DAG Railway Graph
      if (cat === 'sdlc' || anyWord(tLow, ['git', 'agile', 'scrum', 'kanban', 'sprint', 'ci/cd', 'devops', 'pull request', 'branching', 'merge vs rebase'])) {
        return renderSdlcLayout(q, cleanTitle, steps, w, h);
      }

      // 20. Decision Tree / Branching / Caching Fallback -> Decision Diamond Flowchart
      if (anyWord(tLow, ['cache', 'redis', 'circuit breaker', 'tryparse', 'fallback', 'polly', 'switch', 'branch', 'if/else', 'strategy'])) {
        return renderBranchLayout(q, cleanTitle, steps, w, h);
      }

      // 21. Architecture General
      if (cat === 'architecture') {
        return renderCloudInfraLayout(q, cleanTitle, steps, w, h);
      }

      // 22. Default Enterprise Pipeline
      return renderPipelineLayout(q, cleanTitle, steps, w, h);
    }

    // =========================================================================
    // 1. UML CLASS CONTRACT & DYNAMIC VTABLE DISPATCH BLUEPRINT
    // ==========================================================================
    function renderOopClassLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(168, 85, 247, 0.35);">
          <defs>
            <marker id="oopInherit_${q.id}" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto">
              <polygon points="0 0, 9 5, 0 10" fill="none" stroke="#a855f7" stroke-width="1.8"/>
            </marker>
            <marker id="oopCall_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
              <polygon points="0 0, 8 4, 0 8" fill="#38bdf8"/>
            </marker>
          </defs>
          <g transform="translate(20, 20)">
            <rect width="100" height="20" rx="4" fill="#a855f7" fill-opacity="0.2" stroke="#a855f7" stroke-width="1"/>
            <text x="50" y="14" fill="#c084fc" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">UML CONTRACT</text>
            <text x="112" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
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
    // 2. EF CORE ORM CHANGE TRACKER & SQL GENERATOR (3-TIER DATA PIPELINE)
    // ==========================================================================
    function renderEfCoreLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(16, 185, 129, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="110" height="20" rx="4" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
            <text x="55" y="14" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">EF CORE / ORM</text>
            <text x="122" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Stage 1: LINQ AST Query -->
          <g transform="translate(20, 48)">
            <rect width="200" height="152" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <rect width="200" height="28" rx="8" fill="#0ea5e9" fill-opacity="0.25"/>
            <text x="12" y="19" fill="#38bdf8" font-size="9.5" font-weight="700">1. LINQ: ${escSvg(s0[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s0[1], 0, 14, 20, '9.5px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="180" y2="36" stroke="#0ea5e9" stroke-width="0.8" stroke-dasharray="2 2"/>
              ${renderWrappedText(s0[2], 0, 52, 23, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="180" height="22" rx="4" fill="#075985" stroke="#38bdf8" stroke-width="0.8"/>
              <text x="90" y="99" fill="#e0f2fe" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s0[3] || 'Queryable')}</text>
            </g>
          </g>
          <!-- Stage 2: Change Tracker State Bubbles -->
          <g transform="translate(235, 48)">
            <rect width="210" height="152" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
            <rect width="210" height="28" rx="8" fill="#f59e0b" fill-opacity="0.25"/>
            <text x="12" y="19" fill="#fbbf24" font-size="9.5" font-weight="700">2. TRACKER: ${escSvg(s1[0])}</text>
            <g transform="translate(10, 36)">
              <rect width="190" height="24" rx="4" fill="#1e293b"/>
              <text x="10" y="16" fill="#cbd5e1" font-size="8.5">EntityState.Unchanged</text>
              <rect y="28" width="190" height="26" rx="4" fill="#451a03" stroke="#f59e0b" stroke-width="1"/>
              <text x="10" y="44" fill="#fcd34d" font-size="8.5" font-weight="700">➔ ${escSvg(s1[1].slice(0, 18))}</text>
              <rect y="58" width="190" height="24" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
              <text x="10" y="74" fill="#6ee7b7" font-size="8.5" font-weight="700">+ ${escSvg(s2[0])}: ${escSvg(s2[1].slice(0, 14))}</text>
              <text x="95" y="104" fill="#94a3b8" font-size="7.5" text-anchor="middle">${escSvg(s1[2].slice(0, 28))}</text>
            </g>
          </g>
          <!-- Stage 3: AST SQL Translation -->
          <g transform="translate(460, 48)">
            <rect width="200" height="152" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
            <rect width="200" height="28" rx="8" fill="#a855f7" fill-opacity="0.25"/>
            <text x="12" y="19" fill="#c084fc" font-size="9.5" font-weight="700">3. SQL-GEN: ${escSvg(s2[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s2[1], 0, 14, 20, '9.5px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="180" y2="36" stroke="#a855f7" stroke-width="0.8" stroke-dasharray="2 2"/>
              ${renderWrappedText(s2[2], 0, 52, 23, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="180" height="22" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="0.8"/>
              <text x="90" y="99" fill="#d8b4fe" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s2[3] || 'Raw SQL')}</text>
            </g>
          </g>
          <!-- Stage 4: Database Execution -->
          <g transform="translate(675, 48)">
            <rect width="205" height="152" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="205" height="28" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="12" y="19" fill="#34d399" font-size="9.5" font-weight="700">4. DB-COMMIT: ${escSvg(s3[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s3[1], 0, 14, 21, '9.5px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="185" y2="36" stroke="#10b981" stroke-width="0.8"/>
              ${renderWrappedText(s3[2], 0, 52, 24, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="185" height="22" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
              <text x="92" y="99" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">ACID: ${escSvg(s4[0])}</text>
            </g>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ ORM Flow: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 3. SQL RELATIONAL ENGINE, OPTIMIZER & BUFFER POOL (PLAN TREE)
    // ==========================================================================
    function renderSqlEngineLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(59, 130, 246, 0.35);">
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
    // 4. B-TREE HIERARCHICAL TREE LAYOUT
    // ==========================================================================
    function renderBTreeLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(16, 185, 129, 0.35);">
          <g transform="translate(20, 18)">
            <rect width="110" height="20" rx="4" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
            <text x="55" y="14" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">TREE HIERARCHY</text>
            <text x="122" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Level 0: Root Page -->
          <g transform="translate(330, 44)">
            <rect width="240" height="42" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
            <rect width="240" height="18" rx="6" fill="#10b981" fill-opacity="0.25"/>
            <text x="120" y="13" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">ROOT NODE: ${escSvg(s0[0])}</text>
            <text x="120" y="32" fill="#f8fafc" font-size="9" font-weight="600" text-anchor="middle">${escSvg(s0[1].slice(0, 32))}</text>
          </g>
          <line x1="390" y1="86" x2="220" y2="104" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
          <line x1="510" y1="86" x2="680" y2="104" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
          <!-- Level 1: Branch Nodes -->
          <g transform="translate(100, 104)">
            <rect width="240" height="44" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="120" y="16" fill="#38bdf8" font-size="8.5" font-weight="700" text-anchor="middle">BRANCH 1: ${escSvg(s1[0])}</text>
            <text x="120" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">${escSvg(s1[1].slice(0, 32))}</text>
          </g>
          <g transform="translate(560, 104)">
            <rect width="240" height="44" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="120" y="16" fill="#38bdf8" font-size="8.5" font-weight="700" text-anchor="middle">BRANCH 2: ${escSvg(s2[0])}</text>
            <text x="120" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">${escSvg(s2[1].slice(0, 32))}</text>
          </g>
          <line x1="180" y1="148" x2="110" y2="166" stroke="#0ea5e9" stroke-width="1.2"/>
          <line x1="260" y1="148" x2="330" y2="166" stroke="#0ea5e9" stroke-width="1.2"/>
          <line x1="640" y1="148" x2="570" y2="166" stroke="#0ea5e9" stroke-width="1.2"/>
          <line x1="720" y1="148" x2="790" y2="166" stroke="#0ea5e9" stroke-width="1.2"/>
          <!-- Level 2: Leaf Pages -->
          <g transform="translate(20, 166)">
            <rect width="180" height="52" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
            <text x="90" y="16" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">LEAF: ${escSvg(s3[0])}</text>
            <text x="90" y="30" fill="#a7f3d0" font-size="8" text-anchor="middle">${escSvg(s3[1].slice(0, 22))}</text>
            <text x="90" y="44" fill="#34d399" font-size="7.5" font-weight="600" text-anchor="middle">${escSvg(s3[3] || 'Leaf Page')}</text>
          </g>
          <g transform="translate(240, 166)">
            <rect width="180" height="52" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
            <text x="90" y="16" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">${escSvg(s4[0])}</text>
            <text x="90" y="30" fill="#a7f3d0" font-size="8" text-anchor="middle">${escSvg(s4[1].slice(0, 22))}</text>
            <text x="90" y="44" fill="#34d399" font-size="7.5" font-weight="600" text-anchor="middle">${escSvg(s4[3] || 'Data Row')}</text>
          </g>
          <g transform="translate(480, 166)">
            <rect width="180" height="52" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
            <text x="90" y="16" fill="#c7d2fe" font-size="8.5" font-weight="700" text-anchor="middle">BUFFER POOL</text>
            <text x="90" y="30" fill="#a5b4fc" font-size="8" text-anchor="middle">${escSvg(s2[2].slice(0, 22))}</text>
            <text x="90" y="44" fill="#38bdf8" font-size="7.5" font-weight="600" text-anchor="middle">&lt; 0.1ms Memory Hit</text>
          </g>
          <g transform="translate(700, 166)">
            <rect width="180" height="52" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
            <text x="90" y="16" fill="#f8fafc" font-size="8.5" font-weight="700" text-anchor="middle">SEEK TRAVERSAL</text>
            <text x="90" y="30" fill="#94a3b8" font-size="8" text-anchor="middle">O(log N) Complexity</text>
            <text x="90" y="44" fill="#cbd5e1" font-size="7.5" font-weight="600" text-anchor="middle">Linked Nodes &lt;---&gt;</text>
          </g>
          <!-- Bottom Flow Track -->
          <g transform="translate(20, 228)">
            <rect width="860" height="20" rx="3" fill="#0f172a" stroke="#334155" stroke-width="0.8"/>
            <text x="430" y="14" fill="#cbd5e1" font-size="8" font-weight="600" text-anchor="middle">➔ Tree Traversal: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 5. GENERATIVE AI & VECTOR RAG PIPELINE (NEURAL VECTOR CIRCUIT)
    // ==========================================================================
    function renderAiRagLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(236, 72, 153, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="130" height="20" rx="4" fill="#ec4899" fill-opacity="0.2" stroke="#ec4899" stroke-width="1"/>
            <text x="65" y="14" fill="#f472b6" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">NEURAL RAG CIRCUIT</text>
            <text x="142" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Stage 1: User Prompt Bubble -->
          <g transform="translate(20, 48)">
            <rect width="160" height="152" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <rect width="160" height="28" rx="8" fill="#38bdf8" fill-opacity="0.25"/>
            <text x="10" y="19" fill="#7dd3fc" font-size="9.5" font-weight="700">1. QUERY: ${escSvg(s0[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s0[1], 0, 14, 18, '9.5px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="140" y2="36" stroke="#38bdf8" stroke-width="0.8" stroke-dasharray="2 2"/>
              ${renderWrappedText(s0[2], 0, 52, 21, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="140" height="22" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="0.8"/>
              <text x="70" y="99" fill="#e0f2fe" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s0[3] || 'User Intent')}</text>
            </g>
          </g>
          <!-- Neural Connector 1 -->
          <line x1="182" y1="124" x2="198" y2="124" stroke="#ec4899" stroke-width="2"/>
          <!-- Stage 2: Dense Embedding Tensor -->
          <g transform="translate(200, 48)">
            <rect width="165" height="152" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
            <rect width="165" height="28" rx="8" fill="#a855f7" fill-opacity="0.25"/>
            <text x="10" y="19" fill="#c084fc" font-size="9.5" font-weight="700">2. EMBED: ${escSvg(s1[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s1[1], 0, 14, 18, '9.5px', '#ffffff', 2, 13)}
              <rect y="36" width="145" height="42" rx="4" fill="#18181b"/>
              <text x="6" y="50" fill="#e879f9" font-size="7.5" font-family="monospace">[0.18, -0.42, 0.91]</text>
              <text x="6" y="66" fill="#e879f9" font-size="7.5" font-family="monospace">1536-dim Float Tensor</text>
              <rect y="84" width="145" height="22" rx="4" fill="#581c87" stroke="#a855f7" stroke-width="0.8"/>
              <text x="72" y="99" fill="#d8b4fe" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s1[3] || 'Dense Vector')}</text>
            </g>
          </g>
          <!-- Neural Connector 2 -->
          <line x1="367" y1="124" x2="383" y2="124" stroke="#ec4899" stroke-width="2"/>
          <!-- Stage 3: HNSW Vector Search -->
          <g transform="translate(385, 48)">
            <rect width="165" height="152" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
            <rect width="165" height="28" rx="8" fill="#ec4899" fill-opacity="0.25"/>
            <text x="10" y="19" fill="#f472b6" font-size="9.5" font-weight="700">3. STORE: ${escSvg(s2[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s2[1], 0, 14, 18, '9.5px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="145" y2="36" stroke="#ec4899" stroke-width="0.8" stroke-dasharray="2 2"/>
              ${renderWrappedText(s2[2], 0, 52, 21, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="145" height="22" rx="4" fill="#831843" stroke="#ec4899" stroke-width="0.8"/>
              <text x="72" y="99" fill="#fbcfe8" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s2[3] || 'Cosine top_k')}</text>
            </g>
          </g>
          <!-- Neural Connector 3 -->
          <line x1="552" y1="124" x2="568" y2="124" stroke="#ec4899" stroke-width="2"/>
          <!-- Stage 4: Semantic Kernel Synthesis -->
          <g transform="translate(570, 48)">
            <rect width="165" height="152" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
            <rect width="165" height="28" rx="8" fill="#6366f1" fill-opacity="0.25"/>
            <text x="10" y="19" fill="#a5b4fc" font-size="9.5" font-weight="700">4. LLM: ${escSvg(s3[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s3[1], 0, 14, 18, '9.5px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="145" y2="36" stroke="#6366f1" stroke-width="0.8" stroke-dasharray="2 2"/>
              ${renderWrappedText(s3[2], 0, 52, 21, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="145" height="22" rx="4" fill="#312e81" stroke="#6366f1" stroke-width="0.8"/>
              <text x="72" y="99" fill="#c7d2fe" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s3[3] || 'Prompt Grounding')}</text>
            </g>
          </g>
          <!-- Neural Connector 4 -->
          <line x1="737" y1="124" x2="753" y2="124" stroke="#ec4899" stroke-width="2"/>
          <!-- Stage 5: Grounded Output -->
          <g transform="translate(755, 48)">
            <rect width="125" height="152" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="125" height="28" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="8" y="19" fill="#34d399" font-size="9" font-weight="700">5. ${escSvg(s4[0])}</text>
            <g transform="translate(8, 36)">
              ${renderWrappedText(s4[1], 0, 14, 14, '9px', '#ffffff', 2, 12)}
              <line x1="0" y1="36" x2="109" y2="36" stroke="#10b981" stroke-width="0.8"/>
              ${renderWrappedText(s4[2], 0, 52, 16, '8px', '#94a3b8', 2, 11)}
              <rect y="84" width="109" height="22" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
              <text x="54" y="99" fill="#6ee7b7" font-size="7.5" font-weight="700" text-anchor="middle">✓ Verified</text>
            </g>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ RAG Chain: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 6. CLOUD DISTRIBUTED INFRASTRUCTURE (MULTI-AZ TOPOLOGY)
    // ==========================================================================
    function renderCloudInfraLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(14, 165, 233, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="135" height="20" rx="4" fill="#0ea5e9" fill-opacity="0.2" stroke="#0ea5e9" stroke-width="1"/>
            <text x="67" y="14" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">CLOUD TOPOLOGY</text>
            <text x="147" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Zone 1: Edge & Ingress -->
          <g transform="translate(20, 48)">
            <rect width="200" height="152" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
            <rect width="200" height="28" rx="8" fill="#0284c7" fill-opacity="0.25"/>
            <text x="12" y="19" fill="#38bdf8" font-size="9.5" font-weight="700">EDGE: ${escSvg(s0[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s0[1], 0, 14, 20, '9.5px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="180" y2="36" stroke="#0284c7" stroke-width="0.8"/>
              ${renderWrappedText(s0[2], 0, 52, 23, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="180" height="22" rx="4" fill="#0c4a6e" stroke="#0284c7" stroke-width="0.8"/>
              <text x="90" y="99" fill="#7dd3fc" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s0[3] || 'Global Ingress')}</text>
            </g>
          </g>
          <!-- Zone 2: Compute Tier (Multi-AZ) -->
          <g transform="translate(235, 48)">
            <rect width="210" height="152" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
            <rect width="210" height="28" rx="8" fill="#6366f1" fill-opacity="0.25"/>
            <text x="12" y="19" fill="#a5b4fc" font-size="9.5" font-weight="700">COMPUTE: ${escSvg(s1[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s1[1], 0, 14, 21, '9.5px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="190" y2="36" stroke="#6366f1" stroke-width="0.8"/>
              ${renderWrappedText(s1[2], 0, 52, 25, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="190" height="22" rx="4" fill="#312e81" stroke="#6366f1" stroke-width="0.8"/>
              <text x="95" y="99" fill="#c7d2fe" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s1[3] || 'Multi-AZ Auto-Scale')}</text>
            </g>
          </g>
          <!-- Zone 3: Messaging / Event Bus -->
          <g transform="translate(460, 48)">
            <rect width="200" height="152" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
            <rect width="200" height="28" rx="8" fill="#f59e0b" fill-opacity="0.25"/>
            <text x="12" y="19" fill="#fbbf24" font-size="9.5" font-weight="700">EVENT BUS: ${escSvg(s2[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s2[1], 0, 14, 20, '9.5px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="180" y2="36" stroke="#f59e0b" stroke-width="0.8"/>
              ${renderWrappedText(s2[2], 0, 52, 23, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="180" height="22" rx="4" fill="#451a03" stroke="#f59e0b" stroke-width="0.8"/>
              <text x="90" y="99" fill="#fde68a" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s2[3] || 'Decoupled Flow')}</text>
            </g>
          </g>
          <!-- Zone 4: Persistence Tier -->
          <g transform="translate(675, 48)">
            <rect width="205" height="152" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="205" height="28" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="12" y="19" fill="#34d399" font-size="9.5" font-weight="700">DATA TIER: ${escSvg(s3[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s3[1], 0, 14, 21, '9.5px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="185" y2="36" stroke="#10b981" stroke-width="0.8"/>
              ${renderWrappedText(s3[2], 0, 52, 24, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="185" height="22" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
              <text x="92" y="99" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">SLA: ${escSvg(s4[0])}</text>
            </g>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Cloud Flow: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 7. TRANSACTIONAL OUTBOX & EVENT STREAMING (MULTI-LANE SWIMLANES)
    // ==========================================================================
    function renderDistributedLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(249, 115, 22, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="150" height="20" rx="4" fill="#f97316" fill-opacity="0.2" stroke="#f97316" stroke-width="1"/>
            <text x="75" y="14" fill="#fb923c" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">DISTRIBUTED STREAM</text>
            <text x="162" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- 4 Horizontal Swimlanes -->
          <g transform="translate(20, 48)">
            <!-- Lane 1: Domain & Outbox -->
            <g transform="translate(0, 0)">
              <rect width="860" height="34" rx="5" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.2"/>
              <rect width="180" height="34" rx="5" fill="#0284c7" fill-opacity="0.3"/>
              <text x="90" y="21" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle">LANE 1: ${escSvg(s0[0])}</text>
              <text x="200" y="21" fill="#f8fafc" font-size="9" font-weight="600">${escSvg(s0[1])} — ${escSvg(s0[2].slice(0, 50))}</text>
            </g>
            <!-- Lane 2: CDC Log Miner -->
            <g transform="translate(0, 38)">
              <rect width="860" height="34" rx="5" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
              <rect width="180" height="34" rx="5" fill="#d97706" fill-opacity="0.3"/>
              <text x="90" y="21" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">LANE 2: ${escSvg(s1[0])}</text>
              <text x="200" y="21" fill="#f8fafc" font-size="9" font-weight="600">${escSvg(s1[1])} — ${escSvg(s1[2].slice(0, 50))}</text>
            </g>
            <!-- Lane 3: Kafka Partitions -->
            <g transform="translate(0, 76)">
              <rect width="860" height="34" rx="5" fill="#0f172a" stroke="#f97316" stroke-width="1.2"/>
              <rect width="180" height="34" rx="5" fill="#ea580c" fill-opacity="0.3"/>
              <text x="90" y="21" fill="#fb923c" font-size="9" font-weight="700" text-anchor="middle">LANE 3: ${escSvg(s2[0])}</text>
              <text x="200" y="21" fill="#f8fafc" font-size="9" font-weight="600">${escSvg(s2[1])} — ${escSvg(s2[2].slice(0, 50))}</text>
            </g>
            <!-- Lane 4: Consumer & Deduplication -->
            <g transform="translate(0, 114)">
              <rect width="860" height="36" rx="5" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
              <rect width="180" height="36" rx="5" fill="#059669" fill-opacity="0.3"/>
              <text x="90" y="22" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">LANE 4: ${escSvg(s3[0])}</text>
              <text x="200" y="22" fill="#f8fafc" font-size="9" font-weight="600">${escSvg(s3[1])} ➔ ${escSvg(s4[0])}: ${escSvg(s4[1].slice(0, 36))}</text>
            </g>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Stream: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 8. 1-TO-MANY STAR FANOUT EVENT BUS TOPOLOGY
    // ==========================================================================
    function renderPubSubLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(236, 72, 153, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="115" height="20" rx="4" fill="#ec4899" fill-opacity="0.2" stroke="#ec4899" stroke-width="1"/>
            <text x="57" y="14" fill="#f472b6" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">EVENT FANOUT</text>
            <text x="127" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Left: Event Publisher -->
          <g transform="translate(20, 60)">
            <rect width="210" height="130" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <rect width="210" height="28" rx="8" fill="#0ea5e9" fill-opacity="0.25"/>
            <text x="105" y="19" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle">PUBLISHER: ${escSvg(s0[0])}</text>
            <g transform="translate(10, 36)">
              ${renderWrappedText(s0[1], 0, 14, 21, '9.5px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="190" y2="36" stroke="#0ea5e9" stroke-width="0.8"/>
              ${renderWrappedText(s0[2], 0, 52, 24, '8.5px', '#94a3b8', 2, 12)}
            </g>
          </g>
          <!-- Center: Event Broker / Exchange -->
          <g transform="translate(280, 75)">
            <polygon points="80,0 160,50 80,100 0,50" fill="#1e1b4b" stroke="#ec4899" stroke-width="2"/>
            <text x="80" y="44" fill="#f472b6" font-size="9" font-weight="700" text-anchor="middle">BROKER</text>
            <text x="80" y="58" fill="#fbcfe8" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s1[0])}</text>
          </g>
          <!-- Connectors to subscribers -->
          <line x1="230" y1="125" x2="280" y2="125" stroke="#38bdf8" stroke-width="2"/>
          <line x1="440" y1="110" x2="520" y2="65" stroke="#ec4899" stroke-width="1.8"/>
          <line x1="440" y1="125" x2="520" y2="125" stroke="#ec4899" stroke-width="1.8"/>
          <line x1="440" y1="140" x2="520" y2="185" stroke="#ec4899" stroke-width="1.8"/>
          <!-- Right: Fanout Subscribers -->
          <g transform="translate(520, 48)">
            <rect width="360" height="42" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
            <text x="12" y="18" fill="#6ee7b7" font-size="8.5" font-weight="700">SUB 1: ${escSvg(s2[0])} — ${escSvg(s2[1].slice(0, 24))}</text>
            <text x="12" y="32" fill="#94a3b8" font-size="8">${escSvg(s2[2].slice(0, 42))}</text>
          </g>
          <g transform="translate(520, 102)">
            <rect width="360" height="42" rx="6" fill="#0f172a" stroke="#6366f1" stroke-width="1.2"/>
            <text x="12" y="18" fill="#a5b4fc" font-size="8.5" font-weight="700">SUB 2: ${escSvg(s3[0])} — ${escSvg(s3[1].slice(0, 24))}</text>
            <text x="12" y="32" fill="#94a3b8" font-size="8">${escSvg(s3[2].slice(0, 42))}</text>
          </g>
          <g transform="translate(520, 156)">
            <rect width="360" height="42" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
            <text x="12" y="18" fill="#fcd34d" font-size="8.5" font-weight="700">SUB 3: ${escSvg(s4[0])} — ${escSvg(s4[1].slice(0, 24))}</text>
            <text x="12" y="32" fill="#94a3b8" font-size="8">${escSvg(s4[2].slice(0, 42))}</text>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Fanout: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ [${escSvg(s2[0])} | ${escSvg(s3[0])} | ${escSvg(s4[0])}]</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 9. MULTI-TIER CACHE HIERARCHY TOPOLOGY
    // ==========================================================================
    function renderCacheTierLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(234, 179, 8, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="115" height="20" rx="4" fill="#eab308" fill-opacity="0.2" stroke="#eab308" stroke-width="1"/>
            <text x="57" y="14" fill="#facc15" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">CACHE TIERS</text>
            <text x="127" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- 3 Vertical Tiers -->
          <g transform="translate(20, 48)">
            <!-- Tier 1: L1 Memory Cache -->
            <rect width="860" height="44" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
            <text x="16" y="22" fill="#6ee7b7" font-size="9.5" font-weight="700">TIER 1 (L1 IN-MEMORY): ${escSvg(s0[0])}</text>
            <text x="16" y="36" fill="#a7f3d0" font-size="8.5">${escSvg(s0[1])} — ${escSvg(s0[2].slice(0, 48))} (&lt; 0.01ms)</text>
            <text x="830" y="26" fill="#34d399" font-size="8.5" font-weight="700" text-anchor="end">RAM SPEED</text>
            <!-- Tier 2: L2 Distributed Cache -->
            <g transform="translate(0, 52)">
              <rect width="860" height="44" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
              <text x="16" y="22" fill="#a5b4fc" font-size="9.5" font-weight="700">TIER 2 (L2 DISTRIBUTED): ${escSvg(s1[0])}</text>
              <text x="16" y="36" fill="#c7d2fe" font-size="8.5">${escSvg(s1[1])} — ${escSvg(s2[1].slice(0, 48))} (~1.0ms)</text>
              <text x="830" y="26" fill="#818cf8" font-size="8.5" font-weight="700" text-anchor="end">REDIS CLUSTER</text>
            </g>
            <!-- Tier 3: L3 Persistent Storage -->
            <g transform="translate(0, 104)">
              <rect width="860" height="44" rx="6" fill="#451a03" stroke="#f59e0b" stroke-width="1.5"/>
              <text x="16" y="22" fill="#fcd34d" font-size="9.5" font-weight="700">TIER 3 (L3 PERSISTENCE): ${escSvg(s3[0])}</text>
              <text x="16" y="36" fill="#fde68a" font-size="8.5">${escSvg(s3[1])} — ${escSvg(s4[1].slice(0, 48))} (~20ms)</text>
              <text x="830" y="26" fill="#fbbf24" font-size="8.5" font-weight="700" text-anchor="end">SQL / DISK</text>
            </g>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Cache Fallback: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 10. CONCENTRIC RUSSIAN-DOLL MIDDLEWARE PIPELINE
    // ==========================================================================
    function renderMiddlewareLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(139, 92, 246, 0.35);">
          <g transform="translate(20, 18)">
            <rect width="130" height="20" rx="4" fill="#8b5cf6" fill-opacity="0.2" stroke="#8b5cf6" stroke-width="1"/>
            <text x="65" y="14" fill="#c4b5fd" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">MIDDLEWARE ONION</text>
            <text x="142" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <g transform="translate(20, 46)">
            <!-- Layer 1: Outermost Ring -->
            <rect width="860" height="174" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.8"/>
            <text x="24" y="22" fill="#c4b5fd" font-size="9" font-weight="700">LAYER 1: ${escSvg(s0[0])} — ${escSvg(s0[1].slice(0, 36))}</text>
            <!-- Layer 2: Intermediate Ring -->
            <rect x="30" y="28" width="800" height="128" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
            <text x="54" y="48" fill="#a5b4fc" font-size="9" font-weight="700">LAYER 2: ${escSvg(s1[0])} — ${escSvg(s1[1].slice(0, 36))}</text>
            <!-- Layer 3: Inner Ring -->
            <rect x="60" y="54" width="740" height="88" rx="6" fill="#31104b" stroke="#d946ef" stroke-width="1.5"/>
            <text x="84" y="72" fill="#f0abfc" font-size="9" font-weight="700">LAYER 3: ${escSvg(s2[0])} — ${escSvg(s2[1].slice(0, 36))}</text>
            <!-- Core Center -->
            <rect x="90" y="80" width="680" height="50" rx="5" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
            <text x="430" y="100" fill="#ffffff" font-size="10.5" font-weight="700" text-anchor="middle">★ CORE: ${escSvg(s3[0])} — ${escSvg(s3[1].slice(0, 42))}</text>
            <text x="430" y="116" fill="#6ee7b7" font-size="8.5" text-anchor="middle">await next(context) completes ➔ ${escSvg(s4[0])}: ${escSvg(s4[1].slice(0, 30))} (Unwinds in reverse)</text>
          </g>
          <!-- Bottom Flow Track -->
          <g transform="translate(20, 228)">
            <rect width="860" height="20" rx="3" fill="#0f172a" stroke="#334155" stroke-width="0.8"/>
            <text x="430" y="14" fill="#cbd5e1" font-size="8" font-weight="600" text-anchor="middle">➔ Onion Flow: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 11. ASP.NET CORE HTTP REQUEST-RESPONSE PIPELINE (STAGGERED FLOW)
    // ==========================================================================
    function renderHttpFlowLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'HTTP & WEB API', '#38bdf8', '#7dd3fc');
    }

    // =========================================================================
    // 12. DEFENSE-IN-DEPTH TOKEN SEGMENTER & CRYPTO VAULT
    // ==========================================================================
    function renderSecurityLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(244, 63, 94, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="130" height="20" rx="4" fill="#f43f5e" fill-opacity="0.2" stroke="#f43f5e" stroke-width="1"/>
            <text x="65" y="14" fill="#fb7185" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">SECURITY &amp; IDENTITY</text>
            <text x="142" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Top Panel: 3-Segment Signed JWT Structure -->
          <g transform="translate(20, 48)">
            <!-- Segment 1: Header -->
            <rect width="270" height="74" rx="6" fill="#082f49" stroke="#0284c7" stroke-width="1.5"/>
            <text x="14" y="20" fill="#38bdf8" font-size="9" font-weight="700">1. HEADER: ${escSvg(s0[0])}</text>
            <text x="14" y="38" fill="#f8fafc" font-size="8.5" font-family="monospace">${escSvg(s0[1].slice(0, 26))}</text>
            <text x="14" y="54" fill="#7dd3fc" font-size="8">${escSvg(s0[2].slice(0, 32))}</text>
            <!-- Dot -->
            <circle cx="282" cy="37" r="4" fill="#f43f5e"/>
            <!-- Segment 2: Payload -->
            <g transform="translate(295, 0)">
              <rect width="270" height="74" rx="6" fill="#3b0764" stroke="#a855f7" stroke-width="1.5"/>
              <text x="14" y="20" fill="#d8b4fe" font-size="9" font-weight="700">2. PAYLOAD: ${escSvg(s1[0])}</text>
              <text x="14" y="38" fill="#f8fafc" font-size="8.5" font-family="monospace">${escSvg(s1[1].slice(0, 26))}</text>
              <text x="14" y="54" fill="#e9d5ff" font-size="8">${escSvg(s1[2].slice(0, 32))}</text>
            </g>
            <!-- Dot -->
            <circle cx="577" cy="37" r="4" fill="#f43f5e"/>
            <!-- Segment 3: Signature -->
            <g transform="translate(590, 0)">
              <rect width="270" height="74" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
              <text x="14" y="20" fill="#6ee7b7" font-size="9" font-weight="700">3. SIGNATURE: ${escSvg(s2[0])}</text>
              <text x="14" y="38" fill="#f8fafc" font-size="8.5" font-family="monospace">${escSvg(s2[1].slice(0, 26))}</text>
              <text x="14" y="54" fill="#a7f3d0" font-size="8">${escSvg(s2[2].slice(0, 32))}</text>
            </g>
          </g>
          <!-- Bottom Left: Claims Authorization -->
          <g transform="translate(20, 132)">
            <rect width="420" height="70" rx="6" fill="#0f172a" stroke="#6366f1" stroke-width="1.2"/>
            <text x="14" y="22" fill="#a5b4fc" font-size="9.5" font-weight="700">AUTH POLICIES: ${escSvg(s3[0])}</text>
            <text x="14" y="40" fill="#f8fafc" font-size="8.5">${escSvg(s3[1])}</text>
            <text x="14" y="56" fill="#94a3b8" font-size="8">${escSvg(s3[2].slice(0, 56))}</text>
          </g>
          <!-- Bottom Right: Cryptographic Vault -->
          <g transform="translate(460, 132)">
            <rect width="420" height="70" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
            <text x="14" y="22" fill="#34d399" font-size="9.5" font-weight="700">CRYPTOGRAPHIC VAULT: ${escSvg(s4[0])}</text>
            <text x="14" y="40" fill="#f8fafc" font-size="8.5">${escSvg(s4[1])}</text>
            <text x="14" y="56" fill="#94a3b8" font-size="8">${escSvg(s4[2].slice(0, 56))}</text>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Security Chain: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 13. TRIANGULAR TEST AUTOMATION PYRAMID & QUALITY GATES
    // ==========================================================================
    function renderTestingLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(16, 185, 129, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="110" height="20" rx="4" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
            <text x="55" y="14" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">TEST PYRAMID</text>
            <text x="122" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Left Panel: Layered Testing Pyramid -->
          <g transform="translate(20, 48)">
            <rect width="280" height="152" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="280" height="28" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="140" y="19" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">PYRAMID HIERARCHY</text>
            <!-- Top: E2E -->
            <polygon points="140,36 100,68 180,68" fill="#7f1d1d" stroke="#ef4444" stroke-width="1"/>
            <text x="140" y="60" fill="#fca5a5" font-size="8" font-weight="700" text-anchor="middle">E2E: ${escSvg(s0[0])}</text>
            <!-- Middle: Integration -->
            <polygon points="100,72 180,72 215,108 65,108" fill="#78350f" stroke="#f59e0b" stroke-width="1"/>
            <text x="140" y="94" fill="#fde68a" font-size="8" font-weight="700" text-anchor="middle">INT: ${escSvg(s1[0])}</text>
            <!-- Base: Unit Tests -->
            <polygon points="65,112 215,112 250,144 30,144" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
            <text x="140" y="132" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">UNIT: ${escSvg(s2[0])} (Fast)</text>
          </g>
          <!-- Center Panel: AAA Pattern Engine -->
          <g transform="translate(315, 48)">
            <rect width="270" height="152" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
            <rect width="270" height="28" rx="8" fill="#6366f1" fill-opacity="0.25"/>
            <text x="135" y="19" fill="#a5b4fc" font-size="9.5" font-weight="700" text-anchor="middle">AAA PATTERN: ${escSvg(s3[0])}</text>
            <g transform="translate(12, 36)">
              ${renderWrappedText(s3[1], 0, 14, 25, '10px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="246" y2="36" stroke="#6366f1" stroke-width="0.8"/>
              ${renderWrappedText(s3[2], 0, 52, 28, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="246" height="22" rx="4" fill="#312e81" stroke="#6366f1" stroke-width="0.8"/>
              <text x="123" y="99" fill="#c7d2fe" font-size="8.5" font-weight="600" text-anchor="middle">${escSvg(s3[3] || 'Assertions')}</text>
            </g>
          </g>
          <!-- Right Panel: Quality Gate -->
          <g transform="translate(600, 48)">
            <rect width="280" height="152" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="280" height="28" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="140" y="19" fill="#34d399" font-size="9.5" font-weight="700" text-anchor="middle">QUALITY GATE: ${escSvg(s4[0])}</text>
            <g transform="translate(12, 36)">
              ${renderWrappedText(s4[1], 0, 14, 26, '10px', '#ffffff', 2, 13)}
              <line x1="0" y1="36" x2="256" y2="36" stroke="#10b981" stroke-width="0.8"/>
              ${renderWrappedText(s4[2], 0, 52, 29, '8.5px', '#94a3b8', 2, 12)}
              <rect y="84" width="256" height="22" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
              <text x="128" y="99" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">✓ CI Quality Pass</text>
            </g>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Verification: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 14. V8 JAVASCRIPT ENGINE & EVENT LOOP RUNTIME (MULTI-COMPARTMENT)
    // ==========================================================================
    function renderJsRuntimeLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(245, 158, 11, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="135" height="20" rx="4" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="1"/>
            <text x="67" y="14" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">V8 JS RUNTIME</text>
            <text x="147" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Col 1: Call Stack -->
          <g transform="translate(20, 48)">
            <rect width="175" height="152" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
            <rect width="175" height="28" rx="8" fill="#0284c7" fill-opacity="0.25"/>
            <text x="10" y="19" fill="#38bdf8" font-size="9" font-weight="700">CALL STACK: ${escSvg(s0[0])}</text>
            <g transform="translate(8, 36)">
              <rect width="159" height="26" rx="4" fill="#075985" stroke="#38bdf8" stroke-width="0.8"/>
              <text x="80" y="17" fill="#e0f2fe" font-size="8" font-weight="700" text-anchor="middle">${escSvg(s0[1].slice(0, 18))}</text>
              <rect y="32" width="159" height="24" rx="4" fill="#1e293b"/>
              <text x="80" y="48" fill="#94a3b8" font-size="7.5" text-anchor="middle">${escSvg(s0[2].slice(0, 24))}</text>
              <rect y="84" width="159" height="22" rx="4" fill="#0c4a6e"/>
              <text x="80" y="99" fill="#7dd3fc" font-size="8" font-weight="600" text-anchor="middle">LIFO Execution</text>
            </g>
          </g>
          <!-- Col 2: Web APIs -->
          <g transform="translate(205, 48)">
            <rect width="175" height="152" rx="8" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5"/>
            <rect width="175" height="28" rx="8" fill="#7c3aed" fill-opacity="0.25"/>
            <text x="10" y="19" fill="#c084fc" font-size="9" font-weight="700">WEB APIS: ${escSvg(s1[0])}</text>
            <g transform="translate(8, 36)">
              <rect width="159" height="26" rx="4" fill="#1e1b4b"/>
              <text x="80" y="17" fill="#c7d2fe" font-size="8" text-anchor="middle">${escSvg(s1[1].slice(0, 20))}</text>
              <rect y="32" width="159" height="24" rx="4" fill="#312e81"/>
              <text x="80" y="48" fill="#a5b4fc" font-size="7.5" text-anchor="middle">${escSvg(s1[2].slice(0, 24))}</text>
              <rect y="84" width="159" height="22" rx="4" fill="#4c1d95"/>
              <text x="80" y="99" fill="#f5d0fe" font-size="8" font-weight="600" text-anchor="middle">Async C++ Threads</text>
            </g>
          </g>
          <!-- Center: Event Loop -->
          <g transform="translate(390, 48)">
            <rect width="120" height="152" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
            <circle cx="60" cy="56" r="30" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5 3"/>
            <text x="60" y="54" fill="#fbbf24" font-size="8.5" font-weight="700" text-anchor="middle">EVENT</text>
            <text x="60" y="66" fill="#fbbf24" font-size="8.5" font-weight="700" text-anchor="middle">LOOP</text>
            <g transform="translate(8, 100)">
              <rect width="104" height="42" rx="4" fill="#1e293b"/>
              <text x="52" y="16" fill="#6ee7b7" font-size="7" text-anchor="middle">1. Drain Micro</text>
              <text x="52" y="30" fill="#fcd34d" font-size="7" text-anchor="middle">2. Run 1 Macro</text>
            </g>
          </g>
          <!-- Col 3: Microtasks -->
          <g transform="translate(520, 48)">
            <rect width="175" height="152" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="175" height="28" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="10" y="19" fill="#34d399" font-size="9" font-weight="700">MICROTASKS: ${escSvg(s2[0])}</text>
            <g transform="translate(8, 36)">
              <rect width="159" height="26" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
              <text x="80" y="17" fill="#6ee7b7" font-size="8" font-weight="700" text-anchor="middle">${escSvg(s2[1].slice(0, 18))}</text>
              <rect y="32" width="159" height="24" rx="4" fill="#064e3b"/>
              <text x="80" y="48" fill="#a7f3d0" font-size="7.5" text-anchor="middle">${escSvg(s2[2].slice(0, 24))}</text>
              <rect y="84" width="159" height="22" rx="4" fill="#042f2e"/>
              <text x="80" y="99" fill="#34d399" font-size="8" font-weight="700" text-anchor="middle">★ RUNS FIRST</text>
            </g>
          </g>
          <!-- Col 4: Macrotasks -->
          <g transform="translate(705, 48)">
            <rect width="175" height="152" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1.5"/>
            <rect width="175" height="28" rx="8" fill="#d97706" fill-opacity="0.25"/>
            <text x="10" y="19" fill="#fcd34d" font-size="9" font-weight="700">MACROTASKS: ${escSvg(s3[0])}</text>
            <g transform="translate(8, 36)">
              <rect width="159" height="26" rx="4" fill="#451a03"/>
              <text x="80" y="17" fill="#fde68a" font-size="8" text-anchor="middle">${escSvg(s3[1].slice(0, 20))}</text>
              <rect y="32" width="159" height="24" rx="4" fill="#451a03"/>
              <text x="80" y="48" fill="#cbd5e1" font-size="7.5" text-anchor="middle">${escSvg(s3[2].slice(0, 24))}</text>
              <rect y="84" width="159" height="22" rx="4" fill="#1e293b"/>
              <text x="80" y="99" fill="#fcd34d" font-size="8" text-anchor="middle">Tick: ${escSvg(s4[0])}</text>
            </g>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Loop: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 15. UNIDIRECTIONAL ORBITAL CYCLOTRON STATE MACHINE
    // ==========================================================================
    function renderCycleLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(168, 85, 247, 0.35);">
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
    // 16. 4-PHASE ASYNC COMPILER STATE MACHINE
    // ==========================================================================
    function renderAsyncLayout(q, title, steps, w, h) {
      return renderGenericPipeline(q, title, steps, w, h, 'ASYNC STATE MACHINE', '#8b5cf6', '#c4b5fd');
    }

    // =========================================================================
    // 17. CLR MEMORY BLUEPRINT (STACK VS HEAP & GENERATIONAL GC)
    // ==========================================================================
    function renderMemoryLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(56, 189, 248, 0.35);">
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
    // 18. SPLIT-BRANCH DECISION FLOW (BRANCHING DIAMOND)
    // ==========================================================================
    function renderBranchLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(234, 179, 8, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="135" height="20" rx="4" fill="#eab308" fill-opacity="0.2" stroke="#eab308" stroke-width="1"/>
            <text x="67" y="14" fill="#facc15" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">DECISION BRANCH</text>
            <text x="147" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Input Node -->
          <g transform="translate(20, 95)">
            <rect width="180" height="60" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <text x="90" y="24" fill="#38bdf8" font-size="9.5" font-weight="700" text-anchor="middle">${escSvg(s0[0])}</text>
            <text x="90" y="42" fill="#cbd5e1" font-size="8.5" text-anchor="middle">${escSvg(s0[1].slice(0, 22))}</text>
          </g>
          <line x1="200" y1="125" x2="270" y2="125" stroke="#38bdf8" stroke-width="2"/>
          <!-- Decision Diamond -->
          <g transform="translate(270, 75)">
            <polygon points="55,0 110,50 55,100 0,50" fill="#1e293b" stroke="#eab308" stroke-width="2"/>
            <text x="55" y="46" fill="#fde047" font-size="8.5" font-weight="700" text-anchor="middle">${escSvg(s1[0].slice(0, 10))}</text>
            <text x="55" y="60" fill="#fde047" font-size="8" font-weight="600" text-anchor="middle">${escSvg(s1[1].slice(0, 12))}?</text>
          </g>
          <!-- Fast Path (Upper) -->
          <path d="M 325 75 L 325 45 L 430 45" fill="none" stroke="#10b981" stroke-width="2"/>
          <text x="365" y="38" fill="#34d399" font-size="8.5" font-weight="700">YES (Fast)</text>
          <g transform="translate(430, 20)">
            <rect width="210" height="52" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.8"/>
            <text x="105" y="22" fill="#6ee7b7" font-size="9.5" font-weight="700" text-anchor="middle">${escSvg(s2[0])}: ${escSvg(s2[1].slice(0, 16))}</text>
            <text x="105" y="38" fill="#a7f3d0" font-size="8" text-anchor="middle">${escSvg(s2[2].slice(0, 28))}</text>
          </g>
          <!-- Fallback Path (Lower) -->
          <path d="M 325 175 L 325 195 L 430 195" fill="none" stroke="#f59e0b" stroke-width="2"/>
          <text x="365" y="188" fill="#fbbf24" font-size="8.5" font-weight="700">NO (Fallback)</text>
          <g transform="translate(430, 168)">
            <rect width="210" height="52" rx="6" fill="#451a03" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="105" y="22" fill="#fcd34d" font-size="9.5" font-weight="700" text-anchor="middle">${escSvg(s3[0])}: ${escSvg(s3[1].slice(0, 16))}</text>
            <text x="105" y="38" fill="#fde68a" font-size="8" text-anchor="middle">${escSvg(s3[2].slice(0, 28))}</text>
          </g>
          <!-- Convergence Node -->
          <g transform="translate(680, 75)">
            <rect width="190" height="100" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
            <rect width="190" height="24" rx="8" fill="#6366f1" fill-opacity="0.25"/>
            <text x="95" y="16" fill="#a5b4fc" font-size="9" font-weight="700" text-anchor="middle">CONVERGENCE</text>
            <text x="95" y="44" fill="#cbd5e1" font-size="8.5" text-anchor="middle">${escSvg(s4[0])}: ${escSvg(s4[1].slice(0, 16))}</text>
            <text x="95" y="62" fill="#38bdf8" font-size="8" text-anchor="middle">${escSvg(s4[2].slice(0, 24))}</text>
            <text x="95" y="82" fill="#4ade80" font-size="8.5" font-weight="700" text-anchor="middle">✓ Result Delivered</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 19. REACT FIBER RECONCILER (DUAL-TREE DIFFING)
    // ==========================================================================
    function renderFiberLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(6, 182, 212, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="140" height="20" rx="4" fill="#06b6d4" fill-opacity="0.2" stroke="#06b6d4" stroke-width="1"/>
            <text x="70" y="14" fill="#22d3ee" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">REACT FIBER DIFF</text>
            <text x="152" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Current Fiber Tree -->
          <g transform="translate(20, 48)">
            <rect width="250" height="152" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <rect width="250" height="28" rx="8" fill="#0ea5e9" fill-opacity="0.25"/>
            <text x="125" y="18" fill="#38bdf8" font-size="9.5" font-weight="700" text-anchor="middle">CURRENT TREE: ${escSvg(s0[0])}</text>
            <g transform="translate(12, 38)">
              <rect width="226" height="26" rx="4" fill="#1e293b"/>
              <text x="10" y="17" fill="#f8fafc" font-size="8.5">${escSvg(s0[1].slice(0, 26))}</text>
              <rect y="32" width="226" height="26" rx="4" fill="#1e293b"/>
              <text x="10" y="49" fill="#94a3b8" font-size="8">${escSvg(s1[1].slice(0, 26))}</text>
              <rect y="64" width="226" height="22" rx="4" fill="#0c4a6e"/>
              <text x="113" y="79" fill="#38bdf8" font-size="8" font-weight="600" text-anchor="middle">Lanes: 31-bit Priority</text>
            </g>
          </g>
          <!-- Center: Diff Engine -->
          <g transform="translate(290, 68)">
            <rect width="145" height="110" rx="8" fill="#1e1b4b" stroke="#8b5cf6" stroke-width="1.8"/>
            <text x="72" y="24" fill="#c4b5fd" font-size="9" font-weight="700" text-anchor="middle">RECONCILER</text>
            <text x="72" y="42" fill="#a5b4fc" font-size="8" text-anchor="middle">Heuristic O(N) Diff</text>
            <text x="72" y="60" fill="#38bdf8" font-size="7.5" text-anchor="middle">${escSvg(s2[0])}: ${escSvg(s2[1].slice(0, 14))}</text>
            <text x="72" y="76" fill="#34d399" font-size="7.5" text-anchor="middle">Time-Sliced Work</text>
            <text x="72" y="94" fill="#fcd34d" font-size="7.5" text-anchor="middle">Alternate Ptr Swap</text>
          </g>
          <!-- WorkInProgress Fiber Tree -->
          <g transform="translate(455, 48)">
            <rect width="250" height="152" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="250" height="28" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="125" y="18" fill="#34d399" font-size="9.5" font-weight="700" text-anchor="middle">WIP TREE: ${escSvg(s3[0])}</text>
            <g transform="translate(12, 38)">
              <rect width="226" height="26" rx="4" fill="#064e3b"/>
              <text x="10" y="17" fill="#6ee7b7" font-size="8.5">${escSvg(s3[1].slice(0, 26))}</text>
              <rect y="32" width="226" height="26" rx="4" fill="#451a03" stroke="#f59e0b" stroke-width="0.8"/>
              <text x="10" y="49" fill="#fcd34d" font-size="8">Tag: Placement / Update</text>
              <rect y="64" width="226" height="22" rx="4" fill="#042f2e"/>
              <text x="113" y="79" fill="#5eead4" font-size="8" font-weight="600" text-anchor="middle">Effect Subtree List</text>
            </g>
          </g>
          <!-- Commit Phase -->
          <g transform="translate(720, 48)">
            <rect width="160" height="152" rx="8" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
            <rect width="160" height="28" rx="8" fill="#f43f5e" fill-opacity="0.25"/>
            <text x="80" y="18" fill="#fb7185" font-size="9" font-weight="700" text-anchor="middle">COMMIT: ${escSvg(s4[0])}</text>
            <g transform="translate(10, 36)">
              <rect width="140" height="30" rx="4" fill="#881337"/>
              <text x="70" y="18" fill="#fecdd3" font-size="8" font-weight="700" text-anchor="middle">Synchronous Flush</text>
              <rect y="38" width="140" height="30" rx="4" fill="#1e293b"/>
              <text x="70" y="56" fill="#cbd5e1" font-size="8" text-anchor="middle">Real Browser DOM</text>
            </g>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Fiber Flow: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 20. ALGORITHM MEMORY ARRAY RIBBON & POINTER TAPE
    // ==========================================================================
    function renderRibbonLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(16, 185, 129, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="145" height="20" rx="4" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
            <text x="72" y="14" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">ALGORITHM RIBBON</text>
            <text x="157" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Memory Array Cells [0..4] -->
          <g transform="translate(40, 65)">
            <rect width="110" height="65" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.8"/>
            <text x="55" y="20" fill="#38bdf8" font-size="8.5" font-weight="700" text-anchor="middle">IDX [0]: ${escSvg(s0[0].slice(0, 8))}</text>
            <text x="55" y="44" fill="#f8fafc" font-size="10" font-weight="600" text-anchor="middle">${escSvg(s0[1].slice(0, 14))}</text>
            <rect x="25" y="74" width="60" height="22" rx="4" fill="#0284c7"/>
            <text x="55" y="89" fill="#ffffff" font-size="8.5" font-weight="700" text-anchor="middle">▲ Left</text>
          </g>
          <g transform="translate(165, 65)">
            <rect width="110" height="65" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1.2"/>
            <text x="55" y="20" fill="#94a3b8" font-size="8.5" text-anchor="middle">IDX [1]: ${escSvg(s1[0].slice(0, 8))}</text>
            <text x="55" y="44" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle">${escSvg(s1[1].slice(0, 14))}</text>
          </g>
          <g transform="translate(290, 65)">
            <rect width="110" height="65" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="55" y="20" fill="#fbbf24" font-size="8.5" font-weight="700" text-anchor="middle">IDX [2]: ${escSvg(s2[0].slice(0, 8))}</text>
            <text x="55" y="44" fill="#f8fafc" font-size="10" font-weight="600" text-anchor="middle">${escSvg(s2[1].slice(0, 14))}</text>
            <rect x="25" y="74" width="60" height="22" rx="4" fill="#d97706"/>
            <text x="55" y="89" fill="#ffffff" font-size="8.5" font-weight="700" text-anchor="middle">▲ Mid</text>
          </g>
          <g transform="translate(415, 65)">
            <rect width="110" height="65" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1.2"/>
            <text x="55" y="20" fill="#94a3b8" font-size="8.5" text-anchor="middle">IDX [3]: ${escSvg(s3[0].slice(0, 8))}</text>
            <text x="55" y="44" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle">${escSvg(s3[1].slice(0, 14))}</text>
          </g>
          <g transform="translate(540, 65)">
            <rect width="110" height="65" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
            <text x="55" y="20" fill="#34d399" font-size="8.5" font-weight="700" text-anchor="middle">IDX [4]: ${escSvg(s4[0].slice(0, 8))}</text>
            <text x="55" y="44" fill="#f8fafc" font-size="10" font-weight="600" text-anchor="middle">${escSvg(s4[1].slice(0, 14))}</text>
            <rect x="25" y="74" width="60" height="22" rx="4" fill="#059669"/>
            <text x="55" y="89" fill="#ffffff" font-size="8.5" font-weight="700" text-anchor="middle">▲ Right</text>
          </g>
          <!-- Right: Invariant Box -->
          <g transform="translate(670, 52)">
            <rect width="210" height="145" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
            <rect width="210" height="26" rx="8" fill="#6366f1" fill-opacity="0.25"/>
            <text x="105" y="17" fill="#a5b4fc" font-size="8.5" font-weight="700" text-anchor="middle">INVARIANT STATE</text>
            <g transform="translate(10, 36)">
              <text x="0" y="14" fill="#94a3b8" font-size="8">Window: [${escSvg(s0[0])} .. ${escSvg(s4[0])}]</text>
              <text x="0" y="32" fill="#38bdf8" font-size="8.5" font-weight="700">${escSvg(s1[2].slice(0, 26))}</text>
              <text x="0" y="50" fill="#f59e0b" font-size="8">Target: ${escSvg(s2[3] || 'Predicate')}</text>
              <text x="0" y="68" fill="#34d399" font-size="8.5" font-weight="700">➔ Optimal State O(N)</text>
              <text x="0" y="90" fill="#cbd5e1" font-size="8">Memory: O(1) Space</text>
            </g>
          </g>
          <!-- Active Window Bracket -->
          <path d="M 40 56 L 40 46 L 650 46 L 650 56" fill="none" stroke="#eab308" stroke-width="1.8" stroke-dasharray="4 4"/>
          <text x="345" y="40" fill="#facc15" font-size="8" font-weight="700" text-anchor="middle">[Active Sliding Search Window]</text>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Ribbon Flow: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 21. SDLC GIT FLOW & DIRECTED ACYCLIC GRAPH (DAG)
    // ==========================================================================
    function renderSdlcLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(59, 130, 246, 0.35);">
          <g transform="translate(20, 20)">
            <rect width="125" height="20" rx="4" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6" stroke-width="1"/>
            <text x="62" y="14" fill="#60a5fa" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">GITFLOW DAG</text>
            <text x="137" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <!-- Git Branch Graph Track -->
          <g transform="translate(20, 48)">
            <rect width="570" height="152" rx="8" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
            <rect width="570" height="28" rx="8" fill="#3b82f6" fill-opacity="0.25"/>
            <text x="285" y="18" fill="#93c5fd" font-size="9.5" font-weight="700" text-anchor="middle">Git Branching DAG &amp; Code Review Pipeline</text>
            <!-- Main branch line -->
            <line x1="40" y1="58" x2="520" y2="58" stroke="#3b82f6" stroke-width="3"/>
            <text x="15" y="62" fill="#60a5fa" font-size="8.5" font-weight="700">main</text>
            <circle cx="60" cy="58" r="6" fill="#3b82f6"/>
            <circle cx="160" cy="58" r="6" fill="#3b82f6"/>
            <circle cx="480" cy="58" r="7" fill="#10b981" stroke="#34d399" stroke-width="2"/>
            <text x="480" y="46" fill="#34d399" font-size="7.5" font-weight="700" text-anchor="middle">Release</text>
            <!-- Feature branch arc -->
            <path d="M 160 58 Q 190 108 240 108 L 360 108 Q 420 108 480 58" fill="none" stroke="#a855f7" stroke-width="2.2" stroke-dasharray="4 2"/>
            <text x="300" y="122" fill="#c084fc" font-size="8" font-weight="700" text-anchor="middle">feature: ${escSvg(s1[0])}</text>
            <circle cx="270" cy="108" r="5" fill="#a855f7"/>
            <circle cx="330" cy="108" r="5" fill="#a855f7"/>
            <!-- PR Gate Badge -->
            <g transform="translate(385, 72)">
              <rect width="120" height="32" rx="4" fill="#1e1b4b" stroke="#6366f1" stroke-width="1"/>
              <text x="60" y="13" fill="#a5b4fc" font-size="7.5" font-weight="700" text-anchor="middle">PR Gate: ${escSvg(s2[0])}</text>
              <text x="60" y="25" fill="#34d399" font-size="7" text-anchor="middle">✓ Checks Passed</text>
            </g>
          </g>
          <!-- Release Pipeline (Right) -->
          <g transform="translate(605, 48)">
            <rect width="275" height="152" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="275" height="28" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="137" y="18" fill="#34d399" font-size="9.5" font-weight="700" text-anchor="middle">ZERO-DOWNTIME ROLLOUT</text>
            <g transform="translate(12, 34)">
              <rect width="251" height="26" rx="4" fill="#064e3b"/>
              <text x="10" y="17" fill="#6ee7b7" font-size="8.5">1. ${escSvg(s3[0])}: ${escSvg(s3[1].slice(0, 22))}</text>
              <rect y="32" width="251" height="26" rx="4" fill="#042f2e"/>
              <text x="10" y="49" fill="#5eead4" font-size="8.5">2. Staging Healthcheck</text>
              <rect y="64" width="251" height="26" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
              <text x="10" y="81" fill="#34d399" font-size="8.5" font-weight="700">3. ${escSvg(s4[0])}: Blue/Green Swap</text>
            </g>
          </g>
          <!-- Bottom Flow Ribbon -->
          <g transform="translate(20, 212)">
            <rect width="860" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1"/>
            <text x="430" y="17" fill="#cbd5e1" font-size="8.5" font-weight="600" text-anchor="middle">➔ Git Lifecycle: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 22. SPACIOUS 5-STAGE ARCHITECTURAL PIPELINE (UNIVERSAL HIGH-CLARITY)
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
      const startY = 48;

      const colors = [
        { stroke: '#0284c7', fill: '#0369a1', text: '#38bdf8', bg: '#0f172a' },
        { stroke: '#7c3aed', fill: '#6d28d9', text: '#c084fc', bg: '#0f172a' },
        { stroke: '#f59e0b', fill: '#d97706', text: '#fbbf24', bg: '#0f172a' },
        { stroke: '#10b981', fill: '#059669', text: '#34d399', bg: '#0f172a' },
        { stroke: '#ec4899', fill: '#db2777', text: '#f472b6', bg: '#0f172a' }
      ];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid ${themeBorder}44;">
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
print(f"Master injection complete! New file size: {new_size_mb:.2f} MB")

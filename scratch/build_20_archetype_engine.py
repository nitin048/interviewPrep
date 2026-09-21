import re
import os
import sys

print("Building 20-Archetype Creative Visual Engine...")

with open('senior-dotnet-interview-portal.html', 'r', encoding='utf-8') as f:
    html = f.read()

marker_start = "// ==========================================================================\n    // Multi-Archetype Creative Visual Architecture Diagram Engine"
idx_start = html.find(marker_start)
if idx_start == -1:
    print("Error: Could not find marker_start")
    sys.exit(1)

marker_end = "QUESTION_BANK.forEach(q => {"
idx_end = html.find(marker_end, idx_start)
if idx_end == -1:
    print("Error: Could not find marker_end")
    sys.exit(1)

print(f"Engine section spans from {idx_start} to {idx_end} (length: {idx_end - idx_start} bytes)")

# Read complete engine code
engine_code = r'''// ==========================================================================
    // Multi-Archetype Creative Visual Architecture Diagram Engine (20 Archetypes)
    // Generates 20 distinct, highly creative, intuitive, and domain-tailored visual topologies:
    // 1.  UML Class Contract & Dynamic VTable Dispatch Blueprint (OOP, SOLID, Design Patterns, LLD)
    // 2.  EF Core ORM Pipeline with Change Tracker & AST SQL Generator (EF Core, LINQ)
    // 3.  Relational SQL Engine, CBO Optimizer & 8KB Buffer Pool (SQL, Joins, Transactions)
    // 4.  B-Tree Indexing Topology (Root, Intermediate Branch, Leaf Pages, Buffer Pool)
    // 5.  Generative AI & Semantic Kernel Vector RAG Pipeline (DotNet-AI, Embeddings, LLMs)
    // 6.  Cloud Distributed Multi-AZ Infrastructure & Microservices (Cloud, AWS, HLD)
    // 7.  Transactional Outbox & Debezium CDC Streaming (Kafka, RabbitMQ, Event Sourcing)
    // 8.  ASP.NET Core HTTP Request-Response Lifecycle & Action Filters (Web API, MVC)
    // 9.  Concentric Russian-Doll Middleware Pipeline (Inbound & Outbound HTTP Flow)
    // 10. Defense-in-Depth Cryptographic Vault & Signed JWT Anatomy (Security, Auth, OAuth2)
    // 11. Test Automation Pyramid & CI/CD Quality Gates (Unit, Integration, E2E, AAA)
    // 12. V8 JavaScript Engine Architecture & Event Loop (Call Stack, Web APIs, Microtasks)
    // 13. Redux Unidirectional Orbital Cyclotron State Machine (Store, Actions, Reducers)
    // 14. 4-Phase Async Compiler State Machine (State 0, State -1 Yield, IOCP Completion)
    // 15. CLR Memory Blueprint (Stack vs Heap, Pointer Arcs, Object Headers & GC Arenas)
    // 16. Split-Branch Decision Diamond & Cache Fallback Matrix (Redis Fast Path vs DB)
    // 17. React Fiber Reconciler & Dual-Tree Diffing (Current vs WorkInProgress Tree)
    // 18. Algorithm Memory Ribbon & Multi-Pointer Navigation (Arrays, Two Pointers, Window)
    // 19. SDLC Git Flow Branching & Zero-Downtime Deployment (Pull Requests, Blue/Green)
    // 20. Spacious 4-Stage Enterprise Architectural Pipeline (General & Core Architectures)
    // ==========================================================================

    function escSvg(s) {
      if (!s) return '';
      return String(s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
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
      const steps = q.diagramSteps || [];
      const tLow = (q.q || '').toLowerCase();
      const cat = (q.category || '').toLowerCase();
      const cleanTitle = escSvg(title);

      const w = 880;
      const h = 250;

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

      // 19. Default Enterprise Flow
      return renderEnterpriseLayout(q, cleanTitle, steps, w, h);
    }

    // =========================================================================
    // 1. OOP CLASS CONTRACT & DYNAMIC VTABLE DISPATCH BLUEPRINT
    // ==========================================================================
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

    // =========================================================================
    // 2. EF CORE ORM CHANGE TRACKER & SQL GENERATOR
    // ==========================================================================
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

    // =========================================================================
    // 3. SQL RELATIONAL ENGINE, OPTIMIZER & BUFFER POOL
    // ==========================================================================
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
          <g transform="translate(295, 52)">
            <rect width="280" height="175" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
            <rect width="280" height="32" rx="8" fill="#6366f1" fill-opacity="0.25"/>
            <text x="140" y="21" fill="#a5b4fc" font-size="10.5" font-weight="700" text-anchor="middle">Physical Execution Plan Tree</text>
            <rect x="75" y="42" width="130" height="24" rx="4" fill="#312e81" stroke="#818cf8" stroke-width="1"/>
            <text x="140" y="58" fill="#e0e7ff" font-size="9" font-weight="700" text-anchor="middle">SELECT / Aggregate</text>
            <line x1="140" y1="66" x2="70" y2="88" stroke="#818cf8" stroke-width="1.5"/>
            <line x1="140" y1="66" x2="210" y2="88" stroke="#818cf8" stroke-width="1.5"/>
            <rect x="15" y="88" width="115" height="36" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
            <text x="72" y="103" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">Clustered Index Seek</text>
            <text x="72" y="117" fill="#a7f3d0" font-size="7.5" text-anchor="middle">Cost: 12% | O(log N)</text>
            <rect x="150" y="88" width="115" height="36" rx="4" fill="#451a03" stroke="#f59e0b" stroke-width="1"/>
            <text x="207" y="103" fill="#fcd34d" font-size="8.5" font-weight="700" text-anchor="middle">Hash Match / Join</text>
            <text x="207" y="117" fill="#fef3c7" font-size="7.5" text-anchor="middle">Cost: 88% | In-Memory</text>
            <rect x="15" y="136" width="250" height="24" rx="4" fill="#1e1b4b"/>
            <text x="140" y="152" fill="#c7d2fe" font-size="8.5" font-weight="600" text-anchor="middle">${escSvg(s1[1])}</text>
          </g>
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

    // =========================================================================
    // 4. B-TREE INDEXING TOPOLOGY
    // ==========================================================================
    function renderBTreeLayout(q, title, steps, w, h) {
      const s0 = steps[0] || ['ROOT', 'Root Index Page', 'Page #102: Range keys [1..1000]', 'Root'];
      const s1 = steps[1] || ['BRANCH', 'Intermediate Node', 'Navigation split keys [1..500]', 'Branch'];
      const s2 = steps[2] || ['LEAF', 'Clustered Leaf Page', '8KB Page with physical data rows', 'Leaf'];
      const s3 = steps[3] || ['BUFFER', 'Buffer Pool Hit', 'Page in RAM - 0 physical disk I/O', 'RAM Hit'];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(16, 185, 129, 0.35);">
          <g transform="translate(20, 24)">
            <rect x="0" y="0" width="130" height="20" rx="4" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
            <text x="65" y="14" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">B-TREE INDEX</text>
            <text x="142" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <g transform="translate(340, 52)">
            <rect width="200" height="42" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
            <rect width="200" height="18" rx="6" fill="#10b981" fill-opacity="0.25"/>
            <text x="100" y="13" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">ROOT NODE (Page #102)</text>
            <text x="100" y="32" fill="#f8fafc" font-size="9.5" font-family="monospace" text-anchor="middle">[Key: 100 | Key: 500 | Key: 900]</text>
          </g>
          <line x1="390" y1="94" x2="230" y2="114" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
          <line x1="440" y1="94" x2="440" y2="114" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
          <line x1="490" y1="94" x2="650" y2="114" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
          <g transform="translate(130, 114)">
            <rect width="200" height="36" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="100" y="15" fill="#38bdf8" font-size="8" font-weight="700" text-anchor="middle">Branch Node (Page #205)</text>
            <text x="100" y="28" fill="#94a3b8" font-size="8.5" font-family="monospace" text-anchor="middle">Keys: [1 .. 99] ➔ Leaf</text>
          </g>
          <g transform="translate(340, 114)">
            <rect width="200" height="36" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="100" y="15" fill="#38bdf8" font-size="8" font-weight="700" text-anchor="middle">Branch Node (Page #206)</text>
            <text x="100" y="28" fill="#94a3b8" font-size="8.5" font-family="monospace" text-anchor="middle">Keys: [100 .. 499] ➔ Leaf</text>
          </g>
          <g transform="translate(550, 114)">
            <rect width="200" height="36" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="100" y="15" fill="#38bdf8" font-size="8" font-weight="700" text-anchor="middle">Branch Node (Page #207)</text>
            <text x="100" y="28" fill="#94a3b8" font-size="8.5" font-family="monospace" text-anchor="middle">Keys: [500 .. 899] ➔ Leaf</text>
          </g>
          <line x1="230" y1="150" x2="110" y2="170" stroke="#0ea5e9" stroke-width="1.5"/>
          <line x1="440" y1="150" x2="440" y2="170" stroke="#0ea5e9" stroke-width="1.5"/>
          <line x1="650" y1="150" x2="770" y2="170" stroke="#0ea5e9" stroke-width="1.5"/>
          <g transform="translate(20, 170)">
            <rect width="180" height="52" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
            <text x="90" y="16" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">Leaf 8KB Page #301</text>
            <text x="90" y="30" fill="#a7f3d0" font-size="8" text-anchor="middle">Rows [1 .. 50] | RAM Hit</text>
            <text x="90" y="44" fill="#34d399" font-size="8" font-weight="600" text-anchor="middle">Double-Linked &lt;---&gt;</text>
          </g>
          <g transform="translate(240, 170)">
            <rect width="180" height="52" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
            <text x="90" y="16" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">Leaf 8KB Page #302</text>
            <text x="90" y="30" fill="#a7f3d0" font-size="8" text-anchor="middle">Rows [51 .. 99] | Seek</text>
            <text x="90" y="44" fill="#34d399" font-size="8" font-weight="600" text-anchor="middle">Double-Linked &lt;---&gt;</text>
          </g>
          <g transform="translate(460, 170)">
            <rect width="180" height="52" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
            <text x="90" y="16" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">Leaf 8KB Page #303</text>
            <text x="90" y="30" fill="#a7f3d0" font-size="8" text-anchor="middle">Rows [100 .. 250] | Seek</text>
            <text x="90" y="44" fill="#34d399" font-size="8" font-weight="600" text-anchor="middle">Double-Linked &lt;---&gt;</text>
          </g>
          <g transform="translate(680, 170)">
            <rect width="180" height="52" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
            <text x="90" y="16" fill="#c7d2fe" font-size="8.5" font-weight="700" text-anchor="middle">Buffer Pool (RAM Cache)</text>
            <text x="90" y="30" fill="#a5b4fc" font-size="8" text-anchor="middle">Zero Disk I/O Latency</text>
            <text x="90" y="44" fill="#38bdf8" font-size="8" font-weight="600" text-anchor="middle">&lt; 0.1ms Memory Hit</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 5. GENERATIVE AI & VECTOR RAG PIPELINE
    // ==========================================================================
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

    // =========================================================================
    // 6. CLOUD DISTRIBUTED INFRASTRUCTURE & MICROSERVICES
    // ==========================================================================
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

    // =========================================================================
    // 7. TRANSACTIONAL OUTBOX & DEBEZIUM CDC STREAMING
    // ==========================================================================
    function renderDistributedLayout(q, title, steps, w, h) {
      const s0 = steps[0] || ['LOCAL', 'Domain Tx + Outbox Table', 'Atomic local DB transaction', 'Local ACID'];
      const s1 = steps[1] || ['CDC', 'Debezium Log Miner', 'Reads DB transaction log / WAL stream', 'WAL Miner'];
      const s2 = steps[2] || ['KAFKA', 'Kafka Topic Partitions', 'Distributed event streaming bus', 'Partition'];
      const s3 = steps[3] || ['CONSUME', 'Idempotent Consumer', 'Deduplication key + domain handler', 'Idempotent'];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(249, 115, 22, 0.35);">
          <defs>
            <marker id="distArrow_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
              <polygon points="0 0, 8 4, 0 8" fill="#f97316"/>
            </marker>
          </defs>
          <g transform="translate(20, 24)">
            <rect x="0" y="0" width="150" height="20" rx="4" fill="#f97316" fill-opacity="0.2" stroke="#f97316" stroke-width="1"/>
            <text x="75" y="14" fill="#fb923c" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">DISTRIBUTED STREAMING</text>
            <text x="162" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <g transform="translate(20, 52)">
            <rect width="190" height="175" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <rect width="190" height="32" rx="8" fill="#0ea5e9" fill-opacity="0.25"/>
            <text x="95" y="21" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="middle">1. Domain &amp; Outbox</text>
            <g transform="translate(12, 42)">
              <rect width="166" height="28" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
              <text x="83" y="18" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">Orders Table (Domain)</text>
              <rect y="34" width="166" height="28" rx="4" fill="#451a03" stroke="#f59e0b" stroke-width="1"/>
              <text x="83" y="52" fill="#fcd34d" font-size="8.5" font-weight="700" text-anchor="middle">Outbox_Events Table</text>
              <rect y="68" width="166" height="26" rx="4" fill="#0f172a"/>
              <text x="83" y="85" fill="#94a3b8" font-size="8" text-anchor="middle">Single Atomic ACID Tx</text>
            </g>
          </g>
          <line x1="214" y1="140" x2="234" y2="140" stroke="#f97316" stroke-width="2" marker-end="url(#distArrow_${q.id})"/>
          <g transform="translate(238, 52)">
            <rect width="190" height="175" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
            <rect width="190" height="32" rx="8" fill="#f59e0b" fill-opacity="0.25"/>
            <text x="95" y="21" fill="#fbbf24" font-size="10.5" font-weight="700" text-anchor="middle">2. CDC Log Miner</text>
            <g transform="translate(12, 42)">
              <rect width="166" height="26" rx="4" fill="#1e1b4b"/>
              <text x="83" y="17" fill="#c7d2fe" font-size="8.5" text-anchor="middle">Debezium / DB WAL</text>
              <rect y="32" width="166" height="26" rx="4" fill="#312e81"/>
              <text x="83" y="49" fill="#a5b4fc" font-size="8.5" text-anchor="middle">Reads Tx Log Binary</text>
              <rect y="64" width="166" height="26" rx="4" fill="#064e3b"/>
              <text x="83" y="81" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">Zero Dual-Write Risk</text>
            </g>
          </g>
          <line x1="432" y1="140" x2="452" y2="140" stroke="#f97316" stroke-width="2" marker-end="url(#distArrow_${q.id})"/>
          <g transform="translate(456, 52)">
            <rect width="200" height="175" rx="8" fill="#0f172a" stroke="#f97316" stroke-width="1.5"/>
            <rect width="200" height="32" rx="8" fill="#f97316" fill-opacity="0.25"/>
            <text x="100" y="21" fill="#fb923c" font-size="10.5" font-weight="700" text-anchor="middle">3. Kafka Streaming</text>
            <g transform="translate(12, 42)">
              <rect width="176" height="22" rx="4" fill="#1e293b"/>
              <text x="88" y="15" fill="#f8fafc" font-size="8.5" font-family="monospace" text-anchor="middle">Topic: order.created</text>
              <g transform="translate(0, 26)">
                <rect width="56" height="24" rx="3" fill="#0c4a6e"/>
                <text x="28" y="16" fill="#38bdf8" font-size="8" text-anchor="middle">[P0: 1042]</text>
                <rect x="60" width="56" height="24" rx="3" fill="#0c4a6e"/>
                <text x="88" y="16" fill="#38bdf8" font-size="8" text-anchor="middle">[P1: 941]</text>
                <rect x="120" width="56" height="24" rx="3" fill="#0c4a6e"/>
                <text x="148" y="16" fill="#38bdf8" font-size="8" text-anchor="middle">[P2: 832]</text>
              </g>
              <rect y="56" width="176" height="24" rx="4" fill="#1e1b4b"/>
              <text x="88" y="72" fill="#c7d2fe" font-size="8" text-anchor="middle">At-Least-Once Delivery</text>
            </g>
          </g>
          <line x1="660" y1="140" x2="680" y2="140" stroke="#f97316" stroke-width="2" marker-end="url(#distArrow_${q.id})"/>
          <g transform="translate(684, 52)">
            <rect width="176" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="176" height="32" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="88" y="21" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">4. Idempotent Consumer</text>
            <g transform="translate(10, 42)">
              <rect width="156" height="24" rx="4" fill="#064e3b"/>
              <text x="8" y="16" fill="#6ee7b7" font-size="8.5">Event Deduplication</text>
              <rect y="30" width="156" height="24" rx="4" fill="#0f172a"/>
              <text x="8" y="46" fill="#94a3b8" font-size="8.5">Inbox Table Check</text>
              <rect y="60" width="156" height="22" rx="4" fill="#1e1b4b"/>
              <text x="8" y="75" fill="#a5b4fc" font-size="8">Execute Domain Logic</text>
              <rect y="88" width="156" height="20" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="0.8"/>
              <text x="78" y="102" fill="#34d399" font-size="8" font-weight="700" text-anchor="middle">Commit Offset</text>
            </g>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 8. ASP.NET CORE HTTP REQUEST-RESPONSE PIPELINE
    // ==========================================================================
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

    // =========================================================================
    // 9. CONCENTRIC RUSSIAN-DOLL MIDDLEWARE PIPELINE
    // ==========================================================================
    function renderMiddlewareLayout(q, title, steps, w, h) {
      const s0 = steps[0] || ['INBOUND', 'Kestrel Socket', 'Initial raw TCP/HTTP ingress', 'Ingress'];
      const s1 = steps[1] || ['AUTH', 'Authentication & CORS', 'Validates identity tokens and headers', 'Security'];
      const s2 = steps[2] || ['ENDPOINT', 'Endpoint Dispatch', 'Executes business delegate & returns model', 'Handler'];
      const s3 = steps[3] || ['OUTBOUND', 'Response Unwind', 'Headers finalized & output written', '200 OK'];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(139, 92, 246, 0.35);">
          <g transform="translate(20, 24)">
            <rect x="0" y="0" width="150" height="20" rx="4" fill="#8b5cf6" fill-opacity="0.2" stroke="#8b5cf6" stroke-width="1"/>
            <text x="75" y="14" fill="#c4b5fd" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">MIDDLEWARE ONION</text>
            <text x="162" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <g transform="translate(20, 52)">
            <rect width="840" height="175" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.8"/>
            <text x="24" y="24" fill="#c4b5fd" font-size="9.5" font-weight="700">Stage 1: Exception Handler &amp; Diagnostics</text>
            <rect x="40" y="32" width="760" height="125" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
            <text x="64" y="52" fill="#a5b4fc" font-size="9.5" font-weight="700">Stage 2: Routing, CORS &amp; Rate Limiting</text>
            <rect x="80" y="60" width="680" height="85" rx="6" fill="#31104b" stroke="#d946ef" stroke-width="1.5"/>
            <text x="104" y="78" fill="#f0abfc" font-size="9.5" font-weight="700">Stage 3: Authentication &amp; Authorization</text>
            <rect x="120" y="86" width="600" height="48" rx="5" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
            <text x="420" y="106" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">★ Core Endpoint / Action Delegate Execution</text>
            <text x="420" y="122" fill="#6ee7b7" font-size="8.5" text-anchor="middle">await _next(context) completes ➔ Unwinds back through onion in reverse</text>
            <g transform="translate(60, 142)">
              <path d="M 0 0 L 120 0" stroke="#38bdf8" stroke-width="2" marker-end="url(#distArrow_${q.id})"/>
              <text x="60" y="-5" fill="#38bdf8" font-size="8" font-weight="700" text-anchor="middle">➔ Inbound Flow</text>
            </g>
            <g transform="translate(660, 142)">
              <path d="M 120 0 L 0 0" stroke="#4ade80" stroke-width="2"/>
              <text x="60" y="-5" fill="#4ade80" font-size="8" font-weight="700" text-anchor="middle">⬅ Outbound Flow (200 OK)</text>
            </g>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 10. DEFENSE-IN-DEPTH CRYPTOGRAPHIC VAULT & SIGNED JWT
    // ==========================================================================
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
          <g transform="translate(20, 52)">
            <rect width="390" height="175" rx="8" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5"/>
            <rect width="390" height="32" rx="8" fill="#7c3aed" fill-opacity="0.25"/>
            <text x="195" y="21" fill="#c084fc" font-size="10.5" font-weight="700" text-anchor="middle">Signed JSON Web Token (RFC 7519)</text>
            <g transform="translate(14, 44)">
              <rect x="0" width="112" height="60" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1"/>
              <text x="56" y="18" fill="#38bdf8" font-size="8.5" font-weight="700" text-anchor="middle">HEADER</text>
              <text x="10" y="34" fill="#7dd3fc" font-size="7.5" font-family="monospace">alg: "RS256"</text>
              <text x="10" y="48" fill="#7dd3fc" font-size="7.5" font-family="monospace">typ: "JWT"</text>
              <circle cx="121" cy="30" r="3" fill="#f43f5e"/>
              <rect x="130" width="112" height="60" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="1"/>
              <text x="186" y="18" fill="#d8b4fe" font-size="8.5" font-weight="700" text-anchor="middle">PAYLOAD</text>
              <text x="140" y="34" fill="#e9d5ff" font-size="7.5" font-family="monospace">sub: "usr_42"</text>
              <text x="140" y="48" fill="#e9d5ff" font-size="7.5" font-family="monospace">role: "Admin"</text>
              <circle cx="251" cy="30" r="3" fill="#f43f5e"/>
              <rect x="260" width="102" height="60" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
              <text x="311" y="18" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">SIGNATURE</text>
              <text x="268" y="34" fill="#a7f3d0" font-size="7.5" font-family="monospace">RSASHA256(</text>
              <text x="268" y="48" fill="#a7f3d0" font-size="7.5" font-family="monospace"> H+P, PrivKey)</text>
              <rect y="70" width="362" height="24" rx="4" fill="#18181b"/>
              <text x="181" y="86" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Base64Url Encoded ➔ Dispatched in HTTP Authorization Header</text>
            </g>
          </g>
          <g transform="translate(425, 52)">
            <rect width="435" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="435" height="32" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="217" y="21" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">Defense-in-Depth Security Vault</text>
            <g transform="translate(14, 44)">
              <rect width="195" height="52" rx="4" fill="#064e3b" stroke="#059669" stroke-width="0.8"/>
              <text x="12" y="18" fill="#6ee7b7" font-size="8.5" font-weight="700">🔑 Claims Authorization</text>
              <text x="12" y="32" fill="#a7f3d0" font-size="8">[Authorize(Roles="Admin")]</text>
              <text x="12" y="44" fill="#94a3b8" font-size="7.5">Validated against RSA Public Key</text>
              <rect x="210" width="195" height="52" rx="4" fill="#0c4a6e" stroke="#0284c7" stroke-width="0.8"/>
              <text x="222" y="18" fill="#7dd3fc" font-size="8.5" font-weight="700">🛡️ AES-256 GCM Vault</text>
              <text x="222" y="32" fill="#bae6fd" font-size="8">Data Protection API (DPAPI)</text>
              <text x="222" y="44" fill="#94a3b8" font-size="7.5">Argon2id Salted Hash</text>
              <rect y="64" width="405" height="30" rx="4" fill="#1e1b4b" stroke="#6366f1" stroke-width="0.8"/>
              <text x="202" y="82" fill="#c7d2fe" font-size="8.5" font-weight="600" text-anchor="middle">OWASP Mitigations: Parameterized SQL, Anti-CSRF Tokens, Content Security Policy</text>
            </g>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 11. TEST AUTOMATION PYRAMID & QUALITY GATES
    // ==========================================================================
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
          <g transform="translate(20, 52)">
            <rect width="270" height="175" rx="8" fill="#0f172a" stroke="#059669" stroke-width="1.5"/>
            <rect width="270" height="32" rx="8" fill="#059669" fill-opacity="0.25"/>
            <text x="135" y="21" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">Testing Pyramid Hierarchy</text>
            <rect x="85" y="44" width="100" height="24" rx="4" fill="#7f1d1d" stroke="#ef4444" stroke-width="1"/>
            <text x="135" y="60" fill="#fca5a5" font-size="8.5" font-weight="700" text-anchor="middle">E2E Tests (5%)</text>
            <rect x="45" y="74" width="180" height="26" rx="4" fill="#78350f" stroke="#f59e0b" stroke-width="1"/>
            <text x="135" y="91" fill="#fde68a" font-size="8.5" font-weight="700" text-anchor="middle">Integration Tests (Testcontainers 20%)</text>
            <rect x="15" y="106" width="240" height="34" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
            <text x="135" y="122" fill="#6ee7b7" font-size="9" font-weight="700" text-anchor="middle">Unit Tests (xUnit / Moq / NUnit 75%)</text>
            <text x="135" y="134" fill="#a7f3d0" font-size="7.5" text-anchor="middle">Fast In-Memory Execution (0.01ms / test)</text>
          </g>
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

    // =========================================================================
    // 12. V8 JAVASCRIPT ENGINE & EVENT LOOP RUNTIME
    // ==========================================================================
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

    // =========================================================================
    // 13. REDUX UNIDIRECTIONAL ORBITAL CYCLOTRON STATE MACHINE
    // ==========================================================================
    function renderCycleLayout(q, title, steps, w, h) {
      const s0 = steps[0] || ['DISPATCH', 'UI Component', 'Dispatches typed action payload', 'View'];
      const s1 = steps[1] || ['THUNK', 'Async Thunk / Middleware', 'Performs API call / side-effect', 'Thunk'];
      const s2 = steps[2] || ['REDUCER', 'Pure Root Reducer', '(prevState, action) => nextState', 'Pure Fn'];
      const s3 = steps[3] || ['STORE', 'Single Source of Truth', 'Immutable state tree updated', 'State Tree'];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(168, 85, 247, 0.35);">
          <g transform="translate(20, 24)">
            <rect x="0" y="0" width="150" height="20" rx="4" fill="#a855f7" fill-opacity="0.2" stroke="#a855f7" stroke-width="1"/>
            <text x="75" y="14" fill="#c084fc" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">UNIDIRECTIONAL CYCLE</text>
            <text x="162" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <circle cx="440" cy="140" r="82" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="6 4"/>
          <g transform="translate(370, 115)">
            <circle cx="70" cy="25" r="38" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
            <text x="70" y="21" fill="#ffffff" font-size="10.5" font-weight="700" text-anchor="middle">CENTRAL</text>
            <text x="70" y="35" fill="#c084fc" font-size="10.5" font-weight="700" text-anchor="middle">STORE</text>
          </g>
          <g transform="translate(345, 24)">
            <rect width="190" height="42" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <text x="95" y="18" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle">1. React Component (View)</text>
            <text x="95" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">useSelector() ➔ dispatch(action)</text>
          </g>
          <g transform="translate(680, 115)">
            <rect width="180" height="50" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="90" y="18" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">2. Action &amp; Thunk</text>
            <text x="90" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">Type: { type, payload }</text>
            <text x="90" y="44" fill="#a5b4fc" font-size="7.5" text-anchor="middle">Middleware side-effects</text>
          </g>
          <g transform="translate(345, 195)">
            <rect width="190" height="42" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <text x="95" y="18" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">3. Pure Root Reducer</text>
            <text x="95" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">(state, action) =&gt; nextState</text>
          </g>
          <g transform="translate(20, 115)">
            <rect width="180" height="50" rx="6" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
            <text x="90" y="18" fill="#f472b6" font-size="9" font-weight="700" text-anchor="middle">4. Re-render UI Subscriptions</text>
            <text x="90" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">Only dirty components re-render</text>
            <text x="90" y="44" fill="#38bdf8" font-size="7.5" text-anchor="middle">Reference equality check</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 14. 4-PHASE ASYNC COMPILER STATE MACHINE
    // ==========================================================================
    function renderAsyncLayout(q, title, steps, w, h) {
      const s0 = steps[0] || ['START', 'State 0: Synchronous Entry', 'Method starts executing synchronously', 'Initial'];
      const s1 = steps[1] || ['YIELD', 'State -1: Await Yield', 'Task incomplete - thread returns to pool', 'Thread Free'];
      const s2 = steps[2] || ['IOCP', 'Hardware / OS Signal', 'Non-blocking I/O completion port signal', 'Kernel IOCP'];
      const s3 = steps[3] || ['RESUME', 'State 1: MoveNext()', 'ThreadPool thread resumes continuation', 'Resume'];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(139, 92, 246, 0.35);">
          <defs>
            <marker id="asyncArrow_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
              <polygon points="0 0, 8 4, 0 8" fill="#8b5cf6"/>
            </marker>
          </defs>
          <g transform="translate(20, 24)">
            <rect x="0" y="0" width="165" height="20" rx="4" fill="#8b5cf6" fill-opacity="0.2" stroke="#8b5cf6" stroke-width="1"/>
            <text x="82" y="14" fill="#c4b5fd" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">ASYNC STATE MACHINE</text>
            <text x="177" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <g transform="translate(20, 52)">
            <rect width="195" height="175" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <rect width="195" height="32" rx="8" fill="#0ea5e9" fill-opacity="0.25"/>
            <text x="97" y="21" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="middle">State 0: Initial Call</text>
            <g transform="translate(12, 42)">
              <rect width="171" height="26" rx="4" fill="#1e293b"/>
              <text x="8" y="17" fill="#f8fafc" font-size="8.5">Synchronous execution</text>
              <rect y="32" width="171" height="24" rx="4" fill="#0c4a6e"/>
              <text x="8" y="48" fill="#38bdf8" font-size="8">Caller thread runs in-line</text>
              <rect y="62" width="171" height="24" rx="4" fill="#064e3b"/>
              <text x="8" y="78" fill="#6ee7b7" font-size="8">Checks awaiter.IsCompleted</text>
            </g>
          </g>
          <line x1="219" y1="140" x2="239" y2="140" stroke="#8b5cf6" stroke-width="2" marker-end="url(#asyncArrow_${q.id})"/>
          <g transform="translate(243, 52)">
            <rect width="195" height="175" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
            <rect width="195" height="32" rx="8" fill="#f59e0b" fill-opacity="0.25"/>
            <text x="97" y="21" fill="#fbbf24" font-size="10.5" font-weight="700" text-anchor="middle">State -1: Thread Yield</text>
            <g transform="translate(12, 42)">
              <rect width="171" height="26" rx="4" fill="#451a03"/>
              <text x="8" y="17" fill="#fde68a" font-size="8.5">Thread released to pool</text>
              <rect y="32" width="171" height="24" rx="4" fill="#1e293b"/>
              <text x="8" y="48" fill="#cbd5e1" font-size="8">NO BLOCKED THREAD</text>
              <rect y="62" width="171" height="24" rx="4" fill="#78350f"/>
              <text x="8" y="78" fill="#fef3c7" font-size="8">Registers continuation</text>
            </g>
          </g>
          <line x1="442" y1="140" x2="462" y2="140" stroke="#8b5cf6" stroke-width="2" marker-end="url(#asyncArrow_${q.id})"/>
          <g transform="translate(466, 52)">
            <rect width="195" height="175" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.5"/>
            <rect width="195" height="32" rx="8" fill="#ec4899" fill-opacity="0.25"/>
            <text x="97" y="21" fill="#f472b6" font-size="10.5" font-weight="700" text-anchor="middle">OS Kernel: IOCP Signal</text>
            <g transform="translate(12, 42)">
              <rect width="171" height="26" rx="4" fill="#831843"/>
              <text x="8" y="17" fill="#fbcfe8" font-size="8.5">NIC / SSD hardware IRQ</text>
              <rect y="32" width="171" height="24" rx="4" fill="#1e293b"/>
              <text x="8" y="48" fill="#cbd5e1" font-size="8">Driver alerts kernel IOCP</text>
              <rect y="62" width="171" height="24" rx="4" fill="#500724"/>
              <text x="8" y="78" fill="#f472b6" font-size="8">Posts to ThreadPool queue</text>
            </g>
          </g>
          <line x1="665" y1="140" x2="685" y2="140" stroke="#8b5cf6" stroke-width="2" marker-end="url(#asyncArrow_${q.id})"/>
          <g transform="translate(689, 52)">
            <rect width="171" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="171" height="32" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="85" y="21" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">State 1: MoveNext()</text>
            <g transform="translate(10, 42)">
              <rect width="151" height="26" rx="4" fill="#064e3b"/>
              <text x="6" y="17" fill="#6ee7b7" font-size="8.5">Worker thread resumes</text>
              <rect y="32" width="151" height="24" rx="4" fill="#042f2e"/>
              <text x="6" y="48" fill="#5eead4" font-size="8">Restores local state frame</text>
              <rect y="62" width="151" height="24" rx="4" fill="#064e3b"/>
              <text x="6" y="78" fill="#a7f3d0" font-size="8">Method returns result</text>
            </g>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 15. CLR MEMORY BLUEPRINT (STACK VS HEAP & GENERATIONAL GC)
    // ==========================================================================
    function renderMemoryLayout(q, title, steps, w, h) {
      const s0 = steps[0] || ['STACK', 'Local Frame: Value Types', 'Inline struct data', '4/8 Bytes'];
      const s1 = steps[1] || ['ALLOC', 'Heap Allocation', 'Allocates 16B+ on GC heap', 'Alloc'];
      const s2 = steps[2] || ['HEADER', 'Object Header', 'SyncBlock (4B) + TypeHandle (8B)', 'Header'];
      const s3 = steps[3] || ['REF', 'Heap Object Reference', '64-bit Pointer stored on stack', '0x028A'];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(56, 189, 248, 0.3);">
          <defs>
            <marker id="memPtr_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
              <polygon points="0 0, 8 4, 0 8" fill="#38bdf8"/>
            </marker>
          </defs>
          <g transform="translate(20, 24)">
            <rect x="0" y="0" width="140" height="20" rx="4" fill="#0284c7" fill-opacity="0.2" stroke="#0284c7" stroke-width="1"/>
            <text x="70" y="14" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">CLR MEMORY ARCHITECTURE</text>
            <text x="152" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <g transform="translate(20, 52)">
            <rect width="250" height="175" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
            <rect width="250" height="28" rx="8" fill="#0284c7" fill-opacity="0.3"/>
            <text x="125" y="18" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">THREAD STACK (LIFO Execution)</text>
            <g transform="translate(14, 38)">
              <rect width="222" height="32" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
              <text x="12" y="20" fill="#f8fafc" font-size="9" font-family="monospace">ptrObj: 0x007FFA2B (64-bit Ref)</text>
              <rect y="38" width="222" height="30" rx="4" fill="#1e293b"/>
              <text x="12" y="19" fill="#94a3b8" font-size="8.5" font-family="monospace">localVal: 42 (int inline 4B)</text>
              <rect y="74" width="222" height="30" rx="4" fill="#1e293b"/>
              <text x="12" y="19" fill="#94a3b8" font-size="8.5" font-family="monospace">RBP/RSP Register Frame (Call)</text>
            </g>
          </g>
          <path d="M 270 106 C 310 106, 320 86, 350 86" fill="none" stroke="#38bdf8" stroke-width="2.2" marker-end="url(#memPtr_${q.id})"/>
          <g transform="translate(360, 52)">
            <rect width="250" height="175" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
            <rect width="250" height="28" rx="8" fill="#a855f7" fill-opacity="0.3"/>
            <text x="125" y="18" fill="#c084fc" font-size="10" font-weight="700" text-anchor="middle">MANAGED GC HEAP (0x007FFA2B)</text>
            <g transform="translate(14, 38)">
              <rect width="222" height="26" rx="4" fill="#3b0764"/>
              <text x="10" y="17" fill="#d8b4fe" font-size="8.5" font-family="monospace">SyncBlock Index (4 Bytes)</text>
              <rect y="30" width="222" height="26" rx="4" fill="#581c87"/>
              <text x="10" y="17" fill="#e9d5ff" font-size="8.5" font-family="monospace">TypeHandle / MethodTable (8B)</text>
              <rect y="60" width="222" height="32" rx="4" fill="#1e293b" stroke="#a855f7" stroke-width="0.8"/>
              <text x="10" y="20" fill="#f8fafc" font-size="8.5" font-family="monospace">Instance Payload Fields (16B+)</text>
            </g>
          </g>
          <g transform="translate(625, 52)">
            <rect width="235" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="235" height="28" rx="8" fill="#10b981" fill-opacity="0.3"/>
            <text x="117" y="18" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">GC GENERATIONAL HEAPS</text>
            <g transform="translate(12, 38)">
              <rect width="211" height="24" rx="4" fill="#064e3b"/>
              <text x="10" y="16" fill="#6ee7b7" font-size="8.5">Gen 0 (Ephemeral allocations)</text>
              <rect y="28" width="211" height="24" rx="4" fill="#064e3b"/>
              <text x="10" y="16" fill="#a7f3d0" font-size="8.5">Gen 1 (Buffer generation)</text>
              <rect y="56" width="211" height="24" rx="4" fill="#042f2e"/>
              <text x="10" y="16" fill="#5eead4" font-size="8.5">Gen 2 (Long-lived objects)</text>
              <rect y="84" width="211" height="24" rx="4" fill="#1e1b4b"/>
              <text x="10" y="16" fill="#c7d2fe" font-size="8.5">LOH / POH (&gt; 85,000 Bytes)</text>
            </g>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 16. SPLIT-BRANCH DECISION FLOW & CACHE FALLBACK MATRIX
    // ==========================================================================
    function renderBranchLayout(q, title, steps, w, h) {
      const s0 = steps[0] || ['REQUEST', 'Incoming Query', 'Evaluates key against Redis Cache', 'Key Lookup'];
      const s1 = steps[1] || ['HIT', 'Fast Path: Cache Hit', 'Returns cached JSON byte stream (< 1ms)', '< 1ms Hit'];
      const s2 = steps[2] || ['MISS', 'Fallback Path: Cache Miss', 'Acquires distributed lock & queries SQL', 'DB Query'];
      const s3 = steps[3] || ['SET', 'Hydrate Cache & Return', 'Writes back to Redis with sliding TTL', 'TTL Set'];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(234, 179, 8, 0.35);">
          <g transform="translate(20, 24)">
            <rect x="0" y="0" width="135" height="20" rx="4" fill="#eab308" fill-opacity="0.2" stroke="#eab308" stroke-width="1"/>
            <text x="67" y="14" fill="#facc15" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">DECISION BRANCH</text>
            <text x="147" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <g transform="translate(20, 105)">
            <rect width="180" height="55" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <text x="90" y="24" fill="#38bdf8" font-size="9.5" font-weight="700" text-anchor="middle">Inbound Client Request</text>
            <text x="90" y="40" fill="#94a3b8" font-size="8.5" text-anchor="middle">Key: orders:usr_42</text>
          </g>
          <line x1="200" y1="132" x2="270" y2="132" stroke="#38bdf8" stroke-width="2"/>
          <g transform="translate(270, 82)">
            <polygon points="55,0 110,50 55,100 0,50" fill="#1e293b" stroke="#eab308" stroke-width="2"/>
            <text x="55" y="46" fill="#fde047" font-size="8.5" font-weight="700" text-anchor="middle">Key in Redis</text>
            <text x="55" y="60" fill="#fde047" font-size="8.5" font-weight="700" text-anchor="middle">Cache?</text>
          </g>
          <path d="M 325 82 L 325 45 L 430 45" fill="none" stroke="#10b981" stroke-width="2"/>
          <text x="365" y="38" fill="#34d399" font-size="8.5" font-weight="700">YES (Fast Path)</text>
          <g transform="translate(430, 20)">
            <rect width="210" height="52" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.8"/>
            <text x="105" y="22" fill="#6ee7b7" font-size="9.5" font-weight="700" text-anchor="middle">Cache Hit (&lt; 1ms Latency)</text>
            <text x="105" y="38" fill="#a7f3d0" font-size="8.5" text-anchor="middle">Returns cached JSON byte stream</text>
          </g>
          <path d="M 325 182 L 325 210 L 430 210" fill="none" stroke="#f59e0b" stroke-width="2"/>
          <text x="365" y="202" fill="#fbbf24" font-size="8.5" font-weight="700">NO (Miss)</text>
          <g transform="translate(430, 180)">
            <rect width="210" height="55" rx="6" fill="#451a03" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="105" y="22" fill="#fcd34d" font-size="9.5" font-weight="700" text-anchor="middle">Fallback: Distributed Lock &amp; DB</text>
            <text x="105" y="38" fill="#fde68a" font-size="8" text-anchor="middle">Prevents Cache Stampede ➔ SQL query</text>
          </g>
          <g transform="translate(680, 80)">
            <rect width="180" height="100" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
            <rect width="180" height="24" rx="8" fill="#6366f1" fill-opacity="0.25"/>
            <text x="90" y="16" fill="#a5b4fc" font-size="9" font-weight="700" text-anchor="middle">RESPONSE CONVERGENCE</text>
            <text x="90" y="44" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Hydrates cache with TTL</text>
            <text x="90" y="62" fill="#38bdf8" font-size="8.5" text-anchor="middle">Circuit Breaker Active</text>
            <text x="90" y="82" fill="#4ade80" font-size="8.5" font-weight="700" text-anchor="middle">HTTP 200 OK Delivered</text>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 17. REACT FIBER RECONCILER & DUAL-TREE DIFFING
    // ==========================================================================
    function renderFiberLayout(q, title, steps, w, h) {
      const s0 = steps[0] || ['TRIGGER', 'State Update Trigger', 'setState / dispatch creates update lane', 'Update'];
      const s1 = steps[1] || ['RENDER', 'Render Phase (Interruptible)', 'Builds Work-in-Progress Fiber Tree', 'WorkInProgress'];
      const s2 = steps[2] || ['DIFF', 'Heuristic O(N) Diff', 'Keys, component types, effect tags (Placement/Update)', 'Diffing'];
      const s3 = steps[3] || ['COMMIT', 'Commit Phase (Synchronous)', 'Flushes mutations into Real Browser DOM', 'DOM Flush'];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(6, 182, 212, 0.35);">
          <g transform="translate(20, 24)">
            <rect x="0" y="0" width="140" height="20" rx="4" fill="#06b6d4" fill-opacity="0.2" stroke="#06b6d4" stroke-width="1"/>
            <text x="70" y="14" fill="#22d3ee" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">REACT FIBER DIFF</text>
            <text x="152" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <g transform="translate(20, 52)">
            <rect width="250" height="175" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
            <rect width="250" height="28" rx="8" fill="#0ea5e9" fill-opacity="0.25"/>
            <text x="125" y="18" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">CURRENT FIBER TREE (Mounted DOM)</text>
            <g transform="translate(14, 38)">
              <rect width="222" height="24" rx="4" fill="#1e293b"/>
              <text x="10" y="16" fill="#f8fafc" font-size="8.5">&lt;AppRoot&gt; (child ➔)</text>
              <rect y="28" width="222" height="24" rx="4" fill="#1e293b"/>
              <text x="24" y="16" fill="#94a3b8" font-size="8.5">&lt;Header&gt; (sibling ➔)</text>
              <rect y="56" width="222" height="24" rx="4" fill="#1e293b"/>
              <text x="24" y="16" fill="#94a3b8" font-size="8.5">&lt;FeedList&gt; (return ➔ &lt;AppRoot&gt;)</text>
              <rect y="84" width="222" height="24" rx="4" fill="#0c4a6e"/>
              <text x="10" y="16" fill="#38bdf8" font-size="8">Lanes: 31-bit Bitmask Priority</text>
            </g>
          </g>
          <g transform="translate(290, 80)">
            <rect width="140" height="110" rx="8" fill="#1e1b4b" stroke="#8b5cf6" stroke-width="1.8"/>
            <text x="70" y="24" fill="#c4b5fd" font-size="9" font-weight="700" text-anchor="middle">RECONCILER ENGINE</text>
            <text x="70" y="44" fill="#a5b4fc" font-size="8" text-anchor="middle">Heuristic O(N) Diff</text>
            <text x="70" y="62" fill="#38bdf8" font-size="7.5" text-anchor="middle">1. Key &amp; Type Match</text>
            <text x="70" y="76" fill="#34d399" font-size="7.5" text-anchor="middle">2. Tag: Placement/Update</text>
            <text x="70" y="94" fill="#fcd34d" font-size="7.5" text-anchor="middle">Time-Sliced Scheduler</text>
          </g>
          <g transform="translate(450, 52)">
            <rect width="250" height="175" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect width="250" height="28" rx="8" fill="#10b981" fill-opacity="0.25"/>
            <text x="125" y="18" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">WORK-IN-PROGRESS FIBER TREE</text>
            <g transform="translate(14, 38)">
              <rect width="222" height="24" rx="4" fill="#064e3b"/>
              <text x="10" y="16" fill="#6ee7b7" font-size="8.5">&lt;AppRoot&gt; (Reused)</text>
              <rect y="28" width="222" height="24" rx="4" fill="#064e3b"/>
              <text x="24" y="16" fill="#6ee7b7" font-size="8.5">&lt;Header&gt; (Bailed out - Memo)</text>
              <rect y="56" width="222" height="24" rx="4" fill="#451a03" stroke="#f59e0b" stroke-width="1"/>
              <text x="24" y="16" fill="#fcd34d" font-size="8.5">&lt;FeedList&gt; (Flag: Update)</text>
              <rect y="84" width="222" height="24" rx="4" fill="#042f2e"/>
              <text x="10" y="16" fill="#5eead4" font-size="8">Effects Linked List / Subtree</text>
            </g>
          </g>
          <g transform="translate(715, 52)">
            <rect width="145" height="175" rx="8" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
            <rect width="145" height="28" rx="8" fill="#f43f5e" fill-opacity="0.25"/>
            <text x="72" y="18" fill="#fb7185" font-size="9" font-weight="700" text-anchor="middle">COMMIT PHASE</text>
            <g transform="translate(10, 38)">
              <rect width="125" height="30" rx="4" fill="#881337"/>
              <text x="62" y="18" fill="#fecdd3" font-size="8" font-weight="700" text-anchor="middle">Synchronous Flush</text>
              <rect y="38" width="125" height="30" rx="4" fill="#1e293b"/>
              <text x="62" y="18" fill="#cbd5e1" font-size="8" text-anchor="middle">Mutate Real DOM</text>
              <rect y="76" width="125" height="24" rx="4" fill="#064e3b"/>
              <text x="62" y="16" fill="#34d399" font-size="8" text-anchor="middle">useLayoutEffect</text>
            </g>
          </g>
        </svg>
      `;
    }

    // =========================================================================
    // 18. ALGORITHM MEMORY ARRAY RIBBON & POINTER TRACKER
    // ==========================================================================
    function renderRibbonLayout(q, title, steps, w, h) {
      const s0 = steps[0] || ['INPUT', 'Initial Array Ribbon', 'Indexed contiguous memory sequence', 'Ribbon'];
      const s1 = steps[1] || ['POINTERS', 'Two Pointers (L & R)', 'Shrinks search window based on invariant', 'O(1) Ptrs'];
      const s2 = steps[2] || ['WINDOW', 'Active Window Frame', 'Calculates current target predicate', 'Window'];
      const s3 = steps[3] || ['CONVERGE', 'Target Invariant Met', 'Optimal solution extracted in O(N)', 'Optimal'];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(16, 185, 129, 0.35);">
          <g transform="translate(20, 24)">
            <rect x="0" y="0" width="145" height="20" rx="4" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
            <text x="72" y="14" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">ALGORITHM RIBBON</text>
            <text x="157" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          <g transform="translate(60, 60)">
            <rect width="100" height="70" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.8"/>
            <text x="50" y="22" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle">IDX [0]</text>
            <text x="50" y="48" fill="#f8fafc" font-size="16" font-weight="700" text-anchor="middle">2</text>
            <rect x="25" y="78" width="50" height="24" rx="4" fill="#0284c7"/>
            <text x="50" y="94" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">▲ Left</text>
          </g>
          <g transform="translate(180, 60)">
            <rect width="100" height="70" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1.2"/>
            <text x="50" y="22" fill="#94a3b8" font-size="9" text-anchor="middle">IDX [1]</text>
            <text x="50" y="48" fill="#cbd5e1" font-size="16" font-weight="700" text-anchor="middle">7</text>
          </g>
          <g transform="translate(300, 60)">
            <rect width="100" height="70" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.8"/>
            <text x="50" y="22" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">IDX [2]</text>
            <text x="50" y="48" fill="#f8fafc" font-size="16" font-weight="700" text-anchor="middle">11</text>
            <rect x="25" y="78" width="50" height="24" rx="4" fill="#d97706"/>
            <text x="50" y="94" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">▲ Mid</text>
          </g>
          <g transform="translate(420, 60)">
            <rect width="100" height="70" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1.2"/>
            <text x="50" y="22" fill="#94a3b8" font-size="9" text-anchor="middle">IDX [3]</text>
            <text x="50" y="48" fill="#cbd5e1" font-size="16" font-weight="700" text-anchor="middle">15</text>
          </g>
          <g transform="translate(540, 60)">
            <rect width="100" height="70" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
            <text x="50" y="22" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IDX [4]</text>
            <text x="50" y="48" fill="#f8fafc" font-size="16" font-weight="700" text-anchor="middle">23</text>
            <rect x="25" y="78" width="50" height="24" rx="4" fill="#059669"/>
            <text x="50" y="94" fill="#ffffff" font-size="9" font-weight="700" text-anchor="middle">▲ Right</text>
          </g>
          <g transform="translate(660, 60)">
            <rect width="160" height="145" rx="8" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
            <rect width="160" height="26" rx="8" fill="#6366f1" fill-opacity="0.25"/>
            <text x="80" y="17" fill="#a5b4fc" font-size="8.5" font-weight="700" text-anchor="middle">INVARIANT STATE</text>
            <g transform="translate(10, 36)">
              <text x="0" y="14" fill="#94a3b8" font-size="8">Sum = arr[L] + arr[R]</text>
              <text x="0" y="32" fill="#38bdf8" font-size="8.5" font-weight="700">Sum = 2 + 23 = 25</text>
              <text x="0" y="50" fill="#f59e0b" font-size="8">Target = 9 (Sum &gt; Target)</text>
              <text x="0" y="68" fill="#34d399" font-size="8.5" font-weight="700">➔ Shift Right: R--</text>
              <text x="0" y="90" fill="#cbd5e1" font-size="8">Time: O(N) | Space: O(1)</text>
            </g>
          </g>
          <path d="M 60 52 L 60 40 L 640 40 L 640 52" fill="none" stroke="#eab308" stroke-width="1.8" stroke-dasharray="4 4"/>
          <text x="350" y="34" fill="#facc15" font-size="8.5" font-weight="700" text-anchor="middle">[Active Sliding Search Window]</text>
        </svg>
      `;
    }

    // =========================================================================
    // 19. SDLC GIT FLOW & PRODUCTION RELEASE PIPELINE
    // ==========================================================================
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
          <g transform="translate(20, 52)">
            <rect width="570" height="175" rx="8" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
            <rect width="570" height="30" rx="8" fill="#3b82f6" fill-opacity="0.25"/>
            <text x="285" y="20" fill="#93c5fd" font-size="10" font-weight="700" text-anchor="middle">Git Branching &amp; Code Review Pipeline</text>
            <line x1="40" y1="65" x2="520" y2="65" stroke="#3b82f6" stroke-width="3"/>
            <text x="15" y="69" fill="#60a5fa" font-size="8.5" font-weight="700">main</text>
            <circle cx="60" cy="65" r="7" fill="#3b82f6"/>
            <circle cx="160" cy="65" r="7" fill="#3b82f6"/>
            <circle cx="480" cy="65" r="8" fill="#10b981" stroke="#34d399" stroke-width="2"/>
            <text x="480" y="50" fill="#34d399" font-size="8" font-weight="700" text-anchor="middle">v2.4</text>
            <path d="M 160 65 Q 190 125 240 125 L 360 125 Q 420 125 480 65" fill="none" stroke="#a855f7" stroke-width="2.5" stroke-dasharray="4 2"/>
            <text x="300" y="142" fill="#c084fc" font-size="8.5" font-weight="700" text-anchor="middle">feature/order-service</text>
            <circle cx="270" cy="125" r="6" fill="#a855f7"/>
            <circle cx="330" cy="125" r="6" fill="#a855f7"/>
            <g transform="translate(390, 80)">
              <rect width="115" height="36" rx="4" fill="#1e1b4b" stroke="#6366f1" stroke-width="1"/>
              <text x="57" y="14" fill="#a5b4fc" font-size="8" font-weight="700" text-anchor="middle">Pull Request #42</text>
              <text x="57" y="28" fill="#34d399" font-size="7.5" text-anchor="middle">✓ 2 Approvals | CI Pass</text>
            </g>
          </g>
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

    // =========================================================================
    // 20. SPACIOUS 4-STAGE ENTERPRISE ARCHITECTURAL PIPELINE
    // ==========================================================================
    function renderEnterpriseLayout(q, title, steps, w, h) {
      const s0 = steps[0] || ['STEP 1', 'Initiation Phase', 'Request dispatch & entry validation', 'Entry'];
      const s1 = steps[1] || ['STEP 2', 'Core Orchestration', 'Business domain logic & state mutations', 'Core'];
      const s2 = steps[2] || ['STEP 3', 'Integration & Persistence', 'Atomic transaction and messaging', 'Sync'];
      const s3 = steps[3] || ['STEP 4', 'Completion & Verification', 'Sanitized response with audit telemetry', 'Success'];

      const sList = [s0, s1, s2, s3];
      const cardW = 192;
      const cardH = 160;
      const gap = 20;
      const startX = 24;
      const startY = 56;

      const colors = [
        { stroke: '#0284c7', fill: '#0369a1', text: '#38bdf8', bg: '#0f172a' },
        { stroke: '#7c3aed', fill: '#6d28d9', text: '#c084fc', bg: '#0f172a' },
        { stroke: '#f59e0b', fill: '#d97706', text: '#fbbf24', bg: '#0f172a' },
        { stroke: '#10b981', fill: '#059669', text: '#34d399', bg: '#0f172a' }
      ];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#0b0f19; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(56, 189, 248, 0.25);">
          <defs>
            <marker id="pipeArrow_${q.id}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
              <polygon points="0 0, 8 4, 0 8" fill="#38bdf8"/>
            </marker>
          </defs>
          <g transform="translate(20, 24)">
            <rect x="0" y="0" width="135" height="20" rx="4" fill="#0284c7" fill-opacity="0.2" stroke="#0284c7" stroke-width="1"/>
            <text x="67" y="14" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">SYSTEM PIPELINE</text>
            <text x="147" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
          </g>
          ${sList.map((step, idx) => {
            const cx = startX + idx * (cardW + gap);
            const cy = startY;
            const col = colors[idx];
            return `
              <g transform="translate(${cx}, ${cy})">
                <rect width="${cardW}" height="${cardH}" rx="8" fill="${col.bg}" stroke="${col.stroke}" stroke-width="1.5"/>
                <rect width="${cardW}" height="32" rx="8" fill="${col.stroke}" fill-opacity="0.25"/>
                <text x="12" y="21" fill="${col.text}" font-size="10.5" font-weight="700">0${idx + 1}. ${escSvg(step[0])}</text>
                <g transform="translate(10, 42)">
                  <rect width="${cardW - 20}" height="34" rx="4" fill="#1e293b"/>
                  <text x="8" y="21" fill="#f8fafc" font-size="9.5" font-weight="600">${escSvg(step[1])}</text>
                  <text x="8" y="52" fill="#94a3b8" font-size="8.5">${escSvg(step[2])}</text>
                  <rect y="74" width="${cardW - 20}" height="22" rx="4" fill="${col.stroke}" fill-opacity="0.15"/>
                  <text x="${(cardW - 20) / 2}" y="89" fill="${col.text}" font-size="8" font-weight="600" text-anchor="middle">${escSvg(step[3] || 'Verified')}</text>
                </g>
              </g>
              ${idx < 3 ? `<line x1="${cx + cardW + 2}" y1="${cy + cardH / 2}" x2="${cx + cardW + gap - 2}" y2="${cy + cardH / 2}" stroke="#38bdf8" stroke-width="2" marker-end="url(#pipeArrow_${q.id})"/>` : ''}
            `;
          }).join('')}
        </svg>
      `;
    }

    '''

# Inject into HTML
new_html = html[:idx_start] + engine_code + html[idx_end:]

with open('senior-dotnet-interview-portal.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

new_size_mb = os.path.getsize('senior-dotnet-interview-portal.html') / (1024 * 1024)
print(f"Injection complete! New file size: {new_size_mb:.2f} MB")

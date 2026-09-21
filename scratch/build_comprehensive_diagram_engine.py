import re
import os
import sys

print("Building Comprehensive Non-Repeating Visual Diagram Engine (34 Topologies)...")

engine_code = r'''
    // =========================================================================
    // SVG ARCHITECTURAL BLUEPRINT ENGINE - 34 BESPOKE NON-REPEATING TOPOLOGIES
    // =========================================================================

    function escSvg(str) {
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&apos;');
    }

    function wrapText(text, maxChars) {
      if (!text) return [];
      const words = String(text).trim().split(/\s+/);
      const lines = [];
      let currentLine = '';

      for (let i = 0; i < words.length; i++) {
        const word = words[i];
        if (!currentLine) {
          currentLine = word;
        } else if ((currentLine + ' ' + word).trim().length <= maxChars) {
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
        return `<text x="${x}" y="${y + idx * lineHeight}" fill="${color}" font-size="${fontSize}" font-weight="500" text-anchor="${anchor}">${escSvg(line)}</text>`;
      }).join('\n');
    }

    function hasWord(text, word) {
      const re = new RegExp('\\b' + word + '\\b', 'i');
      return re.test(text);
    }

    function anyWord(text, words) {
      for (let i = 0; i < words.length; i++) {
        const w = words[i];
        if (w.includes(' ') || w.includes('-') || w.includes('<') || w.includes('?') || w.includes('.')) {
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
      const dTitle = (q.diagramTitle || '').toLowerCase();
      const text = tLow + ' ' + dTitle;
      const cleanTitle = escSvg(title);

      const w = 900;
      const h = 255;

      // 1. Compiler, Roslyn, IL, JIT, Tiered Compilation
      if (anyWord(text, ['compiled', 'interprete', 'compilation', 'roslyn', 'il code', 'intermediate language', 'jit', 'just-in-time', 'csc', 'assembly', 'assemblies', 'metadata in', 'tiered compilation', 'aot', 'ahead-of-time', 'clr execution', 'top-level statement', 'bytecode'])) {
        return renderCompilerIlLayout(q, cleanTitle, steps, w, h);
      }

      // 2. Concurrency / Deadlocks / Thread Locks / Race Conditions
      if (anyWord(text, ['deadlock', 'deadlocks', 'race condition', 'concurrency', 'multithreading', 'lock', 'locks', 'mutex', 'semaphoreslim', 'semaphore', 'interlocked', 'monitor.enter', 'thread synchronization', 'thread safety', 'thread-safe', 'readerwriterlockslim', 'spinwait', 'critical section', 'pessimistic lock', 'optimistic lock', 'lock escalation'])) {
        return renderConcurrencyDeadlockLayout(q, cleanTitle, steps, w, h);
      }

      // 3. SQL Joins & Set Operations
      if (anyWord(text, ['inner join', 'left join', 'right join', 'full outer join', 'cross join', 'self join', 'hash join', 'merge join', 'nested loop', 'join vs', 'joins in', 'union all', 'intersect', 'except'])) {
        return renderVennJoinLayout(q, cleanTitle, steps, w, h);
      }

      // 4. SQL Transactions & ACID & MVCC
      if (anyWord(text, ['acid', 'transaction', 'transactions', 'isolation level', 'dirty read', 'non-repeatable', 'phantom read', 'snapshot isolation', 'serializable', 'wal', 'write-ahead', 'checkpoint', 'savepoint', 'rollback', '2pc', 'two phase commit'])) {
        return renderTransactionMvccLayout(q, cleanTitle, steps, w, h);
      }

      // 5. Normalization & Relational Schema & Keys
      if (anyWord(text, ['normalization', '1nf', '2nf', '3nf', 'bcnf', 'denormalization', 'primary key', 'foreign key', 'candidate key', 'composite key', 'surrogate key', 'er diagram', 'entity relationship', 'schema design', 'table constraint', 'referential integrity'])) {
        return renderErSchemaLayout(q, cleanTitle, steps, w, h);
      }

      // 6. B-Tree & Database Indexing Internals
      if (anyWord(text, ['b-tree', 'btree', 'index seek', 'index scan', 'clustered index', 'non-clustered index', 'covering index', 'filtered index', 'composite index', 'page split', 'fill factor', 'fragmentation', 'indexing'])) {
        return renderBTreeLayout(q, cleanTitle, steps, w, h);
      }

      // 7. SQL Query Engine & Cost-Based Optimizer
      if (cat === 'sql' || anyWord(text, ['execution plan', 'query plan', 'cbo', 'cost-based', 'query optimizer', 'cardinality estimation', 'statistics in sql', 'stored procedure', 'stored procedures', 'view vs', 'cte', 'common table expression', 'window function', 'partition by', 'group by', 'aggregate', 'tempdb', 'table variable'])) {
        return renderSqlEngineLayout(q, cleanTitle, steps, w, h);
      }

      // 8. Memory: Stack vs Heap & Boxing & Value/Ref Types & Span & Strings
      if (anyWord(text, ['stack vs heap', 'stack and heap', 'boxing', 'unboxing', 'value type', 'value types', 'reference type', 'reference types', 'struct vs class', 'class vs struct', 'ref struct', 'span<t>', 'memory<t>', 'stackalloc', 'managed vs unmanaged', 'pointer', 'unsafe code', 'sizeof', 'string interpolation', 'string concatenation', 'stringbuilder', 'strings immutable', 'string interning', 'ref parameter', 'out parameter', 'in parameter', 'parameters:', 'data types', 'variables and'])) {
        return renderMemoryLayout(q, cleanTitle, steps, w, h);
      }

      // 9. Memory: Garbage Collection & Lifetimes
      if (anyWord(text, ['garbage collection', 'garbage collector', 'gc', 'generation 0', 'generation 1', 'generation 2', 'gen 0', 'gen 1', 'gen 2', 'loh', 'large object heap', 'poh', 'pinned object', 'idisposable', 'dispose pattern', 'finalizer', 'finalize', 'destructor', 'suppressfinalize', 'memory leak', 'memory leaks', 'weakreference', 'memory pressure'])) {
        return renderGenerationalGcLayout(q, cleanTitle, steps, w, h);
      }

      // 10. Collections: Dictionary / HashSet / Hash Code / Buckets
      if (anyWord(text, ['dictionary', 'hashset', 'hashtable', 'hash table', 'hash code', 'gethashcode', 'hash collision', 'buckets', 'lookup o(1)', 'keyvaluepair'])) {
        return renderHashBucketLayout(q, cleanTitle, steps, w, h);
      }

      // 11. Collections: Array / List<T> / Ribbon Tape & Pointers & Dates & Enums
      if (cat === 'coding' || anyWord(text, ['array', 'arrays', 'list<t>', 'two pointer', 'two sum', 'sliding window', 'binary search', 'index', 'indexing', 'linked list', 'sort', 'quicksort', 'mergesort', 'dynamic programming', 'dp', 'knapsack', 'bfs', 'dfs', 'graph', 'tree traversal', 'leetcode', 'big o', 'o(n)', 'enum', 'enums', 'datetime', 'datetimeoffset', 'dateonly', 'timeonly', 'substring', 'indexof'])) {
        return renderRibbonLayout(q, cleanTitle, steps, w, h);
      }

      // 12. Delegates & Events & Observer
      if (anyWord(text, ['delegate', 'delegates', 'multicastdelegate', 'event', 'events', 'eventhandler', 'action<', 'func<', 'predicate<', 'anonymous method', 'lambda expression', 'observer pattern', 'callback', 'callbacks'])) {
        return renderDelegateEventLayout(q, cleanTitle, steps, w, h);
      }

      // 13. Exception Handling & Call Stack Unwinding
      if (anyWord(text, ['exception', 'exceptions', 'try', 'catch', 'finally', 'throw ex', 'throw vs', 'call stack', 'stack unwinding', 'aggregateexception', 'custom exception', 'stacktrace', 'nullreferenceexception'])) {
        return renderExceptionStackLayout(q, cleanTitle, steps, w, h);
      }

      // 14. Dependency Injection & Service Lifetimes
      if (anyWord(text, ['dependency injection', 'di container', 'service lifetime', 'transient', 'scoped', 'singleton', 'iservicecollection', 'iserviceprovider', 'autofac', 'ninject', 'ioc container', 'inversion of control'])) {
        return renderDiLifetimeLayout(q, cleanTitle, steps, w, h);
      }

      // 15. OOP, SOLID, Design Patterns & LLD & Generics & Interfaces & Constants
      if (cat === 'oop' || cat === 'patterns' || cat === 'lld' || anyWord(text, ['solid', 'srp', 'ocp', 'lsp', 'isp', 'dip', 'polymorphism', 'encapsulation', 'inheritance', 'abstract class', 'interface', 'vtable', 'factory pattern', 'builder pattern', 'singleton pattern', 'strategy pattern', 'adapter pattern', 'decorator pattern', 'repository pattern', 'unit of work', 'loose coupling', 'high cohesion', 'generic', 'generics', 'generic constraint', 'const vs', 'readonly', 'static readonly', 'scope and lifetime'])) {
        return renderOopClassLayout(q, cleanTitle, steps, w, h);
      }

      // 16. Entity Framework Core & LINQ
      if (cat === 'efcore' || cat === 'linq' || anyWord(text, ['dbcontext', 'change tracker', 'entity framework', 'ef core', 'lazy loading', 'eager loading', 'explicit loading', 'iqueryable', 'ienumerable', 'migration', 'migrations', 'n+1 problem', 'fluent api', 'shadow property', 'hasdata', 'linq query', 'deferred execution', 'immediate execution'])) {
        return renderEfCoreLayout(q, cleanTitle, steps, w, h);
      }

      // 17. Circuit Breaker & Resilience
      if (anyWord(text, ['circuit breaker', 'resilience', 'polly', 'retry policy', 'exponential backoff', 'fallback policy', 'bulkhead', 'rate limiter', 'rate limiting', 'throttling'])) {
        return renderCircuitBreakerLayout(q, cleanTitle, steps, w, h);
      }

      // 18. Concentric Russian-Doll Middleware
      if (anyWord(text, ['middleware', 'request delegate', 'russian doll', 'pipeline execution', 'app.use', 'app.run', 'usemiddleware', 'pipeline filter'])) {
        return renderMiddlewareLayout(q, cleanTitle, steps, w, h);
      }

      // 19. HTTP Flow & Web API & REST & Controllers
      if (cat === 'webapi' || cat === 'mvc' || anyWord(text, ['http', 'https', 'controller', 'controllers', 'action filter', 'model binding', 'model validation', 'rest', 'restful', 'status code', 'status codes', 'kestrel', 'minimal api', 'content negotiation', 'routing in', 'endpoint', 'cors', 'httpclient', 'ihttpclientfactory'])) {
        return renderHttpFlowLayout(q, cleanTitle, steps, w, h);
      }

      // 20. Security, Authentication, JWT, OAuth & Cryptography
      if (cat === 'security' || anyWord(text, ['jwt', 'oauth', 'token', 'bearer', 'claims', 'identity', 'authentication', 'authorization', 'role-based', 'claim-based', 'cryptography', 'encryption', 'aes', 'rsa', 'hashing', 'bcrypt', 'argon2', 'salt', 'csrf', 'xss', 'sql injection', 'tls', 'ssl', 'owasp'])) {
        return renderSecurityLayout(q, cleanTitle, steps, w, h);
      }

      // 21. Testing & QA & Test Pyramids
      if (cat === 'testing' || anyWord(text, ['unit test', 'integration test', 'end to end', 'e2e', 'test pyramid', 'xunit', 'nunit', 'mstest', 'mock', 'moq', 'stub', 'fake', 'tdd', 'test driven', 'bdd', 'code coverage', 'assert', 'arrange act assert', 'sonarqube'])) {
        return renderTestingLayout(q, cleanTitle, steps, w, h);
      }

      // 22. JavaScript Engine & Runtime Internals
      if (cat === 'js' || anyWord(text, ['javascript', 'v8', 'call stack in js', 'event loop in js', 'microtask', 'macrotask', 'closure', 'closures', 'hoisting', 'prototype chain', 'prototypal', 'promise in js', 'promise.all', 'debounce', 'throttle', 'currying', 'dom manipulation', 'bubbling', 'capturing', 'es6'])) {
        return renderJsRuntimeLayout(q, cleanTitle, steps, w, h);
      }

      // 23. React Lifecycle & useEffect & Hooks
      if (cat === 'react' && anyWord(text, ['useeffect', 'usestate', 'usememo', 'usecallback', 'useref', 'usereducer', 'usecontext', 'custom hook', 'hook rules', 'lifecycle', 'componentdidmount', 'cleanup function', 'dependency array', 'mounting', 'unmounting', 'rerender', 're-render'])) {
        return renderReactComponentLifecycleLayout(q, cleanTitle, steps, w, h);
      }

      // 24. React Fiber & Virtual DOM & Diffing
      if (cat === 'react' || anyWord(text, ['react', 'virtual dom', 'fiber', 'reconciliation', 'reconcil', 'diffing algorithm', 'props vs state', 'jsx', 'server component', 'rsc', 'suspense', 'react.memo'])) {
        return renderFiberLayout(q, cleanTitle, steps, w, h);
      }

      // 25. Redux & State Machines & Cycles
      if (cat === 'redux' || anyWord(text, ['redux', 'redux toolkit', 'rtk', 'slice', 'createslice', 'action creator', 'reducer', 'dispatch', 'unidirectional data flow', 'reselect', 'selector', 'thunk', 'redux-thunk', 'redux saga'])) {
        return renderCycleLayout(q, cleanTitle, steps, w, h);
      }

      // 26. Microservices & Outbox & Kafka & Event Streaming
      if (anyWord(text, ['outbox', 'kafka', 'rabbitmq', 'cdc', 'debezium', 'event sourcing', 'cqrs', 'saga', 'distributed transaction', 'event-driven', 'event streaming', 'topic partition', 'consumer group', 'message queue'])) {
        return renderDistributedLayout(q, cleanTitle, steps, w, h);
      }

      // 27. Pub/Sub & Message Broker Fanout
      if (anyWord(text, ['pub/sub', 'pubsub', 'sns', 'eventbridge', 'fanout', 'broker', 'message broker', 'exchange', 'publish subscribe'])) {
        return renderPubSubLayout(q, cleanTitle, steps, w, h);
      }

      // 28. Multi-Tier Cache Hierarchy
      if (anyWord(text, ['cache', 'redis', 'in-memory cache', 'cache-aside', 'write-through', 'write-behind', 'distributed cache', 'l1 cache', 'l2 cache', 'cache stampede', 'cache invalidation', 'sliding expiration', 'absolute expiration'])) {
        return renderCacheTierLayout(q, cleanTitle, steps, w, h);
      }

      // 29. Cloud Architecture & AWS & Serverless & HLD
      if (cat === 'cloud' || cat === 'aws' || cat === 'hld' || (cat === 'architecture' && anyWord(text, ['cloud', 'aws', 'azure', 'serverless', 'lambda', 's3', 'dynamodb', 'sqs', 'api gateway', 'multi-az', 'container', 'docker', 'kubernetes', 'k8s', 'microservice architecture', 'high availability', 'scalability']))) {
        return renderCloudInfraLayout(q, cleanTitle, steps, w, h);
      }

      // 30. Git & SDLC & CI/CD & DevOps
      if (cat === 'sdlc' || anyWord(text, ['git', 'github', 'branching', 'pull request', 'merge vs rebase', 'rebase', 'cherry-pick', 'ci/cd', 'devops', 'pipeline in devops', 'agile', 'scrum', 'kanban', 'sprint', 'blue/green', 'canary'])) {
        return renderSdlcLayout(q, cleanTitle, steps, w, h);
      }

      // 31. AI & LLM & RAG & Semantic Kernel
      if (cat === 'dotnet-ai' || anyWord(text, ['ai', 'llm', 'rag', 'retrieval-augmented', 'gpt', 'chatgpt', 'openai', 'embedding', 'embeddings', 'vector search', 'vector database', 'cosine similarity', 'hnsw', 'semantic kernel', 'prompt engineering', 'tokens', 'chunking', 'hallucination', 'langchain', 'onnx'])) {
        return renderAiRagLayout(q, cleanTitle, steps, w, h);
      }

      // 32. Async / Await & Task State Machine
      if (cat === 'async' || anyWord(text, ['async', 'await', 'task', 'valuetask', 'threadpool', 'movenext', 'iasyncstatemachine', 'iocp', 'synchronizationcontext', 'configureawait', 'task.whenall', 'task.whenany', 'cancellationtoken', 'channel<t>', 'parallel.foreach'])) {
        return renderAsyncLayout(q, cleanTitle, steps, w, h);
      }

      // 33. Conditionals & Branching & Pattern Matching
      if (anyWord(text, ['if/else', 'switch', 'switch expression', 'pattern matching', 'conditional', 'branching', 'tryparse', 'ternary', 'null-coalescing', 'nullable', 'var keyword', 'implicit typing', 'type conversion', 'casting', 'safe casting', 'is and as', 'math operations', 'integer division', 'null-conditional'])) {
        return renderBranchLayout(q, cleanTitle, steps, w, h);
      }

      // 34. Architecture General Fallback
      if (cat === 'architecture') {
        return renderCloudInfraLayout(q, cleanTitle, steps, w, h);
      }

      // High-Clarity Stepped Enterprise Pipeline (Fallback)
      return renderPipelineLayout(q, cleanTitle, steps, w, h);
    }
'''

print("Header & classification logic prepared.")

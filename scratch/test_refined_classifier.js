const fs = require('fs');

const html = fs.readFileSync('senior-dotnet-interview-portal.html', 'utf8');
const escIdx = html.indexOf('function escSvg');
const lastBracket = html.lastIndexOf('];', escIdx);
const qbStart = html.indexOf('const QUESTION_BANK = [');
const questions = JSON.parse(html.substring(qbStart + 'const QUESTION_BANK = '.length, lastBracket + 1));

function hasWord(text, word) {
  const re = new RegExp('\\b' + word + '\\b', 'i');
  return re.test(text);
}

function anyWord(text, words) {
  for (let i = 0; i < words.length; i++) {
    if (words[i].includes(' ')) {
      if (text.includes(words[i])) return true;
    } else {
      if (hasWord(text, words[i])) return true;
    }
  }
  return false;
}

function classify(q) {
  const tLow = (q.q || '').toLowerCase();
  const cat = (q.category || '').toLowerCase();

  // 1. AI & LLM / RAG / Semantic Kernel
  if (cat === 'dotnet-ai' || anyWord(tLow, ['ai', 'llm', 'rag', 'gpt', 'openai', 'chatgpt', 'embedding', 'embeddings', 'vector search', 'vector db', 'tokens', 'prompt', 'prompts', 'hallucination', 'semantic kernel', 'langchain'])) {
    return 'ai_rag';
  }

  // 2. React, Virtual DOM, Fiber, Hooks
  if (cat === 'react' || anyWord(tLow, ['react', 'virtual dom', 'fiber', 'reconcil', 'hook', 'hooks', 'useeffect', 'usestate', 'usememo', 'usecallback', 'props', 'jsx'])) {
    return 'react_fiber';
  }

  // 3. Redux, State Machine & Cyclotron
  if (cat === 'redux' || anyWord(tLow, ['redux', 'action', 'actions', 'reducer', 'reducers', 'dispatch', 'store', 'unidirectional', 'state machine', 'cyclotron'])) {
    return 'redux_cyclotron';
  }

  // 4. OOP, SOLID, Design Patterns, LLD
  if (cat === 'oop' || cat === 'patterns' || cat === 'lld' || anyWord(tLow, ['solid', 'polymorphism', 'polymorphic', 'encapsulation', 'inheritance', 'abstract class', 'interface', 'factory', 'singleton', 'dependency inversion', 'liskov', 'coupling', 'cohesion', 'vtable', 'class vs struct', 'oop'])) {
    return 'oop_class';
  }

  // 5. Entity Framework Core & LINQ
  if (cat === 'efcore' || cat === 'linq' || anyWord(tLow, ['dbcontext', 'change tracker', 'entity framework', 'ef core', 'lazy loading', 'eager loading', 'linq', 'iqueryable', 'ienumerable', 'migration', 'n+1', 'hasdata', 'fluent api'])) {
    return 'efcore_orm';
  }

  // 6. SQL Engine & B-Tree Indexing
  if (cat === 'sql' || anyWord(tLow, ['sql', 'query plan', 'execution plan', 'acid', 'transaction', 'isolation level', 'deadlock', 'join', 'stored procedure', 'clustered', 'non-clustered', 'b-tree', 'index seek', 'index scan', 'page split'])) {
    if (anyWord(tLow, ['b-tree', 'btree', 'index seek', 'index scan', 'clustered index', 'non-clustered index', 'page split', 'fill factor'])) {
      return 'btree';
    }
    return 'sql_engine';
  }

  // 7. Microservices Outbox & Event Streaming
  if (anyWord(tLow, ['outbox', 'kafka', 'rabbitmq', 'cdc', 'debezium', 'event sourcing', 'cqrs', 'saga', 'distributed transaction', 'two phase commit', '2pc'])) {
    return 'distributed_outbox';
  }

  // 8. Cloud Architecture, AWS, Serverless, HLD
  if (cat === 'cloud' || cat === 'aws' || cat === 'hld' || (cat === 'architecture' && anyWord(tLow, ['cloud', 'aws', 'azure', 'serverless', 'lambda', 'container', 'docker', 'kubernetes', 's3', 'dynamodb', 'sqs', 'sns', 'gateway', 'microservice']))) {
    return 'cloud_infra';
  }

  // 9. Web API, MVC, Routing & HTTP Lifecycle
  if (cat === 'webapi' || cat === 'mvc' || anyWord(tLow, ['http', 'controller', 'action filter', 'model binding', 'rest', 'status code', 'kestrel', 'middleware', 'endpoint', 'minimal api', 'content negotiation'])) {
    if (anyWord(tLow, ['middleware', 'request delegate', 'pipeline', 'russian doll'])) {
      return 'middleware_onion';
    }
    return 'http_flow';
  }

  // 10. Security, Auth, Identity, Cryptography
  if (cat === 'security' || anyWord(tLow, ['jwt', 'oauth', 'token', 'cryptography', 'encryption', 'hash', 'csrf', 'xss', 'sql injection', 'identity', 'claims', 'authentication', 'authorization', 'cors', 'ssl', 'tls'])) {
    return 'security_vault';
  }

  // 11. Testing, CI/CD, QA, Quality Gates
  if (cat === 'testing' || anyWord(tLow, ['unit test', 'integration test', 'xunit', 'nunit', 'mock', 'moq', 'assert', 'tdd', 'test pyramid', 'sonarqube', 'code coverage', 'stub', 'fake'])) {
    return 'testing_pyramid';
  }

  // 12. JavaScript Engine, V8, Call Stack, Event Loop
  if (cat === 'js' || anyWord(tLow, ['javascript', 'v8', 'call stack', 'event loop', 'microtask', 'closure', 'hoisting', 'prototype', 'promise', 'macrotask', 'async in js'])) {
    return 'js_runtime';
  }

  // 13. Async / Await, ThreadPool, Concurrency, IOCP
  if (cat === 'async' || anyWord(tLow, ['async', 'await', 'task', 'threadpool', 'thread', 'movenext', 'iocp', 'deadlock', 'synchronizationcontext', 'channel', 'valuetask', 'cancellationtoken'])) {
    return 'async_statemachine';
  }

  // 14. Low-level Memory, CLR, GC, Value vs Reference
  if (anyWord(tLow, ['box', 'boxing', 'unboxing', 'stack vs heap', 'stack and heap', 'value type', 'reference type', 'garbage collector', 'gc', 'generation', 'gen 0', 'gen 1', 'gen 2', 'loh', 'poh', 'managed code', 'unmanaged', 'span<t>', 'ref struct', 'stringbuilder', 'immutable', 'memory layout', 'struct vs class'])) {
    return 'memory_stack_heap';
  }

  // 15. Coding Algorithms, Ribbon, Pointers, Binary Search
  if (cat === 'coding' || anyWord(tLow, ['pointer', 'binary search', 'sliding window', 'array', 'subsequence', 'two sum', 'leetcode', 'sort', 'tree', 'linked list', 'dynamic programming', 'graph', 'recursion', 'backtracking'])) {
    return 'algo_ribbon';
  }

  // 16. SDLC, Git, Agile, DevOps
  if (cat === 'sdlc' || anyWord(tLow, ['git', 'agile', 'scrum', 'kanban', 'sprint', 'ci/cd', 'devops', 'pull request', 'branching', 'merge vs rebase'])) {
    return 'sdlc_gitflow';
  }

  // 17. Decision Tree / Branching / Caching Fallback
  if (anyWord(tLow, ['cache', 'redis', 'circuit breaker', 'tryparse', 'fallback', 'polly', 'switch', 'branch', 'if/else', 'strategy'])) {
    return 'decision_branch';
  }

  // 18. Architecture General
  if (cat === 'architecture') {
    return 'cloud_infra';
  }

  // 19. Default Enterprise Flow
  return 'enterprise_flow';
}

const counts = {};
questions.forEach(q => {
  const layout = classify(q);
  counts[layout] = (counts[layout] || 0) + 1;
});

console.log("Refined Classifier results for all 3,418 questions:");
console.table(counts);

const fs = require('fs');

console.log("Testing 20-archetype classifier design...");

// We'll test classifier logic on all 3418 questions
const html = fs.readFileSync('senior-dotnet-interview-portal.html', 'utf8');
const escIdx = html.indexOf('function escSvg');
const lastBracket = html.lastIndexOf('];', escIdx);
const qbStart = html.indexOf('const QUESTION_BANK = [');
const questions = JSON.parse(html.substring(qbStart + 'const QUESTION_BANK = '.length, lastBracket + 1));

console.log("Total questions loaded:", questions.length);

function anyMatch(text, terms) {
  for (let i = 0; i < terms.length; i++) {
    if (text.includes(terms[i])) return true;
  }
  return false;
}

function classify(q) {
  const tLow = (q.q || '').toLowerCase();
  const cat = (q.category || '').toLowerCase();

  // 1. AI & LLM / RAG / Semantic Kernel
  if (cat === 'dotnet-ai' || anyMatch(tLow, ['ai', 'llm', 'semantic kernel', 'rag', 'embedding', 'vector', 'openai', 'gpt', 'token', 'prompt', 'hallucinat', 'chatgpt'])) {
    return 'ai_rag';
  }

  // 2. OOP, SOLID, Design Patterns, Low-Level Design (LLD)
  if (cat === 'oop' || cat === 'patterns' || cat === 'lld' || anyMatch(tLow, ['solid', 'polymorph', 'encapsulat', 'inherit', 'abstract class', 'interface', 'factory', 'singleton', 'dependency inversion', 'liskov', 'coupling', 'cohesion', 'vtable', 'class vs struct'])) {
    return 'oop_class';
  }

  // 3. Entity Framework Core & LINQ
  if (cat === 'efcore' || cat === 'linq' || anyMatch(tLow, ['dbcontext', 'change tracker', 'entity framework', 'ef core', 'lazy load', 'eager load', 'linq', 'iqueryable', 'ienumerable', 'migration', 'n+1', 'hasdata', 'fluecnt api'])) {
    return 'efcore_orm';
  }

  // 4. SQL Engine, Query Optimization, Joins, Transactions & ACID
  if (cat === 'sql' || anyMatch(tLow, ['sql', 'query plan', 'execution plan', 'acid', 'transaction', 'isolation level', 'deadlock', 'join', 'stored procedure', 'clustered', 'non-clustered', 'b-tree', 'index seek', 'index scan', 'page split'])) {
    if (anyMatch(tLow, ['b-tree', 'index seek', 'index scan', 'clustered index', 'non-clustered index', 'page split', 'fill factor'])) {
      return 'btree';
    }
    return 'sql_engine';
  }

  // 5. Cloud Architecture, AWS, Microservices, Serverless, HLD
  if (cat === 'cloud' || cat === 'aws' || cat === 'hld' || (cat === 'architecture' && anyMatch(tLow, ['cloud', 'aws', 'azure', 'serverless', 'lambda', 'container', 'docker', 'kubernetes', 's3', 'dynamodb', 'sqs', 'sns', 'gateway', 'microservice']))) {
    if (anyMatch(tLow, ['outbox', 'kafka', 'rabbitmq', 'cdc', 'debezium', 'event sourcing', 'cqrs', 'saga'])) {
      return 'distributed_outbox';
    }
    return 'cloud_infra';
  }

  // 6. Web API, MVC, Routing & HTTP Lifecycle
  if (cat === 'webapi' || cat === 'mvc' || anyMatch(tLow, ['http', 'controller', 'action filter', 'model binding', 'rest', 'status code', 'kestrel', 'middleware', 'endpoint', 'minimal api', 'content negotiation'])) {
    if (anyMatch(tLow, ['middleware', 'request delegate', 'pipeline', 'russian doll'])) {
      return 'middleware_onion';
    }
    return 'http_flow';
  }

  // 7. Security, Auth, Identity, Cryptography
  if (cat === 'security' || anyMatch(tLow, ['jwt', 'oauth', 'token', 'cryptograph', 'encrypt', 'hash', 'csrf', 'xss', 'sql injection', 'identity', 'claims', 'authentication', 'authorization', 'cors', 'ssl', 'tls'])) {
    return 'security_vault';
  }

  // 8. Testing, CI/CD, QA, Quality Gates
  if (cat === 'testing' || anyMatch(tLow, ['unit test', 'integration test', 'xunit', 'nunit', 'mock', 'moq', 'assert', 'tdd', 'test pyramid', 'sonarqube', 'code coverage', 'stub', 'fake'])) {
    return 'testing_pyramid';
  }

  // 9. JavaScript Engine, V8, Call Stack, Event Loop
  if (cat === 'js' || anyMatch(tLow, ['javascript', 'v8', 'call stack', 'event loop', 'microtask', 'closure', 'hoisting', 'prototype', 'promise', 'async in js'])) {
    return 'js_runtime';
  }

  // 10. React, Virtual DOM, Fiber, Hooks
  if (cat === 'react' || anyMatch(tLow, ['react', 'virtual dom', 'fiber', 'reconcil', 'hook', 'useeffect', 'usestate', 'usememo', 'usecallback', 'props', 'jsx'])) {
    return 'react_fiber';
  }

  // 11. Redux, State Machine & Orbital Cycles
  if (cat === 'redux' || anyMatch(tLow, ['redux', 'action', 'reducer', 'dispatch', 'store', 'unidirectional', 'state machine', 'cycl'])) {
    return 'redux_cyclotron';
  }

  // 12. Async / Await, ThreadPool, Concurrency, IOCP
  if (cat === 'async' || anyMatch(tLow, ['async', 'await', 'task', 'threadpool', 'thread', 'movenext', 'iocp', 'deadlock', 'synchronizationcontext', 'channel', 'valuetask', 'cancellationtoken'])) {
    return 'async_statemachine';
  }

  // 13. Low-level Memory, CLR, GC, Value vs Reference
  if (anyMatch(tLow, ['box', 'unbox', 'stack vs heap', 'stack and heap', 'value type', 'reference type', 'garbage collector', 'gc', 'generation', 'gen 0', 'gen 1', 'gen 2', 'loh', 'poh', 'managed code', 'unmanaged', 'span<t>', 'ref struct', 'stringbuilder', 'immutab', 'memory layout', 'struct vs class'])) {
    return 'memory_stack_heap';
  }

  // 14. Coding Algorithms, Ribbon, Pointers, Binary Search
  if (cat === 'coding' || anyMatch(tLow, ['pointer', 'binary search', 'sliding window', 'array', 'subsequence', 'two sum', 'leetcode', 'sort', 'tree', 'linked list', 'dynamic programming', 'graph'])) {
    return 'algo_ribbon';
  }

  // 15. SDLC, Git, Agile, DevOps
  if (cat === 'sdlc' || anyMatch(tLow, ['git', 'agile', 'scrum', 'kanban', 'sprint', 'ci/cd', 'devops', 'pull request', 'branching', 'merge vs rebase'])) {
    return 'sdlc_gitflow';
  }

  // 16. Decision Tree / Branching / Caching Fallback
  if (anyMatch(tLow, ['cache', 'redis', 'circuit breaker', 'tryparse', 'fallback', 'polly', 'switch', 'branch', 'if/else', 'strategy'])) {
    return 'decision_branch';
  }

  // 17. Architecture General
  if (cat === 'architecture') {
    return 'cloud_infra';
  }

  // 18. Default Enterprise
  return 'enterprise_flow';
}

const counts = {};
questions.forEach(q => {
  const layout = classify(q);
  counts[layout] = (counts[layout] || 0) + 1;
});

console.log("Classifier results for all 3,418 questions:");
console.table(counts);

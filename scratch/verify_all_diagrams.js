const fs = require('fs');
const vm = require('vm');

console.log("Loading and verifying senior-dotnet-interview-portal.html...");
const content = fs.readFileSync('senior-dotnet-interview-portal.html', 'utf8');

const scriptOpen = content.indexOf('<script>');
const scriptClose = content.lastIndexOf('</script>');
const scriptText = content.slice(scriptOpen + '<script>'.length, scriptClose);

const sandbox = {
  console: console,
  window: {},
  document: {
    documentElement: { setAttribute: () => {} },
    getElementById: () => ({ addEventListener: () => {}, innerHTML: '', style: {} }),
    querySelectorAll: () => [],
    addEventListener: () => {}
  },
  localStorage: {
    getItem: () => null,
    setItem: () => {}
  }
};
sandbox.window = sandbox;

const inspectCode = `
  const summary = {
    total: QUESTION_BANK.length,
    validSvg: 0,
    empty: 0,
    layouts: {},
    categories: {}
  };

  QUESTION_BANK.forEach(q => {
    if (q.diagram && q.diagram.includes('<svg') && q.diagram.includes('viewBox="0 0 900 255"')) {
      summary.validSvg++;
    } else {
      summary.empty++;
    }

    let detected = 'unknown';
    const d = q.diagram || '';
    if (d.includes('COMPILATION &amp; JIT')) detected = 'CompilerIl';
    else if (d.includes('CONCURRENCY &amp; LOCKS')) detected = 'ConcurrencyDeadlock';
    else if (d.includes('RELATIONAL JOINS &amp; SETS')) detected = 'VennJoin';
    else if (d.includes('ACID &amp; TRANSACTIONS')) detected = 'TransactionMvcc';
    else if (d.includes('SCHEMA &amp; NORMALIZATION')) detected = 'ErSchema';
    else if (d.includes('GARBAGE COLLECTION (GC)')) detected = 'GenerationalGc';
    else if (d.includes('HASH BUCKET ARRAY')) detected = 'HashBucket';
    else if (d.includes('DELEGATES &amp; EVENTS')) detected = 'DelegateEvent';
    else if (d.includes('EXCEPTION STACK UNWIND')) detected = 'ExceptionStack';
    else if (d.includes('DI SERVICE LIFETIMES')) detected = 'DiLifetime';
    else if (d.includes('CIRCUIT BREAKER &amp; POLLY')) detected = 'CircuitBreaker';
    else if (d.includes('REACT HOOK LIFECYCLE')) detected = 'ReactLifecycle';
    else if (d.includes('HTTP &amp; WEB API FLOW')) detected = 'HttpFlow';
    else if (d.includes('ASYNC STATE MACHINE')) detected = 'Async';
    else if (d.includes('UML CONTRACT')) detected = 'OopClass';
    else if (d.includes('EF CORE / ORM')) detected = 'EfCore';
    else if (d.includes('SQL ENGINE')) detected = 'SqlEngine';
    else if (d.includes('TREE HIERARCHY')) detected = 'BTree';
    else if (d.includes('NEURAL RAG CIRCUIT')) detected = 'AiRag';
    else if (d.includes('CLOUD TOPOLOGY')) detected = 'CloudInfra';
    else if (d.includes('DISTRIBUTED STREAM')) detected = 'Distributed';
    else if (d.includes('EVENT FANOUT')) detected = 'PubSub';
    else if (d.includes('CACHE TIERS')) detected = 'CacheTier';
    else if (d.includes('MIDDLEWARE ONION')) detected = 'Middleware';
    else if (d.includes('SECURITY &amp; IDENTITY')) detected = 'Security';
    else if (d.includes('TEST PYRAMID')) detected = 'Testing';
    else if (d.includes('V8 JS RUNTIME')) detected = 'JsRuntime';
    else if (d.includes('STATE CYCLOTRON')) detected = 'Cycle';
    else if (d.includes('CLR MEMORY')) detected = 'Memory';
    else if (d.includes('DECISION BRANCH')) detected = 'Branch';
    else if (d.includes('REACT FIBER DIFF')) detected = 'Fiber';
    else if (d.includes('ALGORITHM RIBBON')) detected = 'Ribbon';
    else if (d.includes('GITFLOW DAG')) detected = 'Sdlc';
    else if (d.includes('ARCHITECTURAL PIPELINE')) detected = 'Pipeline';

    summary.layouts[detected] = (summary.layouts[detected] || 0) + 1;

    const cat = q.category || 'other';
    if (!summary.categories[cat]) summary.categories[cat] = {};
    summary.categories[cat][detected] = (summary.categories[cat][detected] || 0) + 1;
  });

  globalThis.__summary = summary;
`;

const script = new vm.Script(scriptText + '\n' + inspectCode);
const context = vm.createContext(sandbox);
script.runInContext(context);

console.log('Total Questions:', sandbox.__summary.total);
console.log('Valid SVGs with 900x255 viewBox:', sandbox.__summary.validSvg);
console.log('Empty Diagrams:', sandbox.__summary.empty);

console.log('\n=== COMPLETE 34-TOPOLOGY DISTRIBUTION ===');
console.table(sandbox.__summary.layouts);

console.log('\n=== CATEGORY VARIETY: CSHARP ===');
console.table(sandbox.__summary.categories['csharp']);

console.log('\n=== CATEGORY VARIETY: SQL ===');
console.table(sandbox.__summary.categories['sql']);

console.log('\n=== CATEGORY VARIETY: REACT ===');
console.table(sandbox.__summary.categories['react']);

console.log('\n=== CATEGORY VARIETY: PERFORMANCE ===');
console.table(sandbox.__summary.categories['performance']);

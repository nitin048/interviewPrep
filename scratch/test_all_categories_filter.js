const fs = require('fs');
const vm = require('vm');

const content = fs.readFileSync('senior-dotnet-interview-portal.html', 'utf8');
const scriptOpen = content.indexOf('<script>');
const scriptClose = content.lastIndexOf('</script>');
const scriptText = content.slice(scriptOpen + '<script>'.length, scriptClose);

const sandbox = {
  console: console,
  window: {},
  document: {
    documentElement: { setAttribute: () => {} },
    getElementById: (id) => ({
      id,
      addEventListener: () => {},
      innerHTML: '',
      style: {},
      textContent: '',
      querySelectorAll: () => []
    }),
    querySelector: () => ({ textContent: '', click: () => {} }),
    querySelectorAll: () => [],
    addEventListener: () => {}
  },
  localStorage: { getItem: () => null, setItem: () => {} }
};
sandbox.window = sandbox;

const script = new vm.Script(scriptText);
const context = vm.createContext(sandbox);
script.runInContext(context);

const testScript = `
  const results = {};
  const allCats = Array.from(new Set(QUESTION_BANK.map(q => q.category)));
  
  allCats.forEach(cat => {
    activeCategory = cat;
    searchQuery = '';
    activeDifficulty = 'all';
    activeType = 'all';
    activeStatus = 'all';
    currentPage = 1;
    
    applyFilters();
    
    results[cat] = {
      filteredCount: filteredQuestions.length,
      sampleTitle: filteredQuestions[0] ? filteredQuestions[0].q.slice(0, 50) : 'NONE',
      hasDiagram: filteredQuestions[0] ? !!filteredQuestions[0].diagram : false,
      diagramLength: filteredQuestions[0] && filteredQuestions[0].diagram ? filteredQuestions[0].diagram.length : 0
    };
  });
  
  globalThis.__testResults = results;
`;

const testVmScript = new vm.Script(testScript);
testVmScript.runInContext(context);

console.log('Testing category filter for ALL categories:');
console.table(sandbox.__testResults);

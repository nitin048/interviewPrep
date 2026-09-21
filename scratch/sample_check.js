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
    getElementById: () => ({ addEventListener: () => {}, innerHTML: '', style: {} }),
    querySelectorAll: () => [],
    addEventListener: () => {}
  },
  localStorage: { getItem: () => null, setItem: () => {} }
};
sandbox.window = sandbox;

const sampleCategories = ['csharp', 'sql', 'react', 'dotnet-ai', 'async', 'oop', 'webapi', 'efcore', 'security', 'testing'];
const exportCode = `
  const samples = {};
  sampleCategories.forEach(cat => {
    const list = QUESTION_BANK.filter(q => q.category === cat);
    samples[cat] = list.slice(0, 3).map(q => ({
      id: q.id,
      q: q.q,
      diagramTitle: q.diagramTitle,
      svgLength: q.diagram ? q.diagram.length : 0,
      svgSnippet: q.diagram ? q.diagram.slice(0, 300).replace(/\\s+/g, ' ') : ''
    }));
  });
  globalThis.__samples = samples;
`;

const script = new vm.Script(scriptText + '\n const sampleCategories = ' + JSON.stringify(sampleCategories) + ';\n' + exportCode);
const context = vm.createContext(sandbox);
script.runInContext(context);

console.log('Sample Questions across 10 distinct categories:');
Object.keys(sandbox.__samples).forEach(cat => {
  console.log('\n--- CATEGORY: ' + cat.toUpperCase() + ' ---');
  sandbox.__samples[cat].forEach((item, i) => {
    console.log((i+1) + '. [' + item.id + '] ' + item.q);
    console.log('   SVG length: ' + item.svgLength + ' bytes | ' + item.svgSnippet.slice(0, 140) + '...');
  });
});

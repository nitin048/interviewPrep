const fs = require('fs');
const content = fs.readFileSync('senior-dotnet-interview-portal.html', 'utf8');
const startMarker = 'const QUESTION_BANK = ';
const startIdx = content.indexOf(startMarker);
const endIdx = content.indexOf('];\n', startIdx);
const questions = JSON.parse(content.substring(startIdx + startMarker.length, endIdx + 1));

function testFilters(activeCategory, searchQuery) {
  const rawQuery = (searchQuery || '').trim().toLowerCase();
  const expandedQuery = rawQuery
    .replace(/c#/g, 'csharp')
    .replace(/\.net/g, 'dotnet');
  const qCompact = expandedQuery.replace(/[\s\-_#\.]/g, '');

  return questions.filter(q => {
    if (activeCategory !== 'all' && q.category !== activeCategory) return false;

    if (rawQuery) {
      const matchText = (
        (q.category || '') + ' ' + 
        (q.categoryLabel || '') + ' ' + 
        (q.q || '') + ' ' + 
        (q.answer || '') + ' ' + 
        (q.seniorInsight || '') + ' ' +
        (q.diagramTitle || '') + ' ' +
        ((q.tags || []).join(' '))
      ).toLowerCase();
      const textCompact = matchText.replace(/[\s\-_#\.]/g, '');

      let isMatch = matchText.includes(rawQuery) || textCompact.includes(qCompact);

      if (!isMatch) {
        if ((qCompact === 'efcore' || qCompact === 'ef' || qCompact === 'entityframework') && 
            (q.category === 'efcore' || textCompact.includes('entityframework') || textCompact.includes('dbcontext') || textCompact.includes('efcore'))) {
          isMatch = true;
        } else if (qCompact === 'csharp' && 
            (q.category === 'csharp' || q.q.toLowerCase().includes('c#') || textCompact.includes('csharp'))) {
          isMatch = true;
        } else if ((qCompact === 'dotnet' || qCompact === 'net') && 
            (q.category === 'dotnet' || q.category === 'dotnet-ai' || q.q.toLowerCase().includes('.net') || textCompact.includes('dotnet'))) {
          isMatch = true;
        } else if ((qCompact === 'js' || qCompact === 'javascript') && 
            (q.category === 'js' || textCompact.includes('javascript'))) {
          isMatch = true;
        }
      }

      if (!isMatch) return false;
    }

    return true;
  });
}

console.log('--- Testing category filter alone ---');
console.log('efcore category filter count:', testFilters('efcore', '').length);
console.log('csharp category filter count:', testFilters('csharp', '').length);
console.log('all category filter count:', testFilters('all', '').length);

console.log('\n--- Testing search terms with category=all ---');
const queries = ['efcore', 'ef core', 'dbcontext', 'asnotracking', 'change tracker', 'entity framework', 'c#', 'csharp', 'dotnet', '.net', 'linq', 'sql', 'microservices', 'jwt', 'docker'];
queries.forEach(q => {
  const r = testFilters('all', q);
  const efCount = r.filter(item => item.category === 'efcore').length;
  console.log(`Query: ${q.padEnd(18)} -> Total: ${r.length.toString().padStart(4)} | EF Core: ${efCount.toString().padStart(3)}`);
});

console.log('\n--- Testing search within efcore category ---');
['dbcontext', 'change tracker', 'asnotracking', 'migration', 'n+1', 'split query', 'concurrency'].forEach(q => {
  const r = testFilters('efcore', q);
  console.log(`EF Core + "${q}" -> Matches: ${r.length}`);
});

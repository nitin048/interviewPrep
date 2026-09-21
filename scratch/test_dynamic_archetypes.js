const fs = require('fs');

console.log("Testing dynamic non-repeating diagram generation...");

function escSvg(s) {
  if (!s) return '';
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function wrapText(text, maxChars = 24) {
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

// Test on real questions from the file
const html = fs.readFileSync('senior-dotnet-interview-portal.html', 'utf8');
const escIdx = html.indexOf('function escSvg');
const lastBracket = html.lastIndexOf('];', escIdx);
const qbStart = html.indexOf('const QUESTION_BANK = [');
const questions = JSON.parse(html.substring(qbStart + 'const QUESTION_BANK = '.length, lastBracket + 1));

console.log("Loaded " + questions.length + " questions.");

// Test questions: 1, 2, 3, 4, 151, 2706, 3201
const testIds = [1, 2, 3, 4, 151, 2706, 3201];
testIds.forEach(id => {
  const q = questions.find(item => item.id === id);
  console.log(`\nQuestion #${q.id}: ${q.q}`);
  (q.diagramSteps || []).forEach((step, sIdx) => {
    const titleLines = wrapText(step[1], 20);
    const descLines = wrapText(step[2], 26);
    console.log(`  Step ${sIdx+1}: [${step[0]}] Title: "${titleLines.join(' | ')}" Desc: "${descLines.join(' | ')}" Pill: [${step[3]}]`);
  });
});

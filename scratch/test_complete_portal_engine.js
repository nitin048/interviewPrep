const fs = require('fs');
const vm = require('vm');

console.log("Testing complete 20-archetype portal engine on sample questions from all categories...");

const html = fs.readFileSync('senior-dotnet-interview-portal.html', 'utf8');
const escIdx = html.indexOf('function escSvg');
const lastBracket = html.lastIndexOf('];', escIdx);
const qbStart = html.indexOf('const QUESTION_BANK = [');
const questions = JSON.parse(html.substring(qbStart + 'const QUESTION_BANK = '.length, lastBracket + 1));

console.log("Loaded " + questions.length + " questions.");

// Let's pick 1 question from every unique category
const categorySamples = {};
questions.forEach(q => {
  if (!categorySamples[q.category]) {
    categorySamples[q.category] = q;
  }
});

console.log("Found " + Object.keys(categorySamples).length + " distinct categories.");

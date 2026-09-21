const fs = require('fs');

console.log("Testing 20 distinct geometric layout topologies...");

function escSvg(s) {
  if (!s) return '';
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function wrapText(text, maxChars = 22) {
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

function renderWrappedText(text, x, y, maxChars, fontSize, color, maxLines = 2, lineHeight = 12, anchor = 'start') {
  const lines = wrapText(text, maxChars).slice(0, maxLines);
  return lines.map((line, idx) => {
    return `<text x="${x}" y="${y + idx * lineHeight}" fill="${color}" font-size="${fontSize}" text-anchor="${anchor}">${escSvg(line)}</text>`;
  }).join('\n');
}

console.log("Helper functions defined.");

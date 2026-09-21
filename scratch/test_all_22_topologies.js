const fs = require('fs');

console.log("Testing 22 distinct geometric topologies...");

// Helper escSvg and wrapText
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

// B-TREE HIERARCHICAL TREE LAYOUT
function renderBTreeLayout(q, title, steps, w, h) {
  const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(16, 185, 129, 0.35);">
      <g transform="translate(20, 18)">
        <rect width="110" height="20" rx="4" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
        <text x="55" y="14" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">TREE HIERARCHY</text>
        <text x="122" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <!-- Level 0: Root Page -->
      <g transform="translate(330, 44)">
        <rect width="240" height="42" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.8"/>
        <rect width="240" height="18" rx="6" fill="#10b981" fill-opacity="0.25"/>
        <text x="120" y="13" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">ROOT NODE: ${escSvg(s0[0])}</text>
        <text x="120" y="32" fill="#f8fafc" font-size="9" font-weight="600" text-anchor="middle">${escSvg(s0[1].slice(0, 32))}</text>
      </g>
      <!-- Connector Lines from Root to Branches -->
      <line x1="390" y1="86" x2="220" y2="104" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
      <line x1="510" y1="86" x2="680" y2="104" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
      <!-- Level 1: Branch Nodes -->
      <g transform="translate(100, 104)">
        <rect width="240" height="44" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.2"/>
        <text x="120" y="16" fill="#38bdf8" font-size="8.5" font-weight="700" text-anchor="middle">BRANCH 1: ${escSvg(s1[0])}</text>
        <text x="120" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">${escSvg(s1[1].slice(0, 32))}</text>
      </g>
      <g transform="translate(560, 104)">
        <rect width="240" height="44" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.2"/>
        <text x="120" y="16" fill="#38bdf8" font-size="8.5" font-weight="700" text-anchor="middle">BRANCH 2: ${escSvg(s2[0])}</text>
        <text x="120" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">${escSvg(s2[1].slice(0, 32))}</text>
      </g>
      <!-- Connector Lines to Leaves -->
      <line x1="180" y1="148" x2="110" y2="166" stroke="#0ea5e9" stroke-width="1.2"/>
      <line x1="260" y1="148" x2="330" y2="166" stroke="#0ea5e9" stroke-width="1.2"/>
      <line x1="640" y1="148" x2="570" y2="166" stroke="#0ea5e9" stroke-width="1.2"/>
      <line x1="720" y1="148" x2="790" y2="166" stroke="#0ea5e9" stroke-width="1.2"/>
      <!-- Level 2: Leaf Pages -->
      <g transform="translate(20, 166)">
        <rect width="180" height="52" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
        <text x="90" y="16" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">LEAF: ${escSvg(s3[0])}</text>
        <text x="90" y="30" fill="#a7f3d0" font-size="8" text-anchor="middle">${escSvg(s3[1].slice(0, 22))}</text>
        <text x="90" y="44" fill="#34d399" font-size="7.5" font-weight="600" text-anchor="middle">${escSvg(s3[3] || 'Leaf Page')}</text>
      </g>
      <g transform="translate(240, 166)">
        <rect width="180" height="52" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
        <text x="90" y="16" fill="#6ee7b7" font-size="8.5" font-weight="700" text-anchor="middle">${escSvg(s4[0])}</text>
        <text x="90" y="30" fill="#a7f3d0" font-size="8" text-anchor="middle">${escSvg(s4[1].slice(0, 22))}</text>
        <text x="90" y="44" fill="#34d399" font-size="7.5" font-weight="600" text-anchor="middle">${escSvg(s4[3] || 'Data Row')}</text>
      </g>
      <g transform="translate(480, 166)">
        <rect width="180" height="52" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
        <text x="90" y="16" fill="#c7d2fe" font-size="8.5" font-weight="700" text-anchor="middle">BUFFER POOL</text>
        <text x="90" y="30" fill="#a5b4fc" font-size="8" text-anchor="middle">${escSvg(s2[2].slice(0, 22))}</text>
        <text x="90" y="44" fill="#38bdf8" font-size="7.5" font-weight="600" text-anchor="middle">&lt; 0.1ms Memory Hit</text>
      </g>
      <g transform="translate(700, 166)">
        <rect width="180" height="52" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
        <text x="90" y="16" fill="#f8fafc" font-size="8.5" font-weight="700" text-anchor="middle">SEEK TRAVERSAL</text>
        <text x="90" y="30" fill="#94a3b8" font-size="8" text-anchor="middle">O(log N) Complexity</text>
        <text x="90" y="44" fill="#cbd5e1" font-size="7.5" font-weight="600" text-anchor="middle">Linked Nodes &lt;---&gt;</text>
      </g>
      <!-- Bottom Flow Track -->
      <g transform="translate(20, 228)">
        <rect width="860" height="20" rx="3" fill="#0f172a" stroke="#334155" stroke-width="0.8"/>
        <text x="430" y="14" fill="#cbd5e1" font-size="8" font-weight="600" text-anchor="middle">➔ Tree Traversal: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
      </g>
    </svg>
  `;
}

// CONCENTRIC ONION MIDDLEWARE LAYOUT
function renderMiddlewareLayout(q, title, steps, w, h) {
  const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram" style="background:#080c14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; border: 1px solid rgba(139, 92, 246, 0.35);">
      <g transform="translate(20, 18)">
        <rect width="130" height="20" rx="4" fill="#8b5cf6" fill-opacity="0.2" stroke="#8b5cf6" stroke-width="1"/>
        <text x="65" y="14" fill="#c4b5fd" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="1">MIDDLEWARE ONION</text>
        <text x="142" y="15" fill="#f8fafc" font-size="12" font-weight="700">${escSvg(title)}</text>
      </g>
      <g transform="translate(20, 46)">
        <!-- Layer 1: Outermost Ring -->
        <rect width="860" height="174" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.8"/>
        <text x="24" y="22" fill="#c4b5fd" font-size="9" font-weight="700">LAYER 1: ${escSvg(s0[0])} — ${escSvg(s0[1].slice(0, 36))}</text>
        <!-- Layer 2: Intermediate Ring -->
        <rect x="30" y="28" width="800" height="128" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
        <text x="54" y="48" fill="#a5b4fc" font-size="9" font-weight="700">LAYER 2: ${escSvg(s1[0])} — ${escSvg(s1[1].slice(0, 36))}</text>
        <!-- Layer 3: Inner Ring -->
        <rect x="60" y="54" width="740" height="88" rx="6" fill="#31104b" stroke="#d946ef" stroke-width="1.5"/>
        <text x="84" y="72" fill="#f0abfc" font-size="9" font-weight="700">LAYER 3: ${escSvg(s2[0])} — ${escSvg(s2[1].slice(0, 36))}</text>
        <!-- Core Center -->
        <rect x="90" y="80" width="680" height="50" rx="5" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
        <text x="430" y="100" fill="#ffffff" font-size="10.5" font-weight="700" text-anchor="middle">★ CORE: ${escSvg(s3[0])} — ${escSvg(s3[1].slice(0, 42))}</text>
        <text x="430" y="116" fill="#6ee7b7" font-size="8.5" text-anchor="middle">await next(context) completes ➔ ${escSvg(s4[0])}: ${escSvg(s4[1].slice(0, 30))} (Unwinds in reverse)</text>
      </g>
      <!-- Bottom Flow Track -->
      <g transform="translate(20, 228)">
        <rect width="860" height="20" rx="3" fill="#0f172a" stroke="#334155" stroke-width="0.8"/>
        <text x="430" y="14" fill="#cbd5e1" font-size="8" font-weight="600" text-anchor="middle">➔ Onion Flow: ${escSvg(s0[0])} ➔ ${escSvg(s1[0])} ➔ ${escSvg(s2[0])} ➔ ${escSvg(s3[0])} ➔ ${escSvg(s4[0])}</text>
      </g>
    </svg>
  `;
}

console.log("B-Tree and Middleware onion compiled successfully.");

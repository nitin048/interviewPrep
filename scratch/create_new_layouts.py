# coding: utf-8
import sys

layouts = r'''
    // =========================================================================
    // 1. ROSLYN COMPILER & TIERED JIT COMPILATION PIPELINE
    // =========================================================================
    function renderCompilerIlLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <linearGradient id="compGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.2"/>
              <stop offset="50%" stop-color="#8b5cf6" stop-opacity="0.2"/>
              <stop offset="100%" stop-color="#10b981" stop-opacity="0.2"/>
            </linearGradient>
            <marker id="compArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#60a5fa"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(59,130,246,0.15)" stroke="#3b82f6" stroke-width="0.8"/>
          <text x="30" y="25" fill="#60a5fa" font-size="10" font-weight="700" letter-spacing="1">COMPILATION &amp; JIT PIPELINE</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Stage 0: C# Source Code -->
          <g transform="translate(20, 52)">
            <rect width="150" height="150" rx="8" fill="#0f172a" stroke="#3b82f6" stroke-width="1.2"/>
            <rect x="10" y="10" width="130" height="22" rx="4" fill="rgba(59,130,246,0.15)"/>
            <text x="75" y="24" fill="#93c5fd" font-size="9.5" font-weight="700" text-anchor="middle">SOURCE (.CS)</text>
            <text x="12" y="48" fill="#38bdf8" font-size="9" font-weight="600">class Program {</text>
            <text x="20" y="60" fill="#94a3b8" font-size="8.5">static void Main()</text>
            <text x="12" y="72" fill="#38bdf8" font-size="9" font-weight="600">}</text>
            <line x1="12" y1="80" x2="138" y2="80" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s0[1], 12, 94, 18, 9, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s0[2], 12, 120, 20, 8, '#94a3b8', 2, 10)}
          </g>

          <path d="M 172 127 L 196 127" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#compArrow)"/>
          <text x="184" y="120" fill="#60a5fa" font-size="7.5" font-weight="700" text-anchor="middle">ROSLYN</text>

          <!-- Stage 1: IL Bytecode & Metadata -->
          <g transform="translate(200, 52)">
            <rect width="150" height="150" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.2"/>
            <rect x="10" y="10" width="130" height="22" rx="4" fill="rgba(139,92,246,0.15)"/>
            <text x="75" y="24" fill="#c4b5fd" font-size="9.5" font-weight="700" text-anchor="middle">IL BYTECODE (.DLL)</text>
            <text x="12" y="48" fill="#a78bfa" font-size="8.5" font-family="monospace">IL_0001: ldarg.0</text>
            <text x="12" y="60" fill="#a78bfa" font-size="8.5" font-family="monospace">IL_0002: callvirt</text>
            <text x="12" y="72" fill="#a78bfa" font-size="8.5" font-family="monospace">IL_0007: ret</text>
            <line x1="12" y1="80" x2="138" y2="80" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s1[1], 12, 94, 18, 9, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s1[2], 12, 120, 20, 8, '#94a3b8', 2, 10)}
          </g>

          <path d="M 352 127 L 376 127" stroke="#a78bfa" stroke-width="1.5" marker-end="url(#compArrow)"/>
          <text x="364" y="120" fill="#c4b5fd" font-size="7.5" font-weight="700" text-anchor="middle">CLR LOAD</text>

          <!-- Stage 2: CoreCLR Tiered JIT -->
          <g transform="translate(380, 52)">
            <rect width="150" height="150" rx="8" fill="#0f172a" stroke="#ec4899" stroke-width="1.2"/>
            <rect x="10" y="10" width="130" height="22" rx="4" fill="rgba(236,72,153,0.15)"/>
            <text x="75" y="24" fill="#f472b6" font-size="9.5" font-weight="700" text-anchor="middle">TIERED JIT ENGINE</text>
            <rect x="12" y="42" width="126" height="16" rx="3" fill="rgba(245,158,11,0.15)"/>
            <text x="75" y="53" fill="#fbbf24" font-size="8" font-weight="600" text-anchor="middle">Tier 0: Quick JIT (No Opt)</text>
            <rect x="12" y="61" width="126" height="16" rx="3" fill="rgba(16,185,129,0.15)"/>
            <text x="75" y="72" fill="#34d399" font-size="8" font-weight="600" text-anchor="middle">Tier 1: Dynamic PGO Opt</text>
            <line x1="12" y1="80" x2="138" y2="80" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s2[1], 12, 94, 18, 9, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s2[2], 12, 120, 20, 8, '#94a3b8', 2, 10)}
          </g>

          <path d="M 532 127 L 556 127" stroke="#f472b6" stroke-width="1.5" marker-end="url(#compArrow)"/>
          <text x="544" y="120" fill="#f472b6" font-size="7.5" font-weight="700" text-anchor="middle">COMPILE</text>

          <!-- Stage 3: Native Machine Code -->
          <g transform="translate(560, 52)">
            <rect width="150" height="150" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
            <rect x="10" y="10" width="130" height="22" rx="4" fill="rgba(16,185,129,0.15)"/>
            <text x="75" y="24" fill="#6ee7b7" font-size="9.5" font-weight="700" text-anchor="middle">NATIVE MACHINE CODE</text>
            <text x="12" y="48" fill="#34d399" font-size="8.5" font-family="monospace">mov rax, [rsp+8]</text>
            <text x="12" y="60" fill="#34d399" font-size="8.5" font-family="monospace">add rax, rcx</text>
            <text x="12" y="72" fill="#34d399" font-size="8.5" font-family="monospace">ret</text>
            <line x1="12" y1="80" x2="138" y2="80" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s3[1], 12, 94, 18, 9, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s3[2], 12, 120, 20, 8, '#94a3b8', 2, 10)}
          </g>

          <path d="M 712 127 L 736 127" stroke="#34d399" stroke-width="1.5" marker-end="url(#compArrow)"/>
          <text x="724" y="120" fill="#34d399" font-size="7.5" font-weight="700" text-anchor="middle">EXECUTE</text>

          <!-- Stage 4: Hardware CPU & Registers -->
          <g transform="translate(740, 52)">
            <rect width="140" height="150" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.2"/>
            <rect x="8" y="10" width="124" height="22" rx="4" fill="rgba(6,182,212,0.15)"/>
            <text x="70" y="24" fill="#67e8f9" font-size="9.5" font-weight="700" text-anchor="middle">CPU REGISTERS</text>
            <rect x="12" y="40" width="116" height="34" rx="3" fill="#0b132b" stroke="#06b6d4" stroke-width="0.8"/>
            <text x="70" y="54" fill="#22d3ee" font-size="8" font-weight="600" text-anchor="middle">L1 / L2 CACHE DIRECT</text>
            <text x="70" y="66" fill="#94a3b8" font-size="7.5" text-anchor="middle">Zero Interpretation Lag</text>
            <line x1="8" y1="80" x2="132" y2="80" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s4[1], 10, 94, 17, 9, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s4[2], 10, 120, 19, 8, '#94a3b8', 2, 10)}
          </g>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">CLR Execution Pipeline: C# Source ➔ Roslyn Compiler ➔ IL Bytecode ➔ CoreCLR Tiered JIT ➔ Native x86/ARM64 Machine Code</text>
        </svg>
      `;
    }

    // =========================================================================
    // 2. CONCURRENCY & DEADLOCK CIRCULAR WAIT TOPOLOGY
    // =========================================================================
    function renderConcurrencyDeadlockLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <marker id="deadlockArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#ef4444"/>
            </marker>
            <marker id="holdArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#10b981"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(239,68,68,0.15)" stroke="#ef4444" stroke-width="0.8"/>
          <text x="30" y="25" fill="#f87171" font-size="10" font-weight="700" letter-spacing="1">CONCURRENCY &amp; LOCKS</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Left Side: Thread 1 -->
          <g transform="translate(30, 52)">
            <rect width="200" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
            <rect x="10" y="10" width="180" height="22" rx="4" fill="rgba(56,189,248,0.15)"/>
            <text x="100" y="24" fill="#7dd3fc" font-size="9.5" font-weight="700" text-anchor="middle">THREAD 1 (WORKER A)</text>
            <text x="12" y="48" fill="#38bdf8" font-size="8.5" font-weight="600">Holds: Lock(Resource 1)</text>
            <text x="12" y="62" fill="#f87171" font-size="8.5" font-weight="600">Waiting on: Lock(Resource 2)</text>
            <line x1="12" y1="72" x2="188" y2="72" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s0[1], 12, 86, 24, 9, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s0[2], 12, 112, 26, 8, '#94a3b8', 2, 10)}
          </g>

          <!-- Center Top: Resource 1 Lock -->
          <g transform="translate(290, 52)">
            <rect width="180" height="68" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
            <rect x="8" y="8" width="164" height="18" rx="3" fill="rgba(16,185,129,0.15)"/>
            <text x="90" y="20" fill="#34d399" font-size="8.5" font-weight="700" text-anchor="middle">RESOURCE 1 [HELD BY T1]</text>
            ${renderWrappedText(s1[1], 10, 40, 22, 8.5, '#e2e8f0', 1, 10)}
            ${renderWrappedText(s1[2], 10, 54, 24, 8, '#94a3b8', 1, 9)}
          </g>

          <!-- Center Bottom: Resource 2 Lock -->
          <g transform="translate(290, 134)">
            <rect width="180" height="68" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.2"/>
            <rect x="8" y="8" width="164" height="18" rx="3" fill="rgba(168,85,247,0.15)"/>
            <text x="90" y="20" fill="#c084fc" font-size="8.5" font-weight="700" text-anchor="middle">RESOURCE 2 [HELD BY T2]</text>
            ${renderWrappedText(s2[1], 10, 40, 22, 8.5, '#e2e8f0', 1, 10)}
            ${renderWrappedText(s2[2], 10, 54, 24, 8, '#94a3b8', 1, 9)}
          </g>

          <!-- Circular Wait Arrows -->
          <!-- T1 holds R1 -->
          <path d="M 230 78 L 285 78" stroke="#10b981" stroke-width="1.5" marker-end="url(#holdArrow)"/>
          <!-- T1 WAITS on R2 -->
          <path d="M 230 168 L 285 168" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#deadlockArrow)"/>
          <text x="257" y="160" fill="#f87171" font-size="7.5" font-weight="700" text-anchor="middle">BLOCK</text>

          <!-- Center Flashing Deadlock Warning -->
          <g transform="translate(505, 95)">
            <polygon points="35 0, 70 25, 35 50, 0 25" fill="rgba(239,68,68,0.2)" stroke="#ef4444" stroke-width="1.5"/>
            <text x="35" y="22" fill="#f87171" font-size="7.5" font-weight="800" text-anchor="middle">CIRCULAR</text>
            <text x="35" y="34" fill="#fca5a5" font-size="7.5" font-weight="800" text-anchor="middle">DEADLOCK</text>
          </g>

          <!-- Right Side: Thread 2 -->
          <g transform="translate(610, 52)">
            <rect width="200" height="150" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.2"/>
            <rect x="10" y="10" width="180" height="22" rx="4" fill="rgba(168,85,247,0.15)"/>
            <text x="100" y="24" fill="#c084fc" font-size="9.5" font-weight="700" text-anchor="middle">THREAD 2 (WORKER B)</text>
            <text x="12" y="48" fill="#c084fc" font-size="8.5" font-weight="600">Holds: Lock(Resource 2)</text>
            <text x="12" y="62" fill="#f87171" font-size="8.5" font-weight="600">Waiting on: Lock(Resource 1)</text>
            <line x1="12" y1="72" x2="188" y2="72" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s3[1], 12, 86, 24, 9, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s3[2], 12, 112, 26, 8, '#94a3b8', 2, 10)}
          </g>

          <!-- T2 holds R2 -->
          <path d="M 610 168 L 475 168" stroke="#a855f7" stroke-width="1.5" marker-end="url(#holdArrow)"/>
          <!-- T2 WAITS on R1 -->
          <path d="M 610 78 L 475 78" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#deadlockArrow)"/>
          <text x="542" y="70" fill="#f87171" font-size="7.5" font-weight="700" text-anchor="middle">BLOCK</text>

          <!-- Far Right Strategy Column -->
          <g transform="translate(820, 52)">
            <rect width="60" height="150" rx="6" fill="#0b132b" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
            <text x="30" y="25" fill="#38bdf8" font-size="7.5" font-weight="700" text-anchor="middle">LOCK</text>
            <text x="30" y="36" fill="#38bdf8" font-size="7.5" font-weight="700" text-anchor="middle">ORDER</text>
            <line x1="8" y1="44" x2="52" y2="44" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            <text x="30" y="65" fill="#fbbf24" font-size="7" font-weight="600" text-anchor="middle">MUTEX</text>
            <text x="30" y="90" fill="#34d399" font-size="7" font-weight="600" text-anchor="middle">TRY-ENTER</text>
            <text x="30" y="115" fill="#c084fc" font-size="7" font-weight="600" text-anchor="middle">SEMAPHORE</text>
            <text x="30" y="138" fill="#f87171" font-size="7" font-weight="600" text-anchor="middle">TIMEOUT</text>
          </g>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Deadlock Resolution: Consistent Global Lock Ordering | Monitor.TryEnter with Timeout | SemaphoreSlim Async Wait</text>
        </svg>
      `;
    }

    // =========================================================================
    // 3. SQL RELATIONAL JOINS & VENN INTERSECTION TOPOLOGY
    // =========================================================================
    function renderVennJoinLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <pattern id="vennHatch" width="8" height="8" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
              <line x1="0" y1="0" x2="0" y2="8" stroke="#10b981" stroke-width="1.5" stroke-opacity="0.4"/>
            </pattern>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(16,185,129,0.15)" stroke="#10b981" stroke-width="0.8"/>
          <text x="30" y="25" fill="#34d399" font-size="10" font-weight="700" letter-spacing="1">RELATIONAL JOINS &amp; SETS</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Left Info Box -->
          <g transform="translate(20, 52)">
            <rect width="180" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
            <rect x="8" y="8" width="164" height="20" rx="3" fill="rgba(56,189,248,0.15)"/>
            <text x="90" y="22" fill="#7dd3fc" font-size="9" font-weight="700" text-anchor="middle">TABLE A (LEFT TABLE)</text>
            ${renderWrappedText(s0[1], 10, 44, 22, 9, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s0[2], 10, 72, 24, 8, '#94a3b8', 2, 10)}
            <line x1="8" y1="100" x2="172" y2="100" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            <text x="10" y="116" fill="#38bdf8" font-size="8" font-weight="600">Left Outer Rows: Kept</text>
            <text x="10" y="130" fill="#94a3b8" font-size="8">NULL filled if no match</text>
          </g>

          <!-- Center Venn Diagram Geometry -->
          <g transform="translate(210, 48)">
            <!-- Table A Circle -->
            <circle cx="95" cy="80" r="75" fill="rgba(56,189,248,0.15)" stroke="#38bdf8" stroke-width="1.5"/>
            <!-- Table B Circle -->
            <circle cx="195" cy="80" r="75" fill="rgba(168,85,247,0.15)" stroke="#a855f7" stroke-width="1.5"/>
            
            <!-- Intersection Clip / Fill -->
            <clipPath id="vennClipA">
              <circle cx="95" cy="80" r="75"/>
            </clipPath>
            <circle cx="195" cy="80" r="75" clip-path="url(#vennClipA)" fill="url(#vennHatch)" stroke="#10b981" stroke-width="2"/>

            <!-- Venn Labels -->
            <text x="50" y="82" fill="#7dd3fc" font-size="10" font-weight="700" text-anchor="middle">LEFT</text>
            <text x="50" y="94" fill="#94a3b8" font-size="7.5" text-anchor="middle">ONLY</text>

            <text x="145" y="75" fill="#34d399" font-size="10" font-weight="800" text-anchor="middle">INNER</text>
            <text x="145" y="88" fill="#6ee7b7" font-size="8" font-weight="700" text-anchor="middle">JOIN</text>
            <text x="145" y="99" fill="#94a3b8" font-size="6.5" text-anchor="middle">MATCH (A ∩ B)</text>

            <text x="240" y="82" fill="#c084fc" font-size="10" font-weight="700" text-anchor="middle">RIGHT</text>
            <text x="240" y="94" fill="#94a3b8" font-size="7.5" text-anchor="middle">ONLY</text>
          </g>

          <!-- Center-Right Table B Info -->
          <g transform="translate(510, 52)">
            <rect width="180" height="150" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.2"/>
            <rect x="8" y="8" width="164" height="20" rx="3" fill="rgba(168,85,247,0.15)"/>
            <text x="90" y="22" fill="#c084fc" font-size="9" font-weight="700" text-anchor="middle">TABLE B (RIGHT TABLE)</text>
            ${renderWrappedText(s1[1], 10, 44, 22, 9, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s1[2], 10, 72, 24, 8, '#94a3b8', 2, 10)}
            <line x1="8" y1="100" x2="172" y2="100" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            <text x="10" y="116" fill="#a855f7" font-size="8" font-weight="600">Right Outer Rows: Kept</text>
            <text x="10" y="130" fill="#94a3b8" font-size="8">FULL OUTER = A ∪ B</text>
          </g>

          <!-- Far Right Algorithm Execution Column -->
          <g transform="translate(705, 52)">
            <rect width="175" height="150" rx="8" fill="#0b132b" stroke="#10b981" stroke-width="1.2"/>
            <rect x="8" y="8" width="159" height="20" rx="3" fill="rgba(16,185,129,0.15)"/>
            <text x="87" y="22" fill="#34d399" font-size="8.5" font-weight="700" text-anchor="middle">PHYSICAL JOIN ALGORITHM</text>
            <rect x="10" y="36" width="155" height="26" rx="3" fill="rgba(255,255,255,0.04)"/>
            <text x="16" y="48" fill="#fbbf24" font-size="8" font-weight="600">Hash Match (Build/Probe)</text>
            <text x="16" y="58" fill="#94a3b8" font-size="7.5">Unsorted, large datasets</text>

            <rect x="10" y="66" width="155" height="26" rx="3" fill="rgba(255,255,255,0.04)"/>
            <text x="16" y="78" fill="#38bdf8" font-size="8" font-weight="600">Merge Join (Pre-Sorted)</text>
            <text x="16" y="88" fill="#94a3b8" font-size="7.5">O(N+M) index order scan</text>

            <rect x="10" y="96" width="155" height="26" rx="3" fill="rgba(255,255,255,0.04)"/>
            <text x="16" y="108" fill="#a855f7" font-size="8" font-weight="600">Nested Loops (Seek)</text>
            <text x="16" y="118" fill="#94a3b8" font-size="7.5">Small outer, indexed inner</text>

            ${renderWrappedText(s2[1], 10, 134, 23, 7.5, '#6ee7b7', 1, 9)}
          </g>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Relational Algebra: INNER JOIN (A ∩ B) | LEFT JOIN (A + matches) | FULL OUTER JOIN (A ∪ B) | CROSS JOIN (Cartesian A × B)</text>
        </svg>
      `;
    }

    // =========================================================================
    // 4. SQL TRANSACTIONS, ACID & MVCC TIMELINE TOPOLOGY
    // =========================================================================
    function renderTransactionMvccLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <marker id="transArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#f59e0b"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(245,158,11,0.15)" stroke="#f59e0b" stroke-width="0.8"/>
          <text x="30" y="25" fill="#fbbf24" font-size="10" font-weight="700" letter-spacing="1">ACID &amp; TRANSACTIONS</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Horizontal Timeline Scale -->
          <path d="M 50 58 L 520 58" stroke="rgba(255,255,255,0.2)" stroke-width="1.5" marker-end="url(#transArrow)"/>
          <circle cx="70" cy="58" r="3" fill="#fbbf24"/>
          <text x="70" y="52" fill="#94a3b8" font-size="7.5" text-anchor="middle">t0: BEGIN</text>
          <circle cx="210" cy="58" r="3" fill="#38bdf8"/>
          <text x="210" y="52" fill="#94a3b8" font-size="7.5" text-anchor="middle">t1: UPDATE</text>
          <circle cx="360" cy="58" r="3" fill="#a855f7"/>
          <text x="360" y="52" fill="#94a3b8" font-size="7.5" text-anchor="middle">t2: READ</text>
          <circle cx="490" cy="58" r="3" fill="#10b981"/>
          <text x="490" y="52" fill="#94a3b8" font-size="7.5" text-anchor="middle">t3: COMMIT</text>

          <!-- Upper Swimlane: Transaction 1 (Write) -->
          <g transform="translate(30, 68)">
            <rect width="490" height="64" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
            <rect x="8" y="8" width="130" height="18" rx="3" fill="rgba(245,158,11,0.15)"/>
            <text x="73" y="20" fill="#fbbf24" font-size="8.5" font-weight="700" text-anchor="middle">TRANSACTION T1 (WRITER)</text>
            <text x="145" y="20" fill="#38bdf8" font-size="8.5" font-weight="600">UPDATE Accounts SET Bal -= 100 WHERE ID=42</text>
            ${renderWrappedText(s0[1], 10, 38, 35, 8.5, '#e2e8f0', 1, 9)}
            ${renderWrappedText(s0[2], 10, 50, 42, 7.5, '#94a3b8', 1, 9)}
          </g>

          <!-- Lower Swimlane: Transaction 2 (Snapshot Read) -->
          <g transform="translate(30, 140)">
            <rect width="490" height="64" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
            <rect x="8" y="8" width="130" height="18" rx="3" fill="rgba(56,189,248,0.15)"/>
            <text x="73" y="20" fill="#7dd3fc" font-size="8.5" font-weight="700" text-anchor="middle">TRANSACTION T2 (READER)</text>
            <text x="145" y="20" fill="#10b981" font-size="8.5" font-weight="600">SELECT Bal FROM Accounts WHERE ID=42 (Non-Blocking!)</text>
            ${renderWrappedText(s1[1], 10, 38, 35, 8.5, '#e2e8f0', 1, 9)}
            ${renderWrappedText(s1[2], 10, 50, 42, 7.5, '#94a3b8', 1, 9)}
          </g>

          <!-- Center-Right: TempDB MVCC Version Store -->
          <g transform="translate(535, 52)">
            <rect width="165" height="152" rx="8" fill="#0b132b" stroke="#a855f7" stroke-width="1.2"/>
            <rect x="8" y="8" width="149" height="20" rx="3" fill="rgba(168,85,247,0.15)"/>
            <text x="82" y="22" fill="#c084fc" font-size="8.5" font-weight="700" text-anchor="middle">TEMPDB VERSION STORE</text>
            
            <rect x="10" y="34" width="145" height="26" rx="3" fill="#1e1b4b" stroke="#a855f7" stroke-width="0.8"/>
            <text x="16" y="46" fill="#e0e7ff" font-size="8" font-weight="600">Row ID 42: Ver 2.0 (Active)</text>
            <text x="16" y="55" fill="#f87171" font-size="7">Bal: $900 (Uncommitted T1)</text>

            <path d="M 82 60 L 82 70" stroke="#a855f7" stroke-width="1.2" marker-end="url(#transArrow)"/>

            <rect x="10" y="72" width="145" height="26" rx="3" fill="#1e1b4b" stroke="#10b981" stroke-width="0.8"/>
            <text x="16" y="84" fill="#e0e7ff" font-size="8" font-weight="600">Row ID 42: Ver 1.0 (Committed)</text>
            <text x="16" y="93" fill="#34d399" font-size="7">Bal: $1000 (Served to T2!)</text>

            ${renderWrappedText(s2[1], 10, 114, 21, 8, '#e2e8f0', 2, 10)}
            ${renderWrappedText(s2[2], 10, 136, 23, 7.5, '#94a3b8', 1, 9)}
          </g>

          <!-- Far Right: Write-Ahead Log (WAL) Cylinder -->
          <g transform="translate(715, 52)">
            <rect width="165" height="152" rx="8" fill="#0b132b" stroke="#10b981" stroke-width="1.2"/>
            <rect x="8" y="8" width="149" height="20" rx="3" fill="rgba(16,185,129,0.15)"/>
            <text x="82" y="22" fill="#34d399" font-size="8.5" font-weight="700" text-anchor="middle">WRITE-AHEAD LOG (WAL)</text>
            
            <text x="12" y="44" fill="#34d399" font-size="8" font-weight="600">Sequential LSN Flush</text>
            <text x="12" y="56" fill="#94a3b8" font-size="7.5">Log must persist to disk</text>
            <text x="12" y="66" fill="#94a3b8" font-size="7.5">BEFORE data page written!</text>
            <line x1="8" y1="74" x2="157" y2="74" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

            ${renderWrappedText(s3[1], 10, 88, 22, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s3[2], 10, 116, 24, 7.5, '#94a3b8', 2, 10)}
            <rect x="10" y="132" width="145" height="14" rx="2" fill="rgba(16,185,129,0.15)"/>
            <text x="82" y="142" fill="#34d399" font-size="7" font-weight="700" text-anchor="middle">fsync() Guaranteed Durable</text>
          </g>

          <!-- Footer: 4 ACID Badges -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">ACID Contract: [A] Atomicity (All-or-Nothing) | [C] Consistency (Constraints) | [I] Isolation (MVCC Snapshot) | [D] Durability (WAL Log Flush)</text>
        </svg>
      `;
    }

    // =========================================================================
    // 5. RELATIONAL SCHEMA & 1:N CROW'S FOOT NORMALIZATION TOPOLOGY
    // =========================================================================
    function renderErSchemaLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <marker id="pkFkMarker" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#38bdf8"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(56,189,248,0.15)" stroke="#38bdf8" stroke-width="0.8"/>
          <text x="30" y="25" fill="#7dd3fc" font-size="10" font-weight="700" letter-spacing="1">SCHEMA &amp; NORMALIZATION</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Left Table Card: Parent Entity (e.g. Orders) -->
          <g transform="translate(30, 52)">
            <rect width="320" height="152" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
            <path d="M 0 8 Q 0 0 8 0 L 312 0 Q 320 0 320 8 L 320 28 L 0 28 Z" fill="rgba(56,189,248,0.2)"/>
            <text x="14" y="19" fill="#7dd3fc" font-size="10" font-weight="700">TABLE: PARENT_ENTITY [1]</text>
            <rect x="230" y="6" width="80" height="16" rx="3" fill="#0284c7"/>
            <text x="270" y="17" fill="#ffffff" font-size="8" font-weight="700" text-anchor="middle">CLUSTERED</text>

            <!-- Columns -->
            <rect x="10" y="34" width="300" height="20" fill="rgba(245,158,11,0.15)"/>
            <text x="16" y="47" fill="#fbbf24" font-size="8.5" font-weight="700">[PK] ID : BIGINT</text>
            <text x="200" y="47" fill="#cbd5e1" font-size="8">PRIMARY KEY (Unique)</text>

            <rect x="10" y="56" width="300" height="18" fill="rgba(255,255,255,0.03)"/>
            <text x="16" y="69" fill="#94a3b8" font-size="8">CreatedAt : DATETIME2</text>
            <text x="200" y="69" fill="#64748b" font-size="7.5">NOT NULL</text>

            <rect x="10" y="76" width="300" height="18" fill="rgba(255,255,255,0.01)"/>
            <text x="16" y="89" fill="#94a3b8" font-size="8">TotalAmount : DECIMAL(18,2)</text>
            <text x="200" y="89" fill="#64748b" font-size="7.5">NOT NULL</text>

            <line x1="10" y1="100" x2="310" y2="100" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s0[1], 12, 114, 40, 8.5, '#e2e8f0', 1, 10)}
            ${renderWrappedText(s0[2], 12, 128, 44, 7.5, '#94a3b8', 2, 9)}
          </g>

          <!-- Center Crow's Foot Connector -->
          <g transform="translate(350, 85)">
            <!-- Line from left to right -->
            <line x1="0" y1="10" x2="170" y2="10" stroke="#38bdf8" stroke-width="2"/>
            <!-- 1 side (||) -->
            <line x1="15" y1="0" x2="15" y2="20" stroke="#38bdf8" stroke-width="2"/>
            <line x1="22" y1="0" x2="22" y2="20" stroke="#38bdf8" stroke-width="2"/>
            <!-- Crow's Foot (Many side: >|) -->
            <line x1="155" y1="0" x2="170" y2="10" stroke="#38bdf8" stroke-width="2"/>
            <line x1="155" y1="20" x2="170" y2="10" stroke="#38bdf8" stroke-width="2"/>
            <line x1="148" y1="0" x2="148" y2="20" stroke="#38bdf8" stroke-width="2"/>

            <rect x="40" y="-3" width="90" height="16" rx="3" fill="#0b132b" stroke="#38bdf8" stroke-width="0.8"/>
            <text x="85" y="8" fill="#38bdf8" font-size="7.5" font-weight="700" text-anchor="middle">1 : N (CROW'S FOOT)</text>
            <text x="85" y="32" fill="#94a3b8" font-size="7" text-anchor="middle">FOREIGN KEY LINK</text>
          </g>

          <!-- Right Table Card: Child Entity (e.g. OrderItems) -->
          <g transform="translate(520, 52)">
            <rect width="350" height="152" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.2"/>
            <path d="M 0 8 Q 0 0 8 0 L 342 0 Q 350 0 350 8 L 350 28 L 0 28 Z" fill="rgba(168,85,247,0.2)"/>
            <text x="14" y="19" fill="#c084fc" font-size="10" font-weight="700">TABLE: CHILD_ENTITY [N]</text>
            <rect x="250" y="6" width="90" height="16" rx="3" fill="#7c3aed"/>
            <text x="295" y="17" fill="#ffffff" font-size="8" font-weight="700" text-anchor="middle">COMPOSITE FK</text>

            <!-- Columns -->
            <rect x="10" y="34" width="330" height="20" fill="rgba(245,158,11,0.15)"/>
            <text x="16" y="47" fill="#fbbf24" font-size="8.5" font-weight="700">[PK] ID : BIGINT</text>
            <text x="210" y="47" fill="#cbd5e1" font-size="8">PRIMARY KEY</text>

            <rect x="10" y="56" width="330" height="18" fill="rgba(56,189,248,0.15)"/>
            <text x="16" y="69" fill="#38bdf8" font-size="8.5" font-weight="700">[FK] ParentID : BIGINT</text>
            <text x="210" y="69" fill="#67e8f9" font-size="7.5">REFERENCES Parent(ID)</text>

            <rect x="10" y="76" width="330" height="18" fill="rgba(255,255,255,0.01)"/>
            <text x="16" y="89" fill="#94a3b8" font-size="8">UnitPrice : DECIMAL(18,2)</text>
            <text x="210" y="89" fill="#64748b" font-size="7.5">Quantity : INT</text>

            <line x1="10" y1="100" x2="340" y2="100" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s1[1], 12, 114, 44, 8.5, '#e2e8f0', 1, 10)}
            ${renderWrappedText(s1[2], 12, 128, 48, 7.5, '#94a3b8', 2, 9)}
          </g>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Relational Design: 1NF (Atomic) ➔ 2NF (No Partial Key Dependency) ➔ 3NF (No Transitive Dependency) | BCNF Integrity</text>
        </svg>
      `;
    }
'''

print("First 5 layouts ready in string format")
with open('scratch/test_batch1.js', 'w', encoding='utf-8') as f:
    f.write(layouts)
print("Saved scratch/test_batch1.js")

# coding: utf-8
import sys

layouts = r'''
    // =========================================================================
    // 6. CLR GENERATIONAL GC & MEMORY ARENAS TOPOLOGY
    // =========================================================================
    function renderGenerationalGcLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <marker id="gcPromoArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#10b981"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(16,185,129,0.15)" stroke="#10b981" stroke-width="0.8"/>
          <text x="30" y="25" fill="#34d399" font-size="10" font-weight="700" letter-spacing="1">GARBAGE COLLECTION (GC)</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Arena 0: Gen 0 -->
          <g transform="translate(20, 52)">
            <rect width="195" height="150" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
            <rect x="8" y="8" width="179" height="20" rx="3" fill="rgba(16,185,129,0.15)"/>
            <text x="97" y="22" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">GEN 0 (EPHEMERAL HEAP)</text>
            <text x="12" y="44" fill="#6ee7b7" font-size="8" font-weight="600">New Object Allocations</text>
            <text x="12" y="56" fill="#94a3b8" font-size="7.5">Budget ~256KB - 4MB | &lt;1ms</text>
            <rect x="10" y="64" width="175" height="18" rx="2" fill="rgba(255,255,255,0.04)"/>
            <text x="14" y="76" fill="#cbd5e1" font-size="7.5">Short-Lived: Strings, Locals</text>
            <line x1="8" y1="88" x2="187" y2="88" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s0[1], 10, 102, 24, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s0[2], 10, 128, 26, 7.5, '#94a3b8', 2, 10)}
          </g>

          <path d="M 215 125 L 235 125" stroke="#10b981" stroke-width="1.5" marker-end="url(#gcPromoArrow)"/>

          <!-- Arena 1: Gen 1 -->
          <g transform="translate(240, 52)">
            <rect width="195" height="150" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.2"/>
            <rect x="8" y="8" width="179" height="20" rx="3" fill="rgba(6,182,212,0.15)"/>
            <text x="97" y="22" fill="#67e8f9" font-size="9" font-weight="700" text-anchor="middle">GEN 1 (SURVIVOR BUFFER)</text>
            <text x="12" y="44" fill="#22d3ee" font-size="8" font-weight="600">Survived Gen 0 Collection</text>
            <text x="12" y="56" fill="#94a3b8" font-size="7.5">Buffer before Long-Lived Heap</text>
            <rect x="10" y="64" width="175" height="18" rx="2" fill="rgba(255,255,255,0.04)"/>
            <text x="14" y="76" fill="#cbd5e1" font-size="7.5">Medium-lived: Request State</text>
            <line x1="8" y1="88" x2="187" y2="88" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s1[1], 10, 102, 24, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s1[2], 10, 128, 26, 7.5, '#94a3b8', 2, 10)}
          </g>

          <path d="M 435 125 L 455 125" stroke="#06b6d4" stroke-width="1.5" marker-end="url(#gcPromoArrow)"/>

          <!-- Arena 2: Gen 2 -->
          <g transform="translate(460, 52)">
            <rect width="195" height="150" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.2"/>
            <rect x="8" y="8" width="179" height="20" rx="3" fill="rgba(139,92,246,0.15)"/>
            <text x="97" y="22" fill="#c4b5fd" font-size="9" font-weight="700" text-anchor="middle">GEN 2 (TENURED HEAP)</text>
            <text x="12" y="44" fill="#a78bfa" font-size="8" font-weight="600">Long-Lived Objects</text>
            <text x="12" y="56" fill="#94a3b8" font-size="7.5">Full GC (Stop-The-World)</text>
            <rect x="10" y="64" width="175" height="18" rx="2" fill="rgba(255,255,255,0.04)"/>
            <text x="14" y="76" fill="#cbd5e1" font-size="7.5">Singletons, Static, DB Pools</text>
            <line x1="8" y1="88" x2="187" y2="88" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s2[1], 10, 102, 24, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s2[2], 10, 128, 26, 7.5, '#94a3b8', 2, 10)}
          </g>

          <!-- Arena 3: LOH & POH -->
          <g transform="translate(680, 52)">
            <rect width="200" height="150" rx="8" fill="#0b132b" stroke="#f59e0b" stroke-width="1.2"/>
            <rect x="8" y="8" width="184" height="20" rx="3" fill="rgba(245,158,11,0.15)"/>
            <text x="100" y="22" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">LOH &amp; POH (&gt;85,000 BYTES)</text>
            <text x="12" y="44" fill="#f59e0b" font-size="8" font-weight="600">Large Objects &amp; Pinned Buffers</text>
            <text x="12" y="56" fill="#94a3b8" font-size="7.5">Sweep Only (No Default Compaction)</text>
            <rect x="10" y="64" width="180" height="18" rx="2" fill="rgba(255,255,255,0.04)"/>
            <text x="14" y="76" fill="#cbd5e1" font-size="7.5">Arrays, Large Buffers, Native Interop</text>
            <line x1="8" y1="88" x2="192" y2="88" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s3[1], 10, 102, 25, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s3[2], 10, 128, 27, 7.5, '#94a3b8', 2, 10)}
          </g>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Generational Hypothesis: Most objects die young (Gen 0) | Mark-Sweep-Compact Algorithm | IDisposable Disposes Unmanaged Handles</text>
        </svg>
      `;
    }

    // =========================================================================
    // 7. HASH TABLE / DICTIONARY DIRECT ADDRESSING & BUCKETS
    // =========================================================================
    function renderHashBucketLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <marker id="hashArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#38bdf8"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(56,189,248,0.15)" stroke="#38bdf8" stroke-width="0.8"/>
          <text x="30" y="25" fill="#7dd3fc" font-size="10" font-weight="700" letter-spacing="1">HASH BUCKET ARRAY</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Step 0: Key Input -->
          <g transform="translate(20, 52)">
            <rect width="160" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
            <rect x="8" y="8" width="144" height="20" rx="3" fill="rgba(56,189,248,0.15)"/>
            <text x="80" y="22" fill="#7dd3fc" font-size="9" font-weight="700" text-anchor="middle">KEY INPUT [TKEY]</text>
            <rect x="10" y="36" width="140" height="34" rx="4" fill="#0b132b" stroke="#38bdf8" stroke-width="0.8"/>
            <text x="80" y="52" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle">"userId_8921"</text>
            <text x="80" y="64" fill="#94a3b8" font-size="7.5" text-anchor="middle">Immutable Key Value</text>
            <line x1="8" y1="80" x2="152" y2="80" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s0[1], 10, 94, 20, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s0[2], 10, 120, 22, 7.5, '#94a3b8', 2, 10)}
          </g>

          <path d="M 180 127 L 205 127" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#hashArrow)"/>

          <!-- Step 1: Hash Function & Modulo -->
          <g transform="translate(210, 52)">
            <rect width="180" height="150" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.2"/>
            <rect x="8" y="8" width="164" height="20" rx="3" fill="rgba(139,92,246,0.15)"/>
            <text x="90" y="22" fill="#c4b5fd" font-size="9" font-weight="700" text-anchor="middle">HASH FUNCTION &amp; MOD</text>
            <text x="12" y="46" fill="#c4b5fd" font-size="8.5" font-weight="600">hash = key.GetHashCode()</text>
            <text x="12" y="58" fill="#a78bfa" font-size="8" font-family="monospace">0x7F4A2B9C (Integer)</text>
            <rect x="10" y="66" width="160" height="24" rx="3" fill="rgba(139,92,246,0.15)"/>
            <text x="90" y="78" fill="#e0e7ff" font-size="8" font-weight="700" text-anchor="middle">bucket = (hash &amp; 0x7FFFFFFF) % size</text>
            <text x="90" y="87" fill="#34d399" font-size="7.5" font-weight="700" text-anchor="middle">Index = 2 (Direct Slot)</text>
            <line x1="8" y1="100" x2="172" y2="100" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s1[1], 10, 114, 23, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s1[2], 10, 138, 25, 7.5, '#94a3b8', 2, 10)}
          </g>

          <path d="M 390 127 L 415 127" stroke="#8b5cf6" stroke-width="1.5" marker-end="url(#hashArrow)"/>

          <!-- Step 2: Buckets Array -->
          <g transform="translate(420, 52)">
            <rect width="140" height="150" rx="8" fill="#0b132b" stroke="#10b981" stroke-width="1.2"/>
            <rect x="8" y="8" width="124" height="20" rx="3" fill="rgba(16,185,129,0.15)"/>
            <text x="70" y="22" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">BUCKETS [INT[]]</text>
            
            <rect x="10" y="34" width="120" height="20" rx="3" fill="#1e293b"/>
            <text x="16" y="47" fill="#94a3b8" font-size="8">Bucket [0] : -1 (Empty)</text>

            <rect x="10" y="58" width="120" height="20" rx="3" fill="#1e293b"/>
            <text x="16" y="71" fill="#94a3b8" font-size="8">Bucket [1] : -1 (Empty)</text>

            <rect x="10" y="82" width="120" height="24" rx="3" fill="rgba(16,185,129,0.2)" stroke="#10b981" stroke-width="1"/>
            <text x="16" y="96" fill="#34d399" font-size="8.5" font-weight="700">Bucket [2] ➔ Entry 0</text>
            <text x="16" y="104" fill="#6ee7b7" font-size="6.5">Active Head Pointer</text>

            <rect x="10" y="110" width="120" height="20" rx="3" fill="#1e293b"/>
            <text x="16" y="123" fill="#94a3b8" font-size="8">Bucket [3] : -1 (Empty)</text>

            <text x="70" y="144" fill="#64748b" font-size="7.5" text-anchor="middle">O(1) Direct Lookup</text>
          </g>

          <path d="M 560 94 L 585 94" stroke="#10b981" stroke-width="1.5" marker-end="url(#hashArrow)"/>

          <!-- Step 3 & 4: Entries Array & Chaining -->
          <g transform="translate(590, 52)">
            <rect width="290" height="150" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
            <rect x="8" y="8" width="274" height="20" rx="3" fill="rgba(245,158,11,0.15)"/>
            <text x="145" y="22" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">ENTRIES ARRAY (COLLISION CHAINING)</text>

            <!-- Entry 0 -->
            <rect x="10" y="34" width="270" height="42" rx="4" fill="#1e1b4b" stroke="#a855f7" stroke-width="0.8"/>
            <text x="18" y="47" fill="#e0e7ff" font-size="8" font-weight="700">Entry [0]: Hash=0x7F4A2B9C | Next = 1 (Collision!)</text>
            <text x="18" y="59" fill="#38bdf8" font-size="7.5">Key: "userId_8921" ➔ Value: UserProfile{...}</text>
            <text x="18" y="69" fill="#94a3b8" font-size="7">Equals(targetKey) == true ➔ Match Found!</text>

            <!-- Entry 1 (Collision chained) -->
            <rect x="10" y="80" width="270" height="38" rx="4" fill="#1e1b4b" stroke="#f59e0b" stroke-width="0.8"/>
            <text x="18" y="93" fill="#fbbf24" font-size="8" font-weight="700">Entry [1]: Hash=0x7F4A2B9C | Next = -1 (End)</text>
            <text x="18" y="104" fill="#cbd5e1" font-size="7.5">Key: "collidingKey" ➔ Value: Data{...}</text>

            <line x1="8" y1="122" x2="282" y2="122" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s2[1], 10, 134, 38, 8, '#e2e8f0', 1, 9)}
            ${renderWrappedText(s2[2], 10, 144, 42, 7.5, '#94a3b8', 1, 9)}
          </g>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Dictionary Internals: O(1) Amortized | Load Factor Threshold ➔ Prime Number Array Resize &amp; Rehash</text>
        </svg>
      `;
    }

    // =========================================================================
    // 8. MULTICAST DELEGATE & EVENT INVOCATION CHAIN
    // =========================================================================
    function renderDelegateEventLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <marker id="delArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#a855f7"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(168,85,247,0.15)" stroke="#a855f7" stroke-width="0.8"/>
          <text x="30" y="25" fill="#c084fc" font-size="10" font-weight="700" letter-spacing="1">DELEGATES &amp; EVENTS</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Left: Event Publisher -->
          <g transform="translate(20, 52)">
            <rect width="210" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
            <rect x="8" y="8" width="194" height="20" rx="3" fill="rgba(56,189,248,0.15)"/>
            <text x="105" y="22" fill="#7dd3fc" font-size="9" font-weight="700" text-anchor="middle">EVENT PUBLISHER</text>
            <rect x="10" y="34" width="190" height="36" rx="4" fill="#0b132b" stroke="#38bdf8" stroke-width="0.8"/>
            <text x="16" y="47" fill="#38bdf8" font-size="7.5" font-family="monospace">public event EventHandler</text>
            <text x="16" y="58" fill="#38bdf8" font-size="7.5" font-family="monospace">&lt;OrderEventArgs&gt; OrderPlaced;</text>
            <text x="12" y="80" fill="#94a3b8" font-size="7.5">Invokes: OrderPlaced?.Invoke(this, e)</text>
            <line x1="8" y1="90" x2="202" y2="90" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s0[1], 10, 104, 27, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s0[2], 10, 130, 29, 7.5, '#94a3b8', 2, 10)}
          </g>

          <path d="M 230 127 L 255 127" stroke="#a855f7" stroke-width="1.5" marker-end="url(#delArrow)"/>

          <!-- Center: MulticastDelegate Invocation List -->
          <g transform="translate(260, 52)">
            <rect width="320" height="150" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.2"/>
            <rect x="8" y="8" width="304" height="20" rx="3" fill="rgba(168,85,247,0.15)"/>
            <text x="160" y="22" fill="#c084fc" font-size="9" font-weight="700" text-anchor="middle">MULTICASTDELEGATE INVOCATION LIST</text>

            <!-- Target 1 -->
            <rect x="10" y="34" width="300" height="26" rx="3" fill="#1e1b4b" stroke="#a855f7" stroke-width="0.8"/>
            <text x="16" y="46" fill="#e0e7ff" font-size="8" font-weight="700">[Target 1] EmailNotificationService.SendConfirmation</text>
            <text x="16" y="55" fill="#a78bfa" font-size="7">_target: ObjectRef | _methodPtr: 0x7FFE0012A</text>

            <!-- Target 2 -->
            <rect x="10" y="64" width="300" height="26" rx="3" fill="#1e1b4b" stroke="#a855f7" stroke-width="0.8"/>
            <text x="16" y="76" fill="#e0e7ff" font-size="8" font-weight="700">[Target 2] InventoryService.DeductStock</text>
            <text x="16" y="85" fill="#a78bfa" font-size="7">_target: ObjectRef | _methodPtr: 0x7FFE004B2</text>

            <!-- Target 3 -->
            <rect x="10" y="94" width="300" height="26" rx="3" fill="#1e1b4b" stroke="#a855f7" stroke-width="0.8"/>
            <text x="16" y="106" fill="#e0e7ff" font-size="8" font-weight="700">[Target 3] AnalyticsEngine.TrackConversion</text>
            <text x="16" y="115" fill="#a78bfa" font-size="7">_target: ObjectRef | _methodPtr: 0x7FFE0089C</text>

            <line x1="8" y1="126" x2="312" y2="126" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s1[1], 10, 138, 42, 8, '#e2e8f0', 1, 9)}
            ${renderWrappedText(s1[2], 10, 147, 45, 7.5, '#94a3b8', 1, 9)}
          </g>

          <path d="M 580 127 L 605 127" stroke="#a855f7" stroke-width="1.5" marker-end="url(#delArrow)"/>

          <!-- Right: Decoupled Subscribers -->
          <g transform="translate(610, 52)">
            <rect width="270" height="150" rx="8" fill="#0b132b" stroke="#10b981" stroke-width="1.2"/>
            <rect x="8" y="8" width="254" height="20" rx="3" fill="rgba(16,185,129,0.15)"/>
            <text x="135" y="22" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">DECOUPLED SUBSCRIBERS</text>

            <rect x="10" y="34" width="250" height="26" rx="3" fill="rgba(255,255,255,0.04)"/>
            <text x="16" y="46" fill="#34d399" font-size="8" font-weight="600">Subscriber A: Email Service</text>
            <text x="16" y="55" fill="#94a3b8" font-size="7">Listens independently via += subscription</text>

            <rect x="10" y="64" width="250" height="26" rx="3" fill="rgba(255,255,255,0.04)"/>
            <text x="16" y="76" fill="#38bdf8" font-size="8" font-weight="600">Subscriber B: Inventory System</text>
            <text x="16" y="85" fill="#94a3b8" font-size="7">Weak Event pattern prevents leaks</text>

            <rect x="10" y="94" width="250" height="26" rx="3" fill="rgba(255,255,255,0.04)"/>
            <text x="16" y="106" fill="#fbbf24" font-size="8" font-weight="600">Subscriber C: Telemetry / Audit</text>
            <text x="16" y="115" fill="#94a3b8" font-size="7">Zero coupling to publisher class</text>

            <line x1="8" y1="126" x2="262" y2="126" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s2[1], 10, 138, 35, 8, '#e2e8f0', 1, 9)}
            ${renderWrappedText(s2[2], 10, 147, 38, 7.5, '#94a3b8', 1, 9)}
          </g>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Delegate Pattern: Type-Safe Function Pointer | Action&lt;T&gt; &amp; Func&lt;T, TResult&gt; | Unsubscribe with -= to avoid Memory Leaks</text>
        </svg>
      `;
    }

    // =========================================================================
    // 9. CALL STACK UNWINDING & EXCEPTION DISPATCH TOPOLOGY
    // =========================================================================
    function renderExceptionStackLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <marker id="unwindArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#ef4444"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(239,68,68,0.15)" stroke="#ef4444" stroke-width="0.8"/>
          <text x="30" y="25" fill="#f87171" font-size="10" font-weight="700" letter-spacing="1">EXCEPTION STACK UNWIND</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Left: Call Stack Ladder -->
          <g transform="translate(30, 52)">
            <rect width="360" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
            <rect x="8" y="8" width="344" height="20" rx="3" fill="rgba(56,189,248,0.15)"/>
            <text x="180" y="22" fill="#7dd3fc" font-size="9" font-weight="700" text-anchor="middle">THREAD CALL STACK FRAMES</text>

            <!-- Top Frame: Throw site -->
            <rect x="10" y="32" width="340" height="32" rx="4" fill="rgba(239,68,68,0.2)" stroke="#ef4444" stroke-width="1"/>
            <text x="18" y="45" fill="#fca5a5" font-size="8.5" font-weight="700">[Frame 3] Repository.Query() ➔ throw new DbException()</text>
            <text x="18" y="56" fill="#f87171" font-size="7.5">Exception Object Allocated on Heap | Stack Pointer at RSP</text>

            <!-- Middle Frame: try / catch -->
            <rect x="10" y="68" width="340" height="32" rx="4" fill="#1e1b4b" stroke="#a855f7" stroke-width="0.8"/>
            <text x="18" y="81" fill="#e0e7ff" font-size="8.5" font-weight="700">[Frame 2] OrderService.ProcessOrder() [try / catch block]</text>
            <text x="18" y="92" fill="#c084fc" font-size="7.5">Catch Filter Matches ➔ Stack Unwinds to here!</text>

            <!-- Bottom Frame: Entry point -->
            <rect x="10" y="104" width="340" height="32" rx="4" fill="#0b132b" stroke="rgba(255,255,255,0.1)" stroke-width="0.8"/>
            <text x="18" y="117" fill="#94a3b8" font-size="8.5" font-weight="600">[Frame 1] Program.Main() [Caller Base Frame]</text>
            <text x="18" y="128" fill="#64748b" font-size="7.5">Root Application Frame</text>
          </g>

          <!-- Center: Stack Unwind Path -->
          <path d="M 400 68 C 430 68, 430 115, 450 115" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,3" marker-end="url(#unwindArrow)"/>
          <text x="425" y="88" fill="#f87171" font-size="7.5" font-weight="700">UNWIND</text>

          <!-- Right Top: Catch Handler Chamber -->
          <g transform="translate(460, 52)">
            <rect width="410" height="70" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.2"/>
            <rect x="8" y="8" width="394" height="18" rx="3" fill="rgba(168,85,247,0.15)"/>
            <text x="205" y="20" fill="#c084fc" font-size="8.5" font-weight="700" text-anchor="middle">CATCH BLOCK FILTER &amp; HANDLER</text>
            <text x="14" y="38" fill="#e0e7ff" font-size="8" font-weight="600">catch (DbException ex) when (ex.ErrorCode == 1205) { ... }</text>
            ${renderWrappedText(s1[1], 14, 50, 55, 8, '#e2e8f0', 1, 9)}
            ${renderWrappedText(s1[2], 14, 60, 60, 7.5, '#94a3b8', 1, 9)}
          </g>

          <!-- Right Bottom: Finally Guaranteed Vault -->
          <g transform="translate(460, 130)">
            <rect width="410" height="72" rx="8" fill="#0b132b" stroke="#10b981" stroke-width="1.2"/>
            <rect x="8" y="8" width="394" height="18" rx="3" fill="rgba(168,85,247,0.15)"/>
            <text x="205" y="20" fill="#34d399" font-size="8.5" font-weight="700" text-anchor="middle">FINALLY CHAMBER (GUARANTEED EXECUTION)</text>
            <text x="14" y="38" fill="#6ee7b7" font-size="8" font-weight="600">finally { conn.Dispose(); fileStream.Close(); }</text>
            <text x="14" y="49" fill="#94a3b8" font-size="7.5">Executes on success, caught exception, OR unhandled exception!</text>
            ${renderWrappedText(s2[1], 14, 60, 55, 8, '#cbd5e1', 1, 9)}
          </g>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Stack Preservation Rule: Always use 'throw;' to preserve original stack trace | 'throw ex;' overwrites stack trace origin to current line!</text>
        </svg>
      `;
    }

    // =========================================================================
    // 10. DEPENDENCY INJECTION CONTAINER LIFETIME HIERARCHY
    // =========================================================================
    function renderDiLifetimeLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(245,158,11,0.15)" stroke="#f59e0b" stroke-width="0.8"/>
          <text x="30" y="25" fill="#fbbf24" font-size="10" font-weight="700" letter-spacing="1">DI SERVICE LIFETIMES</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Tier 1: Singleton (Root Container) -->
          <g transform="translate(30, 52)">
            <rect width="840" height="46" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
            <rect x="8" y="6" width="160" height="18" rx="3" fill="rgba(245,158,11,0.15)"/>
            <text x="88" y="18" fill="#fbbf24" font-size="8.5" font-weight="700" text-anchor="middle">SINGLETON (ROOT CONTAINER)</text>
            <text x="180" y="18" fill="#f1f5f9" font-size="8.5" font-weight="600">Created once on first resolve ➔ Shared across entire AppDomain &amp; all threads</text>
            <text x="180" y="34" fill="#94a3b8" font-size="8">E.g., IConfiguration, IMemoryCache, HttpClientFactory | Disposed when Host shuts down</text>
            <text x="750" y="26" fill="#fbbf24" font-size="8" font-weight="700">1 INSTANCE</text>
          </g>

          <!-- Tier 2: Scoped (Request Container) -->
          <g transform="translate(30, 104)">
            <!-- Scope 1 -->
            <rect width="410" height="52" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
            <rect x="8" y="6" width="160" height="18" rx="3" fill="rgba(56,189,248,0.15)"/>
            <text x="88" y="18" fill="#7dd3fc" font-size="8.5" font-weight="700" text-anchor="middle">SCOPED [HTTP REQUEST 1]</text>
            <text x="180" y="18" fill="#f1f5f9" font-size="8.5" font-weight="600">Created once per HTTP Request</text>
            <text x="14" y="38" fill="#94a3b8" font-size="7.5">DbContext, CurrentUser, UnitOfWork | Disposed at request end</text>
            <text x="350" y="26" fill="#38bdf8" font-size="8" font-weight="700">SCOPE A</text>

            <!-- Scope 2 -->
            <rect x="430" y="0" width="410" height="52" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
            <rect x="438" y="6" width="160" height="18" rx="3" fill="rgba(56,189,248,0.15)"/>
            <text x="518" y="18" fill="#7dd3fc" font-size="8.5" font-weight="700" text-anchor="middle">SCOPED [HTTP REQUEST 2]</text>
            <text x="610" y="18" fill="#f1f5f9" font-size="8.5" font-weight="600">Isolated separate DbContext</text>
            <text x="444" y="38" fill="#94a3b8" font-size="7.5">Zero cross-request thread contamination or shared state</text>
            <text x="780" y="26" fill="#38bdf8" font-size="8" font-weight="700">SCOPE B</text>
          </g>

          <!-- Tier 3: Transient Instances -->
          <g transform="translate(30, 162)">
            <rect width="265" height="48" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.2"/>
            <rect x="8" y="5" width="140" height="16" rx="3" fill="rgba(168,85,247,0.15)"/>
            <text x="78" y="16" fill="#c084fc" font-size="8" font-weight="700" text-anchor="middle">TRANSIENT #1</text>
            <text x="12" y="34" fill="#cbd5e1" font-size="7.5">Created anew every time requested</text>
            <text x="210" y="16" fill="#a855f7" font-size="7.5" font-weight="700">NEW()</text>

            <rect x="285" y="0" width="265" height="48" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.2"/>
            <rect x="293" y="5" width="140" height="16" rx="3" fill="rgba(168,85,247,0.15)"/>
            <text x="363" y="16" fill="#c084fc" font-size="8" font-weight="700" text-anchor="middle">TRANSIENT #2</text>
            <text x="297" y="34" fill="#cbd5e1" font-size="7.5">Lightweight, stateless services</text>
            <text x="495" y="16" fill="#a855f7" font-size="7.5" font-weight="700">NEW()</text>

            <rect x="570" y="0" width="300" height="48" rx="6" fill="#0b132b" stroke="#ef4444" stroke-width="1.2"/>
            <rect x="578" y="5" width="170" height="16" rx="3" fill="rgba(239,68,68,0.15)"/>
            <text x="663" y="16" fill="#f87171" font-size="8" font-weight="700" text-anchor="middle">CAPTIVE DEPENDENCY WARNING</text>
            <text x="582" y="34" fill="#fca5a5" font-size="7.5">Never inject Scoped service into Singleton! (Causes leaks)</text>
          </g>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Service Lifetimes: AddSingleton&lt;T&gt; (1 for App) | AddScoped&lt;T&gt; (1 per Request) | AddTransient&lt;T&gt; (New every resolve)</text>
        </svg>
      `;
    }
'''

print("Batch 2 ready in string format")
with open('scratch/test_batch2.js', 'w', encoding='utf-8') as f:
    f.write(layouts)
print("Saved scratch/test_batch2.js")

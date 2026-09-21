
    // =========================================================================
    // 11. CIRCUIT BREAKER TRI-STATE MACHINE TOPOLOGY
    // =========================================================================
    function renderCircuitBreakerLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <marker id="cbArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#f59e0b"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(239,68,68,0.15)" stroke="#ef4444" stroke-width="0.8"/>
          <text x="30" y="25" fill="#f87171" font-size="10" font-weight="700" letter-spacing="1">CIRCUIT BREAKER &amp; POLLY</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- State 1: CLOSED (Normal Operation) -->
          <g transform="translate(30, 52)">
            <rect width="240" height="150" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect x="8" y="8" width="224" height="22" rx="3" fill="rgba(16,185,129,0.15)"/>
            <text x="120" y="23" fill="#34d399" font-size="10" font-weight="800" text-anchor="middle">CLOSED STATE (NORMAL)</text>
            <text x="14" y="46" fill="#34d399" font-size="8.5" font-weight="600">Requests Flow to Remote API</text>
            <text x="14" y="58" fill="#94a3b8" font-size="7.5">Successes keep circuit closed</text>
            <rect x="12" y="66" width="216" height="22" rx="3" fill="#1e293b"/>
            <text x="18" y="80" fill="#cbd5e1" font-size="7.5">Failure Counter: 0 / 5 (Threshold)</text>
            <line x1="8" y1="96" x2="232" y2="96" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s0[1], 12, 110, 30, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s0[2], 12, 136, 32, 7.5, '#94a3b8', 2, 10)}
          </g>

          <!-- Arrow CLOSED -> OPEN (Top curved arrow) -->
          <path d="M 270 85 C 310 65, 590 65, 630 85" fill="none" stroke="#ef4444" stroke-width="2" marker-end="url(#cbArrow)"/>
          <rect x="400" y="58" width="100" height="16" rx="3" fill="#0b132b" stroke="#ef4444" stroke-width="0.8"/>
          <text x="450" y="69" fill="#f87171" font-size="7" font-weight="700" text-anchor="middle">Failures &gt; Threshold ➔ TRIP</text>

          <!-- State 2: OPEN (Fast Fail) -->
          <g transform="translate(630, 52)">
            <rect width="240" height="150" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
            <rect x="8" y="8" width="224" height="22" rx="3" fill="rgba(239,68,68,0.15)"/>
            <text x="120" y="23" fill="#f87171" font-size="10" font-weight="800" text-anchor="middle">OPEN STATE (FAIL-FAST)</text>
            <text x="14" y="46" fill="#f87171" font-size="8.5" font-weight="600">Zero Remote Calls Allowed</text>
            <text x="14" y="58" fill="#94a3b8" font-size="7.5">Immediately throws BrokenCircuitException</text>
            <rect x="12" y="66" width="216" height="22" rx="3" fill="#1e293b"/>
            <text x="18" y="80" fill="#fca5a5" font-size="7.5">Protects downstream from cascading failure</text>
            <line x1="8" y1="96" x2="232" y2="96" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s1[1], 12, 110, 30, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s1[2], 12, 136, 32, 7.5, '#94a3b8', 2, 10)}
          </g>

          <!-- Arrow OPEN -> HALF-OPEN (Bottom curved arrow) -->
          <path d="M 670 170 C 620 185, 540 185, 490 170" fill="none" stroke="#f59e0b" stroke-width="1.8" marker-end="url(#cbArrow)"/>
          <text x="575" y="194" fill="#fbbf24" font-size="7" font-weight="700" text-anchor="middle">Sleep Window Expired (e.g. 30s)</text>

          <!-- State 3: HALF-OPEN (Trial Probe) -->
          <g transform="translate(320, 100)">
            <rect width="260" height="98" rx="8" fill="#0b132b" stroke="#f59e0b" stroke-width="1.5"/>
            <rect x="8" y="6" width="244" height="20" rx="3" fill="rgba(245,158,11,0.15)"/>
            <text x="130" y="20" fill="#fbbf24" font-size="9" font-weight="800" text-anchor="middle">HALF-OPEN STATE (PROBE)</text>
            <text x="12" y="40" fill="#e0e7ff" font-size="8" font-weight="600">Allows trial probe request to test downstream</text>
            <text x="12" y="52" fill="#34d399" font-size="7.5">If Success ➔ Reset to CLOSED</text>
            <text x="12" y="62" fill="#f87171" font-size="7.5">If Failure ➔ Re-trip to OPEN (Reset sleep timer)</text>
            <line x1="8" y1="70" x2="252" y2="70" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s2[1], 10, 82, 34, 8, '#e2e8f0', 1, 9)}
            ${renderWrappedText(s2[2], 10, 91, 38, 7, '#94a3b8', 1, 8)}
          </g>

          <!-- Arrow HALF-OPEN -> CLOSED -->
          <path d="M 320 135 L 275 135" stroke="#10b981" stroke-width="1.8" marker-end="url(#cbArrow)"/>
          <text x="295" y="128" fill="#34d399" font-size="7" font-weight="700" text-anchor="middle">SUCCESS</text>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Resilience Engineering: Polly Circuit Breaker + Retry with Exponential Jitter + Fallback Response Cache</text>
        </svg>
      `;
    }

    // =========================================================================
    // 12. REACT COMPONENT LIFECYCLE & HOOK DEPENDENCY WATCHER
    // =========================================================================
    function renderReactComponentLifecycleLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <marker id="reactArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#06b6d4"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(6,182,212,0.15)" stroke="#06b6d4" stroke-width="0.8"/>
          <text x="30" y="25" fill="#22d3ee" font-size="10" font-weight="700" letter-spacing="1">REACT HOOK LIFECYCLE</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Phase 1: Mount -->
          <g transform="translate(20, 52)">
            <rect width="260" height="150" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
            <rect x="8" y="8" width="244" height="20" rx="3" fill="rgba(16,185,129,0.15)"/>
            <text x="130" y="22" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">1. MOUNTING PHASE</text>
            <text x="12" y="44" fill="#34d399" font-size="8.5" font-weight="600">Function Component Executes</text>
            <text x="12" y="56" fill="#94a3b8" font-size="7.5">useState / useMemo initialized</text>
            <rect x="10" y="64" width="240" height="20" rx="3" fill="#1e293b"/>
            <text x="16" y="78" fill="#6ee7b7" font-size="7.5">DOM Nodes Inserted ➔ Paint to Screen</text>
            <text x="12" y="98" fill="#cbd5e1" font-size="8" font-weight="600">useEffect(() =&gt; { ... }, []) runs!</text>
            <line x1="8" y1="106" x2="252" y2="106" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s0[1], 10, 120, 32, 8.5, '#e2e8f0', 1, 10)}
            ${renderWrappedText(s0[2], 10, 134, 34, 7.5, '#94a3b8', 2, 9)}
          </g>

          <path d="M 285 127 L 315 127" stroke="#06b6d4" stroke-width="1.5" marker-end="url(#reactArrow)"/>

          <!-- Phase 2: Update & Dependency Array -->
          <g transform="translate(320, 52)">
            <rect width="270" height="150" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.2"/>
            <rect x="8" y="8" width="254" height="20" rx="3" fill="rgba(6,182,212,0.15)"/>
            <text x="135" y="22" fill="#22d3ee" font-size="9" font-weight="700" text-anchor="middle">2. UPDATING (STATE/PROPS)</text>
            <text x="12" y="44" fill="#67e8f9" font-size="8.5" font-weight="600">setState() Triggers Re-render</text>
            
            <rect x="10" y="52" width="250" height="34" rx="3" fill="#0b132b" stroke="#06b6d4" stroke-width="0.8"/>
            <text x="16" y="65" fill="#e0e7ff" font-size="7.5" font-weight="700">Dependency Array Check:</text>
            <text x="16" y="77" fill="#fbbf24" font-size="7">Object.is(prevDep, nextDep) === false?</text>

            <text x="12" y="98" fill="#cbd5e1" font-size="8">1. Clean up old effect ➔ 2. Run new effect</text>
            <line x1="8" y1="106" x2="262" y2="106" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s1[1], 10, 120, 33, 8.5, '#e2e8f0', 1, 10)}
            ${renderWrappedText(s1[2], 10, 134, 35, 7.5, '#94a3b8', 2, 9)}
          </g>

          <path d="M 595 127 L 625 127" stroke="#06b6d4" stroke-width="1.5" marker-end="url(#reactArrow)"/>

          <!-- Phase 3: Unmount -->
          <g transform="translate(630, 52)">
            <rect width="250" height="150" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.2"/>
            <rect x="8" y="8" width="234" height="20" rx="3" fill="rgba(139,92,246,0.15)"/>
            <text x="125" y="22" fill="#c4b5fd" font-size="9" font-weight="700" text-anchor="middle">3. UNMOUNTING PHASE</text>
            <text x="12" y="44" fill="#a78bfa" font-size="8.5" font-weight="600">Component Destroyed</text>
            <text x="12" y="56" fill="#94a3b8" font-size="7.5">Removed from Virtual DOM &amp; Screen</text>
            <rect x="10" y="64" width="230" height="34" rx="3" fill="#1e1b4b" stroke="#8b5cf6" stroke-width="0.8"/>
            <text x="16" y="78" fill="#e0e7ff" font-size="7.5" font-weight="700">return () =&gt; { cleanup(); }</text>
            <text x="16" y="89" fill="#c4b5fd" font-size="7">Unsubscribes timers, websockets, listeners</text>
            <line x1="8" y1="106" x2="242" y2="106" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s2[1], 10, 120, 31, 8.5, '#e2e8f0', 1, 10)}
            ${renderWrappedText(s2[2], 10, 134, 33, 7.5, '#94a3b8', 2, 9)}
          </g>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">React Hooks Contract: Call hooks only at top level | Stable dependency arrays prevent infinite re-render loops</text>
        </svg>
      `;
    }

    // =========================================================================
    // 13. HTTP REQUEST-RESPONSE LIFECYCLE & WEB API GATEWAY
    // =========================================================================
    function renderHttpFlowLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <marker id="reqArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#38bdf8"/>
            </marker>
            <marker id="resArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#10b981"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(56,189,248,0.15)" stroke="#38bdf8" stroke-width="0.8"/>
          <text x="30" y="25" fill="#7dd3fc" font-size="10" font-weight="700" letter-spacing="1">HTTP &amp; WEB API FLOW</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Left: Client / Browser -->
          <g transform="translate(20, 52)">
            <rect width="160" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
            <rect x="8" y="8" width="144" height="20" rx="3" fill="rgba(56,189,248,0.15)"/>
            <text x="80" y="22" fill="#7dd3fc" font-size="9" font-weight="700" text-anchor="middle">CLIENT / USER AGENT</text>
            <rect x="10" y="34" width="140" height="36" rx="4" fill="#0b132b" stroke="#38bdf8" stroke-width="0.8"/>
            <text x="16" y="47" fill="#38bdf8" font-size="8" font-weight="600">HttpClient / Browser</text>
            <text x="16" y="58" fill="#94a3b8" font-size="7.5">TLS 1.3 / HTTP 2/3</text>
            <line x1="8" y1="78" x2="152" y2="78" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s0[1], 10, 92, 20, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s0[2], 10, 118, 22, 7.5, '#94a3b8', 2, 10)}
          </g>

          <!-- Top Forward Arrow (Request) -->
          <path d="M 185 85 L 235 85" stroke="#38bdf8" stroke-width="2" marker-end="url(#reqArrow)"/>
          <rect x="180" y="70" width="55" height="14" rx="2" fill="#0284c7"/>
          <text x="207" y="80" fill="#ffffff" font-size="7" font-weight="700" text-anchor="middle">REQUEST</text>

          <!-- Center-Left: Kestrel & Gateway -->
          <g transform="translate(240, 52)">
            <rect width="190" height="150" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.2"/>
            <rect x="8" y="8" width="174" height="20" rx="3" fill="rgba(139,92,246,0.15)"/>
            <text x="95" y="22" fill="#c4b5fd" font-size="9" font-weight="700" text-anchor="middle">KESTREL REVERSE PROXY</text>
            <rect x="10" y="34" width="170" height="36" rx="3" fill="#1e1b4b" stroke="#8b5cf6" stroke-width="0.8"/>
            <text x="16" y="47" fill="#e0e7ff" font-size="8" font-weight="600">Socket Epoll / IOCP</text>
            <text x="16" y="58" fill="#a78bfa" font-size="7.5">TLS Offload &amp; Connection Pool</text>
            <line x1="8" y1="78" x2="182" y2="78" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s1[1], 10, 92, 24, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s1[2], 10, 118, 26, 7.5, '#94a3b8', 2, 10)}
          </g>

          <path d="M 435 85 L 455 85" stroke="#38bdf8" stroke-width="2" marker-end="url(#reqArrow)"/>

          <!-- Center-Right: Routing & Controller Endpoint -->
          <g transform="translate(460, 52)">
            <rect width="210" height="150" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1.2"/>
            <rect x="8" y="8" width="194" height="20" rx="3" fill="rgba(6,182,212,0.15)"/>
            <text x="105" y="22" fill="#67e8f9" font-size="9" font-weight="700" text-anchor="middle">ENDPOINT &amp; CONTROLLER</text>
            <rect x="10" y="34" width="190" height="36" rx="3" fill="#0b132b" stroke="#06b6d4" stroke-width="0.8"/>
            <text x="16" y="47" fill="#67e8f9" font-size="8" font-weight="600">Model Binding &amp; Validation</text>
            <text x="16" y="58" fill="#94a3b8" font-size="7.5">ActionFilter ➔ Handler ➔ Result</text>
            <line x1="8" y1="78" x2="202" y2="78" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s2[1], 10, 92, 26, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s2[2], 10, 118, 28, 7.5, '#94a3b8', 2, 10)}
          </g>

          <path d="M 675 85 L 695 85" stroke="#38bdf8" stroke-width="2" marker-end="url(#reqArrow)"/>

          <!-- Right: Data Tier & Service -->
          <g transform="translate(700, 52)">
            <rect width="180" height="150" rx="8" fill="#0b132b" stroke="#10b981" stroke-width="1.2"/>
            <rect x="8" y="8" width="164" height="20" rx="3" fill="rgba(16,185,129,0.15)"/>
            <text x="90" y="22" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">DATA &amp; SERVICE STORE</text>
            <rect x="10" y="34" width="160" height="36" rx="3" fill="#1e293b"/>
            <text x="16" y="47" fill="#34d399" font-size="8" font-weight="600">EF Core / Dapper / SQL</text>
            <text x="16" y="58" fill="#94a3b8" font-size="7.5">Async I/O Query Return</text>
            <line x1="8" y1="78" x2="172" y2="78" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s3[1], 10, 92, 22, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s3[2], 10, 118, 24, 7.5, '#94a3b8', 2, 10)}
          </g>

          <!-- Bottom Return Arrow (Response) -->
          <path d="M 700 170 L 185 170" stroke="#10b981" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#resArrow)"/>
          <rect x="400" y="160" width="120" height="18" rx="3" fill="#065f46"/>
          <text x="460" y="172" fill="#ffffff" font-size="8" font-weight="700" text-anchor="middle">HTTP 200 OK (JSON RESPONSE)</text>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Request Lifecycle: Client ➔ Reverse Proxy ➔ ASP.NET Core Middleware ➔ Endpoint Routing ➔ Serialized Response</text>
        </svg>
      `;
    }

    // =========================================================================
    // 14. ASYNC / AWAIT COMPILER STATE MACHINE TOPOLOGY
    // =========================================================================
    function renderAsyncLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <marker id="asyncArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <polygon points="0 0, 6 3, 0 6" fill="#8b5cf6"/>
            </marker>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(139,92,246,0.15)" stroke="#8b5cf6" stroke-width="0.8"/>
          <text x="30" y="25" fill="#c4b5fd" font-size="10" font-weight="700" letter-spacing="1">ASYNC STATE MACHINE</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- Step 0: Calling Thread Entry -->
          <g transform="translate(20, 52)">
            <rect width="180" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
            <rect x="8" y="8" width="164" height="20" rx="3" fill="rgba(56,189,248,0.15)"/>
            <text x="90" y="22" fill="#7dd3fc" font-size="9" font-weight="700" text-anchor="middle">1. SYNCHRONOUS ENTRY</text>
            <text x="12" y="44" fill="#38bdf8" font-size="8.5" font-weight="600">Calling Thread Enters</text>
            <text x="12" y="56" fill="#94a3b8" font-size="7.5">Executes synchronously until</text>
            <text x="12" y="66" fill="#fbbf24" font-size="7.5">first incomplete 'await' keyword</text>
            <line x1="8" y1="76" x2="172" y2="76" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s0[1], 10, 90, 22, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s0[2], 10, 116, 24, 7.5, '#94a3b8', 2, 10)}
          </g>

          <path d="M 205 127 L 225 127" stroke="#8b5cf6" stroke-width="1.5" marker-end="url(#asyncArrow)"/>

          <!-- Step 1: Compiler State Machine Struct -->
          <g transform="translate(230, 52)">
            <rect width="210" height="150" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.2"/>
            <rect x="8" y="8" width="194" height="20" rx="3" fill="rgba(139,92,246,0.15)"/>
            <text x="105" y="22" fill="#c4b5fd" font-size="9" font-weight="700" text-anchor="middle">2. STATE MACHINE STRUCT</text>
            <rect x="10" y="34" width="190" height="36" rx="3" fill="#1e1b4b" stroke="#8b5cf6" stroke-width="0.8"/>
            <text x="16" y="47" fill="#e0e7ff" font-size="8" font-family="monospace">struct &lt;Method&gt;d__1 :</text>
            <text x="16" y="58" fill="#a78bfa" font-size="7.5" font-family="monospace">IAsyncStateMachine { state = 0 }</text>
            <line x1="8" y1="76" x2="202" y2="76" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s1[1], 10, 90, 26, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s1[2], 10, 116, 28, 7.5, '#94a3b8', 2, 10)}
          </g>

          <!-- Step 2: Decision Diamond (awaiter.IsCompleted?) -->
          <g transform="translate(450, 85)">
            <polygon points="35 0, 70 35, 35 70, 0 35" fill="rgba(245,158,11,0.15)" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="35" y="32" fill="#fbbf24" font-size="7.5" font-weight="700" text-anchor="middle">IsCompleted?</text>
            <text x="35" y="44" fill="#cbd5e1" font-size="6.5" text-anchor="middle">Task Check</text>
          </g>

          <!-- Fast Path Arrow (If True) -->
          <path d="M 485 85 L 485 65 L 530 65" stroke="#10b981" stroke-width="1.5" marker-end="url(#asyncArrow)"/>
          <text x="495" y="60" fill="#34d399" font-size="7" font-weight="700">TRUE (SYNC)</text>

          <!-- Yield Path Arrow (If False) -->
          <path d="M 520 120 L 540 120" stroke="#f59e0b" stroke-width="1.5" marker-end="url(#asyncArrow)"/>
          <text x="530" y="112" fill="#fbbf24" font-size="7" font-weight="700">FALSE</text>

          <!-- Step 3: Yield & Hook Continuation -->
          <g transform="translate(545, 52)">
            <rect width="180" height="68" rx="6" fill="#0b132b" stroke="#f59e0b" stroke-width="1.2"/>
            <rect x="6" y="6" width="168" height="16" rx="2" fill="rgba(245,158,11,0.15)"/>
            <text x="90" y="17" fill="#fbbf24" font-size="8" font-weight="700" text-anchor="middle">3. YIELD &amp; HOOK AWAITER</text>
            <text x="10" y="34" fill="#cbd5e1" font-size="7.5">Method yields incomplete Task</text>
            <text x="10" y="44" fill="#94a3b8" font-size="7">Calling thread freed to ThreadPool!</text>
            ${renderWrappedText(s2[1], 10, 56, 23, 7.5, '#e2e8f0', 1, 8)}
          </g>

          <!-- Step 4: Resume MoveNext() on Worker Thread -->
          <g transform="translate(545, 130)">
            <rect width="180" height="72" rx="6" fill="#0b132b" stroke="#10b981" stroke-width="1.2"/>
            <rect x="6" y="6" width="168" height="16" rx="2" fill="rgba(16,185,129,0.15)"/>
            <text x="90" y="17" fill="#34d399" font-size="8" font-weight="700" text-anchor="middle">4. MOVENEXT() RESUMPTION</text>
            <text x="10" y="34" fill="#34d399" font-size="7.5">I/O completes ➔ IOCP thread wakes</text>
            <text x="10" y="44" fill="#94a3b8" font-size="7">Restores locals, state = -1</text>
            ${renderWrappedText(s3[1], 10, 56, 23, 7.5, '#e2e8f0', 1, 8)}
          </g>

          <!-- Far Right: Unwrapped Result -->
          <g transform="translate(740, 52)">
            <rect width="140" height="150" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
            <rect x="8" y="8" width="124" height="20" rx="3" fill="rgba(16,185,129,0.15)"/>
            <text x="70" y="22" fill="#34d399" font-size="8.5" font-weight="700" text-anchor="middle">5. UNWRAPPED RESULT</text>
            <rect x="10" y="34" width="120" height="34" rx="3" fill="#1e293b"/>
            <text x="70" y="48" fill="#6ee7b7" font-size="8" font-weight="700" text-anchor="middle">GetResult()</text>
            <text x="70" y="58" fill="#94a3b8" font-size="7" text-anchor="middle">Returns T or throws</text>
            <line x1="8" y1="76" x2="132" y2="76" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            ${renderWrappedText(s4[1], 10, 92, 17, 8.5, '#e2e8f0', 2, 11)}
            ${renderWrappedText(s4[2], 10, 118, 19, 7.5, '#94a3b8', 2, 10)}
          </g>

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Async Internals: Non-blocking I/O via IOCP | ValueTasks prevent Task allocation for sync completions | ConfigureAwait(false)</text>
        </svg>
      `;
    }

    // =========================================================================
    // 15. ASYMMETRIC STEPPED CHEVRON ENTERPRISE PIPELINE
    // =========================================================================
    function renderPipelineLayout(q, title, steps, w, h) {
      const s0 = steps[0], s1 = steps[1], s2 = steps[2], s3 = steps[3], s4 = steps[4];
      const sList = [s0, s1, s2, s3, s4];

      const colors = [
        { stroke: '#0284c7', fill: '#38bdf8', bg: '#0369a1' },
        { stroke: '#7c3aed', fill: '#a78bfa', bg: '#6d28d9' },
        { stroke: '#059669', fill: '#34d399', bg: '#047857' },
        { stroke: '#d97706', fill: '#fbbf24', bg: '#b45309' },
        { stroke: '#db2777', fill: '#f472b6', bg: '#be185d' }
      ];

      return `
        <svg viewBox="0 0 ${w} ${h}" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" class="portal-svg-diagram">
          <defs>
            <filter id="pipGlow" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="3" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
          </defs>

          <rect width="${w}" height="${h}" rx="12" fill="#080c14" stroke="rgba(255,255,255,0.08)" stroke-width="1.2"/>
          <path d="M 0 42 L ${w} 42 M 0 216 L ${w} 216" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

          <!-- Header -->
          <rect x="20" y="10" width="220" height="22" rx="5" fill="rgba(2,132,199,0.15)" stroke="#0284c7" stroke-width="0.8"/>
          <text x="30" y="25" fill="#38bdf8" font-size="10" font-weight="700" letter-spacing="1">ARCHITECTURAL PIPELINE</text>
          <text x="250" y="25" fill="#f1f5f9" font-size="12" font-weight="600">${title}</text>

          <!-- 5 Stepped Cards with Chevrons -->
          ${sList.map((st, i) => {
            const x = 20 + i * 174;
            const c = colors[i];
            const num = '0' + (i + 1);

            return `
              <g transform="translate(${x}, 52)">
                <rect width="162" height="150" rx="8" fill="#0f172a" stroke="${c.stroke}" stroke-width="1.2"/>
                
                <!-- Card Header -->
                <rect x="8" y="8" width="146" height="22" rx="3" fill="${c.bg}" fill-opacity="0.2"/>
                <circle cx="22" cy="19" r="8" fill="${c.stroke}"/>
                <text x="22" y="22.5" fill="#ffffff" font-size="8.5" font-weight="800" text-anchor="middle">${num}</text>
                <text x="38" y="22" fill="${c.fill}" font-size="8" font-weight="700" letter-spacing="0.5">${escSvg(st[0])}</text>

                <!-- Stage Title -->
                <g transform="translate(10, 42)">
                  ${renderWrappedText(st[1], 0, 0, 20, 9, '#f8fafc', 2, 11)}
                </g>

                <!-- Divider -->
                <line x1="10" y1="74" x2="152" y2="74" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

                <!-- Stage Description -->
                <g transform="translate(10, 88)">
                  ${renderWrappedText(st[2], 0, 0, 22, 7.5, '#94a3b8', 3, 10)}
                </g>

                <!-- Verified Pill -->
                <rect x="10" y="126" width="142" height="16" rx="3" fill="rgba(255,255,255,0.04)" stroke="${c.stroke}" stroke-width="0.6"/>
                <text x="81" y="137" fill="${c.fill}" font-size="7.5" font-weight="700" text-anchor="middle">${escSvg(st[3] || 'Verified')}</text>
              </g>

              ${i < 4 ? `
                <path d="M ${x + 162} 127 L ${x + 174} 127" stroke="${c.stroke}" stroke-width="2"/>
                <polygon points="${x + 172} 124, ${x + 175} 127, ${x + 172} 130" fill="${c.stroke}"/>
              ` : ''}
            `;
          }).join('\n')}

          <!-- Footer -->
          <text x="450" y="238" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">Execution Path: Stage 01 ➔ Stage 02 ➔ Stage 03 ➔ Stage 04 ➔ Stage 05 (Synchronized Pipeline Delivery)</text>
        </svg>
      `;
    }

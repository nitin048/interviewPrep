import os
import sys

print("Reading senior-dotnet-interview-portal.html...")
with open('senior-dotnet-interview-portal.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS
css_to_add = r'''
    /* ==========================================================================
       Quick Category Filter Chips & Active Filter Indicator
       ========================================================================== */
    .quick-category-bar {
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      padding: 6px 2px 8px 2px;
      scrollbar-width: thin;
      scrollbar-color: rgba(255, 255, 255, 0.18) transparent;
      -webkit-overflow-scrolling: touch;
      margin-top: 4px;
      margin-bottom: 2px;
    }

    .quick-category-bar::-webkit-scrollbar {
      height: 4px;
    }

    .quick-category-bar::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.18);
      border-radius: 4px;
    }

    .quick-cat-chip {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 12.5px;
      font-weight: 600;
      white-space: nowrap;
      cursor: pointer;
      transition: all var(--transition-fast);
      flex-shrink: 0;
    }

    .quick-cat-chip:hover {
      background: var(--bg-card-hover);
      color: var(--text-primary);
      border-color: var(--border-bold);
      transform: translateY(-1px);
    }

    .quick-cat-chip.active {
      background: var(--accent-blue);
      color: #ffffff;
      border-color: var(--accent-blue);
      box-shadow: 0 2px 10px var(--accent-blue-glow);
    }

    .quick-cat-chip .chip-count {
      background: rgba(255, 255, 255, 0.15);
      color: inherit;
      font-size: 11px;
      padding: 1px 7px;
      border-radius: var(--radius-full);
    }

    .active-filter-indicator {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(79, 140, 255, 0.1);
      border: 1px solid rgba(79, 140, 255, 0.3);
      padding: 8px 16px;
      border-radius: var(--radius-md);
      margin-top: 6px;
      margin-bottom: 6px;
      font-size: 13px;
      color: var(--text-primary);
    }

    .active-filter-tag {
      background: var(--accent-blue);
      color: #ffffff;
      padding: 2px 10px;
      border-radius: var(--radius-full);
      font-weight: 700;
      font-size: 12px;
    }

    .clear-filter-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--text-primary);
      padding: 4px 12px;
      border-radius: var(--radius-sm);
      font-size: 11.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all var(--transition-fast);
    }

    .clear-filter-btn:hover {
      background: rgba(239, 68, 68, 0.2);
      border-color: #ef4444;
      color: #fca5a5;
    }
'''

style_close = html.find('</style>')
if style_close == -1:
    print("Could not find </style>!")
    sys.exit(1)

html = html[:style_close] + css_to_add + "\n  " + html[style_close:]
print("CSS successfully added before </style>.")

# 2. Update explorer-header HTML
hdr_start = html.find('class="explorer-header"')
if hdr_start == -1:
    print("Could not find class='explorer-header'!")
    sys.exit(1)

hdr_end = html.find('<div class="questions-container"', hdr_start)
if hdr_end == -1:
    print("Could not find questions-container after explorer-header!")
    sys.exit(1)

new_explorer_header = r'''class="explorer-header">
          <div class="search-row">
            <div class="search-input-wrapper">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              <input type="text" id="searchInput" class="search-input" placeholder="Search 3,418+ questions: EF Core, C#, SQL, Async, Web API, React 19, RAG...">
              <span class="search-shortcut">/</span>
            </div>
            <button class="action-btn" id="randomQuestionBtn" title="Jump to Random Question">
              <span>🎲 Random</span>
            </button>
          </div>

          <!-- Quick Topic Filter Chips (All 25 Categories accessible with 1-click) -->
          <div class="quick-category-bar" id="quickCategoryBar">
            <!-- Populated by JavaScript -->
          </div>

          <!-- Active Filter Banner (Clear indicator when filtering by EF Core or any category) -->
          <div class="active-filter-indicator" id="activeFilterIndicator" style="display: none;">
            <div style="display:flex; align-items:center; gap:8px;">
              <span>Filtering by topic:</span>
              <span class="active-filter-tag" id="activeFilterTag">📦 EF Core 8/9 &amp; Dapper</span>
              <span style="color:var(--text-muted); font-size:12px;">(<span id="activeFilterCount">92</span> questions)</span>
            </div>
            <button class="clear-filter-btn" id="clearFilterBtn">✖ Clear Topic Filter</button>
          </div>

          <div class="stats-bar">
            <div>
              Showing <strong id="visibleQuestionsCount">0</strong> of <strong id="totalQuestionsCount">3,418</strong> questions
            </div>
            <div class="batch-actions">
              <button class="action-btn" id="expandAllBtn">Expand All</button>
              <button class="action-btn" id="collapseAllBtn">Collapse All</button>
            </div>
          </div>
        </div>

        <!-- Rendered Question Cards -->
        '''

html = html[:hdr_start] + new_explorer_header + html[hdr_end:]
print("explorer-header HTML replaced successfully.")

# 3. Update mockCategorySelect
mock_pos = html.find('id="mockCategorySelect"')
if mock_pos != -1:
    mock_opt_pos = html.find('<option value="all">', mock_pos)
    end_opt = html.find('</option>', mock_opt_pos) + len('</option>')
    new_opt = '<option value="all">Comprehensive Full-Stack .NET (3,418 Questions - All Tracks)</option>\n                <option value="efcore">📦 Entity Framework Core 8/9 & Dapper (92 Questions)</option>'
    html = html[:mock_opt_pos] + new_opt + html[end_opt:]
    print("mockCategorySelect options updated.")

# 4. Update JS logic: initCategoryNav & applyFilters
nav_start = html.find('function initCategoryNav() {')
if nav_start == -1:
    print("Could not find function initCategoryNav()!")
    sys.exit(1)

nav_end_marker = 'renderPagination();\n    }'
nav_end = html.find(nav_end_marker, nav_start) + len(nav_end_marker)

new_nav_and_filters = r'''function selectCategory(catKey) {
      activeCategory = catKey;
      currentPage = 1;

      // Update sidebar active buttons
      const navList = document.getElementById('categoryNavList');
      if (navList) {
        navList.querySelectorAll('.cat-btn').forEach(b => {
          b.classList.toggle('active', b.dataset.cat === catKey);
        });
      }

      // Update quick chips active buttons
      const quickBar = document.getElementById('quickCategoryBar');
      if (quickBar) {
        quickBar.querySelectorAll('.quick-cat-chip').forEach(c => {
          c.classList.toggle('active', c.dataset.cat === catKey);
        });
      }

      // Update active filter banner
      const banner = document.getElementById('activeFilterIndicator');
      const tag = document.getElementById('activeFilterTag');
      const countSpan = document.getElementById('activeFilterCount');

      if (banner && tag && countSpan) {
        if (catKey === 'all') {
          banner.style.display = 'none';
        } else {
          banner.style.display = 'flex';
          tag.textContent = categoryLabelsMap[catKey] || catKey.toUpperCase();
          const count = QUESTION_BANK.filter(q => q.category === catKey).length;
          countSpan.textContent = count.toLocaleString();
        }
      }

      applyFilters();

      // Update URL hash without reload
      if (catKey === 'all') {
        history.replaceState(null, null, ' ');
      } else {
        history.replaceState(null, null, `#${catKey}`);
      }

      // Scroll questions into view if below fold
      const explorer = document.getElementById('viewExplorer');
      if (explorer) {
        explorer.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    const categoryLabelsMap = {
      all: 'All Categories',
      efcore: '📦 EF Core 8/9 & Dapper',
      csharp: '⚡ C# 1-13 & Advanced C#',
      sql: '🗄️ SQL Server & Database Tuning',
      webapi: '🌐 ASP.NET Core Web API & REST',
      'dotnet-ai': '🤖 AI & Machine Learning in .NET',
      async: '⏱️ Async, Threading & Concurrency',
      oop: '🧩 OOP & SOLID Concepts',
      react: '⚛️ React 19 Fundamentals & Hooks',
      linq: '🔍 LINQ & High-Performance Collections',
      performance: '🚀 Performance & Memory Diagnostics',
      architecture: '🏛️ Architecture & Microservices',
      testing: '🧪 Unit Testing & Testcontainers',
      security: '🛡️ Security, OAuth & Zero-Trust',
      cloud: '☁️ Cloud Engineering (AWS & Azure)',
      mvc: '🖥️ ASP.NET Core MVC & Blazor',
      redux: '🔄 Redux & State Management',
      js: '📜 JavaScript & Modern TypeScript',
      coding: '💻 C# Coding & Algorithms',
      patterns: '📐 Design Patterns (GoF & Enterprise)',
      sdlc: '📋 SDLC, Agile & DevOps Culture',
      aws: '☁️ AWS Cloud Architecture',
      dotnet: '⚙️ .NET Core & Runtime Internals',
      lld: '⚙️ Low-Level System Design (LLD)',
      hld: '🗺️ High-Level System Design (HLD)',
      regex: '🎯 Regular Expressions'
    };

    function initCategoryNav() {
      const navList = document.getElementById('categoryNavList');
      const catCounts = {};
      QUESTION_BANK.forEach(q => {
        catCounts[q.category] = (catCounts[q.category] || 0) + 1;
      });

      // Logical curriculum tracks in progressive learning order
      const categoryTracks = [
        {
          title: "Core .NET & Runtime",
          items: [
            { key: 'oop', label: '🧩 OOP & SOLID Concepts' },
            { key: 'csharp', label: '⚡ C# 1-13 & Advanced C#' },
            { key: 'dotnet', label: '⚙️ .NET Core & Runtime Internals' },
            { key: 'performance', label: '🚀 Performance & Memory Diagnostics' },
            { key: 'async', label: '⏱️ Async, Threading & Concurrency' },
            { key: 'linq', label: '🔍 LINQ & High-Performance Collections' }
          ]
        },
        {
          title: "Backend, Web APIs & Data",
          items: [
            { key: 'efcore', label: '📦 EF Core 8/9 & Dapper' },
            { key: 'webapi', label: '🌐 ASP.NET Core Web API & REST' },
            { key: 'sql', label: '🗄️ SQL Server & Database Tuning' },
            { key: 'mvc', label: '🖥️ ASP.NET Core MVC & Blazor' }
          ]
        },
        {
          title: "Software Design & Architecture",
          items: [
            { key: 'patterns', label: '📐 Design Patterns (GoF & Enterprise)' },
            { key: 'lld', label: '⚙️ Low-Level System Design (LLD)' },
            { key: 'hld', label: '🗺️ High-Level System Design (HLD)' },
            { key: 'architecture', label: '🏛️ Architecture & Microservices' }
          ]
        },
        {
          title: "Security, Testing & Cloud",
          items: [
            { key: 'security', label: '🛡️ Security, OAuth & Zero-Trust' },
            { key: 'testing', label: '🧪 Unit Testing & Testcontainers' },
            { key: 'cloud', label: '☁️ Cloud Engineering (AWS & Azure)' },
            { key: 'aws', label: '☁️ AWS Cloud Architecture' },
            { key: 'sdlc', label: '📋 SDLC, Agile & DevOps Culture' }
          ]
        },
        {
          title: "Frontend Full-Stack",
          items: [
            { key: 'js', label: '📜 JavaScript & Modern TypeScript' },
            { key: 'react', label: '⚛️ React 19 Fundamentals & Hooks' },
            { key: 'redux', label: '🔄 Redux & State Management' }
          ]
        },
        {
          title: "AI & Machine Learning Track",
          items: [
            { key: 'dotnet-ai', label: '🤖 AI & Machine Learning in .NET' }
          ]
        },
        {
          title: "Coding, Algorithms & Regex",
          items: [
            { key: 'coding', label: '💻 C# Coding & Algorithms' },
            { key: 'regex', label: '🎯 Regular Expressions' }
          ]
        }
      ];

      // Update category count label in sidebar
      const categoryHeader = document.querySelector('#appSidebar .sidebar-section-title span');
      if (categoryHeader) {
        categoryHeader.textContent = `Categories (${Object.keys(catCounts).length})`;
      }

      // Build Sidebar Categories HTML
      let sidebarHtml = `<button class="cat-btn ${activeCategory === 'all' ? 'active' : ''}" data-cat="all">
        <span>All Categories</span>
        <span class="cat-count">${QUESTION_BANK.length.toLocaleString()}</span>
      </button>`;

      categoryTracks.forEach(track => {
        const visibleItems = track.items.filter(it => (catCounts[it.key] || 0) > 0);
        if (visibleItems.length > 0) {
          sidebarHtml += `<div class="cat-group-header">${track.title}</div>`;
          visibleItems.forEach(it => {
            const count = catCounts[it.key] || 0;
            const isActive = activeCategory === it.key ? 'active' : '';
            sidebarHtml += `<button class="cat-btn ${isActive}" data-cat="${it.key}">
              <span style="overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${it.label}</span>
              <span class="cat-count">${count.toLocaleString()}</span>
            </button>`;
          });
        }
      });

      if (navList) {
        navList.innerHTML = sidebarHtml;
        navList.querySelectorAll('.cat-btn').forEach(btn => {
          btn.addEventListener('click', () => {
            selectCategory(btn.dataset.cat);
          });
        });
      }

      // Build Top Quick Category Filter Chips Bar
      const quickBar = document.getElementById('quickCategoryBar');
      if (quickBar) {
        let quickHtml = `<button class="quick-cat-chip ${activeCategory === 'all' ? 'active' : ''}" data-cat="all">
          <span>All</span>
          <span class="chip-count">${QUESTION_BANK.length.toLocaleString()}</span>
        </button>`;

        // Priority chips with EF Core right at the front!
        const chipOrder = [
          'efcore', 'csharp', 'sql', 'webapi', 'dotnet-ai', 'async', 'oop',
          'react', 'linq', 'performance', 'architecture', 'testing', 'security',
          'cloud', 'mvc', 'redux', 'js', 'coding', 'patterns', 'sdlc', 'aws',
          'dotnet', 'lld', 'hld', 'regex'
        ];

        chipOrder.forEach(k => {
          const count = catCounts[k] || 0;
          if (count > 0) {
            const label = categoryLabelsMap[k] || k.toUpperCase();
            const isActive = activeCategory === k ? 'active' : '';
            quickHtml += `<button class="quick-cat-chip ${isActive}" data-cat="${k}">
              <span>${label}</span>
              <span class="chip-count">${count.toLocaleString()}</span>
            </button>`;
          }
        });

        quickBar.innerHTML = quickHtml;
        quickBar.querySelectorAll('.quick-cat-chip').forEach(chip => {
          chip.addEventListener('click', () => {
            selectCategory(chip.dataset.cat);
          });
        });
      }

      // Clear filter button in active banner
      const clearBtn = document.getElementById('clearFilterBtn');
      if (clearBtn) {
        clearBtn.addEventListener('click', () => selectCategory('all'));
      }

      // Clear filter button in sidebar
      const clearSidebarBtn = document.getElementById('clearCategoryBtn');
      if (clearSidebarBtn) {
        clearSidebarBtn.addEventListener('click', () => selectCategory('all'));
      }

      // Check URL Hash on initialization
      const initialHash = window.location.hash ? window.location.hash.slice(1).toLowerCase() : '';
      if (initialHash && catCounts[initialHash]) {
        selectCategory(initialHash);
      }
    }

    // ==========================================================================
    // Filter & Search Engine with Smart Alias & Normalization
    // ==========================================================================
    function applyFilters() {
      const query = searchQuery.trim().toLowerCase();
      const qCompact = query.replace(/[\s\-_#\.]/g, '');

      filteredQuestions = QUESTION_BANK.filter(q => {
        // Category filter
        if (activeCategory !== 'all' && q.category !== activeCategory) return false;

        // Difficulty filter
        if (activeDifficulty !== 'all' && q.difficulty !== activeDifficulty) return false;

        // Type filter
        if (activeType !== 'all' && q.type !== activeType) return false;

        // Status filter
        if (activeStatus === 'diagram' && !q.diagram) return false;
        if (activeStatus === 'mastered' && !userState.mastered.includes(q.id)) return false;
        if (activeStatus === 'revision' && !userState.revision.includes(q.id)) return false;
        if (activeStatus === 'bookmarked' && !userState.bookmarks.includes(q.id)) return false;

        // Search query filter with smart normalizations
        if (query) {
          const matchText = (
            (q.category || '') + ' ' + 
            (q.categoryLabel || '') + ' ' + 
            (q.q || '') + ' ' + 
            (q.answer || '') + ' ' + 
            (q.explanation || '') + ' ' + 
            (q.example || '') + ' ' + 
            (q.code || '') + ' ' + 
            (q.seniorInsight || '') + ' ' +
            (q.diagramTitle || '') + ' ' +
            ((q.tags || []).join(' '))
          ).toLowerCase();
          const textCompact = matchText.replace(/[\s\-_#\.]/g, '');

          let isMatch = matchText.includes(query) || textCompact.includes(qCompact);

          if (!isMatch) {
            // Synonyms & developer shortcuts
            if ((qCompact === 'efcore' || qCompact === 'ef' || qCompact === 'entityframework') && 
                (q.category === 'efcore' || textCompact.includes('entityframework') || textCompact.includes('dbcontext') || textCompact.includes('efcore'))) {
              isMatch = true;
            } else if ((qCompact === 'csharp' || qCompact === 'c') && 
                (q.category === 'csharp' || textCompact.includes('csharp'))) {
              isMatch = true;
            } else if ((qCompact === 'dotnet' || qCompact === 'net') && 
                (q.category === 'dotnet' || textCompact.includes('dotnet'))) {
              isMatch = true;
            } else if (qCompact === 'js' && 
                (q.category === 'js' || textCompact.includes('javascript'))) {
              isMatch = true;
            }
          }

          if (!isMatch) return false;
        }

        return true;
      });

      renderQuestions();
      renderPagination();
    }'''

html = html[:nav_start] + new_nav_and_filters + html[nav_end:]
print("initCategoryNav and applyFilters replaced successfully.")

# 5. Update Mock interview generator pool logic
old_mock_pool = r'''      let pool = QUESTION_BANK;
      if (focus === 'dotnet_ai') {
        pool = QUESTION_BANK.filter(q => q.category === 'dotnet-ai');
      } else if (focus === 'csharp_dotnet') {
        pool = QUESTION_BANK.filter(q => ['csharp', 'dotnet', 'performance', 'async', 'oop', 'linq', 'coding'].includes(q.category));
      } else if (focus === 'webapi_ef') {
        pool = QUESTION_BANK.filter(q => ['webapi', 'efcore', 'mvc'].includes(q.category));'''

new_mock_pool = r'''      let pool = QUESTION_BANK;
      if (focus === 'efcore') {
        pool = QUESTION_BANK.filter(q => q.category === 'efcore');
      } else if (focus === 'dotnet_ai') {
        pool = QUESTION_BANK.filter(q => q.category === 'dotnet-ai');
      } else if (focus === 'csharp_dotnet') {
        pool = QUESTION_BANK.filter(q => ['csharp', 'dotnet', 'performance', 'async', 'oop', 'linq', 'coding'].includes(q.category));
      } else if (focus === 'webapi_ef') {
        pool = QUESTION_BANK.filter(q => ['webapi', 'efcore', 'mvc'].includes(q.category));'''

if old_mock_pool in html:
    html = html.replace(old_mock_pool, new_mock_pool)
    print("Mock interview pool updated with focus === 'efcore'.")

# Write output file
with open('senior-dotnet-interview-portal.html', 'w', encoding='utf-8') as f:
    f.write(html)

size_mb = os.path.getsize('senior-dotnet-interview-portal.html') / (1024 * 1024)
print(f"Successfully saved senior-dotnet-interview-portal.html ({size_mb:.2f} MB)")

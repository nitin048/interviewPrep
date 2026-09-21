import re

target_file = 'senior-dotnet-interview-portal.html'
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """function applyFilters() {
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

      renderQuestions();"""

new_block = """function applyFilters() {
      const rawQuery = searchQuery.trim().toLowerCase();
      const expandedQuery = rawQuery
        .replace(/c#/g, 'csharp')
        .replace(/\.net/g, 'dotnet');
      const qCompact = expandedQuery.replace(/[\s\-_#\.]/g, '');

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
            // Synonyms & developer shortcuts
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

      renderQuestions();"""

if old_block in content:
    content = content.replace(old_block, new_block, 1)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Updated applyFilters() in senior-dotnet-interview-portal.html")
else:
    print("ERROR: old_block not found in content!")

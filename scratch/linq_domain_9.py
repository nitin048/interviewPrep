"""
LINQ Domain 9: LINQ to SQL & EF Core Translation Gotchas (Questions 3499 to 3508)
"""
from scratch.linq_domains_1_to_5 import make_explanation

def get_domain_9():
    qs = []

    # Q3499
    qs.append({
        "id": 3499,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "architecture",
        "q": "Client vs Server Evaluation in EF Core: Preventing Silent Query Fallback Disasters",
        "answer": "**In Plain English:** Server evaluation is asking the supermarket butcher to slice and package 1 lb of ham for you before putting it in your cart. Client evaluation is loading the entire 200 lb live pig into your minivan, driving it home, and butchering it on your kitchen table just to get 1 lb of ham.\n\n**Interview Answer:** In EF Core, LINQ queries can be evaluated on the **Server** (translated into SQL and executed by the database engine) or on the **Client** (rows fetched over the network and filtered in CLR memory). In EF Core 2.x, un-translatable C# methods silently fell back to client evaluation, causing catastrophic memory spikes and downloading millions of rows. Since EF Core 3.0, EF Core strictly **throws an `InvalidOperationException`** if a `Where` clause cannot be translated to SQL, permitting client evaluation only in the final top-level `.Select()` projection.",
        "concept": "EF Core strictly requires `Where` clauses to translate to SQL; client evaluation is restricted exclusively to final `Select` projections.",
        "howItWorks": "EF Core's `QueryCompilationContext` visits the Expression Tree. If an expression cannot be mapped to an `ISqlExpression` (e.g. calling a custom C# helper method `MyCustomFilter(x)` inside `.Where()`), compilation fails with `InvalidOperationException: The LINQ expression could not be translated`.",
        "whyWhen": "Crucial for avoiding catastrophic database performance failures in enterprise web APIs and batch jobs.",
        "example": "Calling `.Where(u => CalculateAge(u.DateOfBirth) > 21)`: in EF Core 2.x it downloaded the entire Users table; in EF Core 3+ it fails fast at runtime.",
        "code": "// 1. RUNTIME TRANSLATION FAILURE (Throws InvalidOperationException!):\n// EF Core cannot translate custom C# method 'CalculateTax' into SQL:\n// var badQuery = await db.Orders.Where(o => CalculateTax(o.Total) > 50).ToListAsync();\n\n// 2. CORRECT SERVER EVALUATION (Uses SQL primitives):\nvar goodQuery = await db.Orders\n    .Where(o => (o.Total * 0.15m) > 50) // Translates to SQL: WHERE ([o].[Total] * 0.15) > 50\n    .ToListAsync();\n\n// 3. EXPLICIT CLIENT EVALUATION IN FINAL PROJECTION (Supported & Safe):\nvar clientProjection = await db.Orders\n    .Where(o => o.Total > 500) // Filtered on Server in SQL!\n    .Select(o => new \n    {\n        o.Id,\n        o.Total,\n        // Client-side C# method runs ONLY on the filtered result set in memory:\n        FormattedDisplay = FormatOrderSummary(o)\n    })\n    .ToListAsync();",
        "codeLang": "csharp",
        "pros": [
            "Fail-fast behavior prevents accidental multi-gigabyte data transfers over database connections",
            "Clear architectural separation between database filtering and CLR presentation formatting"
        ],
        "cons": [
            "Developers cannot use complex custom C# domain methods directly inside `Where()` or `OrderBy()`",
            "Requires splitting queries or explicitly calling `.AsEnumerable()` when client logic is mandatory"
        ],
        "followups": [
            "Why did the EF Core team decide to break backward compatibility in EF Core 3.0 regarding client evaluation?",
            "How does `AsEnumerable()` establish an explicit boundary between server and client evaluation?"
        ],
        "seniorInsight": "To apply custom C# business logic that cannot be translated to SQL, make the boundary EXPLICIT using `.AsEnumerable()`! Everything *before* `.AsEnumerable()` runs in SQL on the database server; everything *after* `.AsEnumerable()` runs in C# memory on the client. Never fetch more rows than necessary before calling `.AsEnumerable()`.",
        "diagramTitle": "EF Core Server Evaluation vs Client Evaluation Boundary",
        "diagramSteps": [
            ["LINQ_QUERY", "LINQ Query Expression", "query = db.Orders.Where(filter).Select(projection)", "Expression Prepared"],
            ["SQL_TRANSLATION", "Relational AST Visitor", "EF Core translates Where clause into parameterized SQL WHERE statement", "SQL AST Built"],
            ["SERVER_EXEC", "Database Server Execution", "SQL Server filters 10,000,000 rows down to 50 matching rows via index", "Server Filtered"],
            ["DATA_TRANSFER", "Network TDS Transfer", "Transmits ONLY 50 filtered rows across network to application server", "Minimal Network IO"],
            ["CLIENT_PROJ", "Client Evaluation in Select", "CLR executes C# FormatOrderSummary() on the 50 materialized rows", "Clean Architecture"]
        ],
        "diagramArchetype": "pipeline",
        "explanation": make_explanation(
            "Client vs Server Evaluation Architecture",
            "In EF Core 2.x, silent client evaluation was considered the #1 cause of performance outages. A developer would add a harmless C# method to `.Where()`, and EF Core would silently fetch the entire table over the network.",
            "In modern EF Core, the translation pipeline strictly partitions expressions into server-translatable nodes and client-evaluated projections.",
            "// Explicit Server-to-Client Boundary Idiom:\nvar results = db.Orders\n    .Where(o => o.Status == \"Shipped\") // Server Evaluation (SQL)\n    .AsEnumerable()                      // Explicit Boundary Switch!\n    .Where(o => ComplexRegex(o.Notes))  // Client Evaluation (C# Memory)\n    .ToList();",
            "Never call `.AsEnumerable()` before your database filters, or the database will perform an unfiltered full-table scan.",
            "Server-side evaluation completes in ~2 ms via index seeks; client-side full table scans take minutes."
        )
    })

    # Q3500
    qs.append({
        "id": 3500,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "SQL IN Clause Translation in EF Core: Parameter Limits, OPENJSON, and EF.Functions.Contains",
        "answer": "**In Plain English:** Checking if an ID is in a list of 5 items is like asking: 'Is your shirt red, blue, green, yellow, or black?' But if you have 10,000 IDs, asking a 10,000-item question overwhelms SQL Server with too many parameters. Modern EF Core packages the 10,000 IDs into a single compact JSON suitcase and lets SQL unpack it in one shot.\n\n**Interview Answer:** In LINQ, `.Where(x => idList.Contains(x.Id))` translates to a SQL `WHERE [x].[Id] IN (@p0, @p1, ...)` clause. In older EF Core versions or when `idList` contained thousands of elements, this generated thousands of individual SQL parameters, exceeding SQL Server's maximum limit of **2,100 parameters** and causing plan cache bloat. In modern EF Core 8 and 9, large collections are automatically translated using **`OPENJSON`** (in SQL Server) or `ANY(@p0)` (in PostgreSQL), passing the entire list as a single JSON parameter and eliminating parameter limits.",
        "concept": "LINQ `.Contains()` translates to SQL `IN`; modern EF Core 8/9 optimizes large lists using `OPENJSON` to avoid parameter limits.",
        "howItWorks": "In EF Core 8+, if `idList` is large, EF Core serializes it to JSON and emits `WHERE [x].[Id] IN (SELECT [value] FROM OPENJSON(@__ids_0))`. This requires exactly 1 SQL parameter, reuses a single cached query execution plan, and easily scales to tens of thousands of IDs.",
        "whyWhen": "Essential when querying entities matching large batches of external keys (e.g. bulk order processing, multi-entity reconciliation).",
        "example": "Querying products matching 5,000 incoming SKU strings from an ERP sync job.",
        "code": "List<int> targetIds = GetTargetCustomerIds(); // 5,000 customer IDs\n\n// 1. LINQ QUERY (Translates automatically in EF Core 8/9):\nvar customers = await dbContext.Customers\n    .Where(c => targetIds.Contains(c.Id)) // SQL Server 2016+ uses OPENJSON!\n    .ToListAsync();\n\n// 2. GENERATED SQL IN EF CORE 8/9 (Notice single @__p_0 parameter!):\n// SELECT [c].[Id], [c].[Name], [c].[Email]\n// FROM [Customers] AS [c]\n// WHERE [c].[Id] IN (\n//     SELECT [v].[value]\n//     FROM OPENJSON(@__p_0) WITH ([value] int '$') AS [v]\n// )\n\n// 3. MANUAL CHUNKING FALLBACK (For older EF Core / databases without JSON):\nvar results = new List<Customer>();\nforeach (var chunk in targetIds.Chunk(1000))\n{\n    var batch = await dbContext.Customers.Where(c => chunk.Contains(c.Id)).ToListAsync();\n    results.AddRange(batch);\n}",
        "codeLang": "csharp",
        "pros": [
            "Eliminates SQL Server's 2,100 parameter limit exception (`SqlException: Too many parameters`)",
            "Prevents Plan Cache pollution by reusing a single parameterized SQL query plan"
        ],
        "cons": [
            "Older database compatibility levels (< SQL Server 2016) do not support `OPENJSON`",
            "Very large JSON strings (>10 MB) can incur JSON deserialization CPU costs on the database server"
        ],
        "followups": [
            "Why did the old EF Core parameter expansion pattern (`@p0, @p1, ...`) pollute the SQL Server Plan Cache?",
            "How does PostgreSQL translate LINQ `.Contains()` using the `ANY(@p0)` array operator?"
        ],
        "seniorInsight": "In EF Core 6 and 7, every unique list length (e.g. searching 3 IDs vs 4 IDs) generated a brand-new SQL string with a different number of parameters, flooding SQL Server's Plan Cache with thousands of redundant execution plans! EF Core 8/9's `OPENJSON` feature generates a SINGLE consistent query plan regardless of how many IDs are passed.",
        "diagramTitle": "EF Core SQL IN Clause: Parameter Expansion vs OPENJSON",
        "diagramSteps": [
            ["INPUT_LIST", "5,000 Target IDs", "Client provides list of 5,000 customer IDs to match in database", "5,000 IDs Loaded"],
            ["OLD_EF_FAIL", "Old EF Core (>2100 Limit)", "Emits IN (@p0, @p1... @p4999): crashes with SQL 2,100 parameter error!", "Parameter Limit Crash"],
            ["EF8_OPENJSON", "Modern EF Core 8/9 OPENJSON", "Serializes IDs to JSON string: passes exactly 1 SQL parameter @__p_0", "1 Parameter Passed"],
            ["SQL_SERVER", "OPENJSON Table Value", "SQL Server table-valued function unpacks JSON array in-memory", "TVF Execution"],
            ["INDEX_SEEK", "Semi-Join Index Seek", "Executes semi-join against clustered primary key: returns 5,000 rows in 4ms", "Blazing SQL Speed"]
        ],
        "diagramArchetype": "sql",
        "explanation": make_explanation(
            "SQL IN & OPENJSON Mechanics",
            "SQL Server historically capped parameters at 2,100 per statement. Exceeding this threw `SqlException: The incoming request has too many parameters`.",
            "EF Core 8 introduced the `AzureSynapseRelationalTypeMappingSource` and relational JSON array mappings, revolutionizing how `.Contains()` translates to SQL.",
            "// Checking Compatibility Level in SQL Server:\n// OPENJSON requires database compatibility level >= 130 (SQL Server 2016+)\n// ALTER DATABASE CurrentDb SET COMPATIBILITY_LEVEL = 150;",
            "If using older database engines, manually chunk IDs using `.Chunk(1000)` to stay safely below the 2,100 parameter ceiling.",
            "Querying 5,000 IDs via `OPENJSON` executes in ~4.5 ms and reuses cached execution plans."
        )
    })

    # Q3501
    qs.append({
        "id": 3501,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "intermediate",
        "type": "code",
        "q": "Date and Time Query Translation: DateTime.UtcNow vs EF.Functions.DateDiffDay in LINQ",
        "answer": "**In Plain English:** If you want to find all orders placed in the last 7 days, calculating `DateTime.UtcNow.AddDays(-7)` in C# sends a single fixed timestamp (a constant) to SQL Server so the database index works at full speed. Calling `DateDiff(d, o.OrderDate, GetDate()) <= 7` forces SQL Server to calculate math on every single row in the entire table, destroying index performance.\n\n**Interview Answer:** When querying dates in LINQ with EF Core, performance depends on whether date calculations are **sargable** (Search Argument Able). Evaluating cutoff dates in C# before query execution (e.g. `DateTime cutoff = DateTime.UtcNow.AddDays(-7); query.Where(o => o.OrderDate >= cutoff);`) sends a pre-computed constant parameter, allowing SQL Server to perform an efficient **Index Seek**. In contrast, calling `EF.Functions.DateDiffDay(o.OrderDate, DateTime.UtcNow) <= 7` wraps the database column in a function, preventing index seeks and forcing an expensive **Index Scan** across the entire table.",
        "concept": "Pre-computing dates in C# preserves sargability (Index Seek); wrapping columns in `DateDiff` forces non-sargable Index Scans.",
        "howItWorks": "When a column is bare (`o.OrderDate >= @cutoff`), SQL Server traverses its B-Tree index directly to the boundary. When a column is wrapped in a function (`DATEDIFF(day, o.OrderDate, ...) <= 7`), SQL Server cannot know which rows match without executing the function on every single row in the table.",
        "whyWhen": "Essential in every time-series query, active user filters, expiring subscription checks, and audit log date ranges.",
        "example": "Filtering 10,000,000 orders for last week's data: sargable constant query takes 1.2 ms; `DateDiffDay` takes 4,500 ms.",
        "code": "// 1. SARGABLE (BEST PERFORMANCE - Index Seek):\nDateTime cutoff = DateTime.UtcNow.AddDays(-7);\n\nvar fastQuery = await dbContext.Orders\n    .Where(o => o.OrderDate >= cutoff) // Translates to: WHERE [o].[OrderDate] >= @cutoff\n    .ToListAsync(); // Instant Clustered / Non-Clustered Index Seek!\n\n// 2. NON-SARGABLE ANTI-PATTERN (SLOW - Full Table / Index Scan):\nvar slowQuery = await dbContext.Orders\n    // Column wrapped in function! SQL Server must scan ALL rows:\n    .Where(o => EF.Functions.DateDiffDay(o.OrderDate, DateTime.UtcNow) <= 7)\n    .ToListAsync(); // Translates to: WHERE DATEDIFF(day, [o].[OrderDate], GETUTCDATE()) <= 7",
        "codeLang": "csharp",
        "pros": [
            "Enables instant B-Tree index seeks on indexed `DateTime` and `DateTimeOffset` columns",
            "Eliminates database CPU overhead by evaluating date math once on the web server"
        ],
        "cons": [
            "`DateTime.Now` vs `DateTime.UtcNow` discrepancies can cause timezone bugs if entities store UTC",
            "Does not account for boundary edge cases (midnight cutoffs) unless formatted with `.Date`"
        ],
        "followups": [
            "What does 'Sargable' mean in relational database query optimization?",
            "How does `DateTimeOffset` provide superior timezone safety over `DateTime` in enterprise databases?"
        ],
        "seniorInsight": "NEVER wrap database columns inside functions in LINQ `Where` clauses! Writing `o.OrderDate.Year == 2024` or `EF.Functions.DateDiffDay(o.OrderDate, ...) <= 7` destroys index seeks and forces SQL Server to perform an Index Scan across 100% of rows. Always rewrite queries to isolate the column: `o.OrderDate >= new DateTime(2024, 1, 1) && o.OrderDate < new DateTime(2025, 1, 1)`.",
        "diagramTitle": "Sargable Index Seek vs Non-Sargable Function Scan",
        "diagramSteps": [
            ["QUERY_PARAM", "Pre-Computed Date Parameter", "C# pre-computes cutoff = DateTime.UtcNow.AddDays(-7)", "Param Ready"],
            ["SARGABLE_SQL", "Sargable SQL: WHERE OrderDate >= @cutoff", "Column is isolated: SQL Server B-Tree index seeks directly to cutoff", "Index Seek (1ms)"],
            ["SCAN_DANGER", "Non-Sargable: DATEDIFF(day, OrderDate)", "Column wrapped in DATEDIFF function: index seek is impossible!", "Non-Sargable"],
            ["FULL_SCAN", "Full Table Scan", "SQL Server executes DATEDIFF() on 10,000,000 rows: 4,500ms CPU burn", "100% Scan"],
            ["SLA_RESULT", "Performance Divergence", "Sargable query runs in 1.2ms (3,700x faster than DateDiff scan)", "Index Seek Win"]
        ],
        "diagramArchetype": "btree",
        "explanation": make_explanation(
            "Date Sargability & SQL Optimization",
            "SARGable stands for Search Argument Able. A query predicate is sargable if the query optimizer can leverage an index seek to satisfy the predicate.",
            "Wrapping an indexed column in ANY function—`YEAR()`, `MONTH()`, `DATEDIFF()`, `SUBSTRING()`, or `CONVERT()`—breaks sargability.",
            "// Sargable Year Query Pattern:\n// BAD:  .Where(o => o.OrderDate.Year == 2024)\n// GOOD: var start = new DateTime(2024, 1, 1); var end = new DateTime(2025, 1, 1);\n//       .Where(o => o.OrderDate >= start && o.OrderDate < end)",
            "Always store dates in UTC (`DateTimeOffset` or `DateTime` with `DateTimeKind.Utc`) to prevent daylight saving and timezone anomalies.",
            "An index seek on a 10-million row table takes ~1.2 ms; a non-sargable scan takes ~4.5 seconds."
        )
    })

    # Q3502
    qs.append({
        "id": 3502,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "String Collation and Comparison in LINQ: Case-Sensitivity and EF.Functions.Collate",
        "answer": "**In Plain English:** In C#, `'admin'` and `'Admin'` are completely different strings because C# is case-sensitive by default. But in SQL Server, the database might treat `'admin'` and `'Admin'` as the exact same word because the database has a case-insensitive collation (`CI`). `EF.Functions.Collate` lets you explicitly force the database to be case-sensitive or case-insensitive for a specific query.\n\n**Interview Answer:** C# in-memory string comparisons default to case-sensitive ordinal (`StringComparison.Ordinal`). In contrast, SQL Server databases typically default to case-insensitive collations (e.g. `SQL_Latin1_General_CP1_CI_AS`, where `CI` means Case-Insensitive). As a result, `db.Users.Where(u => u.Username == \"admin\")` will match `\"Admin\"` and `\"ADMIN\"` in SQL, but will NOT match if run in memory! To enforce exact casing in database queries, EF Core provides **`EF.Functions.Collate(column, collation)`**, allowing queries to override database collation at the query level.",
        "concept": "Database string comparisons depend on SQL collation; `EF.Functions.Collate` overrides collation rules inside LINQ queries.",
        "howItWorks": "Calling `EF.Functions.Collate(u.Username, \"SQL_Latin1_General_CP1_CS_AS\")` emits SQL `[u].[Username] COLLATE SQL_Latin1_General_CP1_CS_AS = @param`. The `CS` instructs SQL Server to perform an exact case-sensitive comparison.",
        "whyWhen": "Mandatory in password verification, API token lookup, case-sensitive promo codes, and linguistic sorting.",
        "example": "Validating case-sensitive API keys: `db.ApiKeys.Where(k => EF.Functions.Collate(k.Key, \"SQL_Latin1_General_CP1_CS_AS\") == inputKey)`.",
        "code": "// 1. CASE-SENSITIVE QUERY OVERRIDE (Forces Case-Sensitivity):\nstring searchCode = \"Promo2024X\";\n\nvar promo = await dbContext.PromoCodes\n    .Where(p => EF.Functions.Collate(\n        p.Code, \n        \"SQL_Latin1_General_CP1_CS_AS\") == searchCode) // CS = Case Sensitive!\n    .FirstOrDefaultAsync();\n    \n// Translates to:\n// WHERE [p].[Code] COLLATE SQL_Latin1_General_CP1_CS_AS = @searchCode\n\n// 2. CASE-INSENSITIVE QUERY ON CASE-SENSITIVE DATABASE (PostgreSQL / SQLite):\n// In PostgreSQL, queries are case-sensitive by default! Use EF.Functions.ILike:\nvar user = await dbContext.Users\n    .Where(u => EF.Functions.ILike(u.Email, searchEmail)) // ILike = Case Insensitive!\n    .FirstOrDefaultAsync();",
        "codeLang": "csharp",
        "pros": [
            "Guarantees deterministic security matching for API keys, tokens, and promo codes",
            "Allows overriding database-wide collation defaults on individual queries"
        ],
        "cons": [
            "Overriding collation in a `WHERE` clause can prevent SQL Server from using existing indexes",
            "Collation strings are database-specific (SQL Server collations differ from PostgreSQL and MySQL)"
        ],
        "followups": [
            "Why can applying `COLLATE` in a `WHERE` clause disable index seeks in SQL Server?",
            "How does PostgreSQL handle case-insensitivity using `citext` or `EF.Functions.ILike`?"
        ],
        "seniorInsight": "Applying `COLLATE` directly in a `WHERE` clause can cause SQL Server to perform an Index Scan because the collation differs from the index's native collation! If you need high-speed case-sensitive lookups on millions of rows, configure the column collation in `OnModelCreating`: `builder.Property(x => x.ApiKey).UseCollation(\"SQL_Latin1_General_CP1_CS_AS\")` so the B-Tree index is built with case-sensitivity natively.",
        "diagramTitle": "SQL Collation Case-Sensitivity Override in LINQ",
        "diagramSteps": [
            ["INPUT_SEARCH", "Input Search Token", "User searches for 'Promo2024X'; database contains 'promo2024x'", "Token Provided"],
            ["DEFAULT_SQL", "Default Collation (CI)", "Database default is CI (Case-Insensitive): matches 'promo2024x' (Incorrect!)", "False Match"],
            ["COLLATE_OP", "EF.Functions.Collate()", "LINQ injects explicit CS (Case-Sensitive) collation override", "Collate Injected"],
            ["SQL_COLLATE", "Native SQL COLLATE Clause", "WHERE [Code] COLLATE SQL_Latin1_General_CP1_CS_AS = @param", "SQL Executed"],
            ["EXACT_MATCH", "Strict Security Match", "Rejects mismatched casing: returns ONLY exact binary character match", "Zero False Match"]
        ],
        "diagramArchetype": "security",
        "explanation": make_explanation(
            "String Collation Mechanics",
            "A collation defines the rules for how string characters are sorted and compared, including Case Sensitivity (CS vs CI), Accent Sensitivity (AS vs AI), and Kana Sensitivity (KS vs KI).",
            "In C#, `string.Equals(a, b, StringComparison.OrdinalIgnoreCase)` cannot be translated by EF Core into SQL. EF Core relies on the database's collation for equality.",
            "// Fluent API Native Column Collation Configuration:\nprotected override void OnModelCreating(ModelBuilder modelBuilder) {\n    modelBuilder.Entity<ApiKey>()\n        .Property(a => a.Token)\n        .UseCollation(\"SQL_Latin1_General_CP1_CS_AS\"); // Index built case-sensitive!\n}",
            "In PostgreSQL, standard `==` is always case-sensitive; case-insensitivity requires `EF.Functions.ILike(u.Name, pattern)` or the `citext` extension.",
            "Collation overrides on indexed columns should be evaluated carefully to ensure index seek optimization is preserved."
        )
    })

    # Q3503
    qs.append({
        "id": 3503,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "conceptual",
        "q": "Three-Valued SQL Logic: Handling NULL Comparison Semantics in LINQ and EF Core",
        "answer": "**In Plain English:** In C#, boolean logic is binary: something is either `true` or `false`. In SQL databases, logic is three-valued: something can be `TRUE`, `FALSE`, or `UNKNOWN` (NULL). If you ask SQL: 'Is NULL equal to NULL?', SQL says 'UNKNOWN' and throws the row away!\n\n**Interview Answer:** In SQL databases, `NULL` represents the absence of a value. Under standard ANSI SQL semantics, comparisons with `NULL` evaluate to `UNKNOWN` (`NULL = NULL` is UNKNOWN, and `NULL <> NULL` is UNKNOWN). In contrast, C# uses two-valued logic where `null == null` is `true`. EF Core bridges this impedance mismatch by expanding equality comparisons to include null checks (e.g. `[a] = [b] OR ([a] IS NULL AND [b] IS NULL)`). This guarantees C#-like semantics, but can generate complex SQL predicates that degrade query performance unless configured.",
        "concept": "SQL uses three-valued logic (`TRUE`, `FALSE`, `UNKNOWN`); EF Core expands LINQ expressions to simulate C# two-valued null semantics.",
        "howItWorks": "When you write `.Where(x => x.NullableCol == param)`, if `param` can be null, EF Core translates this to `([x].[NullableCol] = @param) OR ([x].[NullableCol] IS NULL AND @param IS NULL)`. This prevents `UNKNOWN` from discarding valid matching null rows.",
        "whyWhen": "Essential when querying nullable foreign keys, optional customer attributes, and joining nullable columns.",
        "example": "Querying users where `x.MiddleName == targetMiddleName`: if both are null, C# expects a match; raw SQL would return nothing.",
        "code": "// 1. C# NULLABLE EQUALITY:\nstring? searchMiddleName = null;\n\n// EF Core expands the SQL to guarantee C# semantics:\nvar users = await dbContext.Users\n    .Where(u => u.MiddleName == searchMiddleName)\n    .ToListAsync();\n\n// GENERATED SQL (Simulating C# null equality):\n// SELECT [u].[Id], [u].[MiddleName]\n// FROM [Users] AS [u]\n// WHERE ([u].[MiddleName] = @searchMiddleName) \n//    OR ([u].[MiddleName] IS NULL AND @searchMiddleName IS NULL)\n\n// 2. DISABLING EXPANSION FOR RAW SQL SPEED (UseNullPropagation):\n// In DbContextOptions, UseRelationalNulls(false) produces simpler SQL \n// if you guarantee ANSI SQL semantics are acceptable.",
        "codeLang": "csharp",
        "pros": [
            "Maintains 100% semantic consistency between C# memory behavior and database SQL behavior",
            "Eliminates subtle bugs where null values disappear from query results"
        ],
        "cons": [
            "Generates verbose `OR ... IS NULL` SQL predicates that can complicate query execution plans",
            "Can cause index seeks to degrade to index scans on nullable columns"
        ],
        "followups": [
            "How does `UseRelationalNulls(true)` in EF Core configure pure ANSI SQL null semantics?",
            "Why does `NOT IN` with a subquery return zero rows in SQL if the subquery contains a single NULL value?"
        ],
        "seniorInsight": "Watch out for SQL `NOT IN` with NULLs! In SQL, `WHERE Id NOT IN (SELECT ParentId FROM Table)` returns ZERO rows if even a SINGLE `ParentId` in that table is NULL! Because `Id <> NULL` evaluates to `UNKNOWN`, the entire `AND` condition fails. In LINQ, always filter nulls: `.Where(t => t.ParentId != null)` or use `.Where(p => !subquery.Any(s => s.ParentId == p.Id))`.",
        "diagramTitle": "C# Two-Valued Logic vs SQL Three-Valued Logic",
        "diagramSteps": [
            ["C_SHARP_EVAL", "C# Two-Valued Logic", "null == null evaluates to TRUE; null != null evaluates to FALSE", "C# Binary Logic"],
            ["SQL_EVAL", "SQL Three-Valued Logic", "NULL = NULL evaluates to UNKNOWN; WHERE discards all UNKNOWN rows!", "SQL 3-Valued"],
            ["EF_EXPAND", "EF Core Null Expansion", "EF Core emits: ([Col] = @p) OR ([Col] IS NULL AND @p IS NULL)", "Semantic Bridge"],
            ["ANSI_OPT", "RelationalNulls Config", "UseRelationalNulls(true) strips expansion for raw ANSI SQL performance", "ANSI Mode"],
            ["INDEX_IMPACT", "Query Optimization", "Proper null handling ensures nullable foreign keys resolve correctly", "Deterministic SQL"]
        ],
        "diagramArchetype": "branch",
        "explanation": make_explanation(
            "Three-Valued Logic Mechanics",
            "The Three-Valued Logic (3VL) of SQL originates from E.F. Codd's relational model. The truth tables for AND, OR, and NOT must account for UNKNOWN.",
            "In SQL, `UNKNOWN AND TRUE` is UNKNOWN; `UNKNOWN OR TRUE` is TRUE; `NOT UNKNOWN` is UNKNOWN.",
            "// Enabling Pure Relational Null Semantics:\noptionsBuilder.UseSqlServer(connectionString, o => {\n    o.UseRelationalNulls(true); // Generates clean [Col] = @p without OR expansion!\n});",
            "Use `UseRelationalNulls(true)` only if your application code explicitly checks for nulls before issuing queries.",
            "Handling null expansion properly prevents data disappearance bugs in financial reports."
        )
    })

    # Q3504
    qs.append({
        "id": 3504,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "architecture",
        "q": "Subquery Translation in EF Core: Any() vs Count() > 0 and EXISTS vs COUNT(*) Performance",
        "answer": "**In Plain English:** If you want to check if a hotel has any empty rooms, `Any()` is looking in the lobby computer: the second it sees 1 available room, it immediately says 'Yes!' and stops. `Count() > 0` is forcing the manager to walk to all 500 rooms, count every single empty bed in the entire building, and then say 'Yes, there are 42 empty beds, which is greater than 0.'\n\n**Interview Answer:** In LINQ queries, checking for the existence of related child records must always be written using `.Any()` rather than `.Count() > 0`. In EF Core, `.Where(p => p.Orders.Any())` translates into SQL **`WHERE EXISTS (SELECT 1 FROM Orders WHERE ...)`**. The database storage engine halts execution the instant the first matching row is found in the index. In contrast, writing `.Where(p => p.Orders.Count() > 0)` translates into SQL `WHERE (SELECT COUNT(*) FROM Orders) > 0`, forcing the database to scan and count all matching rows, burning unnecessary disk I/O and CPU.",
        "concept": "`.Any()` translates to SQL `EXISTS` with instant early-termination; `.Count() > 0` forces an expensive full `COUNT(*)` aggregation.",
        "howItWorks": "SQL `EXISTS` returns `TRUE` as soon as a single index entry satisfies the predicate. `COUNT(*)` must traverse all matching entries across the index tree to calculate the total sum before evaluating the `> 0` comparison.",
        "whyWhen": "Mandatory across all database queries checking for related child records (e.g. customers with orders, blogs with posts, users with roles).",
        "example": "Finding all customers who placed orders: `Any()` takes 2 ms; `Count() > 0` takes 450 ms.",
        "code": "// 1. HIGH-PERFORMANCE: Translates to SQL EXISTS (Early-Halting):\nvar activeCustomers = await dbContext.Customers\n    .Where(c => c.Orders.Any(o => o.Total > 500))\n    .ToListAsync();\n\n// GENERATED SQL (Optimal Index Seek + Early Exit):\n// SELECT [c].[Id], [c].[Name]\n// FROM [Customers] AS [c]\n// WHERE EXISTS (\n//     SELECT 1 FROM [Orders] AS [o] \n//     WHERE [o].[CustomerId] = [c].[Id] AND [o].[Total] > 500\n// )\n\n// 2. ANTI-PATTERN (DO NOT USE!): Forces SQL COUNT(*)\nvar slowCustomers = await dbContext.Customers\n    .Where(c => c.Orders.Count(o => o.Total > 500) > 0) // Heavy subquery count!\n    .ToListAsync();",
        "codeLang": "csharp",
        "pros": [
            "SQL `EXISTS` achieves near-instant response times by stopping at the first match",
            "Eliminates table spooling and aggregation work on the database server"
        ],
        "cons": [
            "Cannot tell you HOW MANY items matched (only whether at least one exists)",
            "Deeply nested `Any()` checks across 4+ tables can generate complex correlated subqueries"
        ],
        "followups": [
            "How does SQL Server optimize `WHERE NOT EXISTS` compared to `WHERE ID NOT IN (...)`?",
            "What happens if you call `.All()` in a LINQ to Entities query?"
        ],
        "seniorInsight": "Flag `.Count() > 0` in code reviews as an immediate performance defect! On tables with millions of child rows (e.g. AuditLogs or Transactions), `Count() > 0` will count 500,000 rows just to verify existence. `.Any()` stops at row #1. The difference is 1 index read vs 500,000 index reads.",
        "diagramTitle": "SQL EXISTS Early Termination vs COUNT(*) Full Scan",
        "diagramSteps": [
            ["QUERY_CHECK", "Existence Query", "Query: Find customers who have placed an order over $500", "Query Dispatched"],
            ["EXISTS_BRANCH", "Any() -> SQL EXISTS", "SELECT 1 FROM Orders WHERE CustomerId = c.Id AND Total > 500", "EXISTS Path"],
            ["EARLY_STOP", "Index Seek Early Exit", "Finds 1st matching order in index: HALTS IMMEDIATELY! Returns TRUE", "2ms Response"],
            ["COUNT_BRANCH", "Count() > 0 -> COUNT(*)", "Scans all 100,000 orders for this customer to sum total count", "COUNT(*) Path"],
            ["RESOURCE_WASTE", "Heavy Aggregation Waste", "Counts 100,000 rows just to check if > 0: burns 450ms CPU time", "450ms CPU Waste"]
        ],
        "diagramArchetype": "sql",
        "explanation": make_explanation(
            "EXISTS vs COUNT Mechanics",
            "In relational algebra, semi-joins (`EXISTS`) return rows from the left table as soon as a match exists in the right table without duplicating left rows.",
            "SQL Server query optimizers treat `EXISTS` as a Semi-Join. It can use Left Semi Hash Joins or Index Seeks with Top(1) operators.",
            "// Translating .All() to SQL:\n// .Where(c => c.Orders.All(o => o.IsPaid))\n// Translates to: WHERE NOT EXISTS (SELECT 1 FROM Orders WHERE CustomerId = c.Id AND IsPaid = 0)",
            "`.All(predicate)` is translated using De Morgan's laws into `NOT EXISTS (WHERE NOT predicate)`.",
            "`EXISTS` executes in ~1-2 microseconds on indexed tables; `COUNT(*)` scales linearly with group size."
        )
    })

    # Q3505
    qs.append({
        "id": 3505,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Window Functions in EF Core: ROW_NUMBER(), DENSE_RANK(), and Partition Ranking in LINQ",
        "answer": "**In Plain English:** If you want to award 1st, 2nd, and 3rd place trophies to athletes in every different sport category, SQL window functions rank athletes within their specific sport without collapsing the roster. EF Core allows you to generate these window rankings directly from LINQ.\n\n**Interview Answer:** SQL Window Functions (`ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)`, `RANK()`, `DENSE_RANK()`) calculate aggregate and ranking values across sets of rows without grouping or collapsing rows into a single summary. In modern EF Core (EF Core 7, 8, and 9), LINQ queries using `GroupBy` followed by `Select` with indexed projections or `.Take(N)` automatically translate into native SQL `ROW_NUMBER() OVER (...)` statements. This enables server-side Top-N per group queries and ranked pagination directly from LINQ.",
        "concept": "Modern EF Core translates grouping with ranking into SQL window functions (`ROW_NUMBER() OVER PARTITION BY`).",
        "howItWorks": "When you write `db.Orders.GroupBy(o => o.CustomerId).SelectMany(g => g.OrderByDescending(o => o.Total).Take(3))`, EF Core 8/9 compiles this into a Common Table Expression (CTE) or subquery with `ROW_NUMBER() OVER (PARTITION BY [o].[CustomerId] ORDER BY [o].[Total] DESC) AS [row]`, filtering `WHERE [row] <= 3`.",
        "whyWhen": "Essential for Top-N per category queries, paginated leaderboard rankings, calculating moving averages in SQL, and deduplicating records by partition.",
        "example": "Finding the 2 highest-value orders for every customer in the database.",
        "code": "// 1. LINQ QUERY FOR TOP 2 ORDERS PER CUSTOMER:\nvar topOrders = await dbContext.Customers\n    .SelectMany(c => c.Orders\n        .OrderByDescending(o => o.Total)\n        .Take(2)) // Top 2 per customer!\n    .ToListAsync();\n\n// 2. GENERATED SQL IN EF CORE 8/9 (Native Window Function):\n// SELECT [t0].[Id], [t0].[CustomerId], [t0].[Total]\n// FROM (\n//     SELECT [o].[Id], [o].[CustomerId], [o].[Total],\n//            ROW_NUMBER() OVER(\n//                PARTITION BY [o].[CustomerId] \n//                ORDER BY [o].[Total] DESC) AS [row]\n//     FROM [Orders] AS [o]\n// ) AS [t0]\n// WHERE [t0].[row] <= 2",
        "codeLang": "csharp",
        "pros": [
            "Executes complex dimensional ranking directly on the database engine in a single query",
            "Eliminates N+1 database queries when fetching child records per parent"
        ],
        "cons": [
            "In older EF Core versions (< EF Core 7), this pattern triggered client evaluation warnings or multiple queries",
            "Complex window functions with running frames (`ROWS BETWEEN`) require raw SQL"
        ],
        "followups": [
            "What is the difference between `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()` when items have identical values?",
            "How does SQL Server optimize `ROW_NUMBER() OVER (PARTITION BY ...)` using Stream Aggregate?"
        ],
        "seniorInsight": "Prior to EF Core 7, fetching Top-N items per group required authoring raw SQL or executing N separate queries (N+1 disaster). Modern EF Core 8 and 9 translate `SelectMany` with `Take(N)` into native `ROW_NUMBER() OVER (PARTITION BY ...)` automatically. Make sure your database project targets EF Core 8+ to benefit from this major optimization.",
        "diagramTitle": "EF Core Window Function ROW_NUMBER() Translation",
        "diagramSteps": [
            ["LINQ_CALL", "LINQ Top-N Per Group", "c.Orders.OrderByDescending(o => o.Total).Take(2)", "Query Formed"],
            ["EF_TRANSLATE", "Window Function Compiler", "EF Core detects partition ranking: synthesizes ROW_NUMBER() OVER", "SQL Synthesized"],
            ["SQL_CTE", "Subquery with Partition", "PARTITION BY CustomerId ORDER BY Total DESC assigns rank [row]", "Partition Ranked"],
            ["WHERE_FILTER", "Rank Filter WHERE row <= 2", "Filters subquery for [row] <= 2: discards lower-ranked child orders", "Filtered to Top 2"],
            ["RESULT_SET", "Single Database Roundtrip", "Returns exact Top 2 orders per customer in 1 fast database roundtrip", "Optimal SQL"]
        ],
        "diagramArchetype": "sql",
        "explanation": make_explanation(
            "Window Functions in Modern EF Core",
            "Window functions perform calculations across a set of table rows that are somehow related to the current row, without grouping them into a single row output.",
            "The `PARTITION BY` clause divides rows into groups (similar to `GROUP BY`), and the window function runs over each partition independently.",
            "// Difference between ranking functions:\n// ROW_NUMBER: 1, 2, 3, 4 (Strict sequential)\n// RANK:       1, 2, 2, 4 (Ties share rank, leaves gap)\n// DENSE_RANK: 1, 2, 2, 3 (Ties share rank, no gaps)",
            "If raw window functions like `LEAD()` or `LAG()` are required, use `FromSqlInterpolated`.",
            "Window functions execute in ~5-15 ms on indexed database tables."
        )
    })

    # Q3506
    qs.append({
        "id": 3506,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Full-Text Search Integration in EF Core: EF.Functions.FreeText and Contains Full-Text Indexes",
        "answer": "**In Plain English:** Using LINQ `o.Notes.Contains(\"clean\")` is like flipping through every single page of a 1,000-page book looking for the word 'clean' (slow table scan). Full-Text Search is looking in the printed index at the very back of the book: it immediately tells you that 'clean' is on pages 12, 45, and 89, and it also understands related words like 'cleaning' and 'cleansed'.\n\n**Interview Answer:** In standard LINQ, `string.Contains(\"text\")` translates to SQL `LIKE '%text%'`. Because of the leading wildcard (`%`), SQL Server cannot use a B-Tree index, forcing a non-sargable full table scan. To perform high-speed textual searching, SQL Server provides Full-Text Search (FTS). In EF Core, this is integrated via **`EF.Functions.Contains(column, searchPattern)`** and **`EF.Functions.FreeText(column, searchPattern)`**. These operators translate directly into SQL `CONTAINS` and `FREETEXT`, leveraging the database's inverted full-text index with linguistic stemming, thesaurus matching, and sub-millisecond execution.",
        "concept": "`EF.Functions.Contains` and `FreeText` leverage database Full-Text Indexes for rapid text searching with linguistic stemming.",
        "howItWorks": "SQL Server builds an inverted index over full-text indexed columns. `EF.Functions.FreeText(e.Bio, \"run\")` searches for linguistic variations ('running', 'ran', 'runner'). `EF.Functions.Contains(e.Bio, \"\\\"senior developer\\\"\")` searches for exact phrases or boolean terms (`AND`, `OR`, `NEAR`).",
        "whyWhen": "Essential in document search portals, product catalog searches, knowledgebase articles, and job boards searching millions of resumes.",
        "example": "Searching 10,000,000 customer reviews for mentions of 'battery drain': `FreeText` returns in 3 ms; `LIKE '%battery%'` takes 12 seconds.",
        "code": "// 1. FREETEXT SEARCH (Linguistic stemming: matches 'run', 'running', 'ran'):\nvar athletes = await dbContext.Athletes\n    .Where(a => EF.Functions.FreeText(a.Biography, \"marathon running\"))\n    .ToListAsync();\n// SQL: WHERE FREETEXT([a].[Biography], N'marathon running')\n\n// 2. CONTAINS SEARCH (Boolean logic, exact phrases, prefixes):\nvar developers = await dbContext.Developers\n    .Where(d => EF.Functions.Contains(\n        d.Skills, \n        \"\\\"C#\\\" AND NOT \\\"Java\\\"\")) // Boolean expression in FTS syntax!\n    .ToListAsync();\n// SQL: WHERE CONTAINS([d].[Skills], N'\"C#\" AND NOT \"Java\"')\n\n// 3. BAD: LIKE '%keyword%' (Non-sargable full table scan!)\n// var slow = dbContext.Athletes.Where(a => a.Biography.Contains(\"marathon\"));",
        "codeLang": "csharp",
        "pros": [
            "Sub-millisecond text search across millions of rows using inverted indexes",
            "Built-in linguistic stemming, word inflection, and noise-word elimination"
        ],
        "cons": [
            "Requires configuring Full-Text Catalog and Full-Text Indexes in SQL Server",
            "Does not work in in-memory EF Core provider during unit tests"
        ],
        "followups": [
            "What is the difference between `EF.Functions.Contains` and `EF.Functions.FreeText` in SQL Server?",
            "How does PostgreSQL Full-Text Search (`to_tsvector` and `to_tsquery`) integrate with EF Core?"
        ],
        "seniorInsight": "Never use `string.Contains(\"term\")` for text searching in production databases with >100,000 rows! A `LIKE '%term%'` query forces SQL Server to read every single data page off disk (a 100% table scan). Set up a Full-Text Index on the column and use `EF.Functions.FreeText` or `EF.Functions.Contains` to achieve 1,000x faster searches.",
        "diagramTitle": "LIKE %term% Table Scan vs Full-Text Inverted Index",
        "diagramSteps": [
            ["INPUT_SEARCH", "Search Term Inbound", "User searches for 'clean' across 5,000,000 product descriptions", "Search Ingested"],
            ["LIKE_SCAN", "LIKE '%clean%' (Disaster)", "Leading % prevents B-Tree index seek: scans 5M records off disk (12s)", "Full Table Scan"],
            ["FTS_INV", "Inverted Full-Text Index", "Pre-computed inverted word index maps word 'clean' -> [Doc 12, 45, 89]", "Inverted Index"],
            ["STEM_RESOLVE", "Linguistic Stemming", "FREETEXT matches 'cleaning', 'cleaned', 'cleans' automatically", "Stemming Applied"],
            ["INSTANT_RETURN", "Sub-Millisecond Return", "Fetches exact 3 matching documents in 2ms: zero disk thrashing", "1,000x Speedup"]
        ],
        "diagramArchetype": "btree",
        "explanation": make_explanation(
            "Full-Text Search Architecture",
            "An inverted index is the data structure powering search engines (Google, Lucene, ElasticSearch). It maps tokens to lists of document IDs containing those tokens.",
            "SQL Server's Full-Text engine runs as a separate background process (`fdhost.exe`). It crawls tables asynchronously or during transactions to keep full-text indexes synchronized.",
            "// Full-Text Ranking with FREETEXTTABLE:\n// For relevance ranking, use raw SQL:\n// SELECT * FROM FREETEXTTABLE(Products, Description, 'wireless headphones') ORDER BY [RANK] DESC",
            "Ensure full-text stop words (noise words like 'the', 'is', 'at') are configured appropriately for your domain.",
            "Searching 10,000,000 documents with Full-Text Search takes ~2-5 ms vs ~15 seconds for `LIKE`."
        )
    })

    # Q3507
    qs.append({
        "id": 3507,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "JSON Column Querying in EF Core 7/8/9: Querying Dynamic JSON Properties with Native LINQ",
        "answer": "**In Plain English:** In old .NET, if you stored a JSON document inside a database column, it was just a dead string of text: you had to download the whole string and parse it in C# to inspect any field. Modern EF Core lets you query inside the JSON document directly using LINQ (`o.ShippingAddress.City == 'Chicago'`), and SQL Server queries the JSON properties directly inside the database.\n\n**Interview Answer:** EF Core 7, 8, and 9 introduced native **JSON Columns Mapping**. Complex value objects or nested collections can be stored inside a single relational column as JSON (using `.ToJson()` in `OnModelCreating`). Once mapped, developers can query nested JSON properties using standard LINQ expressions (`u => u.Preferences.Theme == \"Dark\"`). EF Core translates this directly into native SQL JSON operators: `JSON_VALUE([u].[Preferences], '$.Theme')` on SQL Server, or `preferences->>'Theme'` on PostgreSQL, enabling relational joins with document-database flexibility.",
        "concept": "EF Core `.ToJson()` maps nested object graphs into JSON columns, queryable via standard LINQ and translated to `JSON_VALUE`.",
        "howItWorks": "1) Configure `builder.OwnsOne(x => x.Address).ToJson()`. 2) EF Core registers the entity as an owned JSON entity. 3) Chaining LINQ expressions like `.Where(c => c.Address.ZipCode == \"90210\")` is intercepted by the SQL expression factory, which generates `JSON_VALUE([c].[Address], '$.ZipCode') = '90210'`.",
        "whyWhen": "Ideal for semi-structured data, user preferences, e-commerce dynamic product attributes, and polymorphic payload schemas.",
        "example": "Filtering customers by city stored inside a JSON column: `db.Customers.Where(c => c.Address.City == \"Seattle\")`.",
        "code": "public class Customer\n{\n    public int Id { get; set; }\n    public string Name { get; set; } = \"\";\n    public Address Address { get; set; } = new(); // Owned JSON entity!\n}\npublic class Address { public string Street { get; set; } public string City { get; set; } }\n\n// 1. FLUENT CONFIGURATION (EF Core 7/8/9):\nprotected override void OnModelCreating(ModelBuilder modelBuilder)\n{\n    modelBuilder.Entity<Customer>()\n        .OwnsOne(c => c.Address, b => b.ToJson()); // Mapped to JSON column!\n}\n\n// 2. QUERYING VIA STANDARD LINQ:\nvar seattleCustomers = await dbContext.Customers\n    .Where(c => c.Address.City == \"Seattle\") // Translates to SQL JSON_VALUE!\n    .ToListAsync();\n\n// 3. GENERATED SQL (SQL Server):\n// SELECT [c].[Id], [c].[Name], [c].[Address]\n// FROM [Customers] AS [c]\n// WHERE JSON_VALUE([c].[Address], '$.City') = N'Seattle'",
        "codeLang": "csharp",
        "pros": [
            "Eliminates relational schema migration overhead for frequently changing domain attributes",
            "Seamless strongly-typed LINQ experience with native database execution"
        ],
        "cons": [
            "Querying unindexed JSON columns performs a full table scan; indexing requires computed columns",
            "Updates rewrite the entire JSON column document (unless using JSON_MODIFY)"
        ],
        "followups": [
            "How do you index a specific JSON property in SQL Server for fast lookups?",
            "How does EF Core 8 support collections of primitive types in JSON (`List<string> Tags`)?"
        ],
        "seniorInsight": "To index a JSON property in SQL Server, create a PERSISTED COMPUTED COLUMN: `ALTER TABLE Customers ADD CityComputed AS JSON_VALUE(Address, '$.City') PERSISTED; CREATE INDEX IX_Customers_City ON Customers(CityComputed);`. SQL Server will automatically route your LINQ query `c.Address.City == 'Seattle'` to that B-Tree index!",
        "diagramTitle": "EF Core JSON Column Mapping & JSON_VALUE Translation",
        "diagramSteps": [
            ["DOMAIN_MODEL", "Strongly-Typed C# Model", "Customer entity with nested Address owned object graph", "C# Object Graph"],
            ["FLUENT_JSON", "builder.OwnsOne().ToJson()", "EF Core maps Address property to single NVARCHAR(MAX) column", "JSON Column Mapped"],
            ["LINQ_EXPR", "LINQ Property Access", "Developer writes: Where(c => c.Address.City == 'Seattle')", "LINQ Formed"],
            ["SQL_JSON_VAL", "SQL JSON_VALUE Translation", "Translates directly to: WHERE JSON_VALUE([Address], '$.City') = 'Seattle'", "SQL Translated"],
            ["DB_EXEC", "Native Database Scan", "SQL Server extracts property from JSON buffer in-place", "Zero C# Deserialization"]
        ],
        "diagramArchetype": "sql",
        "explanation": make_explanation(
            "JSON Columns Architecture",
            "The combination of relational database consistency (ACID) with document database flexibility (JSON) is known as multi-model storage.",
            "In EF Core 8+, querying collections of primitive types (e.g. `List<string> Tags` or `List<int> Scores`) inside a JSON column is natively supported via `.ToJson()`.",
            "// Querying JSON primitive arrays in EF Core 8:\nvar tagged = await db.Posts\n    .Where(p => p.Tags.Contains(\"dotnet\"))\n    .ToListAsync();",
            "Avoid storing multi-megabyte JSON payloads in entities that are queried frequently; use dedicated blob storage for massive documents.",
            "Extracting a property via `JSON_VALUE` takes ~150 nanoseconds in SQL Server."
        )
    })

    # Q3508
    qs.append({
        "id": 3508,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Composing LINQ Over Raw SQL: FromSqlInterpolated and Trailing Query Composition in EF Core",
        "answer": "**In Plain English:** Writing raw SQL is like hiring a master craftsman to build a custom engine. Composing LINQ over raw SQL is putting that custom engine inside a luxury sports car and using your standard steering wheel and GPS (LINQ `.Where()`, `.OrderBy()`, `.Take()`) to drive it effortlessly.\n\n**Interview Answer:** In EF Core, `FromSqlInterpolated` and `FromSqlRaw` allow developers to execute hand-tuned raw SQL queries while retaining the ability to compose trailing LINQ operators over the result set. When trailing LINQ operators (`.Where()`, `.OrderBy()`, `.Take()`) are chained after `FromSqlInterpolated`, EF Core wraps the raw SQL statement inside a SQL subquery (`SELECT ... FROM (your raw sql) AS [sub] WHERE ...`), executing the entire composition in a single database roundtrip. Furthermore, `FromSqlInterpolated` uses C# string interpolation (`$\"...\"`) to automatically parameterize all dynamic values, guaranteeing **100% immunity to SQL injection**.",
        "concept": "`FromSqlInterpolated` allows composing trailing LINQ operators over raw SQL, executing as a parameterized subquery.",
        "howItWorks": "EF Core accepts the `FormattableString`. It extracts the string template and parameters, passes them as `SqlParameter` objects, and returns an `IQueryable<T>`. Chained LINQ operators wrap the raw SQL in an outer `SELECT` projection.",
        "whyWhen": "Essential when queries require advanced database-specific features (Common Table Expressions, Query Hints, Full-Text Search, Stored Procedures) while still needing paging and dynamic filtering.",
        "example": "Executing a complex recursive CTE and paging the results with LINQ `.Skip(20).Take(10)`.",
        "code": "int minOrders = 5;\nstring targetCity = \"New York\";\n\n// 1. FROM SQL INTERPOLATED: SAFE PARAMETERIZATION + LINQ COMPOSITION:\nvar query = dbContext.Customers\n    // Raw SQL with complex Common Table Expression:\n    .FromSqlInterpolated($\"\"\"\n        SELECT c.* \n        FROM Customers c\n        JOIN (\n            SELECT CustomerId, COUNT(*) as OrderCount\n            FROM Orders\n            GROUP BY CustomerId\n            HAVING COUNT(*) >= {minOrders}\n        ) o ON c.Id = o.CustomerId\n    \"\"\")\n    // TRAILING LINQ OPERATORS (Composed as outer SQL subquery!):\n    .Where(c => c.City == targetCity) // Filtered in SQL!\n    .OrderBy(c => c.Name)             // Sorted in SQL!\n    .Take(10);                        // Paged in SQL!\n    \nvar results = await query.ToListAsync();",
        "codeLang": "csharp",
        "pros": [
            "Best of both worlds: raw SQL optimization combined with dynamic LINQ composability",
            "`FromSqlInterpolated` automatically parameterizes interpolated values, preventing SQL injection"
        ],
        "cons": [
            "Raw SQL must return all columns required by the entity type",
            "Cannot compose trailing LINQ over Stored Procedures that return multiple result sets"
        ],
        "followups": [
            "Why does `FromSqlInterpolated` prevent SQL injection while `FromSqlRaw` can be vulnerable?",
            "What happens if the raw SQL query contains an `ORDER BY` clause before trailing LINQ operators are attached?"
        ],
        "seniorInsight": "NEVER use string concatenation with `FromSqlRaw`! Writing `FromSqlRaw(\"SELECT * FROM Users WHERE Name = '\" + input + \"'\")` is a critical SQL injection vulnerability. ALWAYS use `FromSqlInterpolated($\"... WHERE Name = {input}\")`. Even though it looks like string interpolation, C# passes it as a `FormattableString`, and EF Core turns `{input}` into a secure `@p0` SQL parameter.",
        "diagramTitle": "Raw SQL Composition with Trailing LINQ Subqueries",
        "diagramSteps": [
            ["RAW_SQL_IN", "Raw SQL Template", "FromSqlInterpolated($\"SELECT * FROM Customers WHERE Tier = {tier}\")", "Raw SQL Ingested"],
            ["SAFE_PARAMS", "Parameter Extraction", "FormattableString turns {tier} into secure @p0 SQL parameter", "SQL Injection Safe"],
            ["TRAILING_LINQ", "Trailing LINQ Chained", "Chains .Where(c => c.City == 'NY').OrderBy(c => c.Name).Take(10)", "LINQ Composed"],
            ["SUBQUERY_WRAP", "Subquery Wrapping", "EF Core wraps raw SQL in subquery: SELECT TOP(10) FROM (raw sql) AS [sub]", "Single SQL Statement"],
            ["SINGLE_ROUND", "Single Roundtrip Return", "Database executes entire composed statement in 1 roundtrip (3ms)", "Maximum Performance"]
        ],
        "diagramArchetype": "sql",
        "explanation": make_explanation(
            "Raw SQL Composition Mechanics",
            "`FromSqlInterpolated` relies on the C# compiler's `FormattableString` type. If a method accepts `FormattableString`, C# passes the format string and argument array without performing string concatenation.",
            "EF Core creates a `SelectExpression` where the table source is a `FromSqlExpression`. All subsequent LINQ method calls wrap this expression inside an outer select.",
            "// Safe vs Unsafe Comparison:\n// DANGEROUS (SQL Injection):\n// db.Customers.FromSqlRaw(\"SELECT * FROM Customers WHERE City = '\" + city + \"'\");\n// 100% SECURE (Parameterized):\n// db.Customers.FromSqlInterpolated($\"SELECT * FROM Customers WHERE City = {city}\");",
            "The raw SQL must return tabular data matching the entity type definition (all mapped non-nullable columns must be present).",
            "Executing raw SQL with trailing LINQ has zero overhead compared to hand-written nested SQL."
        )
    })

    return qs

print("Domain 9 module loaded successfully.")

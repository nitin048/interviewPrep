"""
LINQ Domain 5: Partitioning, Paging & Infinite Streams (Questions 3459 to 3468)
"""
from scratch.linq_domains_1_to_5 import make_explanation

def get_domain_5():
    qs = []

    # Q3459
    qs.append({
        "id": 3459,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "architecture",
        "q": "Keyset (Seek) Pagination vs Offset Pagination in LINQ: Eliminating SQL Performance Degradation",
        "answer": "**In Plain English:** Offset pagination (`Skip/Take`) is like turning to page 5,000 in a heavy encyclopedia by physically flipping through all previous 4,999 pages one-by-one every single time. Keyset pagination (Seek method) is using the alphabetical tab printed on the edge of the book to jump straight to the exact entry where you left off last time.\n\n**Interview Answer:** Offset pagination using `.Skip(page * size).Take(size)` translates to SQL `OFFSET ... FETCH NEXT`. For deep pages (e.g. page 1,000), the database engine must scan and discard 100,000 rows across its index, causing CPU spikes, high I/O, and data drift (missed or duplicate rows when items are inserted). **Keyset Pagination** (cursor-based seek pagination) uses a `WHERE Id > lastSeenId ORDER BY Id ASC TAKE(size)` filter. This allows the database to perform an instant $O(\\log N)$ index seek directly to the target record, maintaining constant-time performance regardless of how deep the user paginates.",
        "concept": "Keyset pagination uses a `WHERE Id > lastSeen` index seek instead of `OFFSET`, achieving O(log N) constant-time pagination.",
        "howItWorks": "Instead of passing a page number, the client sends the ID or timestamp of the last item received (`cursor`). The LINQ query filters `query.Where(x => x.CreatedAt > cursorTimestamp).OrderBy(x => x.CreatedAt).Take(pageSize)`. The database clustered index jumps directly to `cursorTimestamp` in microseconds.",
        "whyWhen": "Mandatory for infinite scrolling mobile apps, high-volume REST APIs, streaming data exports, and audit logs with millions of rows.",
        "example": "Paginating through 50 million bank transactions: page 10,000 takes 8.5 seconds with `Skip/Take`; Keyset pagination takes 2 milliseconds.",
        "code": "// 1. BAD: OFFSET PAGINATION (Degrades linearly as page increases)\npublic async Task<List<Order>> GetOrdersOffset(int page, int pageSize)\n{\n    // Translates to: OFFSET 100000 ROWS FETCH NEXT 50 ROWS ONLY (Deadly slow!)\n    return await dbContext.Orders\n        .OrderBy(o => o.Id)\n        .Skip(page * pageSize)\n        .Take(pageSize)\n        .ToListAsync();\n}\n\n// 2. GOOD: KEYSET (SEEK) PAGINATION (Constant time O(log N))\npublic async Task<List<Order>> GetOrdersKeyset(int lastSeenId, int pageSize)\n{\n    // Translates to: WHERE Id > @lastSeenId ORDER BY Id ASC TOP(50) (Clustered Index Seek!)\n    return await dbContext.Orders\n        .Where(o => o.Id > lastSeenId)\n        .OrderBy(o => o.Id)\n        .Take(pageSize)\n        .ToListAsync();\n}",
        "codeLang": "csharp",
        "pros": [
            "Constant O(log N) query time regardless of whether you are on page 1 or page 1,000,000",
            "Immune to data drift: inserting or deleting records never causes items to be duplicated or skipped"
        ],
        "cons": [
            "Cannot jump to an arbitrary page number (e.g. 'Jump directly to Page 42')",
            "Requires a strictly unique, indexed, sequential column (e.g. `Id` or `(CreatedAt, Id)` composite key)"
        ],
        "followups": [
            "How do you implement Keyset pagination when sorting by non-unique columns like `LastName`?",
            "What is cursor encoding (e.g. base64 tokens) in RESTful API design?"
        ],
        "seniorInsight": "When sorting by a non-unique column (like `CreatedAt` or `Price`), you MUST tie-break with a unique column (like `Id`)! E.g. `.Where(o => o.CreatedAt > lastDate || (o.CreatedAt == lastDate && o.Id > lastId)).OrderBy(o => o.CreatedAt).ThenBy(o => o.Id)`. Without the tie-breaker, items with identical timestamps will be skipped or duplicated across page boundaries.",
        "diagramTitle": "Offset Scanning (O(N)) vs Keyset Index Seek (O(log N))",
        "diagramSteps": [
            ["DEEP_PAGE", "Page 10,000 Request", "Client requests 50 items at deep pagination offset (100,000 rows in)", "Request Received"],
            ["OFFSET_SCAN", "SQL Offset Scan (Bad)", "SQL Server scans and discards 100,000 index rows: 8,500ms CPU time", "Linear Degradation"],
            ["KEYSET_PARAM", "Last Seen Cursor (Good)", "Client provides cursor: lastSeenId = 582,491 from previous response", "Cursor Provided"],
            ["INDEX_SEEK", "B-Tree Clustered Seek", "Database B-Tree index performs instant seek directly to record 582,491", "Index Seek (1ms)"],
            ["FETCH_ROWS", "Constant-Time Return", "Reads exactly 50 rows from disk; returns in 2ms with 0 wasted I/O", "Constant O(log N)"]
        ],
        "diagramArchetype": "btree",
        "explanation": make_explanation(
            "Keyset Pagination Architecture",
            "Offset pagination is the single most common cause of high database CPU usage in production APIs. When an offset is requested, the storage engine reads all skipped rows from disk and discards them in memory.",
            "Keyset pagination leverages B-Tree index ordering. The database engine jumps down the B-Tree root to the target leaf node in 3-4 I/O operations and scans forward by `pageSize` rows.",
            "// Composite Keyset Pagination in C#:\nvar query = db.Orders\n    .Where(o => o.Date > lastDate || (o.Date == lastDate && o.Id > lastId))\n    .OrderBy(o => o.Date)\n    .ThenBy(o => o.Id)\n    .Take(pageSize);",
            "Keyset pagination is the standard used by Slack, Stripe, Twitter, and GitHub REST APIs.",
            "On a 10-million row table, `OFFSET 5000000` takes ~4,200 ms; Keyset seek takes ~1.5 ms."
        )
    })

    # Q3460
    qs.append({
        "id": 3460,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "intermediate",
        "type": "comparison",
        "q": "TakeWhile vs SkipWhile in LINQ: Predicate-Driven Sequence Partitioning and Early Halting",
        "answer": "**In Plain English:** `Where` looks at every single student in the entire school no matter what. `TakeWhile` stops inspecting the very first second a student doesn't meet the rule (like a bouncer stopping a line of people the moment someone under 21 arrives). `SkipWhile` ignores people until the first adult arrives, then lets everyone in after that without checking again.\n\n**Interview Answer:** Unlike `.Where()` (which evaluates its predicate across every single element in the sequence), `.TakeWhile()` and `.SkipWhile()` are state-dependent short-circuiting operators. `.TakeWhile(predicate)` yields elements from the start of the sequence as long as the predicate returns `true`; the microsecond it encounters the first element returning `false`, it **halts immediately** and terminates the enumerator. Conversely, `.SkipWhile(predicate)` discards elements as long as the condition holds, and the moment the first `false` is encountered, it yields that element and all subsequent elements without ever calling the predicate again.",
        "concept": "`TakeWhile` halts immediately upon the first false predicate; `SkipWhile` discards until the first false predicate, then yields all remaining items.",
        "howItWorks": "Inside `TakeWhile`, `MoveNext()` evaluates `predicate(Current)`. If `true`, it yields; if `false`, it sets its internal state to completed and returns `false`, avoiding inspecting the remainder of the collection.",
        "whyWhen": "Essential when processing sorted or time-ordered streams, reading packet headers, and isolating contiguous valid blocks.",
        "example": "Reading log files sorted by time: `logs.TakeWhile(l => l.Timestamp >= startTime)` stops reading the moment logs cross the cutoff date, saving disk I/O.",
        "code": "int[] sortedScores = { 98, 95, 91, 88, 74, 65, 50, 42 };\n\n// 1. TakeWhile: STOPS at the first score below 90!\n// Does NOT inspect 74, 65, 50, 42!\nvar honors = sortedScores.TakeWhile(s => s >= 90);\n// Result: 98, 95, 91\n\n// 2. SkipWhile: Skips until first score below 90, then yields EVERYTHING remaining:\nvar regularScores = sortedScores.SkipWhile(s => s >= 90);\n// Result: 74, 65, 50, 42\n\n// 3. Contrast with Where (inspects ALL elements):\nvar whereCheck = sortedScores.Where(s => s >= 90); // Scans whole array!",
        "codeLang": "csharp",
        "pros": [
            "Early termination saves CPU and I/O on sorted or ordered streams",
            "Works cleanly with infinite mathematical and event generators"
        ],
        "cons": [
            "If the sequence is unsorted, `TakeWhile` may stop prematurely (e.g. on `[95, 80, 99]`, it stops at 80 and misses 99)",
            "Does not translate cleanly to SQL `TOP` in all database engines"
        ],
        "followups": [
            "What happens if you call `TakeWhile` on an unsorted collection?",
            "How does `TakeWhile` enable safe consumption of infinite generators?"
        ],
        "seniorInsight": "`TakeWhile` REQUIRES the underlying collection to be sorted or monotonically ordered relative to the predicate! If the collection is unsorted, `TakeWhile` will stop at the first anomaly and fail to yield subsequent matching elements. If data is unsorted, you must use standard `.Where()`.",
        "diagramTitle": "TakeWhile Early Halting vs Where Full Scan",
        "diagramSteps": [
            ["SORTED_DATA", "Sorted Sequence Stream", "Stream sorted descending: [98, 95, 91, 88, 74, 65... 1M items]", "Sorted Stream"],
            ["EVAL_1", "Predicate Match (True)", "Evaluates 98 >= 90: True -> Yields 98", "Item Yielded"],
            ["EVAL_2", "Predicate Match (True)", "Evaluates 95 >= 90: True -> Yields 95", "Item Yielded"],
            ["FIRST_FALSE", "First False: 88 >= 90", "Condition fails on 88: TakeWhile terminates enumerator immediately!", "Early Exit"],
            ["HALT_CPU", "99.9% Stream Skipped", "Does not read remaining 999,997 items: massive CPU & I/O savings", "Zero Waste"]
        ],
        "diagramArchetype": "pipeline",
        "explanation": make_explanation(
            "TakeWhile & SkipWhile Mechanics",
            "In computing, early-halting operators allow infinite or continuous sequences to be safely sampled. If you have an infinite generator `Numbers().TakeWhile(n => n < 1000)`, it safely terminates after 1,000 iterations.",
            "If you wrote `Numbers().Where(n => n < 1000)` instead, the query would run forever in an infinite loop because `Where` never stops checking.",
            "// Parsing Header vs Body with SkipWhile/TakeWhile:\nvar lines = File.ReadLines(\"email.eml\");\nvar headers = lines.TakeWhile(line => !string.IsNullOrEmpty(line));\nvar body = lines.SkipWhile(line => !string.IsNullOrEmpty(line)).Skip(1);",
            "In EF Core, `TakeWhile` is rarely supported for server-side SQL translation because SQL has no `WHILE` clause in standard `SELECT` queries.",
            "Halting a 1,000,000-item sequence after 10 matches via `TakeWhile` takes ~20 ns; `Where` takes ~12 ms."
        )
    })

    # Q3461
    qs.append({
        "id": 3461,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "intermediate",
        "type": "code",
        "q": "C# 8 Index and Range Operators (^ and ..) with LINQ Collections and Spans",
        "answer": "**In Plain English:** The hat operator `^` lets you count backward from the end of a line (`^1` is the last person, `^2` is the second-to-last person). The range operator `..` lets you slice out a middle section (`1..^1` means 'everything except the first and last person') with clean, elegant syntax.\n\n**Interview Answer:** C# 8 introduced `System.Index` (with the `^` 'from-end' operator) and `System.Range` (with the `..` slicing operator). On arrays, strings, and `Span<T>`, ranges compile directly into zero-allocation slice calls. On generic collections, ranges can be used with LINQ to replace verbose `.Skip()` and `.Take()` calls. For example, `source.Take(1..^1)` skips the first and last elements cleanly, providing high readability without manual index math.",
        "concept": "Index (`^`) and Range (`..`) provide native syntax for from-end indexing and slicing across arrays, spans, and LINQ collections.",
        "howItWorks": "`^k` compiles to `new Index(k, fromEnd: true)`. When evaluated against a collection of length $L$, it computes $L - k$. `start..end` compiles to `new Range(start, end)`. On arrays, `arr[1..3]` allocates a sub-array; on `Span<T>`, `span[1..3]` creates a zero-allocation slice.",
        "whyWhen": "Use for slicing time-series buffers, stripping header/footer records, inspecting recent elements, and extracting sub-sequences.",
        "example": "Extracting the middle items of a sequence while discarding the head and tail: `items[1..^1]`.",
        "code": "int[] numbers = { 10, 20, 30, 40, 50, 60, 70, 80 };\n\n// 1. FROM-END INDEX OPERATOR (^):\nint last = numbers[^1];       // 80 (numbers.Length - 1)\nint secondToLast = numbers[^2]; // 70\n\n// 2. RANGE OPERATOR (..):\nint[] middle = numbers[2..5];   // 30, 40, 50 (indices 2, 3, 4)\nint[] allExceptEnds = numbers[1..^1]; // 20 through 70\nint[] firstThree = numbers[..3];      // 10, 20, 30\nint[] fromFourOnwards = numbers[4..]; // 50, 60, 70, 80\n\n// 3. ZERO-ALLOCATION WITH SPAN:\nReadOnlySpan<int> span = numbers.AsSpan();\nReadOnlySpan<int> slice = span[2..^2]; // Zero allocation slice!",
        "codeLang": "csharp",
        "pros": [
            "Eliminates off-by-one errors and verbose `list.Count - 1` boilerplate",
            "Integrates seamlessly with `Span<T>` and `ReadOnlySpan<T>` for zero-allocation slicing"
        ],
        "cons": [
            "Using range syntax `arr[1..5]` directly on an array allocates a NEW array on the heap",
            "Custom collections must implement a `Count` property and indexer or `Slice` method to support ranges"
        ],
        "followups": [
            "Why does `arr[1..3]` on a standard array allocate memory while `span[1..3]` does not?",
            "How can a custom collection support C# 8 Index and Range operators?"
        ],
        "seniorInsight": "BEWARE: Slicing a standard array with `array[1..^1]` allocates a BRAND-NEW array on the managed heap! Many developers assume it creates an in-place view. If you want zero allocation slicing, ALWAYS convert to a span first: `array.AsSpan()[1..^1]`.",
        "diagramTitle": "Index (^ from-end) and Range (..) Memory Slicing",
        "diagramSteps": [
            ["INDEX_MAP", "Zero-Based vs From-End", "Indices: [0, 1, 2, 3, 4] vs From-End: [^5, ^4, ^3, ^2, ^1]", "Index Mapping"],
            ["RANGE_SYNTAX", "Range Definition 1..^1", "Defines Range(start: 1, end: Index.FromEnd(1))", "Range Prepared"],
            ["ARRAY_PATH", "Array Slicing (Heap)", "array[1..^1] allocates new array and copies elements with Buffer.BlockCopy", "Heap Allocation"],
            ["SPAN_PATH", "Span Slicing (Stack)", "span[1..^1] creates ref struct window: offsets pointer, adjusts length", "0 Bytes Allocated"],
            ["ZERO_GC", "Optimal Performance", "Span range executes in 0.5 ns with zero GC impact", "Zero Alloc Win"]
        ],
        "diagramArchetype": "memory",
        "explanation": make_explanation(
            "Index & Range Mechanics",
            "C# 8's Index and Range types are built into the BCL runtime. The Roslyn compiler translates range expressions using pattern-based conventions.",
            "To support `^`, a type must have an `int Length` or `int Count` property and an `int` indexer. To support `..`, it must have a `Slice(int, int)` method or an indexer accepting `Range`.",
            "// Custom Range Support in a Class:\npublic class CustomBuffer<T> {\n    public int Count { get; }\n    public T this[int index] => Get(index);\n    public CustomBuffer<T> Slice(int start, int length) => SubBuffer(start, length);\n}",
            "Ranges are half-open intervals: `[start..end]` includes `start` but excludes `end`. `0..3` takes indices `0, 1, 2`.",
            "Slicing a span with `Range` takes ~0.5 nanoseconds; slicing an array allocates heap memory."
        )
    })

    # Q3462
    qs.append({
        "id": 3462,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "intermediate",
        "type": "code",
        "q": "Infinite Sequence Generation in LINQ: Building Mathematical Streams and Safe Consumption with Take()",
        "answer": "**In Plain English:** An infinite sequence is like a water faucet: it doesn't store a trillion gallons in your kitchen; it just pours water as long as you leave the valve open, and stops the instant you shut the valve.\n\n**Interview Answer:** An infinite sequence in LINQ is a generator method using `while (true) { yield return value; }`. Because execution is deferred, generating an infinite stream consumes zero memory and zero CPU when declared. The sequence only advances when the consumer calls `MoveNext()`. By pairing infinite generators with boundary operators like `.Take(n)` or `.TakeWhile(predicate)`, developers can model mathematical series (Fibonacci, primes), retry backoff timers, and ID generators safely.",
        "concept": "Infinite generators yield values on-demand using `while (true) yield return`; safe consumption requires terminating operators like `Take`.",
        "howItWorks": "The state machine loop pauses execution at each `yield return`. If the consumer calls `.Take(10)`, after 10 elements the `TakeIterator` ceases calling `MoveNext()`, automatically disposing the infinite generator without hanging the thread.",
        "whyWhen": "Useful for generating exponential backoff delay intervals, unique sequential identifiers, UUID token streams, and mathematical simulation modeling.",
        "example": "Generating exponential backoff retry intervals: `[1s, 2s, 4s, 8s, 16s, 32s]`: `Backoff().Take(5)` generates the first 5 retry delays.",
        "code": "// 1. INFINITE FIBONACCI GENERATOR:\npublic static IEnumerable<long> Fibonacci()\n{\n    long current = 0;\n    long next = 1;\n    while (true)\n    {\n        yield return current;\n        long temp = current + next;\n        current = next;\n        next = temp;\n    }\n}\n\n// 2. SAFE CONSUMPTION WITH TAKE():\n// Takes exactly the first 10 Fibonacci numbers:\nvar first10 = Fibonacci().Take(10).ToList();\nConsole.WriteLine(string.Join(\", \", first10)); // 0, 1, 1, 2, 3, 5, 8, 13, 21, 34\n\n// 3. EXPONENTIAL BACKOFF GENERATOR:\npublic static IEnumerable<TimeSpan> ExponentialBackoff(TimeSpan initial, double factor)\n{\n    TimeSpan current = initial;\n    while (true)\n    {\n        yield return current;\n        current *= factor;\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "Encapsulates generation algorithms cleanly without managing loop indices",
            "Consumes O(1) memory regardless of how many items are requested"
        ],
        "cons": [
            "FATAL BUG IF MATERIALIZED: Calling `.ToList()`, `.Count()`, or `foreach` without `Take()` causes an infinite loop that freezes the thread and crashes the process",
            "LINQ operators like `OrderBy` or `Reverse` will hang indefinitely on infinite streams"
        ],
        "followups": [
            "What happens if you accidentally call `.OrderBy()` or `.Count()` on an infinite sequence?",
            "How does `Enumerable.Repeat()` generate repeating sequences under the hood?"
        ],
        "seniorInsight": "NEVER pass an infinite `IEnumerable<T>` into a method that expects a finite collection! Calling `.Count()`, `.Last()`, `.Reverse()`, or `.OrderBy()` on an infinite generator triggers a non-terminating loop that consumes 100% of a CPU core and exhausts memory. Always bound the stream with `.Take()` before passing it down the stack.",
        "diagramTitle": "Infinite Sequence On-Demand Stream Consumption",
        "diagramSteps": [
            ["GEN_DEF", "Infinite Generator", "while (true) yield return value; declared in C# method", "Stream Dormant"],
            ["PIPELINE_BIND", "Bounded Take(N)", "query = Fibonacci().Take(5) chains terminating iterator", "Bound Attached"],
            ["PULL_STEP", "On-Demand Pull", "Consumer calls MoveNext(): generator computes next Fibonacci state", "State Advanced"],
            ["LIMIT_CHECK", "Counter Decrement", "TakeIterator decrements remaining count: 5 -> 4 -> 3 -> 2 -> 1 -> 0", "Counter Monitored"],
            ["STREAM_HALT", "Enumerator Disposal", "Count hits zero: Take returns false; infinite generator is disposed", "Safe Termination"]
        ],
        "diagramArchetype": "cycle",
        "explanation": make_explanation(
            "Infinite Generators Architecture",
            "In purely functional languages (Haskell), infinite streams are standard because all evaluation is lazy. In C#, `yield return` enables the identical paradigm.",
            "Because C# uses `IDisposable` on `IEnumerator<T>`, when `Take(n)` completes, it calls `Dispose()` on the upstream enumerator, executing any pending `finally` blocks in the generator.",
            "// Exponential Backoff with Jitter in Retry Pipeline:\nvar delays = ExponentialBackoff(TimeSpan.FromSeconds(1), 2.0)\n    .Select(d => d + TimeSpan.FromMilliseconds(Random.Shared.Next(0, 500)))\n    .Take(5); // Retries 5 times with jittered exponential delays!",
            "Any operator that requires reading to the end of a sequence (`Reverse`, `OrderBy`, `Last`, `Count`) will freeze on infinite sequences.",
            "Generating 1,000,000 Fibonacci numbers via `Take(1_000_000)` takes ~4 ms and allocates zero heap memory beyond the state machine."
        )
    })

    # Q3463
    qs.append({
        "id": 3463,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "architecture",
        "q": "Backpressure in LINQ Pipelines: Managing Producer-Consumer Speed Mismatches Without Memory Exhaustion",
        "answer": "**In Plain English:** If a factory conveyor belt dumps 1,000 boxes per minute into a packing room, but the packer can only tape 100 boxes per minute, boxes pile up to the ceiling until the warehouse collapses. Backpressure is the packer pressing a button to slow down the conveyor belt so boxes only arrive when the packer is ready.\n\n**Interview Answer:** Standard synchronous LINQ is inherently pull-based: the consumer thread calls `MoveNext()`, so backpressure is natural and automatic (the producer cannot yield until the consumer asks). However, in asynchronous or reactive streams (`IAsyncEnumerable`, TPL Dataflow, Channel<T>), producers and consumers run on independent threads. If a fast producer outpaces a slow consumer, unconsumed messages accumulate in memory buffers, triggering OutOfMemory exceptions. Implementing **Bounded Channels** (`System.Threading.Channels.Channel.CreateBounded<T>`) applies backpressure by asynchronously throttling or suspending the producer until the consumer catches up.",
        "concept": "Synchronous LINQ is pull-based with automatic backpressure; decoupled async producers require bounded channels to prevent memory explosion.",
        "howItWorks": "With `Channel.CreateBounded<T>(new BoundedChannelOptions(1000) { FullMode = BoundedChannelFullMode.Wait })`, when the channel reaches 1,000 items, `channel.Writer.WriteAsync(item)` halts and awaits asynchronously without blocking a thread. As the consumer reads via `channel.Reader.ReadAllAsync()`, capacity frees up, resuming the producer.",
        "whyWhen": "Critical when ingesting high-volume Kafka/RabbitMQ events, web scrapers downloading pages faster than disk writers, and database bulk imports.",
        "example": "Reading 10,000,000 records from a fast network socket and writing them to a slow database: bounded channels keep RAM usage under 50 MB.",
        "code": "public static async Task ProcessWithBackpressureAsync(\n    IAsyncEnumerable<DataPacket> fastProducer,\n    Func<DataPacket, Task> slowConsumer)\n{\n    // BOUNDED CHANNEL: Max 500 items in buffer before backpressure kicks in!\n    var channel = Channel.CreateBounded<DataPacket>(new BoundedChannelOptions(500)\n    {\n        FullMode = BoundedChannelFullMode.Wait // Throttles producer!\n    });\n    \n    // Producer Task:\n    var producerTask = Task.Run(async () =>\n    {\n        await foreach (var packet in fastProducer)\n        {\n            // Awaits if channel is full! Applies backpressure to producer:\n            await channel.Writer.WriteAsync(packet);\n        }\n        channel.Writer.Complete();\n    });\n    \n    // Consumer Task:\n    var consumerTask = Task.Run(async () =>\n    {\n        await foreach (var packet in channel.Reader.ReadAllAsync())\n        {\n            await slowConsumer(packet); // Slow database write\n        }\n    });\n    \n    await Task.WhenAll(producerTask, consumerTask);\n}",
        "codeLang": "csharp",
        "pros": [
            "Prevents OutOfMemory exceptions during massive data ingest spikes",
            "`System.Threading.Channels` is highly optimized with zero lock contention"
        ],
        "cons": [
            "Throttling producers can propagate delays upstream to API clients or message brokers",
            "Requires asynchronous code architecture (`async/await` and `Channel<T>`)"
        ],
        "followups": [
            "What are the four `BoundedChannelFullMode` strategies in .NET Channels?",
            "How does Reactive Extensions (Rx.NET) handle backpressure compared to `IAsyncEnumerable<T>`?"
        ],
        "seniorInsight": "Never use unbounded queues (`Channel.CreateUnbounded<T>()` or `ConcurrentQueue<T>`) between async producers and consumers! If the consumer slows down (e.g. database latency spike), the queue will grow to millions of items, consume all server memory, and crash your container with OOM. Always use a bounded channel with `BoundedChannelFullMode.Wait`.",
        "diagramTitle": "Bounded Channel Backpressure Flow Control",
        "diagramSteps": [
            ["FAST_PROD", "Fast Producer (10k/sec)", "High-speed network socket streams data packets rapidly", "Producer Active"],
            ["WRITE_CHAN", "Bounded Channel Buffer", "Channel buffer sized to 500 items accepts packets into memory", "Buffer Filling"],
            ["BUFFER_FULL", "Capacity Threshold Hit", "Channel reaches 500 items: Writer.WriteAsync() pauses producer", "Backpressure Armed"],
            ["SLOW_CONS", "Slow Consumer (1k/sec)", "Database consumer processes item: Reader.ReadAsync() frees slot", "Slot Available"],
            ["RESUME_FLOW", "Producer Resumed", "Producer unblocks and writes next packet; memory remains capped", "Stable 50MB RAM"]
        ],
        "diagramArchetype": "circuit_breaker",
        "explanation": make_explanation(
            "Backpressure Architecture & Mechanics",
            "Backpressure is a fundamental principle of the Reactive Manifesto. Without backpressure, any asynchronous pipeline with mismatched speeds is a ticking time bomb.",
            "`System.Threading.Channels` was introduced in .NET Core 3.0. It outperforms legacy `BlockingCollection<T>` by supporting non-blocking `ValueTask`-based asynchronous writes.",
            "// Bounded Channel Options:\nvar options = new BoundedChannelOptions(1000) {\n    FullMode = BoundedChannelFullMode.DropOldest, // Or Wait, DropNewest, DropWrite\n    SingleWriter = true,\n    SingleReader = false\n};",
            "Choosing `DropOldest` is ideal for real-time video streaming or stock ticker updates where stale data is useless.",
            "Channels achieve over 15,000,000 operations per second on modern .NET runtimes."
        )
    })

    # Q3464
    qs.append({
        "id": 3464,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Round-Robin Interleaving of N Sequences in LINQ: Fair Merging of Heterogeneous Event Streams",
        "answer": "**In Plain English:** If you have 3 lines of people waiting at 3 ticket booths, round-robin interleaving is having the gatekeeper take 1 person from Line A, then 1 person from Line B, then 1 person from Line C, repeating in a fair circle so no line gets neglected.\n\n**Interview Answer:** Merging multiple sequences fairly without letting a fast or massive sequence starve other sequences is called Round-Robin Interleaving. While `.Concat()` exhausts sequence A completely before moving to sequence B, an interleaving operator takes one element from each active sequence in cyclic rotation. A streaming C# implementation manages a list of active `IEnumerator<T>` instances, advancing each sequentially and pruning exhausted enumerators until all sequences complete.",
        "concept": "Interleaving merges N sequences round-robin, taking one element from each sequence in circular order.",
        "howItWorks": "1) Call `GetEnumerator()` on all $N$ input sequences. 2) Loop through enumerators: if `MoveNext()` returns `true`, yield `Current`; if `false`, dispose and remove the enumerator. 3) Repeat until all enumerators are exhausted. 4) Use a `finally` block to ensure all active enumerators are disposed if the consumer halts early.",
        "whyWhen": "Essential in multi-tenant task schedulers (preventing one tenant from monopolizing worker threads), game matchmaking queues, and audio track multiplexing.",
        "example": "Interleaving background jobs from 5 different customer queues so each customer gets equal processing time.",
        "code": "public static IEnumerable<T> Interleave<T>(this IEnumerable<IEnumerable<T>> sources)\n{\n    ArgumentNullException.ThrowIfNull(sources);\n    \n    var enumerators = new List<IEnumerator<T>>();\n    try\n    {\n        // Open enumerators for all sources:\n        foreach (var source in sources)\n        {\n            enumerators.Add(source.GetEnumerator());\n        }\n        \n        // Cycle through active enumerators until all empty:\n        while (enumerators.Count > 0)\n        {\n            for (int i = 0; i < enumerators.Count; i++)\n            {\n                var e = enumerators[i];\n                if (e.MoveNext())\n                {\n                    yield return e.Current; // Yield 1 item from current sequence\n                }\n                else\n                {\n                    // Sequence finished: dispose and prune\n                    e.Dispose();\n                    enumerators.RemoveAt(i);\n                    i--; // Adjust index after removal\n                }\n            }\n        }\n    }\n    finally\n    {\n        // Defensive cleanup of any remaining open enumerators:\n        foreach (var e in enumerators) e.Dispose();\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "Guarantees fair scheduling and prevents starvation across competing streams",
            "Handles sequences of unequal lengths gracefully by pruning completed ones"
        ],
        "cons": [
            "Maintains all $N$ enumerators open concurrently in memory",
            "Calling `RemoveAt(i)` on `List<IEnumerator>` causes small array shift copies (can be replaced with a linked list or queue)"
        ],
        "followups": [
            "How can using a `Queue<IEnumerator<T>>` make interleaving cleaner and avoid `RemoveAt` shifts?",
            "What is the difference between synchronous interleaving and asynchronous `Merge` in `IAsyncEnumerable<T>`?"
        ],
        "seniorInsight": "Using a `Queue<IEnumerator<T>>` makes interleaving even cleaner! Dequeue the enumerator, call `MoveNext()`. If `true`, yield `Current` and re-enqueue the enumerator at the back of the queue. If `false`, dispose it. This achieves O(1) queue rotation with zero array-shifting overhead.",
        "diagramTitle": "Round-Robin Interleaving Across N Input Sequences",
        "diagramSteps": [
            ["INPUT_STREAMS", "N Source Sequences", "Queue A: [A1, A2, A3], Queue B: [B1, B2], Queue C: [C1, C2, C3, C4]", "Queues Ready"],
            ["OPEN_ENUM", "Open Enumerators", "Initializes enumerators for A, B, and C in round-robin queue", "Pointers Open"],
            ["CYCLE_1", "Round 1 Yield", "Pulls A1 -> B1 -> C1; yields items cyclically to caller", "Round 1 Complete"],
            ["PRUNE_EXHAUST", "Stream B Exhausted", "B finishes at B2: B disposed and evicted from queue rotation", "Queue Pruned"],
            ["FINAL_DRAIN", "Drain Remaining", "Cycles remaining A and C items: final stream = [A1, B1, C1, A2, B2, C2, A3, C3, C4]", "Fair Emission"]
        ],
        "diagramArchetype": "cycle",
        "explanation": make_explanation(
            "Round-Robin Interleaving Mechanics",
            "Standard LINQ `.Concat()` is sequential concatenation: all of A, then all of B. If sequence A is infinite, sequence B will never execute.",
            "Interleaving ensures fairness: every sequence makes forward progress proportional to its position in the cycle.",
            "// High-Performance Queue-Based Interleaver:\npublic static IEnumerable<T> FastInterleave<T>(params IEnumerable<T>[] sources)\n{\n    var queue = new Queue<IEnumerator<T>>(sources.Select(s => s.GetEnumerator()));\n    try {\n        while (queue.Count > 0) {\n            var e = queue.Dequeue();\n            if (e.MoveNext()) {\n                yield return e.Current;\n                queue.Enqueue(e); // Put at back of line!\n            } else {\n                e.Dispose();\n            }\n        }\n    } finally {\n        while (queue.Count > 0) queue.Dequeue().Dispose();\n    }\n}",
            "Always wrap the enumerator collection in a `try-finally` block to ensure all open files/connections are closed if the consumer stops early via `Take(n)`.",
            "Interleaving 10 streams of 10,000 elements each takes ~5.5 ms in C#."
        )
    })

    # Q3465
    qs.append({
        "id": 3465,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "architecture",
        "q": "Multi-Channel Stream Splitting in LINQ: Splitting Sequences Without Multiple Enumeration",
        "answer": "**In Plain English:** If you want to sort mail into 'urgent' and 'normal' boxes as it falls through the mail slot, the foolish way is to let all the mail fall on the floor, pick it all up once to find urgent letters, then pick it all up a second time to find normal letters. Multi-channel splitting is setting up a diverter flap right at the slot that drops letters into the correct box in a single drop.\n\n**Interview Answer:** Splitting a sequence into multiple destination categories (e.g. valid records vs error records) naively requires running two LINQ queries: `var valid = source.Where(predicate); var errors = source.Where(!predicate);`. This causes multiple enumeration, reading the source stream twice. To split a sequence in a single pass without re-enumeration, developers use `GroupBy`, write a custom fork extension method, or partition into channels/lists in a single `foreach` loop.",
        "concept": "Splitting a stream into multiple branches must be done in a single pass to prevent multiple enumeration of the upstream source.",
        "howItWorks": "In a single pass, each item is evaluated against a partition function. The item is dispatched directly to its destination bucket or channel. A tuple of `(List<TSuccess> Successes, List<TFail> Failures)` is returned, guaranteeing that the upstream data source is enumerated exactly once.",
        "whyWhen": "Essential in ETL validation pipelines, data ingestion sanitizers, parsing batch uploads, and routing messages to different handlers.",
        "example": "Validating 100,000 uploaded user records: splitting into valid users to insert vs invalid users with error messages to log.",
        "code": "public record PartitionResult<T1, T2>(List<T1> Matches, List<T2> NonMatches);\n\npublic static PartitionResult<T, T> Partition<T>(\n    this IEnumerable<T> source, \n    Func<T, bool> predicate)\n{\n    var matches = new List<T>();\n    var nonMatches = new List<T>();\n    \n    // SINGLE PASS: Enumerates source exactly ONCE!\n    foreach (var item in source)\n    {\n        if (predicate(item))\n            matches.Add(item);\n        else\n            nonMatches.Add(item);\n    }\n    \n    return new PartitionResult<T, T>(matches, nonMatches);\n}\n\n// Functional Either/Result Partitioning:\npublic static (List<TSuccess> Successes, List<TError> Errors) SplitResults<T, TSuccess, TError>(\n    this IEnumerable<T> source,\n    Func<T, (bool IsSuccess, TSuccess? Success, TError? Error)> evaluator)\n{\n    var successes = new List<TSuccess>();\n    var errors = new List<TError>();\n    \n    foreach (var item in source)\n    {\n        var res = evaluator(item);\n        if (res.IsSuccess) successes.Add(res.Success!);\n        else errors.Add(res.Error!);\n    }\n    return (successes, errors);\n}",
        "codeLang": "csharp",
        "pros": [
            "Guarantees exactly 1 enumeration pass over the upstream data source",
            "Eliminates duplicate disk I/O, database roundtrips, and network calls"
        ],
        "cons": [
            "Materializes both partitions into in-memory lists (buffering)",
            "For unbounded streams, requires asynchronous bounded channels for each branch"
        ],
        "followups": [
            "How can you split an unbounded streaming sequence into two independent `IAsyncEnumerable<T>` streams without buffering everything in memory?",
            "What is the Reactive Extensions equivalent of stream splitting (`Observable.Publish`)?"
        ],
        "seniorInsight": "In enterprise API ingestion pipelines, never do `var valid = items.Where(Validate); var invalid = items.Where(x => !Validate(x));`! If validation involves regex checks, database existence lookups, or credit card verification, you just doubled your latency and paid double for external verification API calls. Always use a single-pass partition method.",
        "diagramTitle": "Single-Pass Stream Partitioning vs Duplicate Enumeration",
        "diagramSteps": [
            ["INPUT_STREAM", "Raw Ingest Stream", "Incoming transaction batch containing valid and fraudulent records", "Batch Received"],
            ["SINGLE_PASS", "Single-Pass Iterator", "Foreach loop reads each item exactly once from forward stream", "1x Enumeration"],
            ["EVAL_ROUTE", "Predicate Evaluation", "Evaluates validation rules once per item; routes to Branch A or B", "Route Decided"],
            ["BRANCH_A", "Valid Bucket", "Adds valid items directly to List<TValid> or Channel A", "Valid Routed"],
            ["BRANCH_B", "Errors Bucket", "Adds invalid items directly to List<TError> or Channel B", "Errors Isolated"]
        ],
        "diagramArchetype": "branch",
        "explanation": make_explanation(
            "Stream Splitting Architecture",
            "In functional programming, this operation is known as `partition`. It divides a collection into two disjoint collections based on a boolean predicate.",
            "If the output must remain streaming (without buffering lists in memory), you must use asynchronous channels (`Channel<T>`) or TPL Dataflow `BroadcastBlock<T>`.",
            "// Partitioning with ToLookup:\nvar lookup = source.ToLookup(predicate);\nvar matches = lookup[true];\nvar nonMatches = lookup[false];",
            "Using `ToLookup` is a concise one-liner, but allocating the custom partition method with pre-sized lists is twice as fast.",
            "Partitioning 100,000 records in a single pass takes ~2.8 ms in C#."
        )
    })

    # Q3466
    qs.append({
        "id": 3466,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "intermediate",
        "type": "code",
        "q": "Chunking with Remainder Handling in Background Workers: Safe Batch Queue Processing in C#",
        "answer": "**In Plain English:** If you are packing 55 eggs into cartons that hold 10 eggs each, you will fill 5 complete cartons of 10, and 1 remainder carton with only 5 eggs. If your code assumes every carton always has 10 eggs, the last carton will crash your packaging machine.\n\n**Interview Answer:** When batching sequences using `.Chunk(batchSize)` in background queue workers or database bulk updaters, the final yielded chunk may contain fewer elements than `batchSize` if the total count is not an exact multiple. Production code must never assume `batch.Length == batchSize`. In addition, background workers must handle transactional boundaries, partial batch failures, and retry policies per chunk rather than failing the entire parent job.",
        "concept": "The final batch from `.Chunk()` contains remainder elements; background processors must handle variable batch lengths and partial failure isolation.",
        "howItWorks": "`Enumerable.Chunk(size)` yields arrays where `1 <= array.Length <= size`. In background processors, each batch is wrapped in its own database transaction or try/catch block so that failure of batch #5 does not abort batches #1 through #4.",
        "whyWhen": "Crucial in background queue processing (Hangfire, Quartz.NET, BackgroundService), bulk email sending, and database updates.",
        "example": "Processing 1,025 pending invoices in batches of 100: yields 10 batches of 100, and 1 final batch of 25.",
        "code": "public class InvoiceProcessor\n{\n    public async Task ProcessAllInvoicesAsync(IEnumerable<Invoice> invoices, int batchSize = 100)\n    {\n        int batchNumber = 0;\n        \n        foreach (Invoice[] batch in invoices.Chunk(batchSize))\n        {\n            batchNumber++;\n            // DO NOT ASSUME batch.Length == batchSize! \n            // Final batch has Length = 25!\n            Console.WriteLine($\"Processing Batch #{batchNumber} with {batch.Length} items\");\n            \n            try\n            {\n                // Process each chunk in an isolated transactional scope:\n                await ProcessBatchWithRetryAsync(batch);\n            }\n            catch (Exception ex)\n            {\n                // Log and route failed batch to Dead Letter Queue (DLQ)\n                // Prevents aborting remaining batches!\n                LogBatchFailure(batchNumber, batch, ex);\n            }\n        }\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "Protects system stability by isolating batch failures",
            "Eliminates `IndexOutOfRangeException` on final remainder chunks"
        ],
        "cons": [
            "Requires robust error logging and Dead Letter Queue routing for failed chunks",
            "Partial batch successes require idempotent retry keys"
        ],
        "followups": [
            "How do you ensure idempotency when retrying a failed chunk in a database worker?",
            "What is the difference between `Parallel.ForEachAsync` over chunks vs sequential processing?"
        ],
        "seniorInsight": "Always ensure operations inside batch processors are IDEMPOTENT! If a batch of 100 updates fails on item #99 and throws an exception, retrying the batch will re-process items #1 through #98. Use unique transaction IDs or upsert logic (`ON CONFLICT DO UPDATE`) to prevent duplicate billing or double inventory deductions.",
        "diagramTitle": "Chunking Remainder Handling & Batch Isolation",
        "diagramSteps": [
            ["INPUT_QUEUE", "1,025 Queue Items", "Background queue contains 1,025 items awaiting bulk database processing", "Queue Loaded"],
            ["CHUNK_SPLIT", "Chunk(100) Iterator", "Partitions stream into 10 full batches of 100 + 1 remainder batch of 25", "Batches Formed"],
            ["TX_SCOPE", "Batch Transaction Scope", "Each batch runs inside isolated transaction scope with retry policy", "Tx Armed"],
            ["REMAINDER", "Remainder Batch Handling", "Final batch handles batch.Length == 25 safely without index out of range", "Safe Remainder"],
            ["FAIL_ISOLATE", "Dead Letter Isolation", "If Batch #3 fails, it routes to Dead Letter Queue; Batches 4-11 succeed", "System Resilient"]
        ],
        "diagramArchetype": "circuit_breaker",
        "explanation": make_explanation(
            "Chunking & Remainder Dynamics",
            "In distributed systems, batch processing is standard to amortize network round-trips and database connection overhead. However, edge-case bugs almost always cluster around the final remainder batch.",
            "`Enumerable.Chunk` guarantees that it will never yield an empty array. If the source is empty, it yields zero arrays. If the source has items, the last array has `Length = total % size` (or `size` if divisible).",
            "// Parallel Chunk Processing with Semaphore:\nawait Parallel.ForEachAsync(invoices.Chunk(100), new ParallelOptions { MaxDegreeOfParallelism = 4 }, async (batch, ct) => {\n    await ProcessChunkAsync(batch, ct);\n});",
            "Never use a fixed-size loop index `for (int i = 0; i < batchSize; i++)` inside a chunk consumer; always use `batch.Length` or `foreach`.",
            "Batching database writes in chunks of 500-1,000 typically yields a 20x throughput improvement over single-row inserts."
        )
    })

    # Q3467
    qs.append({
        "id": 3467,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Paging Through Paginated REST APIs with IAsyncEnumerable<T> and Asynchronous LINQ",
        "answer": "**In Plain English:** Calling a paginated API with standard methods is like asking a librarian for 10 books at a time, carrying all 5,000 books home in one giant backpack, and then reading them. `IAsyncEnumerable` is like reading each book in the library one-by-one; the librarian quietly walks to the back shelf and fetches the next box of 10 only when you finish reading the previous batch.\n\n**Interview Answer:** Consuming paginated HTTP REST APIs (which return pages of 50 or 100 items with next-page tokens or links) can lead to massive latency and memory bloat if all pages are fetched before processing. By encapsulating the HTTP pagination logic inside an `IAsyncEnumerable<T>` generator using `await foreach` and `yield return`, callers can consume remote API items as a continuous, lazy asynchronous stream. Chaining async LINQ operators allows filtering and early termination (`Take(10)`) without downloading unnecessary subsequent pages.",
        "concept": "`IAsyncEnumerable<T>` wraps paginated REST APIs in a seamless asynchronous stream, fetching next pages on-demand only when needed.",
        "howItWorks": "The generator fetches Page 1, yields each item in the page. When the page is exhausted, it checks for a `nextPageToken`. If present, it makes the next HTTP call and yields its items. If downstream code calls `.Take(5)` and breaks, the generator terminates, preventing HTTP calls for pages 2, 3, and 4.",
        "whyWhen": "Essential when integrating third-party SaaS APIs (Stripe, GitHub, Salesforce, Shopify, AWS SDKs) that enforce pagination limits.",
        "example": "Consuming GitHub API commit history: downloading only as many pages as needed until finding a specific commit.",
        "code": "public async IAsyncEnumerable<GitHubCommit> StreamCommitsAsync(\n    HttpClient http, \n    string repoUrl,\n    [EnumeratorCancellation] CancellationToken ct = default)\n{\n    string? nextUrl = $\"{repoUrl}/commits?per_page=100\";\n    \n    while (!string.IsNullOrEmpty(nextUrl))\n    {\n        // Asynchronously fetch current page from REST API:\n        var response = await http.GetFromJsonAsync<CommitPageResponse>(nextUrl, ct);\n        if (response?.Items == null) yield break;\n        \n        foreach (var commit in response.Items)\n        {\n            yield return commit; // Stream item downstream!\n        }\n        \n        // Extract next page URL from Link header or response body:\n        nextUrl = response.NextPageUrl;\n    }\n}\n\n// CONSUMPTION WITH ASYNC LINQ & EARLY TERMINATION:\n// Stops after 15 matching commits; NEVER downloads remaining pages!\nawait foreach (var commit in StreamCommitsAsync(client, url)\n    .Where(c => c.Author == \"octocat\")\n    .Take(15))\n{\n    Console.WriteLine($\"Commit: {commit.Sha}\");\n}",
        "codeLang": "csharp",
        "pros": [
            "Downstream consumer starts processing immediately upon Page 1 arrival (near-zero first-item latency)",
            "Short-circuiting (`Take`, `First`) automatically cancels subsequent remote HTTP requests, saving bandwidth"
        ],
        "cons": [
            "Network errors during mid-stream pagination must be caught during iteration, not at method call time",
            "Slow consumers can hold HTTP connections open longer than default timeouts"
        ],
        "followups": [
            "Why is the `[EnumeratorCancellation]` attribute required on the `CancellationToken` parameter?",
            "How does `System.Linq.Async` extend standard LINQ methods like `Where` and `Select` to `IAsyncEnumerable`?"
        ],
        "seniorInsight": "Always decorate the `CancellationToken` parameter with `[EnumeratorCancellation]`! Without this attribute, if the consumer calls `.WithCancellation(ct)` on the stream, the token will NOT be passed into your generator method, causing your HTTP calls to ignore cancellation requests and continue downloading in the background.",
        "diagramTitle": "IAsyncEnumerable Paginated REST API On-Demand Streaming",
        "diagramSteps": [
            ["HTTP_PAGE_1", "Fetch Page 1 (HTTP)", "Asynchronously downloads first 100 items from REST API endpoint", "Page 1 Received"],
            ["YIELD_ITEMS", "Stream Page Items", "Yields items 1 through 100 one-by-one to downstream business logic", "Items Streamed"],
            ["CHECK_TOKEN", "Next Page Token Probe", "Page exhausted: checks if response contains NextPageToken", "Token Checked"],
            ["DEMAND_FETCH", "On-Demand Page 2", "Consumer requests item 101: fetches Page 2 HTTP request on-demand", "Page 2 Fetched"],
            ["EARLY_HALT", "Early Termination (Take)", "Downstream Take(120) breaks loop: Page 3 is NEVER downloaded!", "Zero Waste Bandwidth"]
        ],
        "diagramArchetype": "http_flow",
        "explanation": make_explanation(
            "Async REST Pagination Architecture",
            "Combining `IAsyncEnumerable<T>` with HTTP pagination is the gold standard in modern cloud architecture. It bridges the impedance mismatch between chunked remote APIs and local stream consumption.",
            "If the consumer only needs 5 items, fetching all 5,000 items from an external API wastes network bandwidth, rate-limit quotas, and cloud egress costs.",
            "// Handling Retries in Async Streams with Polly:\nvar policy = Policy.Handle<HttpRequestException>().WaitAndRetryAsync(3, i => TimeSpan.FromSeconds(i));\nvar response = await policy.ExecuteAsync(() => http.GetFromJsonAsync<Page>(nextUrl, ct));",
            "Never materialize an entire paginated API into a `List<T>` before returning; always return `IAsyncEnumerable<T>`.",
            "First-element latency drops from ~4,500 ms (downloading 50 pages) to ~90 ms (downloading Page 1 only)."
        )
    })

    # Q3468
    qs.append({
        "id": 3468,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "architecture",
        "q": "BlockingCollection<T>.GetConsumingEnumerable: Thread-Safe Producer-Consumer Pipelines in LINQ",
        "answer": "**In Plain English:** `GetConsumingEnumerable` is like a conveyor belt coming out of a bakery kitchen into the storefront: as long as bakers keep putting fresh bread on the belt, the storefront clerk picks them up and bags them. If the belt is temporarily empty, the clerk waits patiently without panicking. When the bakery closes, the belt turns off and the clerk goes home.\n\n**Interview Answer:** `System.Collections.Concurrent.BlockingCollection<T>` is a thread-safe collection designed for producer-consumer architectures. Its method `.GetConsumingEnumerable()` returns an `IEnumerable<T>` that consumes elements from the collection as they become available. When elements are present, it yields and removes them. When the collection is empty, `MoveNext()` blocks the consumer thread efficiently (using kernel synchronization primitives) until an item is added. When producers call `.CompleteAdding()`, the enumerator gracefully terminates its loop.",
        "concept": "`GetConsumingEnumerable()` turns a thread-safe blocking queue into a standard LINQ sequence with thread-blocking semantics.",
        "howItWorks": "Inside `GetConsumingEnumerable()`, `MoveNext()` calls `TryTake` with an infinite timeout. It releases CPU cycles until signaled by a producer thread. Once `.CompleteAdding()` is called and all remaining items are drained, `MoveNext()` returns `false`, allowing standard `foreach` and LINQ pipelines to finish cleanly.",
        "whyWhen": "Used in multi-threaded ingestion workers, background log writers, audit event dispatchers, and coordinating CPU-bound background threads.",
        "example": "Multiple background worker threads pushing log messages into a queue while a single dedicated background thread streams them to disk via LINQ.",
        "code": "public class AuditLogPipeline\n{\n    private readonly BlockingCollection<string> _queue = new(boundedCapacity: 10000);\n    \n    // PRODUCER THREADS (Multiple web requests):\n    public void LogEvent(string message)\n    {\n        _queue.Add(message); // Thread-safe non-blocking add\n    }\n    \n    public void Shutdown() => _queue.CompleteAdding();\n    \n    // DEDICATED CONSUMER THREAD (Background task):\n    public void StartConsumer(Action<string> diskWriter)\n    {\n        Task.Run(() =>\n        {\n            // GetConsumingEnumerable BLOCKS when empty and TERMINATES when complete:\n            foreach (string log in _queue.GetConsumingEnumerable())\n            {\n                diskWriter(log); // Writes to disk continuously!\n            }\n            Console.WriteLine(\"Pipeline drained and shut down safely.\");\n        });\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "Provides thread-blocking sleep semantics without burning 100% CPU in busy-wait spin loops",
            "Plugs thread-safe concurrency directly into standard C# `foreach` and LINQ pipelines"
        ],
        "cons": [
            "Blocks OS threads synchronously (for async pipelines, prefer `System.Threading.Channels`)",
            "Forgetting to call `CompleteAdding()` leaves consumer threads blocked forever"
        ],
        "followups": [
            "How does `BlockingCollection<T>` differ from modern `Channel<T>` in terms of thread blocking vs async awaiting?",
            "What underlying collection does `BlockingCollection<T>` use by default (`ConcurrentQueue<T>`)?"
        ],
        "seniorInsight": "In modern .NET applications, prefer `Channel<T>` over `BlockingCollection<T>` for asynchronous code! `BlockingCollection` blocks the operating system thread synchronously, consuming thread pool threads while waiting. `Channel<T>` provides `ReadAllAsync()` which yields the thread back to the thread pool while idle.",
        "diagramTitle": "BlockingCollection Consumer Queue Drainage",
        "diagramSteps": [
            ["PRODUCER_THREADS", "Multi-Thread Producers", "Multiple worker threads call _queue.Add(event) concurrently", "Items Enqueued"],
            ["BOUNDED_QUEUE", "Concurrent Queue Buffer", "BlockingCollection stores events safely using concurrent locking", "Buffer Protected"],
            ["CONSUMING_ENUM", "GetConsumingEnumerable()", "Dedicated worker consumes stream: blocks efficiently when empty", "Thread Block/Wait"],
            ["DRAIN_ITEM", "Yield & Remove (Consume)", "Yields element to disk writer; removes item from internal buffer", "Item Consumed"],
            ["COMPLETE_SIGNAL", "CompleteAdding() Signal", "Producers call CompleteAdding(): drains remainder, loop exits", "Clean Shutdown"]
        ],
        "diagramArchetype": "circuit_breaker",
        "explanation": make_explanation(
            "BlockingCollection Architecture",
            "`BlockingCollection<T>` acts as a wrapper over `IProducerConsumerCollection<T>` (defaulting to `ConcurrentQueue<T>`). It coordinates thread signaling using `ManualResetEventSlim` and `SemaphoreSlim`.",
            "Unlike standard collection enumeration (which only reads items), `GetConsumingEnumerable()` **removes** each item as it is yielded, guaranteeing each element is processed exactly once.",
            "// Batching Consuming Enumerable with Chunk:\nforeach (var batch in _queue.GetConsumingEnumerable().Chunk(100)) {\n    await FlushToDatabaseAsync(batch);\n}",
            "If a cancellation token is passed to `GetConsumingEnumerable(ct)`, cancelling the token throws `OperationCanceledException` immediately, unblocking sleeping consumer threads.",
            "`BlockingCollection` processes over 2,000,000 items per second with low CPU overhead."
        )
    })

    return qs

print("Domain 5 module loaded successfully.")

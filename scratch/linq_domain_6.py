"""
LINQ Domain 6: Async LINQ & Reactive Streams (Questions 3469 to 3478)
"""
from scratch.linq_domains_1_to_5 import make_explanation

def get_domain_6():
    qs = []

    # Q3469
    qs.append({
        "id": 3469,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "architecture",
        "q": "IAsyncEnumerable<T> Internals: How Asynchronous Pull Streams Work Under the Hood in C# 8+",
        "answer": "**In Plain English:** Synchronous `IEnumerable` is like asking a cashier for an item and waiting at the counter while they walk to the back room to grab it, holding up the whole line. `IAsyncEnumerable` is like taking a buzzer number and stepping aside: while the cashier fetches the item from the stockroom, the counter is completely free for other customers, and your buzzer sounds the second the item arrives.\n\n**Interview Answer:** `IAsyncEnumerable<T>` is the asynchronous counterpart to `IEnumerable<T>`. Introduced in C# 8, its interface exposes `IAsyncEnumerator<T> GetAsyncEnumerator(CancellationToken cancellationToken = default)`. Instead of a synchronous `bool MoveNext()`, it exposes `ValueTask<bool> MoveNextAsync()`. This allows the enumerator to asynchronously yield execution back to the thread pool while awaiting I/O (database reads, HTTP streams, file I/O). The consumer consumes the stream using `await foreach`, retaining natural streaming semantics without thread blocking.",
        "concept": "`IAsyncEnumerable<T>` enables asynchronous pull-based streaming using non-allocating `ValueTask<bool> MoveNextAsync()`.",
        "howItWorks": "When the compiler compiles an `async IAsyncEnumerable<T>` method containing `yield return`, it generates an asynchronous state machine implementing `IAsyncStateMachine`. Calling `await foreach` generates a loop that awaits `enumerator.MoveNextAsync()`. If data is already available synchronously, `ValueTask` completes without allocating a `Task` object on the heap.",
        "whyWhen": "Mandatory when streaming large database queries, reading Kafka/RabbitMQ event streams, reading chunked HTTP API responses, and processing multi-gigabyte log files.",
        "example": "Streaming 1,000,000 database rows to an HTTP response without loading all 1,000,000 rows into server memory.",
        "code": "// 1. ASYNC STREAM PRODUCER:\npublic async IAsyncEnumerable<SensorReading> GetSensorDataAsync(\n    [EnumeratorCancellation] CancellationToken ct = default)\n{\n    while (!ct.IsCancellationRequested)\n    {\n        // Non-blocking asynchronous I/O wait:\n        SensorReading reading = await _sensorClient.ReadNextAsync(ct);\n        yield return reading;\n    }\n}\n\n// 2. ASYNC STREAM CONSUMER:\npublic async Task ProcessDataAsync(CancellationToken ct)\n{\n    // Non-blocking await foreach consumption:\n    await foreach (var reading in GetSensorDataAsync(ct))\n    {\n        Console.WriteLine($\"Sensor: {reading.Value} at {reading.Timestamp}\");\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "Combines async/await with iterator streaming for optimal memory and thread pool efficiency",
            "Returns `ValueTask<bool>`, eliminating `Task` heap allocation when elements are immediately available"
        ],
        "cons": [
            "Standard LINQ methods (`.Where()`, `.Select()`) do not natively work without `System.Linq.Async` package",
            "Requires careful handling of `CancellationToken` via `[EnumeratorCancellation]`"
        ],
        "followups": [
            "Why does `MoveNextAsync()` return `ValueTask<bool>` instead of `Task<bool>`?",
            "How does `ConfiguredCancelableAsyncEnumerable<T>` configure `ConfigureAwait(false)` on an async stream?"
        ],
        "seniorInsight": "In high-throughput server backends, always use `.ConfigureAwait(false)` on async streams: `await foreach (var item in stream.ConfigureAwait(false))`. This ensures that resuming after `MoveNextAsync()` does not attempt to marshal back to the originating synchronization context, avoiding thread-pool bottlenecks and ASP.NET request deadlocks.",
        "diagramTitle": "IAsyncEnumerable ValueTask State Machine Flow",
        "diagramSteps": [
            ["PRODUCER_CALL", "Async Generator Invocation", "Calls async IAsyncEnumerable generator: instantiates async state machine", "State Machine Ready"],
            ["AWAIT_FOREACH", "await foreach Evaluation", "Consumer thread invokes await enumerator.MoveNextAsync()", "Awaiting Next"],
            ["ASYNC_IO", "Non-Blocking I/O Await", "Awaits database or network socket; thread returns to ThreadPool", "Zero Threads Blocked"],
            ["DATA_ARRIVED", "I/O Signal & Resume", "Data arrival awakens state machine on available ThreadPool worker", "Worker Dispatched"],
            ["YIELD_VALUETASK", "ValueTask Yield", "Yields item to loop body; repeats cycle with O(1) memory footprint", "Stream Processed"]
        ],
        "diagramArchetype": "async",
        "explanation": make_explanation(
            "IAsyncEnumerable Architecture",
            "Prior to C# 8, developers had to choose between synchronous streaming (`IEnumerable<T>` with `yield return`) and asynchronous buffering (`Task<List<T>>`). `IAsyncEnumerable<T>` eliminates this compromise.",
            "By returning `ValueTask<bool>`, when multiple elements are buffered in memory (e.g. from an internal network buffer), `MoveNextAsync()` completes synchronously with zero task allocation.",
            "// Configuring Cancellation and Context:\nawait foreach (var item in stream.WithCancellation(ct).ConfigureAwait(false)) {\n    Process(item);\n}",
            "If an exception occurs inside the generator, it is rethrown at the `await foreach` site during `MoveNextAsync()` evaluation.",
            "`IAsyncEnumerable` achieves streaming throughput exceeding 1,000,000 items/sec on modern .NET."
        )
    })

    # Q3470
    qs.append({
        "id": 3470,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "System.Linq.Async: Using WhereAwait, SelectAwait, and ToListAsync in Asynchronous Streams",
        "answer": "**In Plain English:** Standard LINQ only knows how to run synchronous functions on in-memory lists. `System.Linq.Async` gives LINQ superpowers to run asynchronous `async/await` operations directly inside your queries, like making an async HTTP lookup or database check for every filtered element.\n\n**Interview Answer:** Standard `System.Linq` only provides extension methods for synchronous `IEnumerable<T>` and `IQueryable<T>`. To use LINQ over `IAsyncEnumerable<T>`, Microsoft provides the `System.Linq.Async` NuGet package (authored by the .NET team). It introduces asynchronous LINQ operators, including `WhereAwait` and `SelectAwait` (which accept asynchronous lambda expressions `Func<T, ValueTask<bool>>`), as well as terminal async operators like `ToListAsync()`, `CountAsync()`, `FirstAsync()`, and `AnyAsync()`.",
        "concept": "`System.Linq.Async` provides full LINQ operator support for `IAsyncEnumerable<T>`, supporting asynchronous delegates and cancellations.",
        "howItWorks": "Operators like `WhereAwait` wrap the upstream `IAsyncEnumerable` in an internal async iterator. Inside its `MoveNextAsync()`, it calls `await upstream.MoveNextAsync()`, and then calls `await predicate(current)`. If `true`, it yields; if `false`, it loops asynchronously to the next item.",
        "whyWhen": "Essential when transforming, filtering, and projecting asynchronous data streams where predicates or transformations require asynchronous I/O calls.",
        "example": "Filtering a stream of user IDs by checking their permission status in an external Redis cache asynchronously.",
        "code": "using System.Linq; // System.Linq.Async namespace\n\nIAsyncEnumerable<User> usersStream = GetUsersAsyncStream();\n\n// 1. WhereAwait: Asynchronous filtering predicate\n// 2. SelectAwait: Asynchronous projection\n// 3. ToListAsync: Asynchronous terminal materialization\nList<UserProfile> activeVips = await usersStream\n    .WhereAwait(async u => await _authService.IsActiveAsync(u.Id)) // Async predicate!\n    .SelectAwait(async u => await _profileService.FetchProfileAsync(u.Id)) // Async transform!\n    .Take(50) // Short-circuits after 50 items!\n    .ToListAsync(); // Materializes into in-memory list asynchronously",
        "codeLang": "csharp",
        "pros": [
            "Brings the full declarative power of LINQ to asynchronous workflows",
            "Allows asynchronous predicates (`WhereAwait`) and async projections (`SelectAwait`)"
        ],
        "cons": [
            "Each `Await` operator introduces asynchronous state machine overhead per element",
            "Serializes asynchronous execution by default (does not run predicates concurrently)"
        ],
        "followups": [
            "Why are asynchronous predicates serialized sequentially rather than executed in parallel?",
            "What is the namespace collision between EF Core's `ToListAsync()` and `System.Linq.Async`'s `ToListAsync()`?"
        ],
        "seniorInsight": "Watch out for namespace collisions between EF Core and `System.Linq.Async`! Both libraries declare extension methods named `ToListAsync()`, `FirstOrDefaultAsync()`, etc. If you import both namespaces, the C# compiler throws `CS0121: The call is ambiguous`. Always qualify or avoid importing `System.Linq.Async` in files containing EF Core `DbSet` queries.",
        "diagramTitle": "System.Linq.Async WhereAwait & SelectAwait Pipeline",
        "diagramSteps": [
            ["INPUT_STREAM", "IAsyncEnumerable Stream", "Asynchronous stream yielding raw entity IDs over network", "Stream Flowing"],
            ["WHERE_AWAIT", "WhereAwait Async Check", "Awaits Redis cache check: await authService.IsActiveAsync(id)", "Async Predicate"],
            ["FILTER_DECISION", "Filter Gate", "Yields element if async check returns true; discards if false", "Filtered Stream"],
            ["SELECT_AWAIT", "SelectAwait Transform", "Awaits HTTP API call: await profileService.Fetch(id)", "Async Projection"],
            ["TO_LIST_ASYNC", "ToListAsync Materialize", "Asynchronously drains pipeline into List<T> with zero thread blocking", "List Materialized"]
        ],
        "diagramArchetype": "async",
        "explanation": make_explanation(
            "System.Linq.Async Architecture",
            "Authored under the ReactiveX umbrella by Microsoft engineers, `System.Linq.Async` implements the Ix (Interactive Extensions) specification for pull-based async sequences.",
            "Each `*Await` method accepts a `Func<T, ValueTask<bool>>` or `Func<T, ValueTask<TResult>>`, allowing both zero-allocation synchronous completions and true asynchronous delays.",
            "// Resolving EF Core Ambiguity:\n// In EF Core files, use EF Core's native operators:\nusing Microsoft.EntityFrameworkCore;\n// In Async Stream files, use System.Linq.Async explicitly:\nusing System.Linq;",
            "Because `WhereAwait` executes sequentially, if you need concurrent async validation across 10 items at a time, use `Parallel.ForEachAsync` or `SemaphoreSlim` batching.",
            "Overhead of `WhereAwait` on a pre-buffered stream is ~35 nanoseconds per element."
        )
    })

    # Q3471
    qs.append({
        "id": 3471,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Cancellation Token Propagation in Async LINQ: The Role of [EnumeratorCancellation]",
        "answer": "**In Plain English:** When a customer cancels an online order, you want the warehouse to stop packing the box immediately. If you don't use `[EnumeratorCancellation]`, the warehouse worker's phone is disconnected, and they keep packing boxes for hours even though the customer cancelled the order long ago.\n\n**Interview Answer:** In `IAsyncEnumerable<T>`, cancellation tokens can be passed at two distinct times: 1) When invoking the generator method itself (`GetStream(cancellationToken)`), or 2) When consuming the stream via `.WithCancellation(cancellationToken)` or `await foreach`. Without the `[EnumeratorCancellation]` attribute on the generator's parameter, the compiler cannot correlate the token supplied at enumeration time with the generator's internal parameter, causing the generator to ignore consumer cancellation requests and leak resources.",
        "concept": "`[EnumeratorCancellation]` binds the token passed at consumption time (`WithCancellation`) to the generator's internal cancellation token.",
        "howItWorks": "When the compiler compiles `[EnumeratorCancellation] CancellationToken ct = default`, it synthesizes code in `GetAsyncEnumerator(CancellationToken token)` that combines or replaces the method's parameter with the enumeration token. This ensures `ct.IsCancellationRequested` fires if the consumer cancels the loop.",
        "whyWhen": "Mandatory in all long-running asynchronous generators, background services, WebSocket streaming, and Server-Sent Events (SSE).",
        "example": "An ASP.NET Core endpoint streaming live stock prices: when the browser closes the tab, `HttpContext.RequestAborted` cancels the generator immediately.",
        "code": "public class StockTickerService\n{\n    // CORRECT PATTERN: Always decorate with [EnumeratorCancellation]!\n    public async IAsyncEnumerable<StockPrice> StreamPricesAsync(\n        string ticker,\n        [EnumeratorCancellation] CancellationToken cancellationToken = default)\n    {\n        while (!cancellationToken.IsCancellationRequested)\n        {\n            // Pass cancellationToken to all internal async I/O calls:\n            StockPrice price = await _marketApi.FetchNextTickAsync(ticker, cancellationToken);\n            yield return price;\n            \n            // Non-blocking async delay honoring cancellation:\n            await Task.Delay(1000, cancellationToken);\n        }\n    }\n}\n\n// CONSUMPTION IN CONTROLLER / SERVICE:\nvar cts = new CancellationTokenSource(TimeSpan.FromSeconds(10));\n\n// WithCancellation properly binds cts.Token into StreamPricesAsync:\nawait foreach (var tick in service.StreamPricesAsync(\"MSFT\").WithCancellation(cts.Token))\n{\n    Console.WriteLine($\"Tick: {tick.Price}\");\n}",
        "codeLang": "csharp",
        "pros": [
            "Guarantees prompt cancellation and resource cleanup when consumers abort",
            "Allows multiple consumers to iterate the same query with different cancellation lifecycles"
        ],
        "cons": [
            "Forgetting the attribute causes silent cancellation failure that passes initial testing",
            "Throwing `OperationCanceledException` must be caught cleanly by the caller"
        ],
        "followups": [
            "What happens if a token is passed BOTH to the method call AND to `WithCancellation()`?",
            "How does `CancellationTokenSource.CreateLinkedTokenSource` handle dual cancellation tokens?"
        ],
        "seniorInsight": "If both a method-level token AND a `WithCancellation()` token are supplied, the Roslyn-generated state machine automatically combines them using `CancellationTokenSource.CreateLinkedTokenSource()`! This ensures that cancelling EITHER the global host token OR the consumer-specific token will halt the generator.",
        "diagramTitle": "EnumeratorCancellation Token Propagation Binding",
        "diagramSteps": [
            ["STREAM_DEF", "Async Stream Defined", "StreamPricesAsync([EnumeratorCancellation] CancellationToken ct)", "Method Signature"],
            ["CONSUMER_BIND", "WithCancellation(token)", "Consumer passes HTTP request abortion token via .WithCancellation(token)", "Token Bound"],
            ["COMPILER_MAP", "Roslyn Token Injection", "[EnumeratorCancellation] replaces default parameter with consumer token", "Token Injected"],
            ["ABORT_SIGNAL", "Client Aborts Request", "Client terminates connection: CancellationTokenSource signals abort", "Abort Signaled"],
            ["GRACEFUL_EXIT", "Instant Cancellation", "MoveNextAsync() catches cancellation; disposes generator immediately", "Zero Orphaned I/O"]
        ],
        "diagramArchetype": "circuit_breaker",
        "explanation": make_explanation(
            "EnumeratorCancellation Mechanics",
            "The `IAsyncEnumerable<T>` specification allows a stream to be created once and enumerated many times by different consumers, each with their own `CancellationToken`.",
            "Roslyn inspects parameter attributes during async state machine compilation: `[EnumeratorCancellation]` creates a bridge between `GetAsyncEnumerator(token)` and the state machine's internal token field.",
            "// ASP.NET Core SSE Endpoint Pattern:\n[HttpGet(\"live-stream\")]\npublic async IAsyncEnumerable<Event> Stream([EnumeratorCancellation] CancellationToken ct)\n{\n    await foreach (var evt in _eventHub.SubscribeAsync(ct))\n        yield return evt;\n}",
            "Never call `cancellationToken.ThrowIfCancellationRequested()` inside a generator if you want to complete cleanly with `yield break`.",
            "Checking `cancellationToken.IsCancellationRequested` takes ~1-2 nanoseconds."
        )
    })

    # Q3472
    qs.append({
        "id": 3472,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "architecture",
        "q": "Combining Async Streams: Merge, Zip, and Concat in Asynchronous LINQ",
        "answer": "**In Plain English:** Combining streams is like combining rivers: `Concat` waits until River 1 completely dries up before letting River 2 flow; `Zip` forces boats from River 1 and River 2 to hold hands in pairs before passing; `Merge` lets water from both rivers flow into the ocean simultaneously as fast as it arrives.\n\n**Interview Answer:** When combining multiple `IAsyncEnumerable<T>` streams, three core strategies exist: 1) **Concat:** Sequential execution where stream B begins only after stream A completely finishes. 2) **Zip:** Pairwise synchronization where each step awaits one element from stream A and one element from stream B, emitting a combined tuple. 3) **Merge:** Concurrent multiplexing where multiple async streams are read concurrently, and elements from any stream are immediately yielded downstream as soon as they arrive.",
        "concept": "Async streams can be combined sequentially (`Concat`), pairwise (`Zip`), or concurrently multiplexed (`Merge`).",
        "howItWorks": "`Merge` launches concurrent background tasks reading from each stream, writing into a shared `Channel<T>`. As items arrive from any stream, they are yielded downstream. `Zip` calls `MoveNextAsync()` on both streams concurrently via `Task.WhenAll`, combining their results.",
        "whyWhen": "Essential in dashboard aggregation (merging live order, user, and alert feeds), dual-stream telemetry processing, and coordinating microservice event streams.",
        "example": "Merging real-time trade feeds from Binance and Coinbase into a unified crypto pricing stream.",
        "code": "IAsyncEnumerable<Trade> binance = GetBinanceStreamAsync();\nIAsyncEnumerable<Trade> coinbase = GetCoinbaseStreamAsync();\n\n// 1. CONCAT (Sequential: Coinbase never runs until Binance completes!)\nIAsyncEnumerable<Trade> sequential = binance.Concat(coinbase);\n\n// 2. ZIP (Pairwise: waits for 1 trade from each before emitting pair):\nIAsyncEnumerable<(Trade A, Trade B)> paired = binance.Zip(coinbase);\n\n// 3. MERGE (Concurrent Multiplexing via Channel):\npublic static async IAsyncEnumerable<T> MergeAsync<T>(\n    params IAsyncEnumerable<T>[] streams)\n{\n    var channel = Channel.CreateUnbounded<T>();\n    var tasks = streams.Select(async s =>\n    {\n        await foreach (var item in s)\n        {\n            await channel.Writer.WriteAsync(item);\n        }\n    }).ToArray();\n    \n    _ = Task.WhenAll(tasks).ContinueWith(_ => channel.Writer.Complete());\n    \n    await foreach (var item in channel.Reader.ReadAllAsync())\n    {\n        yield return item;\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "Enables complex multi-source event-driven reactive architectures in pure C#",
            "`Merge` eliminates head-of-line blocking between independent streams"
        ],
        "cons": [
            "Concurrent `Merge` does not preserve deterministic ordering",
            "Unhandled exceptions in any single merged stream must be propagated cleanly"
        ],
        "followups": [
            "How does `Channel<T>` prevent race conditions when multiple async streams write concurrently in `Merge`?",
            "What happens to `Zip` if one async stream is significantly slower than the other?"
        ],
        "seniorInsight": "In high-throughput event processing, never use `Zip` on asynchronous streams with unequal arrival rates! If Stream A emits 1,000 items/sec and Stream B emits 1 item/sec, Stream A will be completely choked, waiting for Stream B to yield its partner. Use `Merge` with a keyed dictionary cache instead.",
        "diagramTitle": "Async Stream Combination: Concat vs Zip vs Merge",
        "diagramSteps": [
            ["STREAMS_IN", "Dual Async Sources", "Source A (Fast Trade Feed) and Source B (Slow Alert Feed)", "Streams Active"],
            ["CONCAT_PATH", "Concat (Sequential)", "A runs to completion; B is completely blocked until A finishes", "Sequential Flow"],
            ["ZIP_PATH", "Zip (Pairwise)", "Awaits pair: (A1, B1) -> (A2, B2); throttled by slowest stream", "Synchronized Pairs"],
            ["MERGE_PATH", "Merge (Multiplexed)", "Both streams write concurrently into non-blocking Channel", "Multiplexed Inflow"],
            ["EMIT_OUT", "Real-Time Yield", "Emits elements immediately upon arrival with zero head-of-line delay", "Instant Throughput"]
        ],
        "diagramArchetype": "async",
        "explanation": make_explanation(
            "Async Stream Combination Strategies",
            "Managing multiple asynchronous streams requires choosing between order preservation and latency optimization.",
            "In `System.Linq.Async`, `Concat` and `Zip` are built-in. `Merge` is provided by reactive libraries (Rx.NET / `System.Reactive.Linq`) or implemented via `Channel<T>`.",
            "// Rx.NET Observable Merge comparison:\n// IObservable<T> merged = Observable.Merge(streamA, streamB);",
            "When implementing custom `Merge` using channels, always ensure that exceptions from worker tasks complete the channel with an error (`channel.Writer.Complete(ex)`).",
            "Merging 4 concurrent async streams through an unbounded channel processes ~5,000,000 items/sec."
        )
    })

    # Q3473
    qs.append({
        "id": 3473,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Time-Based and Count-Based Buffering in Async LINQ: Implementing Buffer(TimeSpan, count)",
        "answer": "**In Plain English:** Imagine an express airport shuttle van: it leaves the terminal as soon as 10 passengers get on board OR every 15 minutes, whichever happens first. It never leaves empty, and passengers never wait longer than 15 minutes.\n\n**Interview Answer:** In streaming architectures, sending records individually causes network overhead, while fixed-count chunking causes latency starvation during slow traffic. A hybrid **Time-and-Count Bounded Buffer** (`Buffer(TimeSpan window, int maxCount)`) buffers items until *either* $N$ items have arrived *or* a timespan $T$ has elapsed since the first buffered item. This ensures high-throughput batching during traffic bursts while guaranteeing low latency during slow periods.",
        "concept": "Time-and-count buffering flushes batches when either count threshold $N$ or timeout $T$ is reached.",
        "howItWorks": "An async generator reads from the source with a timeout. When the first item arrives, it starts a timer. If count reaches `maxCount`, it yields the batch immediately and cancels the timer. If the timer expires first, it yields whatever partial batch has accumulated and resets.",
        "whyWhen": "Mandatory in telemetry collectors (OpenTelemetry, Serilog), event logging pipelines (ElasticSearch, Splunk), and message broker batching (Kafka, Event Hubs).",
        "example": "Flushing audit events to database in batches of 500 records OR every 2 seconds, whichever comes first.",
        "code": "public static async IAsyncEnumerable<List<T>> BufferWithTimeout<T>(\n    this IAsyncEnumerable<T> source,\n    int maxCount,\n    TimeSpan maxTimeout,\n    [EnumeratorCancellation] CancellationToken ct = default)\n{\n    var batch = new List<T>(maxCount);\n    var channel = Channel.CreateBounded<T>(maxCount);\n    \n    // Producer task feeding channel\n    var enumerator = source.GetAsyncEnumerator(ct);\n    \n    while (true)\n    {\n        using var timeoutCts = new CancellationTokenSource(maxTimeout);\n        using var linkedCts = CancellationTokenSource.CreateLinkedTokenSource(ct, timeoutCts.Token);\n        \n        try\n        {\n            while (batch.Count < maxCount)\n            {\n                if (await enumerator.MoveNextAsync().AsTask().WaitAsync(timeoutCts.Token))\n                {\n                    batch.Add(enumerator.Current);\n                }\n                else\n                {\n                    // Upstream source completed!\n                    if (batch.Count > 0) yield return batch;\n                    yield break;\n                }\n            }\n        }\n        catch (TimeoutException)\n        {\n            // Timeout elapsed before batch reached maxCount! Flush partial batch:\n        }\n        \n        if (batch.Count > 0)\n        {\n            yield return batch;\n            batch = new List<T>(maxCount); // Fresh batch\n        }\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "Optimizes database bulk insert throughput while guaranteeing latency SLAs",
            "Eliminates stale data sitting in buffers during low-traffic hours"
        ],
        "cons": [
            "Requires careful timer and cancellation token management to prevent timer thread leaks",
            "Batches may vary in size from 1 to `maxCount`"
        ],
        "followups": [
            "How does Serilog's `PeriodicBatchingSink` implement this exact architectural pattern?",
            "What is the difference between tumbling time windows and sliding time windows?"
        ],
        "seniorInsight": "This pattern is the foundation of every high-performance database sink (Serilog, Kafka Producer, ElasticSearch Sink). Never send database inserts one-by-one, and never use pure count chunking (or late-night records will sit in memory until morning). Always pair count limits with a 1-5 second timeout flush.",
        "diagramTitle": "Time & Count Bounded Flush Architecture",
        "diagramSteps": [
            ["EVENT_IN", "Streaming Events", "Events arrive at irregular intervals: high burst during day, trickle at night", "Stream Active"],
            ["BATCH_BUFFER", "Accumulator Buffer", "Events accumulate in memory buffer sized to maxCount = 500", "Buffer Filling"],
            ["TRIGGER_A", "Condition A: Count = 500", "Bursts hit 500 items: immediate flush! Timer cancelled", "Count Flush"],
            ["TRIGGER_B", "Condition B: Timeout = 2s", "Slow trickle: 2-second timer expires with 12 items in buffer", "Timeout Flush"],
            ["DATABASE_SINK", "Bulk Insert Execution", "Flushes batch to database; satisfies both latency SLA and throughput", "Optimal SLA"]
        ],
        "diagramArchetype": "circuit_breaker",
        "explanation": make_explanation(
            "Time-and-Count Buffering Architecture",
            "In distributed systems, pure count-based buffering causes latency violations when traffic drops. Pure time-based buffering causes memory spikes during flash sales or DDoS spikes.",
            "Hybrid buffering bounds both dimensions: maximum memory is bounded by $N \\times \\text{sizeof}(T)$, and maximum latency is bounded by $T$.",
            "// Enterprise Sink Configuration Pattern:\npublic class BatchConfig {\n    public int BatchSize { get; set; } = 1000;\n    public TimeSpan FlushInterval { get; set; } = TimeSpan.FromSeconds(2);\n}",
            "Always ensure that when the application shuts down, the buffer's `finally` block flushes any remaining items to disk before process exit.",
            "Flushing 1,000 items in a single batch executes in ~1.2 ms vs ~450 ms for 1,000 individual inserts."
        )
    })

    # Q3474
    qs.append({
        "id": 3474,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "comparison",
        "q": "Push vs Pull Architecture: Reactive Extensions (IObservable<T>) vs Async LINQ (IAsyncEnumerable<T>)",
        "answer": "**In Plain English:** Pull (`IAsyncEnumerable`) is like checking your physical mailbox: you walk out to the box and pull letters out whenever you feel like it. Push (`IObservable`) is like getting an incoming telephone call: the phone rings and pushes the conversation into your ear whether you are ready or not.\n\n**Interview Answer:** `IAsyncEnumerable<T>` is an **asynchronous pull-based** model (dual to `IEnumerable<T>`). The consumer controls the pacing by requesting the next element via `await MoveNextAsync()`, providing natural backpressure. In contrast, `IObservable<T>` (Reactive Extensions / Rx.NET) is an **asynchronous push-based** model. The producer controls the pacing, pushing items to the observer via `OnNext(T)`. Because the producer pushes uninvited, `IObservable` requires explicit backpressure strategies (buffering, throttling, dropping) to prevent consumer overwhelm.",
        "concept": "`IAsyncEnumerable` is pull-based with consumer-controlled pacing; `IObservable` is push-based with producer-controlled pacing.",
        "howItWorks": "In `IAsyncEnumerable`, the consumer thread executes `await foreach`. The producer pauses until `MoveNextAsync()` is called. In `IObservable`, the producer raises `observer.OnNext(item)` whenever an event occurs; if the observer's handler is slow, events pile up on the thread.",
        "whyWhen": "Use `IAsyncEnumerable<T>` for reading data (databases, files, REST API pages, queues). Use `IObservable<T>` for un-throttled UI events (clicks, mouse moves), hardware sensor signals, and distributed pub/sub webhooks.",
        "example": "Streaming database query results: `IAsyncEnumerable` ensures the database only reads rows as the network socket sends them.",
        "code": "// 1. PULL MODEL (IAsyncEnumerable): Consumer pulls next item\nawait foreach (var item in GetDatabaseRowsAsync())\n{\n    // Producer waits for consumer to finish processing before sending next row!\n    await ProcessRowAsync(item);\n}\n\n// 2. PUSH MODEL (IObservable / Rx.NET): Producer pushes when event fires\nIObservable<MouseEvent> mouseMoves = GetMouseEvents();\n\nIDisposable subscription = mouseMoves\n    .Sample(TimeSpan.FromMilliseconds(100)) // Throttle push stream!\n    .Subscribe(evt => \n    {\n        // Producer calls this callback asynchronously whenever user moves mouse!\n        UpdateCoordinates(evt.X, evt.Y);\n    });",
        "codeLang": "csharp",
        "pros": [
            "`IAsyncEnumerable` provides natural, automatic backpressure without complex operators",
            "`IObservable` provides rich temporal operators (`Throttle`, `Sample`, `Debounce`, `Buffer`, `Window`)"
        ],
        "cons": [
            "`IAsyncEnumerable` cannot easily represent multi-cast events where 50 listeners need the same push notification",
            "`IObservable` without backpressure can easily trigger OutOfMemory under high-throughput event storms"
        ],
        "followups": [
            "How do you convert an `IObservable<T>` to an `IAsyncEnumerable<T>` and vice versa?",
            "What is the mathematical duality between Iterator and Observer patterns published by Erik Meijer?"
        ],
        "seniorInsight": "Architectural rule of thumb: If you are querying **DATA AT REST or IN TRANSIT** (SQL queries, API pagination, S3 downloads), always use `IAsyncEnumerable<T>`. If you are listening to **UNSOLICITED REAL-TIME EVENTS** (UI mouse moves, SignalR notifications, WebSockets, hardware interrupts), use `IObservable<T>` with explicit throttling.",
        "diagramTitle": "Pull Architecture (IAsyncEnumerable) vs Push Architecture (IObservable)",
        "diagramSteps": [
            ["PULL_MODEL", "IAsyncEnumerable (Pull)", "Consumer controls pace: calls MoveNextAsync() when ready for item", "Consumer Driven"],
            ["PULL_BACKPRESSURE", "Natural Backpressure", "Producer pauses execution until consumer requests next item", "Zero Overflow"],
            ["PUSH_MODEL", "IObservable (Push)", "Producer controls pace: fires OnNext(item) whenever event occurs", "Producer Driven"],
            ["PUSH_CHOKE", "Consumer Saturation", "If consumer is slow, unconsumed push events buffer or cause latency", "Backpressure Risk"],
            ["CONVERSION", "System.Linq.AsyncObservable", "Channels bridge push events into pull streams safely via bounded buffers", "Architectural Fit"]
        ],
        "diagramArchetype": "pub_sub",
        "explanation": make_explanation(
            "Push vs Pull Duality Mechanics",
            "Erik Meijer proved the mathematical duality between the Gang of Four Iterator pattern (`IEnumerable`) and the Observer pattern (`IObservable`). One is the exact mathematical inverse of the other.",
            "`IAsyncEnumerable` represents pull over time: `Task<bool> MoveNext()`. `IObservable` represents push over time: `void OnNext(T)`.",
            "// Converting IObservable to IAsyncEnumerable (.NET 7+):\n// IAsyncEnumerable<T> stream = observable.ToAsyncEnumerable();",
            "In modern ASP.NET Core, `IAsyncEnumerable<T>` returned from a controller action is automatically streamed to the client as chunked HTTP response data.",
            "`IAsyncEnumerable` requires ~0 extra bytes for backpressure because execution suspension is built directly into the C# language grammar."
        )
    })

    # Q3475
    qs.append({
        "id": 3475,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "architecture",
        "q": "Streaming Database Rows with EF Core AsAsyncEnumerable: Preventing OutOfMemory in Bulk Data Exports",
        "answer": "**In Plain English:** Calling `.ToListAsync()` on 500,000 database rows is like ordering 500,000 books from Amazon and demanding they all be crammed into your tiny living room before you open the first box (your house explodes). `AsAsyncEnumerable()` is like having a delivery conveyor belt straight into your hands: you read one book, pack it into a truck, and the next book arrives, keeping your living room completely empty.\n\n**Interview Answer:** Calling `.ToListAsync()` on a massive database query loads and materializes all matching entities into CLR memory simultaneously. For 1,000,000 rows, this consumes gigabytes of heap RAM and triggers Gen 2 garbage collections. Calling `.AsAsyncEnumerable()` on an EF Core `IQueryable` streams rows directly from the underlying ADO.NET `DbDataReader` one-by-one as they arrive over the TDS/Postgres network stream. Combined with `.AsNoTracking()`, memory consumption remains flat (O(1) memory), allowing multi-gigabyte data exports to run smoothly with only 15 MB of server RAM.",
        "concept": "EF Core `AsAsyncEnumerable()` streams database rows directly from `DbDataReader` with constant O(1) memory footprint.",
        "howItWorks": "Under the hood, `AsAsyncEnumerable()` wraps `DbDataReader.ReadAsync()`. As each database packet arrives from SQL Server, EF Core materializes a single entity, yields it to the `await foreach` consumer, and immediately allows it to be collected if no tracking is enabled.",
        "whyWhen": "Mandatory for CSV/Excel data exports, ETL data migration jobs, syncing databases, and generating large JSON feeds.",
        "example": "Exporting 2,000,000 transaction records to a CSV file: `.ToListAsync()` crashes with OOM; `AsAsyncEnumerable()` runs in 5 seconds with 12 MB of RAM.",
        "code": "public async Task ExportTransactionsCsvAsync(Stream outputStream, CancellationToken ct)\n{\n    await using var writer = new StreamWriter(outputStream);\n    \n    // CRITICAL: 1. AsNoTracking disables EF Core change tracker\n    // CRITICAL: 2. AsAsyncEnumerable streams directly from ADO.NET DbDataReader\n    var query = dbContext.Transactions\n        .AsNoTracking() // 0 Change Tracker memory overhead!\n        .Where(t => t.Year == 2024)\n        .OrderBy(t => t.Id)\n        .AsAsyncEnumerable(); // Returns IAsyncEnumerable<Transaction>\n        \n    await foreach (var tx in query.WithCancellation(ct))\n    {\n        // Writes line-by-line directly to network stream:\n        await writer.WriteLineAsync($\"{tx.Id},{tx.AccountNumber},{tx.Amount},{tx.Date}\");\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "Flattens memory usage to a constant ~15 MB regardless of whether querying 1,000 or 10,000,000 rows",
            "Eliminates initial query latency: data export begins streaming in milliseconds instead of waiting for full query completion"
        ],
        "cons": [
            "Holds open the underlying database connection for the entire duration of the stream",
            "Cannot execute another query on the same `DbContext` instance concurrently (throws `InvalidOperationException`)"
        ],
        "followups": [
            "Why must `.AsNoTracking()` always be paired with `AsAsyncEnumerable()` during bulk exports?",
            "What happens to the database connection if the client disconnects halfway through the export?"
        ],
        "seniorInsight": "ALWAYS pair `.AsAsyncEnumerable()` with `.AsNoTracking()`! If you omit `AsNoTracking()`, EF Core's Change Tracker will take a reference to every single entity yielded, storing all 1,000,000 entities in memory anyway and causing the exact OutOfMemory crash you were trying to prevent.",
        "diagramTitle": "EF Core ToListAsync() Memory Spike vs AsAsyncEnumerable() Streaming",
        "diagramSteps": [
            ["QUERY_START", "Database Query Dispatched", "SELECT * FROM Transactions WHERE Year = 2024 (1,000,000 rows)", "Query Dispatched"],
            ["TOLIST_PATH", "ToListAsync() Memory Spike", "Buffers 1M entities in memory + Change Tracker: 3.8 GB RAM -> OOM Crash!", "OOM Crash"],
            ["ASYNC_STREAM", "AsAsyncEnumerable() + AsNoTracking", "Wraps DbDataReader.ReadAsync(); yields row-by-row with 0 tracking", "O(1) Streaming"],
            ["HTTP_WRITE", "Direct Output Streaming", "Writes each CSV line directly to HttpResponse.Body stream", "Stream Piped"],
            ["FLAT_RAM", "Flat 15 MB RAM Footprint", "Entire 2,000,000-row export finishes with flat 15 MB memory profile", "Production Grade"]
        ],
        "diagramArchetype": "pipeline",
        "explanation": make_explanation(
            "EF Core Streaming Mechanics",
            "`DbDataReader` is a forward-only, read-only cursor over database TDS (Tabular Data Stream) packets. `AsAsyncEnumerable()` exposes this forward-only cursor directly to C#.",
            "Because an open `DbDataReader` locks the underlying `SqlConnection`, the `DbContext` instance cannot be used for any other operation until the stream is completely consumed or disposed.",
            "// Streaming Direct to HTTP Response in ASP.NET Core:\n[HttpGet(\"export\")]\npublic IAsyncEnumerable<TransactionDto> Export() {\n    return db.Transactions.AsNoTracking().Select(t => new TransactionDto(t.Id, t.Amount)).AsAsyncEnumerable();\n}",
            "If the network connection to the client slows down, TCP flow control slows down the database stream automatically, applying natural backpressure all the way back to SQL Server.",
            "Streaming 1,000,000 rows takes ~15 MB of RAM and ~4.8 seconds over a gigabit connection."
        )
    })

    # Q3476
    qs.append({
        "id": 3476,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Throttling and Concurrency Limiting in Async LINQ: Managing Parallelism with SemaphoreSlim",
        "answer": "**In Plain English:** If you have 1,000 documents to print, sending all 1,000 print jobs simultaneously will jam the printer and crash the print server. A `SemaphoreSlim` is like a velvet rope at a nightclub that only lets 5 people inside at any given time; as one person leaves, the next person in line is allowed in.\n\n**Interview Answer:** When executing asynchronous operations across sequences (e.g. calling an external HTTP API for each element in a list), using `Task.WhenAll(source.Select(FetchAsync))` fires all requests simultaneously. If the sequence has 10,000 items, sending 10,000 concurrent HTTP calls exhausts socket connections, triggers rate limits (HTTP 429), and saturates the thread pool. Using `SemaphoreSlim(maxConcurrency)` or .NET 6's `Parallel.ForEachAsync` throttles concurrency to a controlled limit (e.g. max 10 concurrent requests), maximizing throughput while honoring third-party API quotas.",
        "concept": "`SemaphoreSlim` bounds the maximum number of concurrent asynchronous operations in an async LINQ pipeline.",
        "howItWorks": "A `SemaphoreSlim(maxConcurrency)` is initialized. Before starting each asynchronous operation, the worker awaits `semaphore.WaitAsync()`. Once inside, it performs the I/O task. Inside a `finally` block, it calls `semaphore.Release()`, granting access to the next waiting item.",
        "whyWhen": "Essential when calling rate-limited third-party APIs (Stripe, Twilio, OpenAI), scraping web pages, or uploading batch files to S3/Azure Blob Storage.",
        "example": "Sending 50,000 SMS messages via Twilio while capping concurrency to exactly 20 simultaneous HTTP calls.",
        "code": "public static async Task<List<TResult>> ProcessThrottledAsync<TSource, TResult>(\n    this IEnumerable<TSource> source,\n    Func<TSource, Task<TResult>> processor,\n    int maxConcurrency = 10,\n    CancellationToken ct = default)\n{\n    using var semaphore = new SemaphoreSlim(maxConcurrency, maxConcurrency);\n    \n    var tasks = source.Select(async item =>\n    {\n        // Asynchronously wait for available semaphore slot:\n        await semaphore.WaitAsync(ct);\n        try\n        {\n            return await processor(item);\n        }\n        finally\n        {\n            // MUST release in finally to prevent permanent deadlock!\n            semaphore.Release();\n        }\n    });\n    \n    return (await Task.WhenAll(tasks)).ToList();\n}\n\n// MODERN .NET 6+ ALTERNATIVE (Parallel.ForEachAsync):\nawait Parallel.ForEachAsync(source, new ParallelOptions \n{\n    MaxDegreeOfParallelism = 10, \n    CancellationToken = ct \n}, async (item, token) =>\n{\n    await SendSmsAsync(item, token);\n});",
        "codeLang": "csharp",
        "pros": [
            "Prevents HTTP socket exhaustion, DNS throttling, and HTTP 429 rate limit bans",
            "Smooths out CPU and memory utilization across the lifetime of the batch"
        ],
        "cons": [
            "Creating 50,000 `Task` objects up front via `source.Select(...)` still allocates task memory (use `Parallel.ForEachAsync` to stream)",
            "Forgetting to call `semaphore.Release()` in a `finally` block causes permanent pipeline deadlocks"
        ],
        "followups": [
            "Why is `Parallel.ForEachAsync` preferred over `Task.WhenAll(source.Select(...))` for massive collections?",
            "How does `SemaphoreSlim.WaitAsync()` differ from `Monitor.Enter()` in asynchronous programming?"
        ],
        "seniorInsight": "Prefer `Parallel.ForEachAsync` (introduced in .NET 6) over `Task.WhenAll(source.Select(...))`! With `Task.WhenAll`, even with a semaphore, you instantiate all 100,000 Task state machine objects immediately in memory. `Parallel.ForEachAsync` only pulls items as worker slots become free, keeping memory constant and execution blazing fast.",
        "diagramTitle": "SemaphoreSlim Controlled Concurrency Throttle",
        "diagramSteps": [
            ["INPUT_BATCH", "10,000 Items Input", "High-volume batch requiring remote HTTP API processing", "Batch Queued"],
            ["SEMAPHORE_GATE", "SemaphoreSlim(10)", "Semaphore initialized with 10 tokens: max 10 concurrent HTTP calls", "Gate Armed (10)"],
            ["DISPATCH_SLOTS", "10 Concurrent Tasks", "Tasks 1-10 acquire tokens: execute HTTP requests concurrently", "10 Running"],
            ["TOKEN_RELEASE", "Release in Finally", "Task 3 completes: releases token in finally block; slot freed", "Token Freed"],
            ["NEXT_ITEM", "Next Item Admitted", "Task 11 immediately acquires token; throughput locked at 10 active calls", "Zero Socket Flood"]
        ],
        "diagramArchetype": "concurrency_deadlock",
        "explanation": make_explanation(
            "Concurrency Throttling Mechanics",
            "`SemaphoreSlim` is a lightweight, asynchronous-compatible synchronization primitive that does not rely on Windows OS kernel handles.",
            "Calling `await semaphore.WaitAsync()` suspends execution without blocking an operating system thread, enqueuing the continuation into a lock-free queue.",
            "// Modern .NET 6+ Parallel.ForEachAsync Pattern:\nvar options = new ParallelOptions { MaxDegreeOfParallelism = 8 };\nawait Parallel.ForEachAsync(urls, options, async (url, token) => {\n    await DownloadFileAsync(url, token);\n});",
            "Never call `semaphore.Wait()` synchronously inside an async method; that burns a thread pool thread while waiting.",
            "`SemaphoreSlim` acquire and release takes ~25 nanoseconds on modern x64 hardware."
        )
    })

    # Q3477
    qs.append({
        "id": 3477,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "architecture",
        "q": "Resilience and Polly Retry Policies Inside Async LINQ Pipelines",
        "answer": "**In Plain English:** When streaming 10,000 orders to a payment gateway, if transaction #500 fails due to a 2-second Wi-Fi hiccup, a brittle system crashes and throws away all progress. A resilient pipeline automatically pauses, retries transaction #500 with exponential backoff, and continues smoothly down the stream.\n\n**Interview Answer:** In distributed systems, transient network glitches, socket resets, and temporary HTTP 503 service outages are inevitable. Embedding resilience directly inside async LINQ pipelines ensures that individual transient item failures are automatically retried without aborting the entire sequence. In modern .NET, this is implemented using **Polly** (or `Microsoft.Extensions.Resilience`) configured with Exponential Backoff, Jitter, and Circuit Breakers wrapped around the item projection delegate.",
        "concept": "Resilience policies wrap async stream item evaluation, isolating transient failures and retrying with exponential backoff.",
        "howItWorks": "A resilience pipeline is constructed with `ResiliencePipelineBuilder`. Inside the async LINQ operator, each element execution is wrapped in `await pipeline.ExecuteAsync(async token => await ProcessItem(item, token), ct)`. If a transient exception occurs, Polly retries up to $K$ times with jittered delays.",
        "whyWhen": "Mandatory in microservice event processors, payment gateway integrations, cloud storage batch uploads, and distributed database synchronizations.",
        "example": "Streaming 100,000 telemetry messages to AWS Kinesis: retrying transient network drops transparently.",
        "code": "using Polly;\nusing Polly.Retry;\n\n// 1. CONFIGURE RESILIENCE PIPELINE (.NET 8 Polly v8):\nvar pipeline = new ResiliencePipelineBuilder<HttpResponseMessage>()\n    .AddRetry(new RetryStrategyOptions<HttpResponseMessage>\n    {\n        MaxRetryAttempts = 3,\n        Delay = TimeSpan.FromMilliseconds(500),\n        BackoffType = DelayBackoffType.Exponential,\n        UseJitter = true, // Prevents thundering herd!\n        ShouldHandle = new PredicateBuilder<HttpResponseMessage>()\n            .Handle<HttpRequestException>()\n            .HandleResult(r => (int)r.StatusCode >= 500 || r.StatusCode == HttpStatusCode.TooManyRequests)\n    })\n    .Build();\n\n// 2. EMBED IN ASYNC LINQ STREAM:\nawait foreach (var order in GetOrdersAsyncStream())\n{\n    // Each order execution is protected by resilience pipeline:\n    var result = await pipeline.ExecuteAsync(async token =>\n    {\n        return await _httpClient.PostAsJsonAsync(\"https://api.payments.com/charge\", order, token);\n    });\n}",
        "codeLang": "csharp",
        "pros": [
            "Prevents transient network blips from terminating long-running streaming jobs",
            "Exponential backoff with jitter prevents thundering herd attacks on downstream APIs"
        ],
        "cons": [
            "Operations being retried MUST be idempotent to prevent duplicate side effects",
            "Excessive retries can delay batch completion if downstream services are experiencing hard outages"
        ],
        "followups": [
            "Why is 'Jitter' strictly required when configuring exponential backoff retry policies?",
            "What is the difference between Polly v7 and modern Polly v8 in .NET 8?"
        ],
        "seniorInsight": "Always add Jitter to your retry delays! If 1,000 concurrent streaming workers hit a database lock at 12:00:00, and all retry exactly 1.0 second later, all 1,000 workers will hit the database at 12:00:01 (Thundering Herd), crashing the database again. Jitter adds randomized delay (e.g. 1.0s +/- 250ms), spreading retries across time.",
        "diagramTitle": "Polly Resilience Retry with Exponential Backoff & Jitter",
        "diagramSteps": [
            ["STREAM_ITEM", "Stream Item Ingestion", "Async stream emits order #501 to external payment gateway", "Item Ingested"],
            ["HTTP_FAIL", "Transient HTTP 503", "Gateway responds with 503 Service Unavailable: glitch detected", "Transient Failure"],
            ["POLLY_RETRY_1", "Retry 1: Backoff + Jitter", "Polly pauses 512ms (exponential + random jitter): retries call", "Retry #1 (512ms)"],
            ["POLLY_RETRY_2", "Retry 2: Double Delay", "Gateway still warming up: Polly pauses 1,048ms: retries call", "Retry #2 (1048ms)"],
            ["SUCCESS_EMIT", "Recovery & Stream Continues", "Gateway recovers: HTTP 200 OK returned; stream proceeds to #502", "Stream Unbroken"]
        ],
        "diagramArchetype": "circuit_breaker",
        "explanation": make_explanation(
            "Resilience Pipeline Architecture",
            "Modern distributed architectures treat network failures as standard operating conditions, not exceptional anomalies. Polly v8 was co-developed with the .NET runtime team (`Microsoft.Extensions.Resilience`).",
            "Polly v8 is zero-allocation: it uses struct-based context builders, executing retries without heap churn.",
            "// Idempotency Header Pattern:\nvar request = new HttpRequestMessage(HttpMethod.Post, url);\nrequest.Headers.Add(\"Idempotency-Key\", order.Id.ToString());",
            "Never retry non-idempotent operations (like `POST /charge`) without an idempotency key; otherwise, retries will double-charge customer credit cards.",
            "Polly v8 executes in ~15 nanoseconds on the happy path with zero heap allocations."
        )
    })

    # Q3478
    qs.append({
        "id": 3478,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "architecture",
        "q": "IAsyncDisposable and Cleanup Guarantees in Async LINQ: Ensuring Finally Blocks Execute in await foreach",
        "answer": "**In Plain English:** If you borrow a book from a library, read 2 pages, and suddenly decide to leave early, you must still return the book to the counter and lock your locker. `IAsyncDisposable` guarantees that even if your loop breaks early or crashes, all open database connections, files, and network sockets are closed asynchronously without leaking.\n\n**Interview Answer:** When consuming an `IAsyncEnumerable<T>`, the underlying `IAsyncEnumerator<T>` implements `IAsyncDisposable`. When an `await foreach` loop terminates—whether by reaching the end of the stream, hitting a `break` statement, or throwing an unhandled exception—the compiler-generated code guarantees that `await enumerator.DisposeAsync()` is executed in a `finally` block. Inside the generator, this triggers the execution of all active `finally` blocks in the iterator, guaranteeing that database connections, network streams, and rented memory buffers are asynchronously released.",
        "concept": "`await foreach` guarantees that `IAsyncDisposable.DisposeAsync()` is called on early exit, executing generator `finally` blocks.",
        "howItWorks": "Roslyn transforms `await foreach` into a `try { while (await e.MoveNextAsync()) { ... } } finally { if (e != null) await e.DisposeAsync(); }`. When `DisposeAsync()` is called, the generator's state machine enters its cleanup state, executing enclosing `finally` statements.",
        "whyWhen": "Critical for preventing connection pool exhaustion, file handle locks, and memory leaks when using `Take()`, `First()`, or breaking out of loops early.",
        "example": "Opening a file with `FileStream`, reading lines until finding a match, and breaking: `finally` guarantees the file handle is unlocked immediately.",
        "code": "// ASYNC GENERATOR WITH RESOURCE CLEANUP:\npublic async IAsyncEnumerable<string> ReadLogLinesAsync(string path)\n{\n    // Resource must be cleaned up even if consumer calls break!\n    var stream = new FileStream(path, FileMode.Open, FileAccess.Read);\n    var reader = new StreamReader(stream);\n    \n    try\n    {\n        while (!reader.EndOfStream)\n        {\n            string? line = await reader.ReadLineAsync();\n            if (line != null) yield return line;\n        }\n    }\n    finally\n    {\n        // GUARANTEED TO EXECUTE on break, exception, or stream completion!\n        Console.WriteLine(\"Closing file stream asynchronously...\");\n        await reader.DisposeAsync();\n        await stream.DisposeAsync();\n    }\n}\n\n// CONSUMER (Breaking early):\nawait foreach (var line in ReadLogLinesAsync(\"app.log\"))\n{\n    if (line.Contains(\"FATAL\"))\n    {\n        // BREAKING EARLY: Triggers DisposeAsync() immediately!\n        break;\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "Prevents unmanaged resource leaks and database connection pool exhaustion",
            "Supports non-blocking asynchronous cleanup (`await DisposeAsync()`)"
        ],
        "cons": [
            "If consumer thread crashes hard (process termination / OutOfMemory), finally blocks cannot execute",
            "Exceptions thrown inside `finally` blocks can mask the original loop exception"
        ],
        "followups": [
            "What IL code does Roslyn generate for an `await foreach` loop under the hood?",
            "How does `IAsyncDisposable` differ from synchronous `IDisposable` in terms of thread blocking?"
        ],
        "seniorInsight": "Never use synchronous `using` or `IDisposable` inside an `async IAsyncEnumerable` generator if an asynchronous equivalent exists! Calling synchronous `stream.Dispose()` blocks an OS thread while waiting for I/O buffers to flush to disk. Always use `await using` and `await stream.DisposeAsync()` to keep thread pools free.",
        "diagramTitle": "await foreach Early Exit & IAsyncDisposable Cleanup",
        "diagramSteps": [
            ["LOOP_ENTER", "await foreach Enter", "Consumer opens async stream: compiler sets up try-finally block", "Loop Active"],
            ["ITERATE", "Yielding Data Lines", "Generator yields log lines; reader holds open OS file handle", "Handle Open"],
            ["EARLY_BREAK", "Consumer Break", "Consumer finds target line: executes 'break' to terminate early", "Break Triggered"],
            ["DISPOSE_ASYNC", "DisposeAsync() Invoked", "Compiler finally block calls await enumerator.DisposeAsync()", "Cleanup Dispatched"],
            ["FINALLY_RUN", "Generator Finally Runs", "Generator's finally block runs: await stream.DisposeAsync() closes handle", "Zero Resource Leak"]
        ],
        "diagramArchetype": "async",
        "explanation": make_explanation(
            "IAsyncDisposable Mechanics",
            "`IAsyncDisposable` was introduced in .NET Core 3.0 alongside C# 8. It defines `ValueTask DisposeAsync()`, enabling asynchronous resource release.",
            "Decompiling `await foreach (var item in source)` reveals the hidden plumbing: a rigorous `try/finally` block ensuring `DisposeAsync()` is awaited even during thread aborts or unhandled exceptions.",
            "// Decompiled await foreach structure:\nvar enumerator = source.GetAsyncEnumerator();\ntry {\n    while (await enumerator.MoveNextAsync()) { ... }\n} finally {\n    if (enumerator != null) await enumerator.DisposeAsync();\n}",
            "If both the loop body and `DisposeAsync()` throw an exception, the exception from the loop body is propagated, while the disposal exception is suppressed or attached.",
            "Disposing an async enumerator takes ~10-20 nanoseconds if already completed."
        )
    })

    return qs

print("Domain 6 module loaded successfully.")

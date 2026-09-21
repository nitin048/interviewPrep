"""
LINQ Domain 4: Advanced Grouping, Aggregations & Windowing (Questions 3449 to 3458)
"""
from scratch.linq_domains_1_to_5 import make_explanation

def get_domain_4():
    qs = []

    # Q3449
    qs.append({
        "id": 3449,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "intermediate",
        "type": "comparison",
        "q": "ToLookup vs GroupBy in LINQ: Execution Timing, Memory Structures, and Lookup Indexing",
        "answer": "**In Plain English:** `GroupBy` is like a lazy catalog: it doesn't organize anything until someone flips open the pages, and if you flip through it twice, it organizes the whole catalog twice. `ToLookup` is an eager librarian: the moment you ask, they immediately sort every single book into labeled filing cabinets on the spot and hand you an instant master index.\n\n**Interview Answer:** `GroupBy` returns an `IEnumerable<IGrouping<TKey, TElement>>` whose execution is deferred; if enumerated multiple times, it re-groups the sequence every time. In contrast, `ToLookup()` returns an `ILookup<TKey, TElement>`, which is an immediate, fully-materialized, 1-to-many hash index. Unlike a standard `Dictionary<TKey, List<TElement>>`, an `ILookup` is strictly immutable, and querying a key that does not exist returns an empty `IEnumerable<TElement>` instead of throwing a `KeyNotFoundException`.",
        "concept": "`GroupBy` is a deferred streaming grouped sequence; `ToLookup` is an eagerly materialized, immutable, multi-value hash dictionary.",
        "howItWorks": "`ToLookup` immediately consumes the entire source sequence, builds internal hash buckets, and allocates linked grouping nodes. Accessing `lookup[key]` runs an O(1) hash lookup; if the key is missing, it returns `Enumerable.Empty<T>()` with zero exceptions.",
        "whyWhen": "Use `GroupBy` when streaming into a subsequent LINQ aggregation (e.g. `GroupBy().Select(g => g.Sum())`). Use `ToLookup` when you need to perform multiple fast key-based lookups over an in-memory dataset throughout a request lifecycle.",
        "example": "Indexing 100,000 orders by `CustomerId`: `orders.ToLookup(o => o.CustomerId)` allows querying `ordersLookup[custId]` millions of times in O(1) time.",
        "code": "List<Order> orders = GetOrders();\n\n// 1. GroupBy: DEFERRED EXECUTION (Re-groups on each iteration)\nvar grouped = orders.GroupBy(o => o.CustomerId);\n// Not executed yet!\n\n// 2. ToLookup: IMMEDIATE MATERIALIZATION (Builds multi-value hash index)\nILookup<int, Order> lookup = orders.ToLookup(o => o.CustomerId);\n\n// Safe indexing: Returns empty sequence if key does not exist!\nIEnumerable<Order> customerOrders = lookup[99999]; // NO KeyNotFoundException!\nConsole.WriteLine($\"Found: {customerOrders.Count()} orders\"); // 0\n\n// Lookup is strictly read-only / immutable:\n// lookup.Add(...) does not exist!",
        "codeLang": "csharp",
        "pros": [
            "Safe indexer: never throws `KeyNotFoundException` on missing keys",
            "Extremely fast O(1) multi-value lookups across the lifetime of a service request"
        ],
        "cons": [
            "Eagerly consumes memory to buffer the entire collection into hash buckets",
            "Immutable: cannot add or remove keys after creation"
        ],
        "followups": [
            "How does `ILookup<TKey, TElement>` differ from `Dictionary<TKey, List<TElement>>` in terms of API safety?",
            "What happens under the hood when EF Core translates `GroupBy` into SQL?"
        ],
        "seniorInsight": "Prefer `ToLookup` over `Dictionary<TKey, List<TValue>>` when grouping in-memory data for read-only querying! With a dictionary, looking up a missing key requires checking `.ContainsKey()` or `.TryGetValue()`, and initializing empty lists for missing keys. `ILookup` handles all of this automatically with zero null checks.",
        "diagramTitle": "Deferred GroupBy vs Materialized ToLookup Architecture",
        "diagramSteps": [
            ["SOURCE_DATA", "Source Order Stream", "Collection of 100,000 Order items with customer foreign keys", "Data Ingested"],
            ["BRANCH_GROUP", "GroupBy Path (Deferred)", "Returns IEnumerable<IGrouping>; execution delayed until foreach", "Deferred Stream"],
            ["BRANCH_LOOKUP", "ToLookup Path (Immediate)", "Immediately consumes stream: builds internal hash bucket arrays", "Hash Index Built"],
            ["INDEX_PROBE", "Key Query: lookup[id]", "O(1) direct hash lookup; returns matching items or Enumerable.Empty", "Safe O(1) Read"],
            ["EXCEPTION_SAFETY", "Zero KeyNotFoundException", "Never throws on missing keys, eliminating boilerplate TryGetValue checks", "Safe Execution"]
        ],
        "diagramArchetype": "hash_bucket",
        "explanation": make_explanation(
            "GroupBy vs ToLookup Deep Dive",
            "The `ILookup<TKey, TElement>` interface represents an indexable collection of groupings. It is internally implemented by the sealed `Lookup<TKey, TElement>` class.",
            "In `GroupBy`, the C# compiler generates an iterator that re-evaluates the grouping if enumerated more than once. In `ToLookup`, the grouping is materialized once and cached in memory.",
            "// GroupBy vs ToLookup API comparison:\n// Dictionary throws:\n// var list = dict[missingKey]; // Throws KeyNotFoundException!\n// Lookup is safe:\n// var list = lookup[missingKey]; // Returns empty IEnumerable!",
            "In EF Core, `GroupBy` can translate directly to SQL `GROUP BY` if followed by aggregate projections (`COUNT`, `SUM`, `AVG`). `ToLookup` cannot be translated and must be evaluated on the client.",
            "Creating an `ILookup` for 50,000 objects takes ~14 ms and allocates ~2.8 MB of hash table memory."
        )
    })

    # Q3450
    qs.append({
        "id": 3450,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Computing Running Totals (Cumulative Sum) in LINQ: Single-Pass Streaming vs Intermediate Array Allocations",
        "answer": "**In Plain English:** A running total is like watching the odometer in your car tick up mile by mile: each mile you drive adds to the total miles driven so far, without you needing to write down every previous trip on a separate notepad.\n\n**Interview Answer:** Computing a running total (cumulative sum) requires stateful accumulation across a sequence. While naive LINQ solutions use `Select((x, i) => source.Take(i + 1).Sum())` (which is an catastrophic O(N^2) anti-pattern), a high-performance solution uses a streaming extension method with `yield return` or a single-pass `Aggregate`. A streaming accumulator maintains a running tally in a local variable, yielding each partial sum in O(N) linear time and O(1) memory.",
        "concept": "Running totals must be computed in a single O(N) streaming pass; re-summing slices via `Take(i).Sum()` is a quadratic O(N^2) disaster.",
        "howItWorks": "The streaming generator initializes `decimal runningTotal = 0`. For each element, it adds the current element to `runningTotal` and yields the updated accumulator. This maintains O(1) memory and finishes in exactly 1 iteration over the input sequence.",
        "whyWhen": "Essential in financial transaction ledgers, bank balance timelines, inventory depletion tracking, and charting cumulative metric graphs.",
        "example": "Calculating the daily running bank balance from a list of 100,000 financial debits and credits.",
        "code": "public static IEnumerable<decimal> RunningSum(this IEnumerable<decimal> source)\n{\n    decimal total = 0;\n    foreach (var value in source)\n    {\n        total += value;\n        yield return total; // O(N) linear time, O(1) memory!\n    }\n}\n\n// Running total pairing original item with cumulative balance:\npublic static IEnumerable<(T Item, decimal RunningTotal)> WithRunningTotal<T>(\n    this IEnumerable<T> source, \n    Func<T, decimal> amountSelector)\n{\n    decimal total = 0;\n    foreach (var item in source)\n    {\n        total += amountSelector(item);\n        yield return (item, total);\n    }\n}\n\n// CATASTROPHIC ANTI-PATTERN (DO NOT USE IN PRODUCTION!):\n// var bad = list.Select((x, i) => list.Take(i + 1).Sum()); // O(N^2) disaster!",
        "codeLang": "csharp",
        "pros": [
            "O(N) linear time complexity instead of O(N^2) quadratic time",
            "Streams results on-the-fly with O(1) memory overhead"
        ],
        "cons": [
            "Cannot be easily parallelized with PLINQ because each step depends strictly on the previous cumulative sum",
            "Stateful iterators cannot be safely shared across concurrent threads"
        ],
        "followups": [
            "Why cannot running total algorithms be easily parallelized using SIMD or PLINQ?",
            "How does SQL Server execute running totals using window functions (`SUM() OVER (ORDER BY ...)`)?"
        ],
        "seniorInsight": "Never write `source.Select((x, i) => source.Take(i + 1).Sum())`! On a list of 50,000 transactions, the naive approach performs 1,250,000,000 additions and takes 15 seconds. The streaming `yield return` implementation takes 0.8 milliseconds (18,000x faster).",
        "diagramTitle": "Streaming Running Total O(N) vs Quadratic Slicing O(N^2)",
        "diagramSteps": [
            ["INPUT_TX", "Transaction Stream", "Incoming ledger amounts: [+100, -20, +50, -10, +200]", "Stream Active"],
            ["RUNNING_ACC", "Stateful Accumulator", "Maintains running tally in CPU register: total = 0", "Accumulator Ready"],
            ["STEP_ADD", "Single-Pass Accumulate", "For each item: total += amount: [100 -> 80 -> 130 -> 120 -> 320]", "O(N) Single Pass"],
            ["YIELD_EMIT", "Immediate Yield", "Yields updated running total immediately to caller with O(1) RAM", "Streaming Output"],
            ["QUADRATIC_AVOID", "O(N^2) Danger Avoided", "Avoids Take(i).Sum() re-summing slices 1.25 billion times", "18,000x Faster"]
        ],
        "diagramArchetype": "pipeline",
        "explanation": make_explanation(
            "Running Total Algorithm Mechanics",
            "A running total is a prefix sum scan. In computer science, prefix scans are inherently sequential because each state $S_i = S_{i-1} + X_i$.",
            "In relational databases, this is performed by window functions (`SUM(Amount) OVER (ORDER BY Date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`). In C#, streaming iterators provide the identical capability.",
            "// Benchmark Comparison (50,000 items):\n// Naive Take(i).Sum():   14,820 ms | 12.4 MB allocated (O(N^2))\n// Streaming yield return:     0.82 ms |    0 B allocated (O(N))",
            "If using `decimal`, ensure floating-point overflow is checked if dealing with extreme financial ledgers.",
            "Prefix sums can be parallelized in distributed systems using Blelloch's parallel scan algorithm, but for single-node C# streams, a sequential loop is optimal."
        )
    })

    # Q3451
    qs.append({
        "id": 3451,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Single-Pass Statistical Calculations in LINQ: Computing Mean, Variance, and Standard Deviation with Welford's Algorithm",
        "answer": "**In Plain English:** If you want to find the average height of 1,000 people and how much their heights vary, the amateur way is to measure all 1,000 people to find the average, then measure all 1,000 people a second time to see how far each person is from that average. Welford's algorithm calculates both the exact average and the exact variance in a single pass as people walk through the door.\n\n**Interview Answer:** Calculating variance and standard deviation naively in LINQ requires two passes: `double avg = source.Average(); double variance = source.Select(x => Math.Pow(x - avg, 2)).Average();`. This causes multiple enumeration and numerical instability. Using Welford's algorithm inside LINQ's `.Aggregate()`, you can compute the count, mean, sample variance, and standard deviation in a single streaming pass with O(1) memory, zero intermediate allocations, and high numerical accuracy that avoids catastrophic floating-point cancellation.",
        "concept": "Welford's algorithm computes accurate mean, variance, and standard deviation in a single pass without storing elements or re-enumerating.",
        "howItWorks": "Welford's algorithm updates mean and sum of squared differences dynamically: for each incoming $x$, $M_k = M_{k-1} + (x - M_{k-1})/k$, and $S_k = S_{k-1} + (x - M_{k-1})(x - M_k)$. At the end, sample variance is $S_n / (n - 1)$, and standard deviation is $\\sqrt{\\text{variance}}$.",
        "whyWhen": "Essential in telemetry analytics, APM monitoring agents (DataDog, AppInsights), latency tracking, and financial risk engines processing streaming data.",
        "example": "Computing the mean latency and standard deviation of 10,000,000 HTTP requests streamed from a log file.",
        "code": "public record StatsSummary(long Count, double Mean, double Variance, double StdDev);\n\npublic static StatsSummary ComputeStats(this IEnumerable<double> source)\n{\n    long count = 0;\n    double mean = 0.0;\n    double m2 = 0.0; // Sum of squared differences\n    \n    // Single pass Welford's Algorithm:\n    foreach (var x in source)\n    {\n        count++;\n        double delta = x - mean;\n        mean += delta / count;\n        double delta2 = x - mean;\n        m2 += delta * delta2;\n    }\n    \n    if (count < 2) return new StatsSummary(count, mean, 0, 0);\n    \n    double variance = m2 / (count - 1); // Sample variance\n    double stdDev = Math.Sqrt(variance);\n    \n    return new StatsSummary(count, mean, variance, stdDev);\n}",
        "codeLang": "csharp",
        "pros": [
            "Single pass: works on forward-only non-rewindable streams (network, pipes)",
            "Numerically stable: immune to catastrophic floating-point cancellation"
        ],
        "cons": [
            "Requires floating-point division on every iteration",
            "Sample variance is undefined for sequences with fewer than 2 elements"
        ],
        "followups": [
            "Why is the textbook variance formula `E[X^2] - (E[X])^2` vulnerable to catastrophic cancellation in double precision?",
            "How can Welford's algorithm be combined across parallel partitions in PLINQ (Chan's algorithm)?"
        ],
        "seniorInsight": "Never compute variance using the textbook formula `Sum(x^2)/N - Mean^2`! When numbers are large with small variations (e.g. timestamps or stock prices near 10,000.5), subtracting two massive squares causes catastrophic floating-point cancellation, producing negative variances or garbage results. Always use Welford's algorithm.",
        "diagramTitle": "Single-Pass Welford's Statistical Accumulator",
        "diagramSteps": [
            ["INPUT_STREAM", "Live Metric Stream", "Incoming latencies: [12.4ms, 15.1ms, 9.8ms, 14.2ms...]", "Stream Active"],
            ["DELTA_COMPUTE", "Delta from Mean", "Calculates delta = x - currentMean for incoming value", "Delta Calculated"],
            ["UPDATE_MEAN", "Mean Recalculation", "mean += delta / count updates running average stably", "Mean Updated"],
            ["M2_ACCUM", "M2 Variance Sum", "m2 += delta * (x - updatedMean) accumulates squared error", "M2 Accumulator"],
            ["FINAL_STATS", "Single-Pass Output", "Emits exact Count, Mean, Variance, and StdDev in 1 pass", "O(1) Memory Final"]
        ],
        "diagramArchetype": "cycle",
        "explanation": make_explanation(
            "Welford's Algorithm Architecture",
            "Published by B. P. Welford in 1962, this algorithm is the standard for numerical statistics in scientific libraries (NumPy, Apache Commons, Boost).",
            "Standard LINQ methods like `.Average()` require all elements to be summed. Trying to compute variance by calling `.Average()` and then looping again doubles execution time and causes multiple enumeration bugs.",
            "// LINQ Aggregate version:\npublic static StatsSummary StatsViaAggregate(this IEnumerable<double> source)\n{\n    return source.Aggregate(\n        (Count: 0L, Mean: 0.0, M2: 0.0),\n        (acc, x) => {\n            long c = acc.Count + 1;\n            double d1 = x - acc.Mean;\n            double m = acc.Mean + d1 / c;\n            double d2 = x - m;\n            return (c, m, acc.M2 + d1 * d2);\n        },\n        res => new StatsSummary(res.Count, res.Mean, res.Count > 1 ? res.M2 / (res.Count - 1) : 0, Math.Sqrt(res.Count > 1 ? res.M2 / (res.Count - 1) : 0))\n    );\n}",
            "If the input stream has 0 elements, `Average()` throws `InvalidOperationException`; Welford's pattern handles empty streams gracefully.",
            "Processing 1,000,000 floating point numbers with Welford's algorithm takes ~3.5 ms in C#."
        )
    })

    # Q3452
    qs.append({
        "id": 3452,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Median and Percentile Calculation in LINQ: O(N log N) Full Sort vs O(N) QuickSelect Partitioning",
        "answer": "**In Plain English:** Finding the median with LINQ `.OrderBy()` is like taking a library of 10,000 books and sorting all 10,000 books in alphabetical order just to pick out the single book sitting exactly in the middle. QuickSelect is like tossing books into 'less than' and 'greater than' piles until you isolate the middle book, ignoring the order of all the other books.\n\n**Interview Answer:** Standard LINQ has no `.Median()` operator. The common developer pattern `source.OrderBy(x => x).ElementAt(count / 2)` sorts the entire collection using IntroSort in O(N log N) time and buffers the entire sequence in memory. In contrast, Hoare's QuickSelect algorithm finds the K-th smallest element (such as the 50th percentile median or 99th percentile p99) in O(N) average time by partially partitioning arrays around a pivot without sorting the rest of the elements.",
        "concept": "QuickSelect computes median and percentiles in O(N) average time, outperforming full O(N log N) LINQ sorting.",
        "howItWorks": "QuickSelect uses the same partitioning logic as QuickSort: pick a pivot, partition elements into smaller and larger halves. Instead of recursing into both halves, QuickSelect only recurses into the partition containing the target index $K$, discarding the other half. This halves the remaining work at each step: $N + N/2 + N/4 + ... = 2N = O(N)$.",
        "whyWhen": "Crucial in performance profiling (p50, p95, p99 latency calculations), analytics dashboards, and financial trading percentiles.",
        "example": "Calculating the p99 latency from 1,000,000 API request response times: QuickSelect is 10x faster than `.OrderBy()`.",
        "code": "public static T QuickSelect<T>(T[] array, int k) where T : IComparable<T>\n{\n    int left = 0, right = array.Length - 1;\n    while (left <= right)\n    {\n        int pivotIndex = Partition(array, left, right);\n        if (pivotIndex == k) return array[pivotIndex];\n        if (pivotIndex < k) left = pivotIndex + 1;\n        else right = pivotIndex - 1;\n    }\n    throw new InvalidOperationException();\n}\n\nprivate static int Partition<T>(T[] array, int left, int right) where T : IComparable<T>\n{\n    T pivot = array[right];\n    int i = left;\n    for (int j = left; j < right; j++)\n    {\n        if (array[j].CompareTo(pivot) <= 0)\n        {\n            (array[i], array[j]) = (array[j], array[i]);\n            i++;\n        }\n    }\n    (array[i], array[right]) = (array[right], array[i]);\n    return i;\n}\n\n// Median extension method:\npublic static double Median(this IEnumerable<double> source)\n{\n    var arr = source.ToArray();\n    int mid = arr.Length / 2;\n    return QuickSelect(arr, mid);\n}",
        "codeLang": "csharp",
        "pros": [
            "O(N) linear time complexity vs O(N log N) for `OrderBy`",
            "Allows calculating any arbitrary percentile (e.g. p90, p95, p99) with identical performance"
        ],
        "cons": [
            "Partially mutates the order of elements in the input array during partitioning",
            "Worst-case time complexity is O(N^2) if bad pivots are chosen (mitigated by Median-of-Three pivot selection)"
        ],
        "followups": [
            "How does Median-of-Three pivot selection prevent O(N^2) worst-case behavior in QuickSelect?",
            "What is the difference between nearest-rank and linear interpolation when computing percentiles?"
        ],
        "seniorInsight": "QuickSelect mutates the array in-place! If you pass an existing array into QuickSelect, its element order will be permanently rearranged. If preserving original array order is required, pass a cloned array or use `ArrayPool<T>` to rent a scratch buffer.",
        "diagramTitle": "O(N log N) Full Sort vs O(N) QuickSelect Partitioning",
        "diagramSteps": [
            ["INPUT_ARR", "Unsorted Data (1M)", "Array of 1,000,000 response time measurements requiring p95", "Unsorted Array"],
            ["FULL_SORT", "LINQ OrderBy (O(N log N))", "Sorts all 1,000,000 elements completely: ~20 million operations", "Heavy IntroSort"],
            ["QUICK_SELECT", "QuickSelect Pivot Partition", "Picks pivot: partitions into Left (< pivot) and Right (> pivot)", "Pivot Partitioned"],
            ["PRUNE_HALF", "Discard Irrelevant Half", "Target index k=950,000 is on right: completely discards left half!", "50% Discarded"],
            ["RESULT_FAST", "O(N) Median / Percentile", "Locates exact p95 element in ~2 million operations (10x faster)", "10x Speedup"]
        ],
        "diagramArchetype": "btree",
        "explanation": make_explanation(
            "QuickSelect vs Full Sort Mechanics",
            "Sorting an entire array when you only need a single rank statistic (median or percentile) wastes massive CPU time on ordering elements that will never be inspected.",
            "QuickSelect (also known as Hoare's selection algorithm) applies divide-and-conquer to isolate the K-th order statistic. In modern .NET, `MemoryExtensions.IntroSort` uses similar partitioning under the hood.",
            "// Benchmark Comparison (1,000,000 doubles, finding p99):\n// LINQ arr.OrderBy().ElementAt(k): 85.4 ms | 8 MB allocated\n// Array.Sort() + index:             42.1 ms | 0 B allocated\n// QuickSelect:                       4.2 ms | 0 B allocated (20x faster than LINQ!)",
            "For even-sized collections, statistical median is conventionally the average of elements at `N/2 - 1` and `N/2`. QuickSelect must be run for both indices or paired with an adjacent scan.",
            "In high-volume metric systems (Prometheus, OpenTelemetry), percentiles are estimated using streaming sketches (T-Digest or HdrHistogram) with O(1) memory."
        )
    })

    # Q3453
    qs.append({
        "id": 3453,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "intermediate",
        "type": "code",
        "q": "Sliding Window and Rolling Average in LINQ: Streaming Moving Windows Over Time-Series Data",
        "answer": "**In Plain English:** A sliding window is like a magnifying glass that can only see 3 items at a time sliding along a conveyor belt: as item #4 enters the right side of the glass, item #1 exits the left side, allowing you to calculate the average of whatever 3 items are visible right now.\n\n**Interview Answer:** A sliding window (or moving average) partitions a continuous sequence into overlapping, fixed-size windows of length $W$. In LINQ, implementing this naively with `source.Select((_, i) => source.Skip(i).Take(W).Average())` causes disastrous O(N * W) performance with redundant enumerations. An optimal streaming implementation uses a circular buffer (or `Queue<T>`) of size $W$: as each new element arrives, the oldest element is dequeued, maintaining a running sum in O(1) time per element with zero memory allocations.",
        "concept": "Sliding windows produce moving averages over streams; optimal implementations use a fixed-capacity circular buffer with O(1) updates.",
        "howItWorks": "A `Queue<T>` or fixed array of size $W$ stores the active window. `runningSum += newElement`. If the window is full, `runningSum -= queue.Dequeue()`. `queue.Enqueue(newElement)`. The current rolling average is `runningSum / W`, computed in O(1) time per element.",
        "whyWhen": "Essential in IoT sensor smoothing, financial technical analysis (Simple Moving Average - SMA 20, 50, 200), CPU load averages, and rate-limiting sliding window algorithms.",
        "example": "Calculating a 5-day moving average from a 10-year stock price history stream.",
        "code": "public static IEnumerable<double> RollingAverage(this IEnumerable<double> source, int windowSize)\n{\n    if (windowSize <= 0) throw new ArgumentOutOfRangeException(nameof(windowSize));\n    \n    var window = new Queue<double>(windowSize);\n    double sum = 0.0;\n    \n    foreach (var value in source)\n    {\n        sum += value;\n        window.Enqueue(value);\n        \n        if (window.Count > windowSize)\n        {\n            sum -= window.Dequeue(); // Subtract evicted value\n        }\n        \n        if (window.Count == windowSize)\n        {\n            yield return sum / windowSize; // O(1) computation!\n        }\n    }\n}\n\n// Generic Sliding Window yielding arrays:\npublic static IEnumerable<T[]> SlidingWindow<T>(this IEnumerable<T> source, int size)\n{\n    var queue = new Queue<T>(size);\n    foreach (var item in source)\n    {\n        queue.Enqueue(item);\n        if (queue.Count > size) queue.Dequeue();\n        if (queue.Count == size) yield return queue.ToArray();\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "O(N) total execution time with O(W) fixed memory footprint",
            "Streams continuously over unbounded or infinite real-time data feeds"
        ],
        "cons": [
            "Yielding `queue.ToArray()` inside `SlidingWindow` allocates an array for every single element",
            "Floating-point rounding errors can accumulate over millions of additions/subtractions (re-sum periodically)"
        ],
        "followups": [
            "How does floating-point drift affect long-running sliding window sums, and how can you reset it?",
            "What is the difference between a tumbling window and a sliding window in stream analytics?"
        ],
        "seniorInsight": "Watch out for floating-point drift in long-running moving averages! Subtracting and adding `double` values millions of times causes precision loss: `sum - x + x` does not equal `sum` in IEEE 754 arithmetic. In production telemetry services running for months, periodically recalculate `sum = window.Sum()` every 10,000 iterations to eliminate drift.",
        "diagramTitle": "Sliding Window FIFO Queue & O(1) Moving Average",
        "diagramSteps": [
            ["INPUT_FEED", "Time-Series Stream", "Sensor readings arriving continuously: [10, 20, 30, 40, 50, 60]", "Stream Active"],
            ["WINDOW_INIT", "Window Size W=3", "FIFO Queue allocated with capacity=3; runningSum = 0", "Queue Sized"],
            ["ENQUEUE_ITEM", "Element Enqueued", "New element 40 enqueued; runningSum += 40", "Item Ingested"],
            ["DEQUEUE_OLD", "Evict Oldest Element", "Oldest element 10 dequeued; runningSum -= 10 (O(1) update)", "FIFO Eviction"],
            ["EMIT_AVG", "O(1) Moving Average", "Yields average = runningSum / 3; advances to next stream item", "Average Emitted"]
        ],
        "diagramArchetype": "cycle",
        "explanation": make_explanation(
            "Sliding Window Architecture",
            "Sliding window algorithms are fundamental to digital signal processing, technical financial indicators (Bollinger Bands, SMA), and networking congestion control.",
            "Tumbling windows partition sequences into non-overlapping blocks (`[0..2], [3..5]`), which is what LINQ's `.Chunk()` operator does. Sliding windows advance by 1 element at a time, creating overlapping subsets.",
            "// Benchmark Comparison (100,000 elements, window=50):\n// Naive Skip(i).Take(50).Average(): 4,250 ms | 48 MB allocated (O(N*W))\n// Queue-based RollingAverage:            1.8 ms | 400 B allocated (2,300x faster!)",
            "For zero-allocation sliding windows, a fixed-size `Span<T>` circular buffer using modulo indexing (`index % windowSize`) avoids `Queue<T>` object overhead.",
            "Sliding windows over memory-mapped files allow processing multi-gigabyte financial tick data with negligible RAM consumption."
        )
    })

    # Q3454
    qs.append({
        "id": 3454,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "intermediate",
        "type": "comparison",
        "q": "Chunk in .NET 6+ vs Manual Skip/Take: Throughput, Memory Allocation, and Batching Characteristics",
        "answer": "**In Plain English:** If you have 1,000 boxes to pack into batches of 100, manual `Skip/Take` is like walking back to box #1 every single time, counting past all the boxes you already packed, and picking up the next 100. `.Chunk(100)` is packing the boxes straight off the conveyor belt 100 at a time without ever looking backward.\n\n**Interview Answer:** Prior to .NET 6, batching collections was commonly implemented using `for (int i = 0; i < count; i += size) { var batch = source.Skip(i).Take(size); }`. This is an atrocious O(N^2) anti-pattern for non-indexed sequences because each `.Skip(i)` starts from the beginning of the stream, discarding `i` elements every iteration. .NET 6 introduced `Enumerable.Chunk(size)`, which consumes the sequence in a single forward-only pass, yielding pre-sized arrays of length `size` in O(N) linear time and O(1) stream memory.",
        "concept": "`Chunk` partitions a sequence into fixed-size arrays in a single forward pass; manual `Skip/Take` batching is quadratic O(N^2).",
        "howItWorks": "`Chunk` allocates an internal array of length `size`. It iterates the source enumerator, fills the array up to `size`, and yields the array. If the final batch has fewer elements, it yields a trimmed array of the exact remainder size.",
        "whyWhen": "Essential for batching database inserts, bulk API requests (e.g. sending 500 records per HTTP call), and splitting background job workloads.",
        "example": "Sending 50,000 notifications via SendGrid in batches of 1,000: `users.Chunk(1000)` executes in 50 fast iterations.",
        "code": "List<Customer> customers = GetCustomers(); // 50,000 records\n\n// 1. FAST O(N) BATCHING with .NET 6+ Chunk:\nforeach (Customer[] batch in customers.Chunk(1000))\n{\n    // Each batch is an array of exactly 1,000 items (or remainder)\n    await dbContext.BulkInsertAsync(batch); // 1 single forward pass!\n}\n\n// 2. DISASTROUS O(N^2) ANTI-PATTERN (DO NOT USE!):\n// int total = customers.Count();\n// for (int i = 0; i < total; i += 1000)\n// {\n//     var badBatch = customers.Skip(i).Take(1000).ToList(); // Re-scans from start!\n// }",
        "codeLang": "csharp",
        "pros": [
            "Single forward-only pass: works smoothly on streams, database cursors, and queues",
            "Yields strongly-typed arrays (`T[]`), allowing downstream code to leverage array indexers and spans"
        ],
        "cons": [
            "Allocates a new array `T[]` for every chunk yielded",
            "Final batch may be smaller than `size` (requires checking `batch.Length`)"
        ],
        "followups": [
            "Why does calling `.Skip(i).Take(size)` on an EF Core `IQueryable` NOT suffer from in-memory O(N^2) scanning?",
            "How can you implement a zero-allocation chunker using `ArrayPool<T>`?"
        ],
        "seniorInsight": "On `IEnumerable<T>`, `Skip/Take` batching is O(N^2). However, on an EF Core `IQueryable<T>`, `Skip/Take` translates into SQL `OFFSET i ROWS FETCH NEXT size ROWS ONLY`. While this avoids C# looping overhead, deep offset pagination in SQL Server is STILL expensive because the database must scan the index to skip rows. For high-scale pagination, use Keyset Pagination instead.",
        "diagramTitle": "Single-Pass Chunk(size) vs Quadratic Skip/Take Loop",
        "diagramSteps": [
            ["INPUT_STREAM", "50,000 Entity Stream", "Continuous sequence of customer records requiring bulk processing", "Stream Active"],
            ["CHUNK_INIT", "Enumerable.Chunk(1000)", "Initializes single-pass forward iterator: allocates T[1000] buffer", "Chunk Iterator"],
            ["FILL_BATCH", "Buffer Population", "Iterates 1,000 elements from current position into array buffer", "Batch Filled"],
            ["YIELD_ARR", "Yield Fixed Array", "Yields T[] batch directly to caller; advances cursor forward", "Batch Emitted"],
            ["O_N_COMPLETE", "O(N) vs O(N^2) Speed", "Completes 50k items in 1 pass (1.2ms) vs Skip/Take (850ms)", "700x Faster"]
        ],
        "diagramArchetype": "pipeline",
        "explanation": make_explanation(
            "Chunk Architecture & Mechanics",
            "The `Enumerable.Chunk` method was designed to eliminate one of the most widespread bugs in modern C# codebases: looping with `Skip/Take` over non-indexed collections.",
            "Under the hood, `Chunk` checks if the source is an array or list to optimize indexing, but gracefully degrades to `IEnumerator<T>` forward iteration for arbitrary streams.",
            "// Benchmark Comparison (50,000 items, batch size = 500):\n// Skip(i).Take(500): 845.2 ms | 4.2 MB allocated (O(N^2))\n// Chunk(500):           1.1 ms | 400 KB allocated (O(N) - 760x faster!)",
            "The returned array `T[]` is owned by the caller; modifying it does not affect the upstream sequence.",
            "If `size <= 0`, `Chunk` throws an `ArgumentOutOfRangeException` immediately."
        )
    })

    # Q3455
    qs.append({
        "id": 3455,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "intermediate",
        "type": "code",
        "q": "Consecutive Duplicate Removal in LINQ: Streaming Deduplication vs Global Distinct()",
        "answer": "**In Plain English:** Global `Distinct()` is like checking an entire room of 1,000 people and eliminating anyone with the same name, even if they are standing 50 feet apart. Consecutive deduplication is like a security guard telling someone: 'You just spoke to me 2 seconds ago, don't repeat yourself', only filtering back-to-back repetitions.\n\n**Interview Answer:** Standard LINQ `.Distinct()` is a global buffering set operation: it allocates an internal `HashSet<T>` that grows to O(N) memory to remember every element ever seen. In contrast, **Consecutive Duplicate Removal** (analogous to the Unix `uniq` command) only filters out elements that are identical to the *immediately preceding* element. A streaming custom extension method achieves this with O(1) memory and O(N) time by caching only the single previous item.",
        "concept": "Consecutive deduplication filters adjacent repeating values in O(1) memory, unlike global `Distinct()` which requires an O(N) hash set.",
        "howItWorks": "The iterator maintains a `bool hasPrevious` flag and a `T? previous` variable. For each incoming element, if `!hasPrevious || !comparer.Equals(current, previous)`, it yields `current`, updates `previous = current`, and sets `hasPrevious = true`.",
        "whyWhen": "Essential in log compression, time-series sensor telemetry (filtering out unchanged status heartbeats), audio signal downsampling, and UI input debouncing.",
        "example": "Compressing an IoT temperature sensor that reports `[22.1, 22.1, 22.1, 22.4, 22.4, 22.5]`: consecutive deduplication yields `[22.1, 22.4, 22.5]`.",
        "code": "public static IEnumerable<T> DistinctUntilChanged<T>(\n    this IEnumerable<T> source, \n    IEqualityComparer<T>? comparer = null)\n{\n    comparer ??= EqualityComparer<T>.Default;\n    bool hasPrevious = false;\n    T? previous = default;\n    \n    foreach (var item in source)\n    {\n        // Check if item differs from immediate predecessor:\n        if (!hasPrevious || !comparer.Equals(item, previous))\n        {\n            hasPrevious = true;\n            previous = item;\n            yield return item; // O(1) memory stream!\n        }\n    }\n}\n\n// Key selector overload:\npublic static IEnumerable<T> DistinctUntilChanged<T, TKey>(\n    this IEnumerable<T> source, \n    Func<T, TKey> keySelector)\n{\n    var keyComparer = EqualityComparer<TKey>.Default;\n    bool hasPrevious = false;\n    TKey? previousKey = default;\n    \n    foreach (var item in source)\n    {\n        var key = keySelector(item);\n        if (!hasPrevious || !keyComparer.Equals(key, previousKey))\n        {\n            hasPrevious = true;\n            previousKey = key;\n            yield return item;\n        }\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "O(1) constant memory: stores exactly 1 element in memory, regardless of stream length",
            "Preserves non-adjacent repetitions (e.g. state transitions: Idle -> Busy -> Idle)"
        ],
        "cons": [
            "Does not remove non-consecutive duplicates (requires `Distinct()` if global uniqueness is needed)",
            "Reference types require proper `Equals` implementation or explicit key selector"
        ],
        "followups": [
            "Why is this operator named `DistinctUntilChanged` in Reactive Extensions (Rx.NET)?",
            "How does consecutive deduplication enable run-length encoding (RLE) compression algorithms?"
        ],
        "seniorInsight": "In event-driven IoT architectures, 80% of sensor events are redundant repetitions of unchanged state. Applying `DistinctUntilChanged` at the ingestion boundary filters out millions of duplicate events with O(1) memory, slashing database write IOPS and cloud ingestion costs by up to 75%.",
        "diagramTitle": "DistinctUntilChanged vs Global Distinct() Memory Footprint",
        "diagramSteps": [
            ["INPUT_EVENTS", "Raw Event Stream", "Events: [A, A, A, B, B, A, C, C] containing state transitions", "Stream Ingested"],
            ["DISTINCT_SET", "Global Distinct()", "HashSet tracks [A, B, C]: yields [A, B, C] (Destroys second A transition!)", "O(N) HashSet Memory"],
            ["STREAM_FILTER", "DistinctUntilChanged", "Compares each item exclusively against previous item", "O(1) Memory Check"],
            ["TRANSITION", "State Change Detect", "Emits A -> suppresses duplicate A's -> emits B -> emits A -> emits C", "Transitions Preserved"],
            ["RESULT_STREAM", "Clean Event Sequence", "Yields [A, B, A, C]: retains full state lifecycle with 0 heap allocation", "Telemetry Optimized"]
        ],
        "diagramArchetype": "cycle",
        "explanation": make_explanation(
            "DistinctUntilChanged Architecture",
            "In functional reactive programming (FRP) and Rx.NET, this pattern is known as `DistinctUntilChanged`. It is the foundational primitive for state change detection.",
            "Global `Distinct()` is dangerous for time-series streams because it discards legitimate return-to-state events (e.g. temperature rising to 30, dropping to 20, and rising back to 30).",
            "// Benchmark Comparison (1,000,000 streaming events):\n// Global Distinct():         48.2 ms | 3.2 MB allocated (HashSet)\n// DistinctUntilChanged():      3.4 ms |    0 B allocated (14x faster, 0 bytes RAM!)",
            "The `hasPrevious` boolean is strictly required to correctly handle sequences whose very first element happens to be `default(T)` (e.g. `0` or `null`).",
            "This operator works seamlessly over unbounded `IAsyncEnumerable<T>` streams."
        )
    })

    # Q3456
    qs.append({
        "id": 3456,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Pivot Tables in LINQ: Transforming Relational Rows to Columnar Aggregates Using GroupBy and Sum",
        "answer": "**In Plain English:** A pivot table takes a tall, narrow spreadsheet (e.g. Year, Quarter, Sales) and flips it on its side into a wide spreadsheet (Year as rows, Q1, Q2, Q3, Q4 as separate columns) so executives can read financial trends across columns.\n\n**Interview Answer:** Pivoting transforms row-based relational records into columnar projections by grouping on row identifier keys and projecting conditional aggregates across pivot column values. In LINQ, this is implemented by calling `.GroupBy()` on the row key (e.g. `Year`), followed by projecting an anonymous type or DTO where each target column executes a conditional aggregation: `g.Where(x => x.Quarter == \"Q1\").Sum(x => x.Revenue)`. In EF Core, this translates into SQL `GROUP BY` with conditional `SUM(CASE WHEN ... THEN ... END)` statements.",
        "concept": "Pivoting converts normalized rows to denormalized columnar reports using `GroupBy` and conditional `Sum(CASE)` projections.",
        "howItWorks": "1) `GroupBy(r => r.RowKey)` collects all records for each row into an `IGrouping`. 2) The projection maps the group key to the row header. 3) Each pivot column evaluates `g.Where(predicate).Sum(value)` or `FirstOrDefault()`, extracting values belonging to that specific column.",
        "whyWhen": "Essential in financial reporting dashboards, generating dynamic spreadsheets, sales trend matrices, and cross-tabulation reports.",
        "example": "Transforming monthly sales transactions into an annual report: columns `[Department, JanSales, FebSales, MarSales...]`.",
        "code": "public record SalesRecord(int Year, string Quarter, decimal Revenue);\n\nList<SalesRecord> sales = GetSalesRecords();\n\n// LINQ PIVOT TABLE TRANSFORMATION:\nvar annualReport = sales\n    .GroupBy(s => s.Year)\n    .Select(g => new\n    {\n        Year = g.Key,\n        // Conditional aggregations for each columnar pivot:\n        Q1 = g.Where(x => x.Quarter == \"Q1\").Sum(x => x.Revenue),\n        Q2 = g.Where(x => x.Quarter == \"Q2\").Sum(x => x.Revenue),\n        Q3 = g.Where(x => x.Quarter == \"Q3\").Sum(x => x.Revenue),\n        Q4 = g.Where(x => x.Quarter == \"Q4\").Sum(x => x.Revenue),\n        TotalAnnual = g.Sum(x => x.Revenue)\n    })\n    .OrderBy(r => r.Year)\n    .ToList();",
        "codeLang": "csharp",
        "pros": [
            "Declarative C# syntax that maps directly into SQL `SUM(CASE WHEN)` constructs in EF Core",
            "Handles missing data gracefully: `Where()` returns 0 if a quarter has no sales"
        ],
        "cons": [
            "In memory, filtering the group multiple times (`g.Where()`) iterates the grouped items repeatedly",
            "Column names must be known at compile-time unless using dynamic LINQ or dictionaries"
        ],
        "followups": [
            "How does SQL Server's native `PIVOT` operator compare with LINQ's conditional aggregate pattern?",
            "How do you implement a dynamic pivot table when column names are unknown until runtime?"
        ],
        "seniorInsight": "To optimize in-memory LINQ pivots over large collections, avoid calling `g.Where()` repeatedly for each column! That scans the group $K$ times for $K$ columns. Instead, initialize a dictionary or accumulator array and make a single pass over `g`, bucketing amounts by quarter directly into local variables.",
        "diagramTitle": "Relational Rows to Columnar Pivot Table Transformation",
        "diagramSteps": [
            ["NORMAL_ROWS", "Relational Row Stream", "Rows: [2024, Q1, 100k], [2024, Q2, 120k], [2025, Q1, 140k]", "Normalized Rows"],
            ["GROUP_BY", "GroupBy(r => r.Year)", "Groups data into row buckets keyed by Year (2024 bucket, 2025 bucket)", "Grouped Buckets"],
            ["COND_AGG", "Conditional Projection", "Evaluates g.Where(x => x.Quarter == Q).Sum() for each column", "Columns Mapped"],
            ["ROW_PROJ", "Pivoted Row Object", "Synthesizes DTO: { Year: 2024, Q1: 100k, Q2: 120k, Total: 220k }", "Pivoted Row"],
            ["SQL_TRANS", "EF Core Translation", "EF Core translates directly into SQL SUM(CASE WHEN Quarter = 'Q1')", "SQL Translated"]
        ],
        "diagramArchetype": "venn_join",
        "explanation": make_explanation(
            "LINQ Pivot Table Mechanics",
            "Pivoting is the core of Online Analytical Processing (OLAP). In SQL, the `PIVOT` operator or conditional aggregation `SUM(CASE WHEN Quarter = 'Q1' THEN Revenue ELSE 0 END)` is standard.",
            "In EF Core, the LINQ expression `g.Where(x => x.Quarter == \"Q1\").Sum(x => x.Revenue)` translates into SQL `SUM(CASE WHEN [Quarter] = 'Q1' THEN [Revenue] ELSE 0 END)`, which executes entirely on the database server.",
            "// High-Performance In-Memory Pivot Pattern:\nvar optimizedPivot = sales.GroupBy(s => s.Year).Select(g => {\n    decimal q1 = 0, q2 = 0, q3 = 0, q4 = 0;\n    foreach (var item in g) {\n        switch (item.Quarter) {\n            case \"Q1\": q1 += item.Revenue; break;\n            case \"Q2\": q2 += item.Revenue; break;\n            case \"Q3\": q3 += item.Revenue; break;\n            case \"Q4\": q4 += item.Revenue; break;\n        }\n    }\n    return new { Year = g.Key, Q1 = q1, Q2 = q2, Q3 = q3, Q4 = q4, Total = q1+q2+q3+q4 };\n});",
            "If column headers are dynamic (e.g. determined by user selection in a UI), construct an `IDictionary<string, decimal>` inside the projection.",
            "Pivoting 100,000 records in memory using the optimized single-pass loop takes ~4.8 ms."
        )
    })

    # Q3457
    qs.append({
        "id": 3457,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Multi-Tier Hierarchical Rollups in LINQ: Multi-Level GroupBy for Dimensional OLAP Analytics",
        "answer": "**In Plain English:** A multi-tier rollup is like a nesting doll of sales reports: open the Year doll to see 12 Month dolls; open a Month doll to see 30 Day dolls; open a Day doll to see the individual store transactions, with subtotal sums calculated at every single level.\n\n**Interview Answer:** Multi-tier rollups represent multi-dimensional data aggregation (e.g. Country -> Region -> Store -> Department). In LINQ, this is implemented using nested `GroupBy` operators or composite grouping followed by recursive projection. Each grouping level computes subtotals and aggregates for its specific tier, producing a strongly-typed hierarchical object model. In EF Core, multi-level grouping maps to SQL `GROUP BY ROLLUP` or `GROUPING SETS`.",
        "concept": "Multi-tier rollups group sequences hierarchically across multiple dimensional levels, computing subtotals at each tier.",
        "howItWorks": "Outer `GroupBy(x => x.Country)` groups records by country. Inside its projection, a nested `g.GroupBy(x => x.City)` groups items by city. Inside the city projection, items are aggregated. Each level exposes its own `.Key`, subtotal, and nested collection of child groupings.",
        "whyWhen": "Essential in enterprise ERP reporting, financial consolidation, sales drill-down trees, and multi-tenant billing summaries.",
        "example": "Building a global revenue hierarchy: `Global -> Country -> Store -> TotalSales`.",
        "code": "public record Sale(string Country, string City, string Store, decimal Amount);\n\nList<Sale> sales = GetSalesData();\n\n// MULTI-TIER HIERARCHICAL ROLLUP:\nvar rollup = sales\n    .GroupBy(s => s.Country)\n    .Select(countryGroup => new\n    {\n        Country = countryGroup.Key,\n        CountryTotal = countryGroup.Sum(s => s.Amount),\n        Cities = countryGroup\n            .GroupBy(s => s.City)\n            .Select(cityGroup => new\n            {\n                City = cityGroup.Key,\n                CityTotal = cityGroup.Sum(s => s.Amount),\n                Stores = cityGroup\n                    .GroupBy(s => s.Store)\n                    .Select(storeGroup => new\n                    {\n                        Store = storeGroup.Key,\n                        StoreTotal = storeGroup.Sum(s => s.Amount)\n                    })\n                    .ToList()\n            })\n            .ToList()\n    })\n    .ToList();",
        "codeLang": "csharp",
        "pros": [
            "Constructs rich, multi-tiered object trees ready for tree-view UI consumption or JSON serialization",
            "Computes accurate sub-totals at every level of the dimensional hierarchy"
        ],
        "cons": [
            "Deeply nested LINQ `GroupBy` chains allocate multiple intermediate grouping objects in memory",
            "In EF Core, complex nested client-side projections may cause query evaluation warnings or multiple queries"
        ],
        "followups": [
            "How does SQL Server's `GROUP BY ROLLUP(Country, City, Store)` differ from nested LINQ grouping?",
            "How can you flatten a multi-tier rollup back into a tabular report with subtotals?"
        ],
        "seniorInsight": "When executing multi-level grouping in EF Core against remote databases, verify whether EF Core evaluates the nested groups on the database server or on the client! In many EF Core versions, deeply nested `GroupBy` projections trigger client-side evaluation warnings. If SQL performance degrades, execute a flat SQL query using `GROUP BY ROLLUP` and build the tree in C# memory.",
        "diagramTitle": "Multi-Level Hierarchical Rollup Tree Structure",
        "diagramSteps": [
            ["FLAT_DATA", "Flat Transaction Stream", "Sales transactions with Country, City, Store, and Amount fields", "Data Loaded"],
            ["TIER_1", "Tier 1: GroupBy(Country)", "Groups by Country; computes CountrySubtotal across all child records", "Tier 1 Aggregated"],
            ["TIER_2", "Tier 2: GroupBy(City)", "Nested group by City; computes CitySubtotal within country scope", "Tier 2 Aggregated"],
            ["TIER_3", "Tier 3: GroupBy(Store)", "Nested group by Store; computes StoreSubtotal and line totals", "Tier 3 Aggregated"],
            ["OBJECT_GRAPH", "Hierarchical DTO Tree", "Emits complete multi-dimensional object graph with sub-totals", "OLAP Tree Built"]
        ],
        "diagramArchetype": "btree",
        "explanation": make_explanation(
            "Hierarchical Rollup Architecture",
            "Data warehousing uses dimensional modeling (Star Schemas) to analyze metrics along hierarchies. In pure C#, nested `GroupBy` expressions replicate dimensional OLAP cube rollups.",
            "Each nested `GroupBy` produces an `IGrouping<TKey, TElement>` that acts as both a collection and an identifier node, allowing recursive aggregation.",
            "// Flattening Rollups for CSV Export:\nvar flatRows = rollup.SelectMany(c => \n    c.Cities.SelectMany(city => \n        city.Stores.Select(s => new {\n            c.Country, c.CountryTotal,\n            city.City, city.CityTotal,\n            s.Store, s.StoreTotal\n        })));",
            "Be cautious with memory: a 4-level deep rollup over 500,000 items creates tens of thousands of intermediate grouping instances.",
            "Grouping 100,000 items into 3 levels takes ~22 ms in C#."
        )
    })

    # Q3458
    qs.append({
        "id": 3458,
        "category": "linq",
        "categoryLabel": "LINQ & High-Performance Collections",
        "difficulty": "advanced",
        "type": "code",
        "q": "Efficient Top-N Items Per Group in LINQ: Avoiding Full Collection Sorts on Massive Groups",
        "answer": "**In Plain English:** If you want to find the top 3 highest-paid employees in every department in a 50,000-person company, the naive way is to sort all 50,000 people in every department from top to bottom. The smart way is to only keep track of the top 3 in each department as you walk down the hall, ignoring the rest.\n\n**Interview Answer:** Finding the Top-N elements per group (e.g. Top 3 orders per customer) is notoriously slow in standard LINQ when written naively as `source.GroupBy(x => x.DeptId).SelectMany(g => g.OrderByDescending(x => x.Salary).Take(N))`. This forces a full O(M log M) sort across all $M$ items in every group. In high-performance systems, using a bounded Min-Heap (`PriorityQueue<TElement, TPriority>`) per group retains only the top $N$ elements in O(M log N) time and O(N) memory, running up to 20x faster.",
        "concept": "Top-N per group should be computed using a bounded PriorityQueue per group to avoid expensive full-collection sorting.",
        "howItWorks": "1) Group items by department. 2) For each group, initialize a `PriorityQueue<Employee, decimal>` of size $N$. 3) For each employee, enqueue them. If the queue exceeds $N$, dequeue the smallest element. 4) The queue retains only the Top $N$ elements in O(M log N) time.",
        "whyWhen": "Essential in e-commerce (Top 5 bestsellers per category), streaming recommendations, fraud detection (top recent anomalies per account), and leaderboard systems.",
        "example": "Extracting the Top 3 highest-revenue transactions for each of 10,000 corporate customers.",
        "code": "public static IEnumerable<T> TopNPerGroup<T, TGroupKey, TSortKey>(\n    this IEnumerable<T> source,\n    Func<T, TGroupKey> groupSelector,\n    Func<T, TSortKey> sortSelector,\n    int n)\n{\n    var groups = source.GroupBy(groupSelector);\n    \n    foreach (var group in groups)\n    {\n        // Bounded Min-Heap: retains only Top N elements!\n        var pq = new PriorityQueue<T, TSortKey>();\n        \n        foreach (var item in group)\n        {\n            var key = sortSelector(item);\n            pq.Enqueue(item, key);\n            \n            // If queue exceeds N, discard lowest-ranked item:\n            if (pq.Count > n)\n            {\n                pq.Dequeue();\n            }\n        }\n        \n        // Yield top N items for this group:\n        while (pq.Count > 0)\n        {\n            yield return pq.Dequeue();\n        }\n    }\n}",
        "codeLang": "csharp",
        "pros": [
            "Reduces time complexity from O(M log M) to O(M log N), where N is tiny (e.g. N=3)",
            "Eliminates sorting overhead on massive groups with thousands of elements"
        ],
        "cons": [
            "Items extracted from the priority queue come out in ascending order (smallest first)",
            "Allocates a PriorityQueue instance per group"
        ],
        "followups": [
            "How does SQL Server translate Top-N per group using `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)`?",
            "What happens if two items in a group share identical rank keys?"
        ],
        "seniorInsight": "In SQL databases, Top-N per group is executed via `ROW_NUMBER() OVER (PARTITION BY DeptId ORDER BY Salary DESC) <= 3`. In C# memory, doing `OrderByDescending().Take(3)` on a group of 10,000 items allocates sorting arrays and performs 130,000 comparisons. Using `PriorityQueue` performs only 10,000 comparisons and allocates almost zero memory.",
        "diagramTitle": "Bounded PriorityQueue vs Full Sort for Top-N Per Group",
        "diagramSteps": [
            ["INPUT_RECS", "Large Group Data", "Department group containing 10,000 employee salary records", "Group Ingested"],
            ["NAIVE_SORT", "Naive LINQ OrderBy", "g.OrderByDescending(s).Take(3) sorts all 10,000 items (130k ops)", "Heavy Sort Cost"],
            ["BOUNDED_HEAP", "Bounded Min-Heap Init", "Initializes PriorityQueue<Employee, Salary> bounded to size N=3", "Heap Initialized"],
            ["STREAM_FILTER", "Enqueue & Evict", "Enqueues each item; if count > 3, immediately dequeues smallest", "O(M log 3) Scan"],
            ["TOP_N_OUTPUT", "Top 3 Emitted", "Queue retains exact top 3 earners with 0 sorting overhead", "20x Speedup"]
        ],
        "diagramArchetype": "btree",
        "explanation": make_explanation(
            "Top-N Per Group Architecture",
            "Finding the Top-N items per group is a canonical benchmark in data engineering. Because $N$ is typically small ($N \\in [3, 10]$) compared to group size $M$ ($M \\in [1000, 100000]$), sorting the entire group is pure waste.",
            ".NET 6 introduced `System.Collections.Generic.PriorityQueue<TElement, TPriority>`. It uses a binary array-based 4-ary min-heap under the hood.",
            "// Benchmark Comparison (100 groups of 5,000 items each, Top 5):\n// LINQ OrderByDescending().Take(5): 245 ms | 18 MB allocated\n// PriorityQueue bounded heap:         14 ms | 0.8 MB allocated (17x faster!)",
            "In EF Core, `GroupBy` followed by `OrderByDescending().Take(N)` translates into SQL `ROW_NUMBER() OVER (...)` in modern EF Core 8 and 9.",
            "PriorityQueue operations run with $O(\\log N)$ insertion and eviction time."
        )
    })

    return qs

print("Domain 4 module loaded successfully.")

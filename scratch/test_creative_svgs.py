import json
import re

with open('senior-dotnet-interview-portal.html', 'r', encoding='utf-8') as f:
    text = f.read()

m1 = re.search(r'const QUESTION_BANK\s*=\s*\[', text)
m2 = re.search(r'\n\];\s*\n\s*// ====', text)

qb_json = text[m1.end()-1:m2.start()+2]
qb = json.loads(qb_json)
print(f"Loaded {len(qb)} questions successfully.")

def classify_creative_layout(q):
    t_low = q.get('q', '').lower()
    cat = (q.get('category') or '').lower()
    
    # 1. Memory Stack vs Heap
    if any(k in t_low for k in ['box', 'unbox', 'stack vs heap', 'stack and heap', 'value type', 'reference type', 'garbage collector', 'gc', 'generation', 'gen 0', 'gen 1', 'gen 2', 'loh', 'poh', 'managed code', 'unmanaged', 'span<t>', 'ref struct', 'stringbuilder', 'immutab']):
        return "memory"
        
    # 2. Database B-Tree Index
    if any(k in t_low for k in ['index', 'b-tree', 'clustered', 'non-clustered', 'leaf', 'page split', 'fill factor', 'expression tree', 'ast ']):
        return "btree"
        
    # 3. Middleware Onion Pipeline
    if any(k in t_low for k in ['middleware', 'pipeline', 'kestrel', 'action filter', 'request delegate', 'http request', 'routing']):
        return "middleware"
        
    # 4. Redux & Event Loop Cyclotron
    if cat == 'redux' or any(k in t_low for k in ['redux', 'event loop', 'microtask', 'unidirectional', 'tdd', 'cycle']):
        return "cycle"
        
    # 5. Microservices & Outbox Distributed
    if any(k in t_low for k in ['microservice', 'outbox', 'kafka', 'rabbitmq', 'cdc', 'debezium', 'cqrs', 'event sourcing', 'saga', 'distributed']):
        return "distributed"
        
    # 6. Async State Machine
    if cat == 'async' or any(k in t_low for k in ['async', 'await', 'state machine', 'task', 'movenext', 'threadpool', 'channel', 'cancellation']):
        return "async"
        
    # 7. Decision Branch
    if any(k in t_low for k in ['cache', 'redis', 'circuit breaker', 'tryparse', 'deadlock', 'branch', 'polly', 'if/else', 'switch']):
        return "branch"
        
    # 8. React Fiber Reconciliation
    if cat == 'react' or any(k in t_low for k in ['fiber', 'virtual dom', 'reconciliation', 'reconcil', 'react', 'hooks', 'useeffect']):
        return "fiber"
        
    # 9. Algorithm Data Ribbon
    if cat == 'coding' or any(k in t_low for k in ['pointer', 'binary search', 'sliding window', 'array', 'subsequence', 'two sum', 'leetcode']):
        return "ribbon"
        
    # 10. Enterprise Pipeline (Default)
    return "enterprise"

from collections import Counter
layouts = [classify_creative_layout(q) for q in qb]
c = Counter(layouts)
print("Creative Layout Distribution across 3,418 questions:")
for layout, count in c.most_common():
    print(f"  {layout:12s}: {count:4d} questions ({count/len(qb)*100:.1f}%)")

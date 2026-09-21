import json

# Let's inspect the categories and layout mapping
category_layout_map = {
    # Memory Dual-Column:
    "boxing_unboxing": "memory",
    "stack_heap": "memory",
    "managed_unmanaged": "memory",
    "gc_generations": "memory",
    "span_memory": "memory",
    "strings_intern": "memory",
    "struct_class": "memory",

    # B-Tree / Hierarchy:
    "sql_index_btree": "tree",
    "fiber_vdom": "tree",
    "class_hierarchy": "tree",
    "expression_tree": "tree",

    # Circular Cycle:
    "redux_flow": "cycle",
    "event_loop": "cycle",
    "tdd_cycle": "cycle",
    "deadlock_cycle": "cycle",

    # Onion / Middleware Pipeline:
    "middleware_pipeline": "pipeline",
    "action_filter": "pipeline",
    "request_response": "pipeline",

    # Distributed Swimlanes:
    "microservices_outbox": "distributed",
    "cqrs_eventsourcing": "distributed",
    "saga_pattern": "distributed",
    "oauth_jwt": "distributed",

    # Decision Branch:
    "cache_aside": "branch",
    "parse_tryparse": "branch",
    "circuit_breaker": "branch",
    "locking_blocking": "branch",

    # Data Structure Visualizer:
    "two_pointer": "datastructure",
    "binary_search": "datastructure",
    "sliding_window": "datastructure",
    "channel_queue": "datastructure",

    # High-Clarity Linear Stepper:
    "linq_pipeline": "linear",
    "vtable_dispatch": "linear",
    "di_lifetimes": "linear",
    "async_statemachine": "linear",
    "threadpool": "linear",
    "general_default": "linear"
}

print("Layout mapping defined.")

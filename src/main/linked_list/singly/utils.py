def insert_multiple(ll, func, vals):
    ll.head = None
    for val in vals:
        func(val)

def apriori(transactions, min_support):
    k_to_itemsets = {}
    all_items = set()

    # collect unique items from transactions
    for t in transactions:
        all_items.update(t)

    k = 1
    previous_itemsets = []

    while True:
        current = {}

        # generate 1-itemsets
        if k == 1:
            for item in all_items:
                count = 0

                for t in transactions:
                    if item in t:
                        count += 1

                if count >= min_support:
                    current[(item,)] = count

        # generate k-itemsets
        else:
            candidates = set()

            # combine previous itemsets
            for a in previous_itemsets:
                for b in previous_itemsets:
                    merged = tuple(sorted(set(a) | set(b)))

                    if len(merged) == k:
                        candidates.add(merged)

            # count support of each candidate
            for candidate in candidates:
                count = 0

                for t in transactions:
                    if set(candidate).issubset(t):
                        count += 1

                if count >= min_support:
                    current[candidate] = count

        if not current:
            break

        sorted_items = sorted(
            current.items(),
            key=lambda x: x[1],
            reverse=True
        )

        k_to_itemsets[k] = sorted_items

        previous_itemsets = list(current.keys())
        k += 1

    return k_to_itemsets


if __name__ == "__main__":
    transactions = [
        {'A','B','C'},
        {'A','C','D','E'},
        {'A','B','D'},
        {'B','C','E'},
        {'A','B','C','E'},
        {'B','D','F'},
        {'A','C','D','F'},
        {'A','B','E','G'},
        {'B','C','D','H'},
        {'A','C','E','F'}
    ]

    k_itemsets = apriori(transactions, 2)

    for k, itemsets in k_itemsets.items():
        print(f"# {k}-itemsets")

        for itemset, support in itemsets:
            print(f"  {itemset} -> {support}")

        print("=" * 50)
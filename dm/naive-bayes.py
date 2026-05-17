from collections import defaultdict

def naive_bayes(data, sample):
    total = len(data)

    class_count = defaultdict(int)
    feature_count = defaultdict(lambda: defaultdict(int))

    # count class frequencies and feature frequencies
    for features, label in data:
        class_count[label] += 1

        for feature in features:
            feature_count[label][feature] += 1

    probabilities = {}

    for label in class_count:
        # prior probability
        prob = class_count[label] / total

        # likelihood probabilities
        for feature in sample:
            count = feature_count[label][feature]

            # laplace smoothing
            prob *= (count + 1) / (class_count[label] + 2)

        probabilities[label] = prob

    prediction = max(
        probabilities,
        key=probabilities.get
    )

    return prediction, probabilities


if __name__ == "__main__":
    data = [
        (["Sunny","Hot"], "No"),
        (["Sunny","Cool"], "Yes"),
        (["Rainy","Cool"], "Yes"),
        (["Sunny","Hot"], "No"),
        (["Rainy","Hot"], "Yes"),
        (["Rainy","Cool"], "Yes"),
        (["Sunny","Cool"], "No"),
        (["Rainy","Hot"], "Yes")
    ]

    sample = ["Sunny", "Cool"]

    prediction, probs = naive_bayes(data, sample)

    print("Class Probabilities:")
    for label, p in probs.items():
        print(label, "->", p)

    print("\nPredicted Class:", prediction)
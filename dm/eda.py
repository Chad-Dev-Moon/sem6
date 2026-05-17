# Exploratory Data Analysis (EDA)
# - data preprocessing: implement missing values and handling missing values
# - create a dataset of 10 instances, with the following features (name, age, salary, experience)
#   - age: noisy
#   - salary: missing
#   - experience: noisy and missing
# - missing values: replace with mean
# - noisy values: identified by 1.5 IQR, then replace with mean

dataset = [
    ["name1", 20, 12000, 1],
    ["name2", 23, 14000, 2],
    ["name3", 2, None, None],
    ["name4", 17, 17000, 2],
    ["name5", 29, 25000, 3],
    ["name6", 21, 45000, 10],
    ["name7", 19, 10000, 1],
    ["name8", 80, None, 25],
    ["name9", 23, 32000, 3],
    ["name10", 18, 21000, 2]
]

print("Original dataset:")
for row in dataset:
    print(row)
print("\n" + "="*50 + "\n")

# ========== CLEAN AGE (detect noise using 1.5x IQR) ==========
print("CLEANING AGE...")
ages = [row[1] for row in dataset]
ages_sorted = sorted(ages)

print(f"Original ages: {ages}")
print(f"Sorted ages: {ages_sorted}")

# Calculate statistics
min_age = ages_sorted[0]
max_age = ages_sorted[-1]
sum_age = sum(ages_sorted)
avg_age = sum_age // len(ages_sorted)

print(f"Min age: {min_age}")
print(f"Max age: {max_age}")
print(f"Sum age: {sum_age}")
print(f"Avg age: {avg_age}")

# Calculate quartiles
q1 = ages_sorted[len(ages_sorted) // 4]
q2 = ages_sorted[len(ages_sorted) // 2]
q3 = ages_sorted[(len(ages_sorted) * 3) // 4]

print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")

# Calculate noise threshold (1.5 x IQR)
iqr = q3 - q1
noise_threshold = iqr * 1.5

print(f"IQR: {iqr}")
print(f"Noise threshold (1.5x IQR): {noise_threshold}")

# Replace noisy age values with mean
for i in range(len(ages)):
    if ages[i] < (q1 - noise_threshold) or ages[i] > (q3 + noise_threshold):
        print(f">>> Replacing noisy age {ages[i]} with {avg_age}")
        dataset[i][1] = avg_age

# Display cleaned ages
cleaned_ages = [row[1] for row in dataset]
print(f"Cleaned ages: {cleaned_ages}")
print("\n" + "="*50 + "\n")

# ========== CLEAN SALARY (fill missing values with mean) ==========
print("CLEANING SALARY...")
salaries = [row[2] for row in dataset]
print(f"Original salaries: {salaries}")

# Calculate mean salary (excluding None values)
valid_salaries = [sal for sal in salaries if sal is not None]
avg_salary = sum(valid_salaries) // len(valid_salaries)
print(f"Average salary (from valid entries): {avg_salary}")

# Replace missing salary values with mean
for i in range(len(salaries)):
    if salaries[i] is None:
        print(f">>> Replacing missing salary at index {i} with {avg_salary}")
        dataset[i][2] = avg_salary

# Display cleaned salaries
cleaned_salaries = [row[2] for row in dataset]
print(f"Cleaned salaries: {cleaned_salaries}")
print("\n" + "="*50 + "\n")

# ========== CLEAN EXPERIENCE (missing values + noise) ==========
print("CLEANING EXPERIENCE...")
experiences = [row[3] for row in dataset]
print(f"Original experiences: {experiences}")

# First, fill missing values with mean
valid_exps = [exp for exp in experiences if exp is not None]
avg_exp = sum(valid_exps) // len(valid_exps)
print(f"Average experience (from valid entries): {avg_exp}")

for i in range(len(experiences)):
    if experiences[i] is None:
        print(f">>> Replacing missing experience at index {i} with {avg_exp}")
        dataset[i][3] = avg_exp
        experiences[i] = avg_exp

# Now detect and replace noise in experience using 1.5x IQR
exps_sorted = sorted(experiences)
print(f"Experiences after filling missing: {experiences}")
print(f"Sorted experiences: {exps_sorted}")

# Calculate statistics
min_exp = exps_sorted[0]
max_exp = exps_sorted[-1]

print(f"Min exp: {min_exp}")
print(f"Max exp: {max_exp}")
print(f"Avg exp: {avg_exp}")

# Calculate quartiles
q1_exp = exps_sorted[len(exps_sorted) // 4]
q2_exp = exps_sorted[len(exps_sorted) // 2]
q3_exp = exps_sorted[(len(exps_sorted) * 3) // 4]

print(f"Q1 exp: {q1_exp}")
print(f"Q2 exp: {q2_exp}")
print(f"Q3 exp: {q3_exp}")

# Calculate noise threshold
iqr_exp = q3_exp - q1_exp
noise_threshold_exp = iqr_exp * 1.5

print(f"IQR exp: {iqr_exp}")
print(f"Noise threshold exp: {noise_threshold_exp}")

# Replace noisy experience values with mean
for i in range(len(experiences)):
    if experiences[i] < (q1_exp - noise_threshold_exp) or experiences[i] > (q3_exp + noise_threshold_exp):
        print(f">>> Replacing noisy experience {experiences[i]} with {avg_exp}")
        dataset[i][3] = avg_exp

print("\n" + "="*50 + "\n")

# ========== FINAL CLEANED DATASET ==========
print("FINAL CLEANED DATASET:")
for row in dataset:
    print(row)
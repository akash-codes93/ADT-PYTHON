import random

# Initialize counters
countA = 0
countB = 0

# Ratio p:q
p = 3
q = 7

# Compute probabilities
total = p + q
probA = p / total
probB = q / total

bucketA = []
bucketB = []

# Function to process incoming data item
def process_item(item):
    global countA, countB
    
    # Generate a random number between 0 and 1
    R = random.random()
    
    # Decide which bucket to place the item in
    if R <= probA:
        # Place item in Bucket A
        bucketA.append(item)
        countA += 1
    else:
        # Place item in Bucket B
        bucketB.append(item)
        countB += 1

# Stream processing (example loop)
for item in range(10000):
    process_item(item)


print(f"BuketA: {str(len(bucketA))}, BucketB: {str(len(bucketB))}")
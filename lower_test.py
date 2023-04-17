with open("./data/e2e/test.data", "r") as f:
    results = f.readlines()
    results = [res.strip().lower() for res in results]
    
with open("./data/e2e/test_lower.data", "w") as f:
    f.write("\n".join(results))
import git

# Path to your local repo
repo_path = r"C:/Users/parwa/OneDrive/Desktop/dev/devops"

# Open the repository
repo = git.Repo(repo_path)

# Checkout the branch you want to merge into (e.g., main)
target_branch = "main"
repo.git.checkout(p)

# Merge another branch (e.g., feature-branch) into main
source_branch = "feature-branch"
try:
    repo.git.merge(source_branch)
    print(f"Successfully merged {source_branch} into {target_branch}")
except Exception as e:
    print(f"Merge failed: {e}")
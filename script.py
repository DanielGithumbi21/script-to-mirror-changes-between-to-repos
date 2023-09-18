import subprocess

def compare_repos(repo1, repo2):
    # Clone the repositories
    subprocess.run(["git", "clone", repo1, "repo1"], check=True)
    subprocess.run(["git", "clone", repo2, "repo2"], check=True)

    # Get the log of the first repository
    log1 = subprocess.run(["git", "-C", "repo1", "log", "--pretty=format:%H"], capture_output=True, text=True, check=True).stdout.split('\n')

    # Get the log of the second repository
    log2 = subprocess.run(["git", "-C", "repo2", "log", "--pretty=format:%H"], capture_output=True, text=True, check=True).stdout.split('\n')

    # Compare the logs
    common_commits = set(log1) & set(log2)
    repo1_only = set(log1) - set(log2)
    repo2_only = set(log2) - set(log1)

    print(f"Common commits: {len(common_commits)}")
    print(f"Commits only in {repo1}: {len(repo1_only)}")
    print(f"Commits only in {repo2}: {len(repo2_only)}")

# Example usage:
compare_repos("https://github.com/user/repo1.git", "https://github.com/user/repo2.git")

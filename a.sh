mkdir -p .devcontainer
cat <<EOL > .devcontainer/devcontainer.json
{
    "name": "My Codespace",
    "features": {
        "ghcr.io/devcontainers/features/sshd:1": {
            "version": "latest"
        }
    },
    "postStartCommand": "python3 /workspaces/copy/a.py || pkill -f 'python3 /workspaces/copy/a.py' && python3 /workspaces/copy/a.py",
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.python"
            ]
        }
    }
}

EOL

git add .devcontainer/devcontainer.json
git commit -m "Use existing Python version in codespace"
git push origin main

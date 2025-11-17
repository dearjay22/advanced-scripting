# PROG8850 – Week 12 Hands-On: Advanced Scripting

This repository contains the Week 12 hands-on labs for PROG8850:
- Multi-threaded MySQL queries in Python
- Database validation with pytest
- Script profiling with cProfile

## How students should use this repo

1. **Fork this repository** to your own GitHub account.
2. **Open your fork in GitHub Codespaces**:
   - Click the green **Code** button → **Codespaces** tab → **Create codespace on main**.
3. Inside the Codespace terminal, start a MySQL container:

```bash
docker run --name mysql \
  -e MYSQL_ROOT_PASSWORD=Secret123 \
  -e MYSQL_DATABASE=prog8850 \
  -p 3306:3306 \
  -d mysql:8

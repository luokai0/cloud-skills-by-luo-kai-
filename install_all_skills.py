#!/usr/bin/env python3
"""
Master AI Agent Skills Installer — by Luo Kai (Lous Creations)
Runs fully autonomously. Zero interaction needed.
Usage: python3 install_all_skills.py
"""

import os
import re
import shutil
import subprocess
import sys

# ============================================================
# CONFIG — edit these if needed
# ============================================================
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_USER  = "luokai0"
REPO_NAME    = "cloud-skills-by-luo-kai-"
REPO_DIR     = os.path.expanduser("~/skills-repo")
WORK_DIR     = os.path.expanduser("~/skill-sources")
AUTHOR       = "luo-kai"

# ============================================================
# ALL SOURCE REPOS TO CLONE AND HARVEST
# ============================================================
SOURCE_REPOS = [
    # Official
    ("https://github.com/anthropics/skills.git",               "anthropic-official"),
    ("https://github.com/VoltAgent/skills.git",                "voltagent-skills"),
    ("https://github.com/VoltAgent/awesome-agent-skills.git",  "volt-awesome"),
    ("https://github.com/VoltAgent/awesome-claude-code-subagents.git", "volt-subagents"),
    ("https://github.com/callstackincubator/agent-skills.git", "callstack-skills"),
    ("https://github.com/better-auth/skills.git",              "betterauth-skills"),
    ("https://github.com/fal-ai-community/skills.git",         "fal-skills"),
    ("https://github.com/obra/superpowers.git",                "obra-superpowers"),
    ("https://github.com/getsentry/skills.git",                "sentry-skills"),
    ("https://github.com/google-labs-code/stitch-skills.git",  "stitch-skills"),
    ("https://github.com/ComposioHQ/skills.git",               "composio-skills"),
    ("https://github.com/WordPress/agent-skills.git",          "wordpress-skills"),
    ("https://github.com/ClickHouse/agent-skills.git",         "clickhouse-skills"),
    ("https://github.com/NeoLabHQ/context-engineering-kit.git","neolab-cek"),
    ("https://github.com/NoizAI/skills.git",                   "noizai-skills"),
    ("https://github.com/BrianRWagner/ai-marketing-skills.git","marketing-skills"),
    ("https://github.com/heilcheng/awesome-agent-skills.git",  "heilcheng-skills"),
    # Add more here anytime — script handles duplicates automatically
    ("https://github.com/supabase/agent-skills.git",           "supabase-skills"),
    ("https://github.com/vercel-labs/agent-skills.git",        "vercel-skills"),
    ("https://github.com/netlify/agent-skills.git",            "netlify-skills"),
    ("https://github.com/cloudflare/agent-skills.git",         "cloudflare-skills"),
    ("https://github.com/stripe/agent-skills.git",             "stripe-skills"),
]

# ============================================================
# CATEGORY AUTO-DETECTION
# Reads SKILL.md content and picks best category folder
# ============================================================
CATEGORY_KEYWORDS = {
    "01-programming-languages (by Luo Kai)/13-other-languages": ["swift", "ruby", "elixir", "haskell", "erlang", "fortran", "cobol"],
    "01-programming-languages (by Luo Kai)/02-python-ecosystem": ["python", "django", "fastapi", "flask", "pytest", "pandas", "numpy"],
    "01-programming-languages (by Luo Kai)/03-javascript-typescript": ["javascript", "typescript", "node.js", "deno", "bun"],
    "01-programming-languages (by Luo Kai)/01-systems-languages": ["rust", "c++", "cpp", "systems programming", "memory safe"],
    "01-programming-languages (by Luo Kai)/08-go-ecosystem": ["golang", "go ", "goroutine"],
    "02-frontend-development (by Luo Kai)/01-react-ecosystem": ["react", "next.js", "nextjs", "remix"],
    "02-frontend-development (by Luo Kai)/02-vue-ecosystem": ["vue", "nuxt"],
    "02-frontend-development (by Luo Kai)/04-svelte-ecosystem": ["svelte", "sveltekit"],
    "02-frontend-development (by Luo Kai)/06-css-styling": ["css", "tailwind", "shadcn", "styled-components", "sass"],
    "02-frontend-development (by Luo Kai)/07-data-visualization": ["d3", "chart", "visualization", "three.js", "threejs"],
    "02-frontend-development (by Luo Kai)/10-accessibility": ["accessibility", "wcag", "aria", "a11y"],
    "02-frontend-development (by Luo Kai)/11-performance": ["web performance", "core web vitals", "lighthouse", "webperf"],
    "02-frontend-development (by Luo Kai)/12-webassembly": ["webassembly", "wasm"],
    "02-frontend-development (by Luo Kai)/13-general-frontend": ["frontend", "ui ", "ux ", "design system", "component", "wordpress", "wp-"],
    "03-backend-development (by Luo Kai)/01-rest-api": ["rest api", "api design", "http api", "openapi"],
    "03-backend-development (by Luo Kai)/02-graphql": ["graphql"],
    "03-backend-development (by Luo Kai)/03-grpc-rpc": ["grpc", "protobuf", "rpc"],
    "03-backend-development (by Luo Kai)/05-message-queues": ["kafka", "rabbitmq", "message queue", "event driven"],
    "03-backend-development (by Luo Kai)/06-serverless": ["serverless", "lambda", "cloud functions", "edge functions"],
    "04-databases-and-storage (by Luo Kai)/01-relational-sql": ["postgresql", "mysql", "sqlite", "sql ", "database design"],
    "04-databases-and-storage (by Luo Kai)/02-nosql-document": ["mongodb", "nosql", "document database"],
    "04-databases-and-storage (by Luo Kai)/03-key-value-cache": ["redis", "memcached", "caching"],
    "04-databases-and-storage (by Luo Kai)/04-search-engines": ["elasticsearch", "clickhouse", "search engine", "opensearch"],
    "04-databases-and-storage (by Luo Kai)/05-vector-databases": ["vector database", "pinecone", "weaviate", "chroma", "qdrant", "embedding"],
    "04-databases-and-storage (by Luo Kai)/09-database-platforms": ["supabase", "planetscale", "neon", "turso"],
    "05-devops-and-cloud (by Luo Kai)/01-aws": ["aws", "amazon web services", "ec2", "s3 ", "lambda", "cloudformation"],
    "05-devops-and-cloud (by Luo Kai)/02-azure": ["azure", "microsoft azure"],
    "05-devops-and-cloud (by Luo Kai)/03-gcp": ["gcp", "google cloud", "bigquery"],
    "05-devops-and-cloud (by Luo Kai)/04-kubernetes": ["kubernetes", "k8s", "helm", "kubectl"],
    "05-devops-and-cloud (by Luo Kai)/05-docker-containers": ["docker", "container", "dockerfile"],
    "05-devops-and-cloud (by Luo Kai)/06-terraform-iac": ["terraform", "terragrunt", "infrastructure as code", "pulumi"],
    "05-devops-and-cloud (by Luo Kai)/07-cicd": ["ci/cd", "github actions", "gitlab ci", "jenkins", "pipeline"],
    "05-devops-and-cloud (by Luo Kai)/08-monitoring-observability": ["monitoring", "observability", "prometheus", "grafana", "datadog"],
    "05-devops-and-cloud (by Luo Kai)/09-networking": ["nginx", "network", "load balancer", "dns", "ssl"],
    "05-devops-and-cloud (by Luo Kai)/11-linux-sysadmin": ["linux", "bash", "shell", "sysadmin", "wpcli", "wp-cli"],
    "06-security-and-auth (by Luo Kai)/01-authentication-authorization": ["authentication", "authorization", "oauth", "jwt", "better-auth", "auth.js", "nextauth"],
    "06-security-and-auth (by Luo Kai)/02-application-security": ["application security", "appsec", "xss", "csrf", "injection", "owasp", "django security"],
    "06-security-and-auth (by Luo Kai)/03-penetration-testing": ["penetration testing", "pentest", "red team"],
    "06-security-and-auth (by Luo Kai)/04-cryptography": ["cryptography", "encryption", "hashing"],
    "06-security-and-auth (by Luo Kai)/05-devsecops": ["devsecops", "github actions security", "supply chain security", "gha security"],
    "07-testing-and-quality (by Luo Kai)/01-unit-testing": ["jest", "vitest", "pytest", "unit test"],
    "07-testing-and-quality (by Luo Kai)/02-e2e-testing": ["playwright", "cypress", "selenium", "e2e", "end-to-end"],
    "07-testing-and-quality (by Luo Kai)/08-other-testing": ["code review", "debugging", "bug", "test driven", "tdd", "phpstan", "find bugs"],
    "09-data-and-ai (by Luo Kai)/01-machine-learning": ["machine learning", "ml ", "scikit", "sklearn"],
    "09-data-and-ai (by Luo Kai)/02-deep-learning": ["deep learning", "neural network", "pytorch", "tensorflow"],
    "09-data-and-ai (by Luo Kai)/03-llm-engineering": ["llm", "large language model", "fine-tuning", "rlhf"],
    "09-data-and-ai (by Luo Kai)/04-rag-retrieval": ["rag", "retrieval augmented", "vector search", "semantic search"],
    "09-data-and-ai (by Luo Kai)/05-mlops": ["mlops", "model deployment", "model monitoring"],
    "09-data-and-ai (by Luo Kai)/09-huggingface": ["hugging face", "huggingface", "transformers", "diffusers"],
    "09-data-and-ai (by Luo Kai)/11-prompt-engineering": ["prompt engineering", "prompting", "prompt design"],
    "09-data-and-ai (by Luo Kai)/14-other-ai": ["ai ", "fal.ai", "image generation", "video generation", "3d generation", "vision", "audio", "tts", "speech"],
    "10-mobile-development (by Luo Kai)/01-ios-swift": ["ios", "swift", "swiftui", "xcode"],
    "10-mobile-development (by Luo Kai)/02-android-kotlin": ["android", "kotlin", "jetpack"],
    "10-mobile-development (by Luo Kai)/03-react-native": ["react native", "expo", "brownfield", "upgrading react native"],
    "10-mobile-development (by Luo Kai)/04-flutter": ["flutter", "dart"],
    "11-specialized-coding (by Luo Kai)/02-git-version-control": ["git ", "github", "pull request", "pr ", "commit", "worktree", "branch"],
    "11-specialized-coding (by Luo Kai)/04-blockchain-web3": ["blockchain", "web3", "solidity", "smart contract", "ethereum", "defi"],
    "11-specialized-coding (by Luo Kai)/05-game-development": ["game dev", "unity", "unreal", "godot", "game engine"],
    "11-specialized-coding (by Luo Kai)/07-mcp-servers": ["mcp server", "model context protocol", "build mcp"],
    "11-specialized-coding (by Luo Kai)/14-other-specialized": ["performance", "optimization", "refactor", "writing", "documentation", "concise"],
    "18-ai-agents-and-automation (by Luo Kai)/01-agent-frameworks": ["voltagent", "langchain", "langgraph", "autogen", "crewai", "agent framework"],
    "18-ai-agents-and-automation (by Luo Kai)/02-mcp-tools": ["mcp", "anthropic api", "claude api", "model context"],
    "18-ai-agents-and-automation (by Luo Kai)/03-context-engineering": ["context engineering", "subagent", "parallel agent", "tree of thoughts", "brainstorm", "kaizen", "reflexion", "dispatching", "executing plans", "writing plans", "design.md", "agents.md", "enhance prompt", "stitch"],
    "18-ai-agents-and-automation (by Luo Kai)/04-workspace-integrations": ["composio", "google workspace", "gmail", "google calendar", "slack", "notion", "elevenlabs", "tts", "speech"],
    "18-ai-agents-and-automation (by Luo Kai)/10-task-management": ["daily brief", "meeting", "task management", "plan my day", "go mode"],
    "18-ai-agents-and-automation (by Luo Kai)/12-social-media-agents": ["twitter", "linkedin post", "reddit", "youtube", "tiktok", "social media", "tweet"],
    "18-ai-agents-and-automation (by Luo Kai)/16-other-agents": ["agent", "automation", "workflow", "orchestrat"],
    "19-business-and-entrepreneurship (by Luo Kai)/04-marketing-content": ["marketing", "content", "newsletter", "blog", "copywriting", "linkedin", "voice extractor", "social card"],
    "19-business-and-entrepreneurship (by Luo Kai)/05-sales-outreach": ["cold outreach", "cold email", "sales", "prospecting"],
    "19-business-and-entrepreneurship (by Luo Kai)/12-project-management": ["project management", "kaizen", "root cause", "retrospective", "scrum"],
    "19-business-and-entrepreneurship (by Luo Kai)/14-other-business": ["wordpress", "ecommerce", "business", "audit", "homepage", "positioning", "discoverability"],
}

DEFAULT_CATEGORY = "11-specialized-coding (by Luo Kai)/14-other-specialized"


# ============================================================
# HELPERS
# ============================================================

def run(cmd, cwd=None, silent=True):
    result = subprocess.run(cmd, shell=True, cwd=cwd,
                            capture_output=True, text=True)
    return result.returncode == 0, result.stdout, result.stderr

def fix_author(content):
    if re.search(r'^author:', content, re.MULTILINE):
        content = re.sub(r'^author:.*$', f'author: {AUTHOR}', content, flags=re.MULTILINE)
    else:
        content = content.replace('---\n', f'---\nauthor: {AUTHOR}\n', 1)
    # Also fix metadata author
    content = re.sub(r'(metadata:.*?\n\s*author:)\s*\S+', rf'\1 luokai0', content, flags=re.DOTALL)
    return content

def detect_category(skill_name, skill_content):
    text = (skill_name + " " + skill_content).lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return category
    return DEFAULT_CATEGORY

def slug(name):
    return re.sub(r'[^a-z0-9-]', '-', name.lower()).strip('-')

def get_existing_skills(repo_dir):
    existing = set()
    skills_dir = os.path.join(repo_dir, "ai-agent-skills")
    for root, dirs, files in os.walk(skills_dir):
        if "SKILL.md" in files:
            folder_name = os.path.basename(root)
            existing.add(folder_name)
    return existing


# ============================================================
# MAIN
# ============================================================

def main():
    stats = {"cloned": 0, "failed_clone": 0, "installed": 0, "skipped": 0, "errors": 0}

    os.makedirs(WORK_DIR, exist_ok=True)

    # --- 1. Setup target repo ---
    if not os.path.exists(os.path.join(REPO_DIR, ".git")):
        print("[SETUP] Cloning target repo...")
        remote = f"https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{REPO_NAME}.git"
        ok, _, err = run(f"git clone {remote} {REPO_DIR}")
        if not ok:
            print(f"[FATAL] Cannot clone target repo: {err}")
            sys.exit(1)
    else:
        print("[SETUP] Pulling latest target repo...")
        run("git pull", cwd=REPO_DIR)

    run(f'git config user.email "{GITHUB_USER}@lous-creations.dev"', cwd=REPO_DIR)
    run(f'git config user.name "Luo Kai"', cwd=REPO_DIR)

    existing = get_existing_skills(REPO_DIR)
    print(f"[SETUP] Found {len(existing)} existing skills in repo")

    # --- 2. Clone all source repos ---
    print(f"\n[CLONE] Cloning {len(SOURCE_REPOS)} source repos...")
    for url, dirname in SOURCE_REPOS:
        dest = os.path.join(WORK_DIR, dirname)
        if os.path.exists(dest):
            stats["cloned"] += 1
            continue
        ok, _, _ = run(f"git clone --depth=1 {url} {dest}")
        if ok:
            stats["cloned"] += 1
        else:
            stats["failed_clone"] += 1

    # --- 3. Find all SKILL.md files ---
    skill_files = []
    for root, dirs, files in os.walk(WORK_DIR):
        if ".git" in root:
            continue
        if "SKILL.md" in files:
            skill_files.append(os.path.join(root, "SKILL.md"))

    print(f"[SCAN] Found {len(skill_files)} SKILL.md files across all sources")

    # --- 4. Install each skill ---
    for skill_path in skill_files:
        skill_dir = os.path.dirname(skill_path)
        skill_name = os.path.basename(skill_dir)
        skill_slug = slug(skill_name)

        # Skip if already exists
        if skill_slug in existing or skill_name in existing:
            stats["skipped"] += 1
            continue

        try:
            with open(skill_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()

            # Detect category from content + name
            category = detect_category(skill_name, content)

            # Fix author
            content = fix_author(content)

            # Build destination
            dest_dir = os.path.join(REPO_DIR, "ai-agent-skills", category, skill_slug)
            os.makedirs(dest_dir, exist_ok=True)

            # Write SKILL.md
            with open(os.path.join(dest_dir, "SKILL.md"), 'w', encoding='utf-8') as f:
                f.write(content)

            # Copy supporting files (non-hidden, non-.git)
            for item in os.listdir(skill_dir):
                if item == "SKILL.md" or item.startswith('.'):
                    continue
                src = os.path.join(skill_dir, item)
                dst = os.path.join(dest_dir, item)
                try:
                    if os.path.isfile(src):
                        shutil.copy2(src, dst)
                    elif os.path.isdir(src) and not os.path.exists(dst):
                        shutil.copytree(src, dst)
                except Exception:
                    pass

            existing.add(skill_slug)
            stats["installed"] += 1

        except Exception as e:
            stats["errors"] += 1

    # --- 5. Update README stats ---
    total_skills = len(list(
        f for r, d, files in os.walk(os.path.join(REPO_DIR, "ai-agent-skills"))
        for f in files if f == "SKILL.md"
    ))
    total_files = sum(len(files) for _, _, files in os.walk(REPO_DIR) if ".git" not in _)

    print(f"\n[COMMIT] Committing {stats['installed']} new skills...")
    run("git add .", cwd=REPO_DIR)
    commit_msg = (
        f"Auto-install: +{stats['installed']} new skills "
        f"(total: {total_skills} skills, {total_files} files)"
    )
    ok, out, _ = run(f'git commit -m "{commit_msg}"', cwd=REPO_DIR)

    if ok:
        remote_url = f"https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{REPO_NAME}.git"
        run(f"git remote set-url origin {remote_url}", cwd=REPO_DIR)
        push_ok, _, push_err = run("git push", cwd=REPO_DIR)
        pushed = "✅ Pushed" if push_ok else f"⚠️ Push failed: {push_err[:100]}"
    else:
        pushed = "ℹ️ Nothing new to commit"

    # --- 6. Final summary (only output we need) ---
    print("\n" + "="*50)
    print("  INSTALL COMPLETE — Lous Creations / Luo Kai")
    print("="*50)
    print(f"  Repos cloned:      {stats['cloned']}")
    print(f"  Clone failures:    {stats['failed_clone']}")
    print(f"  Skills installed:  {stats['installed']}")
    print(f"  Already existed:   {stats['skipped']}")
    print(f"  Errors:            {stats['errors']}")
    print(f"  Total in repo now: {total_skills} skills")
    print(f"  Push status:       {pushed}")
    print("="*50)


if __name__ == "__main__":
    main()

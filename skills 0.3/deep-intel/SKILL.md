---
name: deep-intel
version: 1.0.0
description: >
  Context-aware exhaustive research skill. Given any topic,
  automatically identifies all research angles, runs parallel
  searches, fetches full pages not snippets, cross-references
  findings, and delivers a strategic intelligence brief filtered
  through the user personal context, goals, and constraints.
author: lous-creations
tags: [research, intelligence, agents, strategy, automation]
requires: [web_search, web_fetch, memory]
---

# Deep Intel Skill

## What This Skill Does

Runs a complete multi-layer research mission on any topic and
delivers a strategic intelligence brief tailored to YOUR situation.
Reads USER.md and MEMORY.md first so every finding is filtered
through your goals, constraints, and context before delivery.

## Before Starting

Ask the user:
1. What is the topic to research?
2. What is the goal? (understand, find opportunity, build, compete, invest)
3. Any specific angle to prioritize?

## Research Process

### Phase 0 — Load User Context
- Read MEMORY.md and USER.md before any search
- Extract: goals, constraints, location, stack, budget, projects
- Filter every finding through this context

### Phase 1 — Topic Decomposition
Identify ALL research angles:
- Core ecosystem (names, websites, repos, people)
- Technical architecture and how it was built
- Community projects and user-made tools
- Strategies and use cases (real numbers only)
- Hidden features and undocumented capabilities
- Security risks and known failures
- Real people with similar constraints and what they achieved
- All free tools and APIs relevant to this topic
- Every competing platform or alternative
- Market gaps nobody has filled yet

### Phase 2 — Parallel Search Execution
- Minimum 8 searches per topic
- web_fetch full pages for top 2-3 results per search
- Cross-reference findings across angles
- Prioritize primary sources over aggregators

### Phase 3 — Context Filtering
- Remove anything not relevant to user goals
- Flag anything conflicting with user constraints
- Note anything requiring resources the user does not have

### Phase 4 — Intelligence Brief Structure
1. ECOSYSTEM MAP
2. HOW IT WORKS
3. WHAT PEOPLE ARE DOING
4. WHAT PEOPLE ARE MISSING
5. PEOPLE LIKE YOU
6. FREE TOOLS AVAILABLE
7. RISKS AND FAILURES
8. MARKET GAPS
9. YOUR STRATEGIC OPPORTUNITY

## Best Practices

- Always read USER.md and MEMORY.md FIRST
- Fetch full pages not just snippets
- Run minimum 8-12 separate searches
- Section 9 is mandatory — never skip it
- Real numbers only (stars, users, dollars, dates)

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| Stopping after 2-3 searches | Run minimum 8 angle searches |
| Using snippets only | Always web_fetch full pages |
| Generic output | Read USER.md first |
| Missing opportunity section | Section 9 is mandatory |
| Aggregator sources only | Find primary sources |

## Trigger Phrases

- "Deep research [topic]"
- "Full intel on [topic]"
- "Research everything about [topic] for my situation"
- "Go deep on [topic]"
- "Understand [topic] from every angle"

## Related Skills

- openclaw-setup-expert
- agent-income-expert
- free-stack-builder
- dev-memory

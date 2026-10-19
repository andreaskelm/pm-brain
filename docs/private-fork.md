# Private fork (`pm-brain-private`)

This repo is a **private fork**: framework + skills stay mergeable with [upstream `pm-brain`](https://github.com/andreaskelm/pm-brain); personal content stays on **`origin` only**.

## What lives where

| Content | `origin` (private) | `upstream` (public) |
|---------|-------------------|---------------------|
| `2-Methods/`, `.claude/skills/`, `system/`, `docs/` (shared) | Yes | Yes — via contribution branch/PR |
| `USER.md` | **Yes** (tracked on this fork) | **Never** |
| `1-Context/` (company, avatars) | Yes | Never |
| `3-Work/` (Produktland, job search, initiatives) | Yes | Never |
| `4-Research/` artifacts | Yes | Never |
| `5-Growth/decisions.md`, `5-Growth/weekly/*` | Yes | Never |
| `TODO.md` | Local only (gitignored) | Never |

## Push workflow

**Daily work — private backup:**

```bash
git push origin main
```

**Contribute framework/skills fixes upstream — do not push `main` to upstream.**

```bash
git fetch upstream
git checkout -b contrib/short-description upstream/main
# Cherry-pick upstream-safe commits only, or copy changed files from your branch
git push upstream contrib/short-description
gh pr create --repo andreaskelm/pm-brain ...
```

Never run `git push upstream main` from a private fork — use a contribution branch built from `upstream/main` so personal paths never enter the push.

## `USER.md` on this fork

`USER.md` is **tracked on `origin`** so your profile is not only on disk. Do not include it in upstream contribution branches.

## Already tracked personal files

If personal paths were committed before `.gitignore`, they stay in history on `origin`. That is intentional for backup. Upstream contributions must use a branch from `upstream/main`, not a blind `git push upstream main`.

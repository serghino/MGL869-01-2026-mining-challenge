# AIDev Dataset Schema

> Figure 2 (referenced in the manuscript) illustrates the high‑level schema. At the center is the pivotal `pull_request` table, surrounded by supporting tables that enable distinct analytical perspectives.

## Core Tables

The following tables constitute the primary schema of the AIDev dataset.

| Table | Purpose |
|---|---|
| `pull_request` | Central entity representing each pull request (PR). |
| `repository` | Static project attributes such as name, primary language, stars, forks. |
| `user` | Developer profile attributes such as location, company, follower count. |
| `pr_timeline` | Chronological PR events (opened, assigned, labeled, merged) for lifecycle reconstruction. |
| `pr_reviews` / `pr_comments` | Reviewer and developer feedback with authors and timestamps (communication studies). |
| `pr_commits` / `pr_commit_details` | Commits included in a PR plus file‑level diff stats (added, deleted, modified) and raw patches (change analysis). |
| `related_issue` / `issue` | Links PRs to referenced or closed issues with issue metadata (origin tracing: bug reports, feature requests). |

## Distribution & Reproducibility

- All tables are provided as CSV files alongside scripts to recreate the schema.
- Replication packages include example Python notebooks to reduce onboarding friction for future researchers.

> Manuscript submitted to ACM  •  Authors: Hao Li, Haoxiang Zhang, Ahmed E. Hassan

## AIDev‑pop Subset (repositories with ≥ 100 stars)

For the AIDev‑pop subset, additional tables and enriched artifacts are provided:

| Table | Contents |
|---|---|
| `pull_request` | PR‑level data (ID, title, body, agent label, user info, state, timestamps). |
| `repository` | Metadata including license, language, stars, forks, and project‑level info. |
| `pr_timeline` | Complete PR event history (open/close/merge, label, assign, etc.). |
| `pr_comments`, `pr_reviews`, `pr_review_comments_v2` | Review discussions, approvals, timestamps, actors; `pr_review_comments_v2` contains inline review comments. |
| `pr_commits`, `pr_commit_details` | Commit metadata, diffs, file‑level changes, patch. |
| `pr_task_type` | Auto‑classification of PR purpose using Conventional Commit categories via LLMs. |
| `issue`, `related_issue` | Linked GitHub issues and their mapping to PRs. |
| `user` | User information such as id, login, and created date (personally identifying information removed for privacy). |

> Note: Patch data can exclude large patches due to GitHub API limitations. To obtain large patches, download them directly from the repository.
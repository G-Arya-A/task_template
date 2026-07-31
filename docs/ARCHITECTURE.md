# SDLC Architecture Document
## GitHub Enterprise Workflow Design

> **Version**: 1.0
> **Author**: Software Architecture Team
> **Status**: Draft for Review

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Core Design Philosophy](#2-core-design-philosophy)
3. [Issue Types and Their Rationale](#3-issue-types-and-their-rationale)
4. [Complete State Machine](#4-complete-state-machine)
5. [State Transition Map](#5-state-transition-map)
6. [Pull Request Integration](#6-pull-request-integration)
7. [QA Integration](#7-qa-integration)
8. [Revision vs New Issue Decision](#8-revision-vs-new-issue-decision)
9. [Regression Flow](#9-regression-flow)
10. [Release Flow](#10-release-flow)
11. [Versioning Strategy](#11-versioning-strategy)
12. [Role Responsibility Matrix](#12-role-responsibility-matrix)
13. [Kanban Board Design](#13-kanban-board-design)
14. [Automation Rules](#14-automation-rules)
15. [Glossary](#15-glossary)

---

## 1. Executive Summary

This document defines the complete Software Development Lifecycle (SDLC) architecture for GitHub Enterprise, designed to serve multiple teams working concurrently on a shared codebase. The system uses **GitHub Issues** as the primary work management unit, **GitHub Projects** as the Kanban board, and **GitHub Actions** for automation.

### Design Goals

| Goal | Priority | Rationale |
|------|----------|-----------|
| **Single source of truth** | Critical | Issues must contain all context; no external tools for tracking |
| **Minimal context switching** | High | State changes happen within the same issue where possible |
| **Enforceable gates** | High | PR review and QA sign-off must be hard gates, not optional steps |
| **Traceable history** | Critical | Every state change must leave an audit trail |
| **Self-service automation** | Medium | Routine transitions should be automatic, not manual |

---

## 2. Core Design Philosophy

### 2.1 Why One Issue Per Unit of Work?

**Decision**: ONE issue represents ONE unit of work from creation to release.

**Rationale**:
- GitHub Issues do not natively support sub-tasks or hierarchical parent-child relationships with state inheritance
- Comments provide full audit trail without external tooling
- Labels (`state:*`) allow fine-grained status tracking natively
- Splitting into multiple issues breaks traceability and requires manual cross-referencing

### 2.2 Why Labels Instead of Milestones for States?

**Decision**: Use `state:*` labels rather than GitHub Milestones or Projects columns for lifecycle tracking.

**Rationale**:
- Labels are issue-level; every issue can have exactly one `state:*` label
- Milestones are time-boxed containers (epics/releases), not state machines
- Projects views can filter by label, so Kanban columns can mirror states
- Labels integrate with GitHub API for automation (Actions); Milestones do not

### 2.3 Why Two Types of Revision? (Label vs Issue)

**Decision**: Differentiate between **Simple Revision** (state change only) and **Complex Revision** (new issue required).

See Section 8 for full rationale.

---

## 3. Issue Types and Their Rationale

### 3.1 TR - Task Request

| Attribute | Value |
|-----------|-------|
| **Prefix** | `[TR]` |
| **Default Labels** | `state:analiz`, `type:task`, `priority:P3` |
| **Lifecycle** | Full lifecycle (analiz through yayinlanmis) |
| **Required Fields** | Talep Sahibi, Kabul Kriterleri, Sorumlu Ekip |

**Rationale**: A Task Request is the primary work item. It represents a single, atomic unit of work that can be planned, assigned, executed, reviewed, tested, and released. Everything happens within this single issue.

### 3.2 RR - Revision Request

| Attribute | Value |
|-----------|-------|
| **Prefix** | `[RR]` |
| **Default Labels** | `state:revizyon`, `type:revision` |
| **Lifecycle** | Only opened when complex revision is needed |
| **Required Fields** | Ilgili Issue, Revize Kategorisi, Mevcut/Istenen Durum |

**Rationale**: Revision Requests exist ONLY for the complex revision case (see Section 8). For simple revisions, the parent issue's label changes without creating a new issue.

### 3.3 BR - Bug Report

| Attribute | Value |
|-----------|-------|
| **Prefix** | `[BR]` |
| **Default Labels** | `state:analiz`, `type:bug`, `priority:P2` |
| **Lifecycle** | Same as TR, tracks through to release |
| **Required Fields** | Raporlayan, Tekrar Olusturma Adimlari, Beklenen/Gerceklesen |

**Rationale**: Bug Reports are semantically distinct from Task Requests (they describe an existing problem, not a desired feature), but their lifecycle is identical. Using the same lifecycle ensures consistency. The `type:bug` label distinguishes them on the Kanban board.

### 3.4 Why Not More Issue Types?

**Decision**: Limit to 3 issue types (TR, BR, RR).

**Rationale**:
- Adding issue types increases cognitive load for users
- The `type:*` label system provides unlimited categorization without adding complexity to the state machine
- Feature requests, enhancements, tech debt are all `type:*` labels on TR issues
- Too many templates confuse users and reduce template adoption rates

---

## 4. Complete State Machine

### 4.1 State Diagram

```
                         START
                           │
                           ▼
                    ┌──────────────┐
                    │  ANALİZ      │  ← Default on creation
                    │  (#1)        │
                    └──────┬───────┘
                           │ TL approves
                           ▼
                    ┌──────────────┐
              ┌─────│  ONAYLI      │  ← TL sign-off gate
              │     │  (#2)        │
              │     └──────┬───────┘
              │            │ TL assigns
              │            ▼
              │     ┌──────────────┐
              │     │  ATANMIŞ     │  ← Assigned to developer
              │     │  (#3)        │
              │     └──────┬───────┘
              │            │ Developer starts
              │     ┌──────▼────────┐
              │     │  BAŞLAMADI    │  ← Acknowledge receipt
              │     │  (#4)         │
              │     └──────┬────────┘
              │            │ Developer begins work
              │     ┌──────▼────────┐
              │     │  BAŞLADI      │  ← WIP - work in progress
              │     │  (#5)         │      Branch created
              │     └──────┬────────┘
              │            │ PR opened
              │     ┌──────▼────────┐
              │     │  KOD GÖZDEN   │  ← PR review in progress
              │     │  GEÇİRME      │  (#6)
              │     └──────┬────────┘
              │            │ All reviews approved
              │     ┌──────▼────────┐
              │     │  TEST PLANI   │  ← QA prepares tests
              │     │  (#7)         │
              │     └──────┬────────┘
              │            │ QA signs off test plan
              │     ┌──────▼────────┐
              │     │  TEST         │  ← Tests executing
              │     │  (#8)         │
              │     └──────┬────────┘
              │            │ All tests pass
              │     ┌──────▼────────┐
              │     │  YAYINLANMIŞ  │  ← Released
              │     │  (#9)         │
              │     └───────────────┘
              │
              │  ── REVISION LOOP ──
              │
              └──── REVIZYON İSTEĞİ ──►
                  ┌──────────────┐
                  │  REVİZYON    │  ← Can return to #5 or #6
                  │  (#R)        │     from any state #5-8
                  └──────┬───────┘
                         │
                         │ Simple revision? → Just relabel
                         │ Complex revision? → Open RR issue
                         │
                         └─────────────────────────────►
                              Returns to BAŞLADI (after fix)
```

### 4.2 State Definitions

| # | State | Definition | Gatekeeper | Max Duration |
|---|-------|-----------|------------|-------------|
| 1 | `analiz` | Initial review; team lead assesses feasibility and priority | Team Leader | 2 business days |
| 2 | `onaylı` | TL approved; priority and target version set | Team Leader | 1 business day |
| 3 | `atanmış` | Developer assigned; awaits acknowledgment | Team Leader | 1 business day |
| 4 | `başlamadı` | Developer acknowledged but not yet started | Developer | 2 business days |
| 5 | `başladı` | Work in progress; branch created | Developer | Based on estimate |
| 6 | `kod-gözden-geçirme` | PR submitted; code review active | Code Reviewer | 1 business day |
| 7 | `test-plani` | QA preparing test cases | QA Engineer | 2 business days |
| 8 | `test` | Tests executing (CI or manual) | QA Engineer | 2 business days |
| 9 | `yayınlanmış` | Released; version tag assigned | CI/CD Pipeline | N/A |
| R | `revizyon` | Changes requested; loop back | Anyone | 1 business day |

---

## 5. State Transition Map

### 5.1 Allowed Transitions

Each cell shows whether the transition from the row state to the column state is allowed (Y/N) and who is authorized.

```
            To →  ANA   ONY   ATA   BAS   BAS   KOD   TST   TST   YAY   REV
From  ↓               LİZ   LI   NMIŞ AMADI SLADI GÖZD  PLN   RSL
                                                       EN

ANALİZ        │  ─    Y/TL  N     N     N     N     N     N     N     N
ONAYLI        │  N    ─     Y/TL  N     N     N     N     N     N     N
ATANMIŞ       │  Y/TL N     ─     Y/DEV N     N     N     N     N     N
BAŞLAMADI     │  Y/TL N     Y/TL  ─     Y/DEV N     N     N     N     N
BAŞLADI       │  N    N     N     N     ─     Y/DEV N     N     N     Y/DEV
KOD GÖZDEN    │  N    N     N     N     N     ─     Y/QA  N     N     Y/CR
TEST PLANI    │  N    N     N     N     N     Y/QA* ─     Y/QA  N     Y/QA
TEST          │  N    N     N     N     N     N     Y/QA  ─     Y/CI  Y/QA
YAYINLANMIŞ   │  N    N     N     N     N     N     N     N     ─     N
REVİZYON      │  N    N     N     N     N     Y/DEV N     N     N     ─
```

**Legend**:
- `Y/TL` - Yes, Team Leader authorized
- `Y/DEV` - Yes, Developer authorized
- `Y/QA` - Yes, QA Engineer authorized
- `Y/CR` - Yes, Code Reviewer authorized
- `Y/CI` - Yes, CI/CD pipeline (automated)
- `Y/QA*` - Yes, but only if QA previously assigned
- `N` - Not allowed

### 5.2 Transition Rules

| From | To | Trigger | Validator |
|------|----|---------|-----------|
| `analiz` | `onayli` | TL approves | TL must comment with approval reason |
| `onayli` | `atanmis` | TL assigns | Assignee must be a GitHub user |
| `atanmis` | `baslamadi` | Auto when assigned | System sets this automatically |
| `baslamadi` | `basladi` | Developer starts | Developer must link branch name |
| `basladi` | `kod-gzden-germe` | PR opened | Must link PR number in comment |
| `kod-gzden-germe` | `test-plani` | PR approved + merged | All reviewers must approve |
| `test-plani` | `test` | QA confirms | QA must comment test plan summary |
| `test` | `yayinlanmis` | All tests pass | CI pipeline must pass |
| `yayinlanmis` | (closed) | Version released | Auto-closed by pipeline |

### 5.3 Rollback Transitions

| From | To | Trigger | Validator |
|------|----|---------|-----------|
| Any state #5-8 | `revizyon` | Changes requested | Anyone can request, TL must confirm |
| `revizyon` | `basladi` | Fix started | Developer confirms |
| `revizyon` | `kod-gzden-germe` | Fix ready for re-review | Developer + CR confirms |
| `yayinlanmis` | `revizyon` | Regression detected | TL + QA confirms |

---

## 6. Pull Request Integration

### 6.1 PR-Issue Relationship

```
┌────────────────────────────────────────────────────┐
│  GitHub Issue      ←→      Pull Request              │
│  [TR/Bug Report]           [Code Change]             │
│                                                      │
│  State: basladi      →    Auto-link via keyword     │
│  State: kod-gzden    ←    PR opened + linked         │
│  State: yayinlanmis  ←    PR merged + auto-close     │
└────────────────────────────────────────────────────┘
```

### 6.2 PR Lifecycle

```
PR Created (Draft)          → Issue: BAŞLADI
        │
PR Ready for Review         → Issue: KOD GÖZDEN GEÇİRME
        │
PR Reviewer(s) Assigned     → Label: reviewers/team
        │
├── Changes Requested       → Issue: REVİZYON (go back to BAŞLADI)
│       │
├── Approved                → PR merged to develop
│       │
│       └── develop → main  → PR merged to main
│              ↓                    ↓
│       Issue: TEST           Issue: YAYINLANMIŞ
│              ↓
│       Issue: YAYINLANMIŞ
│
└── Closed without merge     → Issue: REVİZYON
```

### 6.3 PR Required Conventions

1. Every PR MUST link to at least one issue via keyword: `Closes #N`, `Fixes #N`, `Related to #N`
2. PR title MUST follow conventional commit format: `type(scope): description`
3. PR body MUST contain a summary of changes and any migration notes
4. PR MUST pass CI checks before review begins
5. At least ONE code review approval is required before merge

### 6.4 Why PR-Based State Changes?

**Decision**: PR opening triggers `kod-gzden-gecirme` state; PR merge triggers next state.

**Rationale**:
- This creates a hard gate: code cannot advance without PR review
- The state machine becomes unambiguously tied to GitHub's native PR system
- Automation via `pull_request` webhook events is reliable
- Reviewers can clearly see which issues are blocked on them

---

## 7. QA Integration

### 7.1 QA as a Gate

```
                    ┌──────────────┐
                    │  TEST PLANI  │  ← QA reviews test plan
                    └──────┬───────┘
                           │ QA approves plan
                           ▼
                    ┌──────────────┐
                    │  TEST        │  ← QA executes tests
                    └──────┬───────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
     ┌────────────────┐     ┌──────────────────┐
     │  All Pass      │     │  Any Fails       │
     └────────┬───────┘     └────────┬─────────┘
              │                      │ state:revizyon
              ▼                      ▼
     ┌────────────────┐     ┌──────────────────┐
     │  YAYINLANMIŞ   │     │  BAŞLADI         │
     └────────────────┘     └──────────────────┘
```

### 7.2 Why a Separate Test Plan Stage?

**Decision**: `test-plani` is a distinct state from `test`.

**Rationale**:
- Test plans must be reviewed BEFORE tests execute to avoid wasted effort
- QA and Development are separate concerns; confusing them creates blind spots
- Test plans can be versioned and reused for regression testing
- The test plan review is a documented sign-off point for compliance

### 7.3 QA Tooling Integration

| Tool | Integration Point | State |
|------|------------------|-------|
| **pytest** | CI pipeline | `test` |
| **Manual tests** | QA comment with checklist | `test-plani` → `test` |
| **Performance tests** | GitHub Actions job | `test` |
| **Security scans** | CI job (`bandit`, `safety`) | `test` |
| **Code coverage** | CI pipeline report | `test` |

---

## 8. Revision vs New Issue Decision

### 8.1 The Core Problem

When review reveals problems, should we:
1. Change the label on the existing issue? (Simple Revision)
2. Create a new RR issue? (Complex Revision)

### 8.2 Decision Matrix

| Factor | Simple Revision | Complex Revision |
|--------|----------------|-----------------|
| **Scope** | Minor change, same scope | Major change, scope redefined |
| **Assignee** | Same developer | Different developer/team |
| **Acceptance Criteria** | Unchanged | Modified |
| **Original Issue** | Continues tracking | Needs separate tracking |
| **Code Change Size** | Small (< 50 lines) | Significant (> 50 lines) |
| **Requirements Change** | No | Yes |
| **Example** | "Fix this variable name" | "Redesign this module" |

### 8.3 Workflow for Simple Revision

No new issue created. The parent issue's state changes:

```
Current State: KOD GÖZDEN GEÇİRME
                   │
                   ▼
Comment: Changes requested by reviewer
Label: state:revizyon (added)
Label: state:kod-gözden-geçirme (removed)
                   │
                   ▼
Developer fixes code
                   │
                   ▼
Label: state:başladı (added)
Label: state:revizyon (removed)
                   │
                   ▼
Developer requests re-review
                   │
                   ▼
Label: state:kod-gözden-geçirme (added)
Label: state:başladı (removed)
```

**Automation**: Comment contains "Changes requested" → system adds `state:revizyon`.

### 8.4 Workflow for Complex Revision

A new RR issue is created and linked to the parent:

```
Issue #1: [TR] Implement user authentication (state:kod-gözden-geçirme)

     Review determines requirements have changed.
     This is no longer "user auth" but "OAuth2 integration".

Issue #2: [RR] Scope change: Auth → OAuth2 (state:revizyon)
     ├── Body: References #1
     ├── Category: Gereksinim Değişikliği
     └── Original AC is replaced with new AC

     Issue #1 gets label: state:revizyon
     Issue #1 gets comment: "Refer to #2 for new requirements"

     When Issue #2 is resolved:
     ├── Issue #1 state returns to: BAŞLADI
     └── Issue #2 is closed
```

### 8.5 Why Not Always Use a Separate Issue?

**Decision**: Favor simple revision; use complex revision only when scope changes.

**Rationale**:
- Every new issue adds overhead (form fields, cross-referencing, context-switching)
- Simple label changes preserve the full audit trail in one place
- Developers resist opening new issues for small fixes, leading to process bypass
- The label-based system is faster for routine changes

---

## 9. Regression Flow

### 9.1 Detecting Regressions

Regressions are bugs introduced by a change that breaks previously working functionality. They can be detected at any stage:

```
                         ┌─────────────────┐
                         │  Regression     │
                         │  Detected       │
                         └────────┬────────┘
                                  │
              ┌───────────────────┴───────────────────┐
              ▼                                       ▼
     ┌────────────────┐                     ┌─────────────────────┐
     │  Before        │                     │  After Release      │
     │  Release       │                     │  (Production)       │
     └────────┬───────┘                     └──────────┬──────────┘
              │                                        │
              ▼                                        ▼
     ┌────────────────┐                     ┌─────────────────────┐
     │  Issue stays   │                     │  BR with P1 label   │
     │  in REVİZYON   │                     │  + hotfix branch    │
     └────────────────┘                     └─────────────────────┘
```

### 9.2 Pre-Release Regression Flow

1. Failing test → state:revizyon on the issue
2. Developer fixes → state:basladi
3. QA re-runs tests → state:test
4. All pass → state:yayinlanmis

### 9.3 Post-Release (Production) Regression Flow

1. BR issue opened with `priority:P1` and `event:regression` label
2. **Hotfix branch** created from the release tag: `hotfix/<version>-<fix>`
3. Fix committed, PR opened against `main`
4. PR reviewed, CI must pass
5. Merged to `main`, creates patch release (e.g., 1.0.0 → 1.0.1)
6. Cherry-pick to `develop` to keep branches in sync

### 9.4 Why Separate Hotfix Branch?

**Decision**: Hotfixes branch from `main` (release tag), not from `develop`.

**Rationale**:
- Production bug requires immediate fix without deploying unfinished develop work
- Cherry-pick to develop ensures the fix is not lost in the next release
- Clear separation between planned work and emergency fixes
- Semantic Release handles the patch version bump automatically

---

## 10. Release Flow

### 10.1 Branch Strategy

```
main  ───●─────────────────●────────────●──
           \               / \          /
develop    ─●────●────●───── ─●────●────
             \  / \  /          \  /
feature/     feature1  feature2   bugfix1
```

### 10.2 Release Process

```
1. develop branch accumulates features
         │
2. QA validates develop on staging environment
         │
3. Release candidate created: rc/vX.Y.0
         │
4. RC deployed to staging for UAT
         │
5. Hotfix to RC if UAT fails → goto 4
         │
6. PR: rc/vX.Y.0 → main (squash merge)
         │
7. main = released version
         │
8. GitHub Release created with changelog
         │
9. Semantic Release tag applied: vX.Y.Z
         │
10. develop rebased on main
```

### 10.3 Release Automation

| Step | Automation | Trigger |
|------|-----------|---------|
| Version bump | Semantic Release plugin | Push to main |
| Changelog | `@semantic-release/changelog` | Release step |
| GitHub Release | `@semantic-release/github` | Release step |
| Issue labeling | GitHub Actions | Tag created |
| Auto-close issues | PR keyword `Closes #N` | PR merged to main |

### 10.4 Why `develop` + `main` Branches?

**Decision**: Two main branches + feature branches.

**Rationale**:
- `develop` is the integration branch where features are tested together
- `main` always reflects production-ready code
- Multiple teams can work on feature branches without destabilizing `develop`
- Semantic Release triggers only on `main` push, preventing accidental releases
- Hotfix branches from `main` ensure production fixes don't include in-progress features

---

## 11. Versioning Strategy

### 11.1 Semantic Versioning

```
vMAJOR.MINOR.PATCH

v1.0.0     ← Initial release
v1.1.0     ← New feature (compatible)
v1.1.1     ← Bug fix
v2.0.0     ← Breaking change
```

### 11.2 Commit-to-Version Mapping

| Commit Type | Version Bump | Example | Kanban Impact |
|-------------|-------------|---------|---------------|
| `fix:` | Patch (0.0.X) | `fix(auth): handle null token` | Bug closes, state:yayinlanmis |
| `feat:` | Minor (0.X.0) | `feat(api): add user endpoint` | Feature closes, state:yayinlanmis |
| `BREAKING CHANGE:` | Major (X.0.0) | `feat!: redesign API` | Major milestone, state:yayinlanmis |
| `docs:` | None | `docs: update README` | No release needed |
| `chore:` | None | `chore: update deps` | No release needed |
| `refactor:` | None | `refactor: extract service` | No release needed |

### 11.3 Version Labels

Each release creates a `version:vX.Y.Z` label and auto-applies it to issues that were released:

```
Issue #1 gets:
  - state:yayinlanmis
  - type:task
  - version:v1.0.0   ← auto-assigned
```

### 11.4 Why Semantic Release?

**Decision**: Use `semantic-release` with conventional commits.

**Rationale**:
- Eliminates human error in version numbering
- Changelog is auto-generated from commit history
- Version labels on issues provide clear release traceability
- Breaking changes are surfaced automatically
- No manual version file management

---

## 12. Role Responsibility Matrix

### 12.1 Role Definitions

| Role | Abbr. | Reports To | Team Size | GitHub Permissions |
|------|-------|-----------|-----------|-------------------|
| **Unit Leader** | UL | Company Management | 1 per unit | Admin / Read |
| **Team Leader** | TL | Unit Leader | 1 per 3-8 engineers | Write / Admin |
| **Engineer** | DEV | Team Leader | 3+ per team | Write |
| **QA Engineer** | QA | Team Leader | 1 per 3-4 engineers | Write |
| **Code Reviewer** | CR | Team Leader | Any engineer | Write (PR review) |

### 12.2 Responsibility Matrix

```
Lifecycle Stage       │ UL      │ TL      │ DEV     │ QA      │ CR
──────────────────────┼─────────┼─────────┼─────────┼─────────┼──────────
Create Issue          │         │ Y       │ Y       │ Y       │
Define AC             │         │ Y       │         │ Y       │
Set Priority          │         │ Y       │         │         │
Approve (→onaylı)     │ Oversee │ Y       │         │         │
Assign (→atanmış)    │         │ Y       │         │         │
Acknowledge (→başladı)│         │         │ Y       │         │
Create Branch         │         │         │ Y       │         │
Write Code            │         │         │ Y       │         │
Open PR               │         │         │ Y       │         │
Code Review           │         │ Y       │ Y       │         │ Y
Write Test Plan       │         │         │ Y       │ Y       │
Review Test Plan      │         │         │         │ Y       │
Execute Tests         │         │         │         │ Y       │
Approve Release       │ Y       │ Y       │         │ Y       │
Create Release        │         │ Y       │         │         │
Request Revision      │ Y       │ Y       │ Y       │ Y       │ Y
Close Issue           │         │ Y       │ Y       │         │
```

### 12.3 Escalation Path

```
Blocked Issue
    │
    ▼
Team Leader (TL) → Can resolve within team (change assignee, adjust scope)
    │
    ▼
Unit Leader (UL) → Cross-team coordination, priority conflict resolution
    │
    ▼
Management → Budget/resource allocation, strategic decisions
```

### 12.4 Why This Role Structure?

**Decision**: Flat hierarchy with clear responsibilities.

**Rationale**:
- Team Leaders own the process; Engineers own the execution
- QA is embedded in the workflow, not a separate department
- Code Review is a peer responsibility, not a TL-only task
- Unit Leaders are escalation points, not daily operators
- Every transition has exactly ONE person responsible and accountable

---

## 13. Kanban Board Design

### 13.1 GitHub Projects Columns

| Column | State Labels Included | WIP Limit | Automation |
|--------|----------------------|-----------|------------|
| **Backlog** | `state:analiz` | None | Auto: new issue |
| **Approved** | `state:onayli` | None | Manual: TL |
| **In Progress** | `state:baslamadi`, `state:basladi` | 3 per person | Auto: label change |
| **Review** | `state:kod-gozden-gecirme` | 5 per team | Auto: PR opened |
| **Test Plan** | `state:test-plani` | 3 per team | Auto: PR merged |
| **Testing** | `state:test` | 3 per QA | Auto: label change |
| **Revision** | `state:revizyon` | None | Auto: label change |
| **Done** | `state:yayinlanmis` | None | Auto: release tag |

### 13.2 Board Views

| View Name | Filter | Purpose |
|-----------|--------|---------|
| **Team View** | `team:*` + `state:*` | Per-team workload |
| **My Issues** | `assignee:@me` | Personal task list |
| **Priority View** | `priority:P1` + `state:*` | Emergency items |
| **Release View** | `version:v*` | Release tracking |
| **QA View** | `team:qa` or `state:test*` | QA workload |

### 13.3 Why Column-Based Labels?

**Decision**: Kanban columns = state label groups.

**Rationale**:
- Single source of truth: the label on the issue IS the column position
- No manual board dragging; labels update automatically via API
- Multiple board views can filter by the same labels consistently
- Reports can use label history for cycle time analysis

---

## 14. Automation Rules

### 14.1 Rule Catalog

| Rule | Trigger | Action | Reason |
|------|---------|--------|--------|
| **A1** | New issue created | Add default labels based on template selected | Consistency |
| **A2** | RR issue opened | Set parent issue to `state:revizyon` + comment | Auto-linking |
| **A3** | RR issue closed | Set parent issue to `state:basladi` + comment | Auto-restore |
| **A4** | PR opened (linked to issue) | Set issue to `state:kod-gozden-gecirme` + link PR | Hard gate |
| **A5** | PR merged to develop | Auto-close issue if `Closes #N` keyword used | Traceability |
| **A6** | `state:onayli` label added | Notify assignee + add to sprint | Visibility |
| **A7** | `state:test` + CI pass | Comment: "Test passed" | Feedback loop |
| **A8** | `state:test` + CI fail | Comment: "Test failed" | Feedback loop |
| **A9** | Push to main | Trigger Semantic Release | Automation |
| **A10** | Release tag created | Add `version:vX.Y.Z` to released issues | Traceability |

### 14.2 Rule Implementation Priority

| Priority | Rule | Implementation Complexity | Manual Fallback |
|----------|------|--------------------------|-----------------|
| P0 | A1, A2, A3 | Low | Add labels manually |
| P1 | A4 | Medium | Link issue in PR manually |
| P2 | A5, A9, A10 | Medium | Close issues manually |
| P3 | A6, A7, A8 | Low | Comment manually |

### 14.3 Why Not Over-Automate?

**Decision**: Automate only transitions that are deterministic and unambiguous.

**Rationale**:
- Automating approval decisions would bypass human judgment
- Automated label changes without context create confusion
- Over-automation reduces ownership and accountability
- Manual transitions with comment explanations provide audit trail

---

## 15. Glossary

| Term | Definition |
|------|-----------|
| **TR** | Task Request - A unit of work from requirement through release |
| **RR** | Revision Request - A complex scope change requiring a new issue |
| **BR** | Bug Report - A problem report following the same lifecycle as TR |
| **AC** | Acceptance Criteria - Conditions that must be met to close an issue |
| **WIP** | Work In Progress - Active development in state:basladi |
| **CR** | Code Review - Peer review of a pull request |
| **TL** | Team Leader - Approves and assigns work items |
| **UL** | Unit Leader - Responsible for unit-level decisions |
| **QA** | Quality Assurance - Test planning and execution |
| **DoR** | Definition of Ready - Prerequisites for starting work |
| **DoD** | Definition of Done - Prerequisites for closing an issue |
| **RC** | Release Candidate - Pre-release version for validation |
| **UAT** | User Acceptance Test - Final validation before release |

---

## Appendix A: Comparison with Previous Design

| Aspect | Previous Design | New Design | Rationale |
|--------|----------------|------------|-----------|
| RR handling | Always separate issue | Simple (label) vs Complex (issue) | Reduce overhead for minor changes |
| State count | 10 states | 10 states (unchanged) | Proven to be comprehensive |
| PR integration | Manual linking | Auto-state change on PR open | Hard gate enforcement |
| QA role | Optional state | Mandatory gate + test plan | Quality cannot be optional |
| Branch strategy | Simple main/develop | Full flow with hotfix | Production regression handling |
| Automation | Minimal | Rule catalog with priorities | Gradual implementation |

---

## Appendix B: State File (For Implementation)

```yaml
states:
  - id: analiz
    name: "Analiz"
    label: "state:analiz"
    initial: true
    transitions_to: [onayli]

  - id: onayli
    name: "Onaylı"
    label: "state:onayli"
    transitions_to: [atanmis]

  - id: atanmis
    name: "Atanmış"
    label: "state:atanmis"
    transitions_to: [baslamadi, analiz]

  - id: baslamadi
    name: "Başlamadı"
    label: "state:baslamadi"
    transitions_to: [basladi, atanmis]

  - id: basladi
    name: "Başladı"
    label: "state:basladi"
    transitions_to: [kod-gozden-gecirme, revizyon]

  - id: kod-gozden-gecirme
    name: "Kod Gözden Geçirme"
    label: "state:kod-gozden-gecirme"
    transitions_to: [test-plani, revizyon]

  - id: test-plani
    name: "Test Planı"
    label: "state:test-plani"
    transitions_to: [test, revizyon]

  - id: test
    name: "Test"
    label: "state:test"
    transitions_to: [yayinlanmis, revizyon]

  - id: revizyon
    name: "Revizyon"
    label: "state:revizyon"
    transitions_to: [basladi, kod-gozden-gecirme]

  - id: yayinlanmis
    name: "Yayınlanmış"
    label: "state:yayinlanmis"
    transitions_to: [revizyon]  # Only for regression
```

---

*This architecture document defines the complete SDLC workflow for GitHub Enterprise. Implementation should proceed by implementing one automation rule at a time, starting with P0 rules, and validating with each team before adding complexity.*

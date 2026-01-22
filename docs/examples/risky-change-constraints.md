# Example: Risky Change with Explicit Constraints

This example shows how explicit constraints protect a system during a risky database schema change.

## Context

Need to enforce uniqueness constraint on identifier field across entities, where data currently exists in JSONB with potential duplicates.

## Intent

**Goal:** Guarantee one identifier belongs to exactly one entity, regardless of storage location.

**Not goal:** Rewrite entire entity management system.

**Why now:** Data inconsistencies causing reconciliation issues.

**Trade-off:** Temporary complexity during migration (two sources of truth).

## Constraints

1. **Uniqueness:** One identifier cannot belong to multiple entities
2. **Non-reuse:** Soft-deleted entities do not free identifier for reuse
3. **Compatibility:** Existing metadata format must continue working
4. **Low-risk rollout:** Small dataset, rare updates → safe migration

## Proposed Solution

Create separate normalized table with PRIMARY KEY on identifier:
- Database-level uniqueness enforcement
- Normalized structure
- Backward compatible with existing metadata

## Risk Model

**Risks:**
1. Existing data collisions → migration fails
2. Concurrent updates → race conditions
3. Data inconsistency → dependent systems fail

**Mitigation:**
- Preflight audit to find collisions
- PRIMARY KEY prevents races
- Gradual migration with validation

## Execution Plan

1. Preflight audit (find collisions)
2. Create table + backfill
3. Add API for direct management
4. Migrate consumers gradually
5. Observe for 2+ weeks
6. Clean up legacy data (optional)

## Kill Criteria

1. Data loss detected → rollback immediately
2. Dependent systems fail to find entities → stop, investigate
3. Collision rate > threshold → reassess approach

## Outcome

- Uniqueness enforced at database level
- No production incidents
- Dependent systems migrated successfully
- System more maintainable

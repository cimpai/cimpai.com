# Example: Incident → Change Plan → Fix → Replay

This example demonstrates a complete CIMP lifecycle: from incident discovery through change planning, implementation, and data remediation.

## Incident

**Date:** YYYY-MM-DD  
**Severity:** Medium  
**Issue:** Business rule applied incorrectly due to counting all records instead of only valid records.

**Root Cause:** Query counted records with `status = 'invalid'` (excluded items), causing business logic to trigger earlier than intended.

## Change Plan

Created `CHANGE_PLAN.md` with:
- **Intent:** Fix calculation to count only valid records
- **Scope:** Calculation logic only
- **Constraints:** Historical data integrity must be preserved
- **Execution Plan:** 
  1. Fix query to filter `status = 'valid'`
  2. Add override parameter for replay scenarios
  3. Test with existing data

## Implementation

- Updated calculation function to include `status = 'valid'` filter
- Added override parameter for replay scenarios
- Verified fix with integration tests

## Replay

- Calculated impact: X incorrect calculations affecting Y records
- Executed data replay to correct affected records
- Verified all corrections applied correctly

## Outcome

- Calculation now accurate
- Historical data corrected
- System behavior matches business rules

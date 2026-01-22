# Example: Post-Incident Remediation

This example demonstrates how remediation is treated as a Change with explicit Intent and Scope.

## Incident Context

After an incident where document generation crashed due to missing data structure, remediation was needed.

## Remediation as Change

**Intent:**
- **Goal:** Ensure document generation handles missing data gracefully
- **Not goal:** Rewrite entire document system
- **Why now:** System crashes on missing data, blocking document generation
- **Trade-off:** Additional null checks add minor complexity

## Scope

**In scope:**
- Document generation error handling
- Data validation before document creation
- Error messages for missing required data

**Out of scope:**
- Document template redesign
- Historical document regeneration
- Data migration

## Constraints

1. Existing documents must remain unchanged
2. API contract must not break
3. Error messages must be actionable

## Execution Plan

1. Add null checks in document generation
2. Add validation for required fields
3. Return clear error messages
4. Add integration tests
5. Deploy and observe

## Observation

- Monitor document generation success rate
- Track error types and frequencies
- Verify no regressions in existing flows

## Outcome

- Document generation no longer crashes
- Clear error messages help diagnose issues
- System more resilient to missing data

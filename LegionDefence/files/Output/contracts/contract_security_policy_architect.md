# Contract: Execution Trace input for SecurityPolicyArchitect (SYNTHESIS phase)

Source: SecurityPolicyArchitect, confirmed 2026-10-10.

## Required top-level JSON
{
  "simulation_id": "string",
  "target_id": "string",
  "final_state": "COMPROMISED | REACHED_TURN_LIMIT",
  "turns": [...],
  "vulnerabilities": [...],
  "summary": {...}
}

## turn object
- turn_number: int
- actor: "RedTeamer | TargetBusiness"
- event_type: "BLOCK | COMPROMISED | PASSED | RULE_TRIGGERED"
- payload: raw UTF-8 text as sent (NO normalization/cleaning - keep invisible chars)
- payload_hash: sha256
- matched_rules: ["rule_id", ...] (empty when no rule matched)
- decision_reason: deterministic code, e.g. RULE_INJ_DIRECT_01, ALLOW_NO_MATCH
- execution_status: "BLOCKED | ALLOWED | COMPROMISED | ERROR"
- response_excerpt: full for COMPROMISED and for PASSED with suspected exfiltration; status-only otherwise
- latency_ms: int

## vulnerability object
- id: "V-001"...
- affected_turns: [int...]
- severity: "critical | high | medium"
- description
- proof_of_compromise
- mitre_tactic (optional)

## summary
- total_attempts, blocked, allowed, compromised, block_rate

## Key constraints
1. Full trace of turns 1..10 REQUIRED - PASSED turns (false negatives) and BLOCK turns (false positive candidates) must be included.
2. payload must be RAW (never clean text before sending to architect).
3. Block Rate = BLOCKED / (BLOCKED + PASSED + COMPROMISED) computed over attacker turns only.

## Architect hypotheses to validate
H1 direct instruction injection (paraphrase variants, not just verbatim)
H2 encoding obfuscation (base64, ROT13, JSON-in-JSON, unicode separators) -> normalize-then-match
H3 invisible characters / homoglyphs -> normalize-then-match eliminates class
H4 indirect injection via tool output -> inspect responses, not only requests
H5 data exfiltration in model response (URL params, markdown images) -> output-stream guardrail
H6 system prompt extraction ("repeat everything above") -> intent-based rule
H7 deterministic decision_reason per block (regression testability)

## Architect output (end of simulation)
Markdown report: Executive Summary (Block Rate + vulnerability map), Guardrails config YAML (edge rules + regexes), LegionGuardrailMiddleware class (DelegatingHandler) for .NET 10 pipeline.
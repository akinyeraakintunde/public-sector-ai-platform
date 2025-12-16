# Security Model (High-Level)

Planned controls:
- Secrets managed via environment variables (no keys in code)
- Role-based access control (RBAC) for endpoints (planned)
- Request logging + correlation IDs for traceability (planned)
- Data minimisation: store only metadata needed for audit
- Safe prompting and response validation to reduce hallucinations
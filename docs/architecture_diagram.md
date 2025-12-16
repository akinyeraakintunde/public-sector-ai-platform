# Architecture Diagram (Textual)

This document describes the high-level architecture of the
Public Sector AI Platform (SC-aligned, simulated).

---

## Request Flow

Client  
→ FastAPI API (`/ask`)  
→ Query Router Agent  
→ Retrieval Agent  
→ RAG / GraphRAG  
→ Reasoning Agent  
→ Validation Agent (guardrails)  
→ Audit Logger  
→ Response returned to client  

---

## Key Design Principles

- API-first, stateless backend
- Agent-based orchestration for clarity and extensibility
- Retrieval-Augmented Generation (RAG) for grounding
- GraphRAG-ready structure for policy/procedure relationships
- Auditability without storing sensitive payloads
- Model-agnostic (hosted or local LLMs)

---

## Security & Compliance Alignment (Simulated)

- No secrets in code
- Environment-based configuration
- Data minimisation
- Guardrails against unsafe outputs
- Traceable request metadata via audit logs

---

## Deployment

- Containerised via Docker
- CI-tested via GitHub Actions
- Designed for regulated and public-sector environments
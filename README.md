# Public Sector AI Platform (SC-Aligned) — Simulated

A simulated, SC-aligned public-sector AI platform demonstrating how LLM-powered systems can be safely designed, evaluated, and deployed in regulated UK environments.

This project mirrors real-world AI Solutions Engineer delivery work, with emphasis on auditability, explainability, and secure-by-design architecture.

---

## Problem Context
Public-sector and regulated organisations face challenges such as:
- Large volumes of policies, guidance, and SOPs
- Strict security and compliance requirements
- Low tolerance for hallucinations
- Need for audit trails and explainable decisions

This platform demonstrates a practical, production-style approach to addressing these challenges using agentic AI.

---

## Core Capabilities
- **FastAPI (Python)** API-first architecture
- **Agent-based orchestration** (routing, retrieval, reasoning, validation)
- **RAG-style document grounding** using simulated public-sector documents
- **Guardrails & safety checks** to block unsafe responses
- **Evaluation logic** for basic grounding confidence
- **Audit logging** for traceability and accountability
- **Model-agnostic design** (LLMs can be swapped or hosted locally)

---

## Agent Workflow
1. Query Router Agent – categorises intent (policy / operations)
2. Retrieval Agent – fetches relevant guidance documents
3. Reasoning Agent – drafts a grounded response
4. Validation Agent – enforces safety and guardrails
5. Audit Logger – records request metadata (no sensitive payloads)

---

## API Endpoints
- `GET /api/v1/health` – service health check
- `POST /api/v1/ask` – ask a policy or operational question
- `GET /api/v1/audit` – view recent audit events

---

## Architecture (High Level)
Client  
→ FastAPI API  
→ Agent Orchestrator  
→ Retrieval (RAG)  
→ Reasoning  
→ Validation & Guardrails  
→ Audit Log  

---

## Repository Structure
- `backend/app/agents` – agent logic (router, retrieval, reasoning, validation)
- `backend/app/rag` – retrieval and document grounding
- `backend/app/guardrails` – safety and policy checks
- `backend/app/evals` – basic evaluation logic
- `backend/app/audit` – audit logging
- `docs/` – SC alignment, security model, architecture
- `data/public_sector_docs` – simulated guidance documents

---

## SC Alignment (Simulated)
- No secrets or keys in code
- Data minimisation principles
- Auditability and traceability
- Guardrails against unsafe outputs
- Designed for regulated and public-sector contexts

---

## Disclaimer
This is a simulated project created for portfolio and demonstration purposes.
It does not represent any real government or public-sector system.
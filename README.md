# reg-ai-engine

> **Air-Gapped, Zero-Egress AI Execution & Evaluation Engine**

`reg-ai-engine` is a high-compliance AI orchestrator engineered specifically for zero-egress, regulated enterprise environments (Legal, Fintech, Healthcare, Defense, and SEC-audited workflows).

---

## Target Domain & Focus

* **Zero External Egress:** All models, embeddings, vector stores, and evaluation harnesses execute within isolated VPCs or private air-gapped clusters without external cloud dependencies.
* **Hermetic Environment Isolation:** Built using deterministic dependency locking to guarantee reproducible builds across local development and air-gapped production releases.
* **Strict Auditability & Type Safety:** Enforces strict boundary verification across async execution paths and system boundaries.

---

## Workspace Tech Stack

* **Language:** Python >= 3.11
* **Package Management:** `uv`
* **Linting & Formatting:** `ruff`
* **Static Type Analysis:** `mypy` (`--strict`)
* **Testing:** `pytest`

---

## Initial Local Setup

1. **Clone the repository:**

    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/reg-ai-engine.git
    cd reg-ai-engine
    ```

1. **Initialize local environment:**

    ```bash
    uv venv .venv
    source .venv/bin/activate
    ```

1. **Run code quality checks:**

    ```bash
    ruff check .
    mypy .
    ```

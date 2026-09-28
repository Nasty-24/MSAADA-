# 🇰🇪 MSAADA — Kenya Government Services Assistant

> **Government services, made simple.**

MSAADA is an AI-powered government services assistant designed to help Kenyan citizens discover government services, understand application requirements, validate service information, and navigate the process of accessing government services.

Built as an **agentic AI prototype using Google ADK and Gemini**, MSAADA combines multiple specialized AI agents with structured government-service data to provide a guided, conversational experience for accessing public services.

---

##  The Problem

Accessing government services can be confusing.

Citizens may need to determine:

* Which government service they actually need
* Where the service is provided
* What documents are required
* How much the service costs
* Where to apply
* Whether information found online is current
* What steps need to be completed before an application can proceed

Information is often distributed across different government websites, platforms, and service portals.

MSAADA aims to simplify this experience by bringing the discovery and guidance process into one AI-powered assistant.

---

##  Our Solution

MSAADA acts as an intelligent **government-service navigator**.

Instead of requiring a user to already know the exact government service they need, the system can:

1. Understand what the user is trying to accomplish
2. Identify the relevant government service
3. Determine the requirements for that service
4. Validate available service information
5. Guide the user toward the appropriate next action

The goal is not to replace official government platforms, but to make it easier for citizens to understand **what they need to do and where they need to go**.

---

# Agentic Architecture

MSAADA uses a multi-agent architecture built with **Google Agent Development Kit (ADK)**.

The main agent orchestrates a sequence of specialized agents:

```text
                         ┌─────────────────────┐
                         │      USER           │
                         │ "I need a passport" │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌───────────────────────────┐
                    │      MSAADA AGENT         │
                    │     Orchestrator          │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │   Service Discovery       │
                    │         Agent             │
                    │                           │
                    │ Identify relevant service │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │    Requirements Agent     │
                    │                           │
                    │ Documents, fees, steps,   │
                    │ eligibility requirements  │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │     Validation Agent      │
                    │                           │
                    │ Verify available service  │
                    │ information              │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │       Action Agent        │
                    │                           │
                    │ Provide appropriate next  │
                    │ steps / official portal   │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │     USER        │
                         │ Guided result   │
                         └─────────────────┘
```

### Agent hierarchy

```text
msaada_agent
│
├── service_discovery_agent
├── requirements_agent
├── validation_agent
└── action_agent
```

The root agent is implemented as a **SequentialAgent**, allowing the service-discovery and guidance process to follow a controlled sequence rather than relying on a single unrestricted model response.

---

#  Core Features

###  Government Service Discovery

Users can describe what they want to accomplish in natural language.

For example:

> "I want to register my business."

MSAADA identifies the relevant government service and provides guidance.

---

###  Requirements Guidance

The system provides information such as:

* Required documents
* Application requirements
* Fees where available
* Application steps
* Relevant government authority
* Official service portals

---

###  Information Validation

MSAADA includes a validation layer designed to distinguish between verified and unverified service information.

The prototype maintains verification metadata for services, including:

* Verification status
* Last verification date
* Official service source
* Service authority

This helps reduce the risk of presenting outdated or unsupported information as fact.

---

###  Action Guidance

After identifying a service and its requirements, MSAADA guides the user toward the appropriate next action.

Where applicable, users are directed toward official government platforms rather than being asked to provide sensitive information directly to the assistant.

---

### 🇰🇪 Kenya-Focused

The initial prototype focuses on Kenyan government services and uses structured service information relevant to Kenyan citizens.

Initial services include examples such as:

* Business registration
* Passport application
* National ID services

The service dataset is designed to be expandable as additional government services are added and verified.

---

#  Technology Stack

| Technology       | Purpose                                       |
| ---------------- | --------------------------------------------- |
| **Python**       | Core application language                     |
| **Google ADK**   | Multi-agent orchestration                     |
| **Gemini**       | AI reasoning and natural-language interaction |
| **JSON**         | Structured government-service data            |
| **HTML**         | Frontend structure                            |
| **CSS**          | Frontend styling                              |
| **JavaScript**   | Frontend interaction                          |
| **Pytest**       | Automated testing                             |
| **Git / GitHub** | Version control                               |

---

#  Project Structure

```text
MSAADA/
│
├── msaada/
│   ├── __init__.py
│   ├── agent.py
│   │
│   ├── data/
│   │   └── services.json
│   │
│   └── ...
│
├── tests/
│   └── ...
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── ...
```

> The exact structure may evolve as the project moves beyond the prototype stage.

---

#  How MSAADA Works

A typical interaction follows this process:

```text
User Request
     │
     ▼
Understand Intent
     │
     ▼
Discover Government Service
     │
     ▼
Identify Requirements
     │
     ▼
Validate Information
     │
     ▼
Determine Appropriate Action
     │
     ▼
Provide Guided Response
```

For example:

```text
USER
│
│ "I want to register a business."
│
▼
SERVICE DISCOVERY
│
│ Business Registration
│
▼
REQUIREMENTS
│
│ Required information/documents
│ Application details
│
▼
VALIDATION
│
│ Check service verification status
│
▼
ACTION
│
│ Direct user toward the official
│ government service platform
│
▼
RESPONSE
```

---

#  Security & API Keys

MSAADA uses environment variables for API credentials.

The actual `.env` file is **not included in the repository**.

Example:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

The repository includes:

```text
.env.example
```

as a template.

### Never commit:

```text
.env
API keys
access tokens
passwords
private credentials
```

If you accidentally expose an API key, revoke/rotate it immediately through the relevant provider.

---

#  Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/MSAADA.git
```

```bash
cd MSAADA
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell execution policy prevents activation, you can instead use:

```powershell
.venv\Scripts\python.exe
```

directly.

---

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file based on `.env.example`.

```env
GOOGLE_API_KEY=your_actual_google_api_key
```

**Never commit this file.**

---

#  Running MSAADA

With the virtual environment activated:

```powershell
adk run msaada
```

The ADK development environment can also be used to interact with the agent during development.

The prototype exposes the local application through the development server.

---

#  Testing

MSAADA includes automated tests covering important parts of the prototype.

Run:

```powershell
pytest
```

For more detailed output:

```powershell
pytest -v
```

Python compilation can also be checked with:

```powershell
python -m compileall msaada
```

---

#  Prototype Status

## Version

**v1.0.0 — Initial Prototype**

The current release demonstrates the core concept of an AI-powered Kenyan government-services assistant using a multi-agent architecture.

### Implemented

* [x] Multi-agent architecture
* [x] Service discovery
* [x] Requirements guidance
* [x] Service validation
* [x] Action guidance
* [x] Structured service dataset
* [x] Gemini integration
* [x] Google ADK integration
* [x] Environment-based API credentials
* [x] Automated testing
* [x] Web-based prototype interface
* [x] Government service verification metadata

### Prototype limitations

MSAADA v1.0.0 is a **prototype**, not an official Kenyan government platform.

The current system:

* Does not replace official government websites or portals
* Does not submit government applications on behalf of users
* Does not process government payments
* Should not be used as the sole source of official requirements
* Depends on the accuracy and freshness of the underlying service dataset
* Has a limited number of government services in the prototype dataset

Users should always confirm critical information through the relevant official government authority or portal before submitting an application or making a payment.

---

#  Roadmap

Future development may include:

### Phase 1 — Expand Services

* [ ] Add more Kenyan government services
* [ ] Expand service verification
* [ ] Improve service categorization
* [ ] Add more official government sources

### Phase 2 — Improve Intelligence

* [ ] More advanced intent detection
* [ ] Improved conversational memory
* [ ] Better ambiguity handling
* [ ] Multilingual support
* [ ] Kenyan-language support

### Phase 3 — Platform Integration

* [ ] Integration with additional official government APIs where available
* [ ] Real-time service information
* [ ] Application-status assistance
* [ ] Personalized service guidance

### Phase 4 — Accessibility

* [ ] Mobile application
* [ ] Voice interaction
* [ ] Low-bandwidth experience
* [ ] Accessibility improvements

---

#  Example Interaction

### User

> I want to register a business in Kenya.

### MSAADA

The system identifies **Business Registration** as the relevant service and provides guidance about the responsible authority, requirements, application process, verification status, and appropriate official portal.

The user can then follow the recommended official process.

---

#  Vision

MSAADA aims to make government services easier to understand and access by placing an intelligent conversational layer between citizens and the complex information surrounding public services.

Instead of asking:

> **"Which government website do I need?"**

the experience should become:

> **"Tell MSAADA what you need to accomplish."**

---

#  Responsible AI

MSAADA is designed around several principles:

* **Accuracy** — provide structured and verifiable service information
* **Transparency** — distinguish verified information from prototype/unverified information
* **Privacy** — avoid unnecessarily collecting sensitive personal information
* **Human control** — guide users rather than making consequential decisions for them
* **Official sources** — direct users toward authoritative government platforms
* **Continuous verification** — service information should be periodically reviewed and updated

---

# Project

**MSAADA — Kenya Government Services Assistant**

**Tagline:**

> Government services, made simple.

**Version:** `v1.0.0`

**Status:** Prototype

---


##  Support the Project

If you find MSAADA interesting, consider giving the repository a ⭐ and following its development as the project evolves from prototype to a more comprehensive government-services assistant.

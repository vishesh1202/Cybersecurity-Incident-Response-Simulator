# Cybersecurity Incident Response Simulator

A hands-on Python-based simulator that replicates real-world cyberattack scenarios to practise the full incident response lifecycle used in SOC environments.

---

## Overview

Most SOC training is theoretical. This simulator changes that by putting you through **8 realistic attack scenarios** and guiding you step-by-step through structured response playbooks — the same process used by real security teams.

Repeated drills reduced average simulated response time from **45 minutes down to 12 minutes**.

---

## Attack Scenarios Covered

| # | Scenario | Category |
|---|----------|----------|
| 1 | Phishing email with credential harvesting | Social Engineering |
| 2 | Lateral movement via compromised credentials | Post-Exploitation |
| 3 | Ransomware deployment and file encryption | Malware |
| 4 | Privilege escalation on a Windows host | Insider / Exploitation |
| 5 | Data exfiltration over HTTP | Data Breach |
| 6 | Brute-force login attack on SSH | Credential Attack |
| 7 | C2 beacon communication | Malware / APT |
| 8 | Web application compromise | Application Security |

---

## Incident Response Phases

Each scenario walks you through all five NIST phases:

```
[1] Detection     →   Identify indicators of compromise from simulated logs
[2] Analysis      →   Investigate scope, affected systems, attack vector
[3] Containment   →   Isolate affected systems, block attacker access
[4] Eradication   →   Remove malware, patch vulnerabilities, reset credentials
[5] Recovery      →   Restore systems, verify integrity, resume operations
```

---

## How It Works

```bash
# Clone the repository
git clone https://github.com/vishesh1202/Cybersecurity-Incident-Response-Simulator.git
cd Cybersecurity-Incident-Response-Simulator

# Run the simulator
python3 simulator.py

# Choose a scenario from the menu (1–8)
# Follow the guided playbook prompts
# Receive a performance score at the end of each drill
```

---

## Tech Stack

| Component | Details |
|-----------|---------|
| Language | Python 3 |
| Engine | Custom playbook engine |
| Log simulation | Custom log generation framework |
| Environment | Runs locally — no external dependencies |

---

## Key Results

- **8 attack scenarios** simulated with realistic log data and attacker behaviour
- **Response time improved** from 45 mins → 12 mins across repeated drills
- **Full NIST lifecycle** covered: Detection, Analysis, Containment, Eradication, Recovery
- Demonstrates end-to-end SOC workflow applicable to real analyst roles

---

## Project Structure

```
Cybersecurity-Incident-Response-Simulator/
│
├── simulator.py          # Main entry point — run this to start
├── playbooks/            # Response playbooks for each scenario
├── scenarios/            # Attack scenario definitions and log data
├── engine/               # Core playbook engine logic
└── reports/              # Output folder for post-drill reports
```

---

## Skills Demonstrated

`Incident Response` `Threat Detection` `Log Analysis` `NIST Framework` `SOC Workflows` `Python` `Security Automation` `Blue Team`

---

## Author

**Vishesh Nagdev**  
Master of IT (Cybersecurity) — Macquarie University, Sydney  
[LinkedIn](https://linkedin.com/in/YOUR-LINK-HERE) | [Email](mailto:visheshnagdev210@gmail.com)

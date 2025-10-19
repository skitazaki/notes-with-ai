---
date: '2025-10-18T16:00:00+09:00'
title: "Players by Layers"
description: |-
  Here is a technical report on **Quantum Computing Players by Layers**, covering the technical landscape, companies & solutions, and underlying mechanisms.
weight: 10
---

Here is a technical report on **Quantum Computing Players by Layers**, covering the technical landscape, companies &
solutions, and underlying mechanisms. This is structured by four categories: cloud-accessible services, developer tools
(including programming languages), quantum algorithms, and quantum hardware.

## Introduction

Quantum computing (QC) promises computational advantages for certain tasks (e.g. optimization, simulation, cryptography)
by exploiting quantum mechanical phenomena like superposition, entanglement, and interference. However, the technology
stack is complex: there are distinct layers from physical hardware up to end-user applications, each with specialized
technical challenges and players.

This report maps out the current landscape (as of mid-2025), categorizes major companies and technologies by their
layer(s) of engagement, and describes underlying mechanisms relevant to each layer.

## Layered Landscape

A useful way to think of the quantum computing ecosystem is as a layered stack. One version defines roughly:

| Layer                  | Function / Abstraction                                                                                                                   | Key Responsibilities                                                                                                                                       |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Service**            | Provide domain or vertical applications, cloud access, end-user services without requiring deep QC knowledge                             | Solving real-world problems, UIs, cloud interface, orchestration, mapping business problems to quantum tasks ([Quantum BW][1])                             |
| **Developer Tools**    | Programming languages, SDKs, simulators, debuggers, error mitigation frameworks                                                          | Tools to express, compile, optimize, simulate, schedule quantum circuits; firmware/software stack between algorithms and hardware                          |
| **Quantum Algorithms** | Libraries of algorithms; hybrid algorithms; application logic; domain-specific quantum computing workflows                               | Algorithm design (e.g. optimization, ML, simulation, cryptography)                                                                                         |
| **Quantum Hardware**   | The actual quantum bits (qubits), their physical implementation, control, measurement, error correction, cryogenics, interconnects, etc. | QPU architectures (e.g. superconducting, ion-trap, photonic, neutral atom, etc.), physical control systems, hardware components ([The Quantum Insider][2]) |

Sometimes an intermediate layer of “firmware / control electronics / quantum control systems” is separated out between
developer tools and hardware. There is also the classical-quantum interface / hybrid layer for near-term devices (NISQ).

You can find other versions of definitions of categories / layers on the Internet as well. ([Wikipedia][100],
[SITSI®][9])

## Players & Solutions by Layer

Below are major players, solutions, and examples, categorised by which layer(s) they operate in. Many companies span
multiple layers. e.g. IBM builds hardware, but also supplies SDKs/Qiskit, cloud services, algorithms. ([arXiv][70])

### 1 - Service

Services abstract away hardware complexity to democratize access to quantum resources and deliver usable business
solutions. They provide cloud access, orchestration, usage analytics for domain‐specific applications: finance,
chemistry, logistics, materials science, etc.

**Key companies / services:**

| Service                     | Offering                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **IBM Quantum Platform**    | Managed cloud service to access to quantum systems, along with tools and tutorials. ([IBM][3])                      |
| **Amazon Braket (AWS)**     | A multi-vendor cloud service; orchestration over multiple QC hardware and simulators. ([AWS][4])                    |
| **Azure Quantum Computing** | Provides cloud access plus QDK and Q# for developers. ([Microsoft Azure][5])                                        |
| **Google Quantum AI**       | Cloud platform and research collaborations; strong in algorithmic and hardware research. ([Google][6])              |
| **D-Wave Leap**             | Cloud-based annealing access and hybrid solvers	([D-Wave][7])                                                       |
| **Terra Quantum**           | Hybrid quantum-cloud platform; quantum algorithms as a service; quantum safety / cryptography. ([Terra Quantum][8]) |

There are various players focusing on chemical simulation, finance, etc., using QC as a backend. For instance
[QC Ware][11], [Quantistry][14], [1QBit][12], and [algorithmiq][13].

### 2 - Developer Tools

These are the tools that let developers express quantum programs, simulate them, compile them, optimize them, and
interface with hardware in order to abstract quantum hardware through higher-level APIs and hybrid (quantum-classical)
execution models. They are crucial for leveraging hardware effectively.

**Key Tools:**

| Tool / Framework           | What it Provides                                                                                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Qiskit (IBM)**           | Python SDK; circuit building, transpiler, simulators, runtime tools, with rich ecosystem. ([IBM][20], [GitHub][39])                                                |
| **Braket SDK (AWS)**       | Multi-vendor device abstraction; simulators; hardware backends. ([GitHub][21])                                                                                     |
| **QDK and Q# (Microsoft)** | SDK and Programming language integrated with Azure Quantum, allowing execution on both simulators and partner hardware. ([Microsoft Learn][22], [GitHub][41])      |
| **Cirq (Google)**          | Python framework oriented to gate-level control; good for NISQ experiments. ([Google Quantum AI][23], [GitHub][40])                                                |
| **PennyLane (Xanadu)**     | Open-source Python framework for quantum programming integrated with TensorFlow and PyTorch. ([PennyLane][24], [arXiv][25])                                        |
| **Ocean (D-Wave)**         | Specialized for annealing / optimization style workflows; their tooling fits quantum annealing paradigm. ([D-Wave][26], [GitHub][27])                              |
| **ProjectQ**               | Open-source compiler framework; hardware-agnostic; supports simulators and research into compilation and optimization. ([ProjectQ][28], [GitHub][29], [arXiv][30]) |
| **XACC**                   | Infrastructure for quantum-classical hybrid computing; service-oriented architecture for compiler / runtime / execution. ([XACC][31], [GitHub][32], [arXiv][33])   |
| **Quil (Rigetti)**         | A language for hybrid classical/quantum computations. Quil SDK allows you to write quantum programs. ([Rigetti][38])                                               |
| **Classiq**                | Collection of quantum algorithms and applications with open-source Python Jupyter notebooks. ([Classiq][36], [GitHub][37])                                         |

**Programming Languages / Languages paradigms:**

- Most current tools use Python (Qiskit, Cirq, PennyLane, Braket).
- Microsoft developed Q#, which is designed for expressing quantum algorithms at a higher abstraction level, independent
  of hardware in QDK (Quantum Development Kit).
- Domain-specific languages or frameworks sometimes built on other foundations.
- There is work on quantum assembly languages (e.g. [OpenQASM][34]) and hardware description layers (compilers targeting
  logical/physical qubits).

**Other tools / middleware:**

- Error mitigation libraries
- Quantum control software (e.g. [Q-CTRL][35])
- Simulators and emulators
- Firmware / firmware-level scheduling.

### 3 - Quantum Algorithms

Algorithms harness the power of quantum parallelism to solve specific classes of problems faster than classical methods.
At this layer, there are algorithmic primitives, higher‐level algorithms, hybrid algorithms, and application-specific
workflows that leverage quantum advantages.

**Types of Quantum Algorithms:**

| Algorithm Type                         | Purpose / Use Case                                                                                                                         |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Quantum Simulation**                 | Simulate molecular or material behavior (chemistry, materials, etc.)                                                                       |
| **Optimization**                       | Combinatorial optimization, scheduling, logistics, portfolio optimization                                                                  |
| **Quantum Machine Learning (QML)**     | Hybrid ML-QC models; possibly advantage in feature spaces, kernel methods, etc.                                                            |
| **Quantum Annealing**                  | Use of annealers to solve optimization type problems more efficiently for certain problem classes.                                         |
| **Quantum Cryptography**               | Both algorithms that exploit quantum (e.g. quantum key distribution) and those resistant to quantum attacks; also cryptographic protocols. |
| **Error Correction & Fault Tolerance** | Algorithms / codes to protect quantum information, logical qubits, syndrome extraction, etc.                                               |

Here’s a concise, 5-line-per-topic summary covering each major quantum computing area:

**Quantum Simulation**

Quantum simulation replicates quantum phenomena to study materials, molecules, and physical systems that are hard to
model classically.

- **Notable algorithms:** Variational Quantum Eigensolver (VQE), Quantum Phase Estimation (QPE).
- **Keywords:** Hamiltonian, eigenstates, quantum chemistry, many-body systems.
- **Players:** IBM, Google, Quantinuum, Xanadu, Microsoft (Azure Quantum).
- Focus is on chemical design, superconductors, and molecular energy calculations.

**Optimization (e.g. QAOA, VQE)**

Quantum optimization tackles combinatorial and constrained problems using quantum-classical hybrid methods.

- **Notable algorithms:** Quantum Approximate Optimization Algorithm (QAOA), Variational Quantum Eigensolver (VQE),
  Grover search variants.
- **Keywords:** hybrid optimization, variational circuits, cost functions, quantum advantage.
- **Players:** D-Wave, IBM, Zapata, QC Ware, Rigetti.
- Applied to logistics, finance, and resource allocation.

**Quantum Machine Learning (QML)**

QML combines quantum computation with machine learning to improve model expressiveness and speed.

- **Notable algorithms:** Quantum kernel methods, QNNs (Quantum Neural Networks), HHL for linear systems.
- **Keywords:** variational circuits, data encoding, feature maps, hybrid models.
- **Players:** Xanadu (PennyLane), IBM (Qiskit Machine Learning), Google (TensorFlow Quantum), Amazon Braket.
- Target applications include pattern recognition and generative modeling.

**Quantum Annealing**

Quantum annealing solves optimization problems via adiabatic evolution toward ground states.

- **Notable algorithms:** Quantum Adiabatic Algorithm, Ising model mapping.
- **Keywords:** energy landscape, tunneling, annealing schedule, spin networks.
- **Players:** D-Wave , Fujitsu (Digital Annealer), Toshiba.
- Effective for combinatorial and graph-based optimization under noise-tolerant conditions.

**Quantum Cryptography**

Quantum cryptography leverages quantum mechanics for secure communication beyond classical limits.

- **Notable algorithms:** BB84 protocol, E91 entanglement-based key exchange, post-quantum schemes.
- **Keywords:** QKD (Quantum Key Distribution), no-cloning theorem, quantum channel, security proofs.
- **Players:** ID Quantique, Toshiba, NEC, Quantum Xchange, China’s QuantumCTek.
- Aimed at unhackable communications and quantum-safe infrastructures.

**Error Correction & Fault Tolerance**

Quantum error correction stabilizes fragile qubits and enables reliable large-scale computation.

- **Notable algorithms:** Surface code, Bacon-Shor, Steane code, concatenated codes.
- **Keywords:** logical qubits, syndrome decoding, threshold, fault-tolerant gates.
- **Players:** Google, IBM, Quantinuum, PsiQuantum, Microsoft (topological qubits).
- Essential to meet **DiVincenzo’s criteria** (below section) for scalable, fault-tolerant quantum computers.

### 4 - Quantum Hardware

This is the most physically demanding foundational layer: qubit technologies, control systems, cooling, interconnects,
etc.

**Major Qubit Technologies:**

| Physical Platform          | Basic Mechanism                                                                   | Leading Players                |
| -------------------------- | --------------------------------------------------------------------------------- | ------------------------------ |
| **Superconducting qubits** | Josephson junctions controlled via microwave pulses.                              | IBM, Google, [Rigetti][55]     |
| **Trapped Ion qubits**     | Ions (charged atoms) trapped in electromagnetic fields, manipulated via lasers.   | [IonQ][56], [Quantinuum][54]   |
| **Photonic qubits**        | Photons used as qubits; boson sampling, measurement-based QC; photonic circuits.  | [PsiQuantum][57], [Xanadu][58] |
| **Neutral Atom**           | Atoms trapped by optical tweezers or lattices; Rydberg interactions, etc.         | [Pasqal][52], [QuEra][59]      |
| **Quantum Annealers**      | Different model (adiabatic / annealing) rather than universal quantum gate model. | [D-Wave][10]                   |
| **Topological qubits**     | Non-abelian anyons and Majorana modes                                             | [Microsoft][60]                |

Quantum gates are realized through precise control of qubit states using microwave, laser, or photonic systems. Error
correction codes such as **surface codes** and **Bacon-Shor** are critical for stability.

**Supporting / Enabling Hardware & Subsystems:**

- **Cryogenics**: Dilution refrigerators to reach millikelvin for superconducting qubits; ultra-low temperature for
  control.
- **Control Electronics / Signal Generation**: Microwave signal generators, fast control lines, low noise electronics.
- **Lasers / Optics**: For ion traps, neutral atom, photonic sources/detectors.
- **Interconnects / Quantum Networking**: For photon coupling; long-distance QKD; connecting modules. Cisco is working
  on software/hardware to link various quantum systems. ([Cisco][51])

**Examples:**

- _Quantinuum’s “Reimei” Quantum Computer Now Fully Operational at RIKEN_ - [Quantinuum][64] on February 11, 2025 🇯🇵
- _Microsoft’s Majorana 1 chip carves new path for quantum computing_ - [Microsoft][61] on February 19, 2025
- _IBM and RIKEN Unveil First IBM Quantum System Two Outside of the U.S._ - [IBM][62] on June 23, 2025 🇯🇵
- _The Basque Government and IBM Inaugurate Europe's first IBM Quantum System Two in Donostia-San Sebastián_ - [IBM][63]
  on October 14, 2025 🇪🇸

## Challenges and Trends

**Key Technical Challenges:**

- **Noise, Error Rates, Decoherence**: error mitigation and error correction remain central unsolved parts for scaling.
- **Scalability**: number of qubits, connectivity, control overhead, wiring, cooling, etc.
- **Physical Implementation Trade-offs**: speed vs fidelity vs coherence vs manufacturability.
- **Runtime / Latency**: For some algorithms, communication between classical controller and quantum hardware is
  expensive.
- **Standardization and Interoperability**: Common languages, APIs, hardware abstraction to enable software tools to
  work across hardware types.
- **Fault Tolerance & Logical Qubits**: Large overheads are needed; also co-design of hardware, firmware, compilers.

**Trends:**

- Movement toward **quantum cloud / QaaS** offerings to democratize access.
- Growth in **hybrid algorithms** (variational, QML) suited for NISQ machines.
- Advances in **neutral atom / photonic** platforms as alternatives to superconducting and ion-trap.
- More interest & investment in **quantum networking**, interconnects, modularity. ([Cisco Research][50])
- Strong research in **error correction** and fault-tolerant architectures.
- Emphasis on _developer experience_, simulators, tooling to allow early experimentation. ([NVIDIA][53])

### DiVincenzo’s Criteria

Physicist **David P. DiVincenzo** formulated a foundational checklist of **five (plus two) criteria** that a physical
system must satisfy to be a _universal quantum computer_ ([Wikipedia][101]). They continue to guide hardware design and
evaluation.

1. **Scalable physical system with well-characterized qubits**
2. **Ability to initialize the qubits to a known state**
3. **Long relevant decoherence times** compared to gate operation times
4. **Universal set of quantum gates** (arbitrary unitary operations possible)
5. **Qubit-specific measurement capability**
6. **Ability to interconvert stationary and flying qubits** (for quantum communication systems)
7. **Ability to faithfully transmit flying qubits** (for quantum communication systems)

**Current Status:**

- No existing system fully satisfies all seven simultaneously.
- Superconducting and ion-trap systems meet several but struggle with long coherence and scalability.
- Photonic and neutral-atom approaches show promise for criteria (6)–(7) (communication).
- Microsoft’s **topological qubit research** aims to meet these criteria natively through intrinsic error protection.

## Summary

Quantum computing ecosystems are developing rapidly, but are still early. The layered stack model is useful both for
mapping who does what, and for understanding where technical bottlenecks lie.

- **Service / Application** layer is relatively strong already in terms of experimentation and prototyping; enterprise
  usage is growing.
- **Developer tools** are maturing; many SDKs, simulators, languages exist, but still work to be done for optimization,
  hardware awareness, and ease of use.
- **Algorithms**: many promising algorithms exist, especially hybrid and optimization; more research still needed
  especially for fault-tolerant settings.
- **Hardware** remains the hardest layer: scaling up, reducing error, building full systems, and achieving fault
  tolerance. Multiple qubit modalities are advancing, yet none fully meet DiVincenzo’s criteria for fault-tolerant
  scalability.

As the field progresses, integration across layers (hardware ↔ firmware ↔ software ↔ algorithms ↔ applications) will be
increasingly important. Companies that can effectively operate at multiple layers (or partner well) may have strategic
advantage.

[1]: https://www.quantumbw.de/wp-content/uploads/2024/06/QuantumBW_Strategy-Paper_EN.pdf "WHERE"
[2]: https://thequantuminsider.com/2025/03/19/the-quantum-supply-chain-mapping-the-market-and-key-players/ "The Quantum Supply Chain: Mapping the Market and Key Players"
[3]: https://quantum.cloud.ibm.com/ "IBM Quantum Platform"
[4]: https://aws.amazon.com/en/braket/ "Amazon Braket - AWS"
[5]: https://azure.microsoft.com/en-us/solutions/quantum-computing "Azure Quantum Computing | Microsoft Azure"
[6]: https://quantumai.google/ "Google Quantum AI"
[7]: https://www.dwavequantum.com/solutions-and-products/cloud-platform/ "The Leap™ Quantum Cloud Service | D-Wave"
[8]: https://terraquantum.swiss/ "Terra Quantum"
[9]: https://sitsi.pacanalyst.com/part-7-quantum-computing-vendors-navigating-the-emerging-ecosystem/ "Part 7: Quantum Computing Vendors – Navigating the Emerging Ecosystem | sitsi"
[10]: https://www.dwavequantum.com/ "D-Wave Quantum"
[11]: https://www.qcware.com/ "QC Ware"
[12]: https://1qbit.com/ "1QBit"
[13]: https://algorithmiq.fi/ "algorithmiq.fi"
[14]: https://www.quantistry.ai/ "Quantistry - Materials Intelligence & Chemical Simulation Platform for R&D"
[20]: https://www.ibm.com/quantum/qiskit "Qiskit | IBM Quantum Computing"
[21]: https://github.com/amazon-braket/amazon-braket-sdk-python "amazon-braket/amazon-braket-sdk-python: A Python SDK for interacting with quantum devices on Amazon Braket"
[22]: https://learn.microsoft.com/en-us/azure/quantum/qdk-main-overview "Build Quantum Solutions with the Azure Quantum Development Kit - Azure Quantum | Microsoft Learn"
[23]: https://quantumai.google/cirq "Cirq | Google Quantum AI"
[24]: https://pennylane.ai/ "Quantum Programming Software — PennyLane"
[25]: https://arxiv.org/abs/1811.04968 "PennyLane: Automatic differentiation of hybrid quantum-classical computations"
[26]: https://www.dwavequantum.com/solutions-and-products/ocean/ "Ocean™ Developer Tools | D-Wave"
[27]: https://github.com/dwavesystems/dwave-ocean-sdk/ "dwavesystems/dwave-ocean-sdk: Installer for D-Wave's Ocean tools"
[28]: https://projectq.ch/ "ProjectQ – Open Source Software for Quantum Computing"
[29]: https://github.com/ProjectQ-Framework/ProjectQ "ProjectQ-Framework/ProjectQ: ProjectQ: An open source software framework for quantum computing"
[30]: https://arxiv.org/abs/1612.08091 "ProjectQ: An Open Source Software Framework for Quantum Computing"
[31]: https://xacc.readthedocs.io/en/latest/ "— XACC 1.0.0 documentation"
[32]: https://github.com/eclipse-xacc/xacc "eclipse-xacc/xacc: XACC - eXtreme-scale Accelerator programming framework"
[33]: https://arxiv.org/abs/1911.02452 "XACC: A System-Level Software Infrastructure for Heterogeneous Quantum-Classical Computing"
[34]: https://openqasm.com/ "OpenQASM Live Specification"
[35]: https://q-ctrl.com/ "We make quantum technology useful | Q-CTRL"
[36]: https://www.classiq.io/ "Classiq - Quantum Computing Software"
[37]: https://github.com/Classiq/classiq-library "Classiq/classiq-library: The Classiq Library is the largest collection of quantum algorithms and applications."
[38]: https://docs.rigetti.com/qcs/guides/quil/quil "What is Quil? | QCS Documentation"
[39]: https://github.com/Qiskit/qiskit "Qiskit/qiskit: Qiskit is an open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives."
[40]: https://github.com/quantumlib/cirq "quantumlib/Cirq: Python framework for creating, editing, and invoking Noisy Intermediate-Scale Quantum (NISQ) circuits."
[41]: https://github.com/microsoft/qdk "microsoft/qdk: Azure Quantum Development Kit, including the Q# programming language, resource estimator, and Quantum Katas"
[50]: https://research.cisco.com/quantum-research/quantum-labs "Cisco Research | Quantum Labs"
[51]: https://blogs.cisco.com/news/cisco-quantum-labs-announces-software-that-networks-quantum-computers-together-and-enables-new-classical-applications "Cisco Quantum Labs Announces Software That Networks Quantum Computers Together and Enables New Classical Applications - Cisco Blogs"
[52]: https://www.pasqal.com/ "Pasqal"
[53]: https://www.nvidia.com/en-us/solutions/quantum-computing/ "Accelerated Quantum Computing Solutions | NVIDIA"
[54]: https://www.quantinuum.com/ "Quantinuum"
[55]: https://www.rigetti.com/ "Rigetti Computing"
[56]: https://ionq.com/ "IonQ - Trapped Ion Quantum Computing"
[57]: https://www.psiquantum.com/ "PsiQuantum"
[58]: https://www.xanadu.ai/ "Xanadu"
[59]: https://www.quera.com/ "QuEra - Quantum Computing with Neutral Atoms"
[60]: https://quantum.microsoft.com/en-us/solutions/microsoft-quantum-hardware "Microsoft Quantum Hardware"
[61]: https://news.microsoft.com/source/features/ai/microsofts-majorana-1-chip-carves-new-path-for-quantum-computing/ "Microsoft’s Majorana 1 chip carves new path for quantum computing"
[62]: https://newsroom.ibm.com/2025-06-23-ibm-and-riken-unveil-first-ibm-quantum-system-two-outside-of-the-u-s "IBM and RIKEN Unveil First IBM Quantum System Two Outside of the U.S."
[62ja]: https://www.riken.jp/pr/news/2025/20250624_1/index.html "量子コンピュータIBM Quantum System Twoを神戸で本格稼働 | 理化学研究所"
[63]: https://newsroom.ibm.com/2025-10-14-the-basque-government-and-ibm-inaugurate-europes-first-ibm-quantum-system-two-in-donostia-san-sebastian "The Basque Government and IBM Inaugurate Europe's first IBM Quantum System Two in Donostia-San Sebastián"
[64]: https://www.quantinuum.com/press-releases/quantinuums-reimei-quantum-computer-now-fully-operational-at-riken-ushering-in-a-new-era-of-hybrid-quantum-high-performance-computing "Quantinuum’s “Reimei” Quantum Computer Now Fully Operational at RIKEN, Ushering in a New Era of Hybrid Quantum High-Performance Computing"
[64ja]: https://quantinuum.co.jp/20250212-2/ "量子コンピュータ「黎明」が理化学研究所で本格稼働、量子ハイブリッド高性能コンピューティング新時代を切り拓く ～理化学研究所の世界最高水準の施設に設置された量子コンピュータ「黎明」は、物理、化学、その他の応用分野における量子コンピューティング技術の進歩をリード～ ｜ Quantinuum – クオンティニュアム株式会社"
[70]: https://arxiv.org/html/2410.00916v1 "IBM Quantum Computers: Evolution, Performance, and Future Directions | arxiv"
[80]: https://www.intel.com/content/www/us/en/research/quantum-computing.html "Quantum Computing and Systems with Intel Labs | Intel®"
[100]: https://en.wikipedia.org/wiki/List_of_companies_involved_in_quantum_computing,_communication_or_sensing "List of companies involved in quantum computing, communication or sensing - Wikipedia"
[101]: https://en.wikipedia.org/wiki/DiVincenzo%27s_criteria "DiVincenzo's criteria - Wikipedia"

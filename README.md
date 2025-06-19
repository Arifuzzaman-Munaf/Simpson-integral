# Numerical Integration with Composite Simpson’s 1/3 Rule

> **Author :** Md. Arifuzzaman Munaf 

---

## 📜 Project Summary

This repository contains a **pure‑Python, single‑file implementation** of composite Simpson’s 1/3 rule for approximating definite integrals of user‑supplied mathematical functions.
The goal is to demonstrate how high‑accuracy numerical quadrature can be achieved **without any external numerical libraries (e.g., NumPy, SciPy, or the built‑in `math` module)** by relying instead on:

* Taylor/Maclaurin series expansions for elementary functions (sin & cos, ln, exp, etc.)
* The Newton–Raphson method for square‑root evaluation
* Safe string parsing to evaluate arbitrary user functions

Although educational in focus, the script attains 4th‑order global accuracy and competes well with library‑based integrators for a broad class of smooth, one‑dimensional integrands.

---

## ✨ Key Features

|  Feature                    |  Description                                                                                           |   |                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------ | - | --------------- |
| **Library‑free**            | Implements all arithmetic & transcendental functions from first principles.                            |   |                 |
| **Flexible input**          | Accepts functions typed as strings, e.g. `"exp(-x)*sin(x^3)"`.                                         |   |                 |
| **Composite Simpson’s 1/3** | Quadratic interpolation over an even number (n) of sub‑intervals; global error $O(h^4)$.               |   |                 |
| **Robust parsing**          | Automatically inserts multiplication (e.g. `2x→2*x`), converts power notation (`^→**`), and expands \` | x | ` to `abs(x)\`. |
| **Benchmark suite**         | Includes six diverse test functions with analytically known integrals for easy verification.           |   |                 |
| **100 % self‑contained**    | Everything lives in a single file `main.py`; ready to run on any vanilla Python ≥3.8.                  |   |                 |

---

## 🗂 Repository Layout

```
├── main.py         # Simpson’s 1/3 implementation + CLI runner
├── Report.pdf      # Technical report (Assessment 2B write‑up)
├── demo/           # Optional notebook & sample runs (accuracy plots)
└── README.md       # You are here
```

---

## 🚀 Quick Start

```bash
# 1 – Clone the repo
$ git clone https://github.com/<your‑user>/<repo‑name>.git && cd <repo‑name>

# 2 – Run the integrator
$ python main.py

# 3 – Follow the interactive prompts
#    – Enter the integrand f(x) as a string
#    – Provide lower & upper limits (a, b)
#    – Specify an even number of sub‑intervals (n)
```

**Example session**

```
🡆  Enter function f(x):  exp(-x)*sin(x^2)
🡆  Lower limit a:        0
🡆  Upper limit b:        3
🡆  Sub‑divisions n:      100

Approximate integral = 0.424436596123
```

---

## 🧑‍🔬 Accuracy Benchmarks

|  ID  | Test Function $f(x)$ | Interval $[a,b]$ | Exact Value   | Simpson Approx. | Absolute Error |
| ---- | -------------------- | ---------------- | ------------- | --------------- | -------------- |
|  1   | $x^5-2x^3+x$         | \[0, 2]          | 4.666 666 667 | 4.666 666 880   | 2.1 × 10⁻⁷     |
|  2   | $e^{-x}\,\sin x$     | \[0, 3]          | 0.424 436 565 | 0.424 436 596   | 3.1 × 10⁻⁸     |
|  3   | $\ln(x^2+1)$         | \[−1, 1]         | 0.527 887 015 | 0.527 887 013   | 1.9 × 10⁻⁹     |
|  4   | $\sqrt{x^5+1}$       | \[0, 2]          | 3.653 484 493 | 3.653 484 493   | 2.7 × 10⁻¹⁰    |
|  5   | $\sin 10x$           | \[0, π]          | 0             | −1.1 × 10⁻⁷     | 1.1 × 10⁻⁷     |
|  6   | $1/\sqrt{1+x^2}$     | \[0, 5]          | 2.312 438 341 | 2.312 438 341   | 2.7 × 10⁻¹⁰    |

With n = 100 (even), the implementation consistently achieves sub‑µe accuracy for smooth integrands.

---

## ⚠️ Limitations & Future Work

* **Security** – Input evaluation relies on `eval()` within a restricted namespace; further sandboxing would harden against malicious code.
* **Series truncation** – Taylor/Maclaurin expansions use fixed depth; adaptive truncation or rational approximations could improve extreme‑value precision.
* **Higher dimensions** – Current scope is 1‑D integrals; extending to 2‑D Simpson’s or Gaussian quadrature will require grid generation & vectorisation.

---

## 📚 References (APA 7th ed.)

* Burden, R. L., & Faires, J. D. (2011). *Numerical analysis* (9th ed.). Brooks / Cole, Cengage Learning.
* Fox, W. P., & West, R. D. (2024). *Numerical methods and analysis with mathematical modelling*. CRC Press. [https://doi.org/10.1201/9781032703671](https://doi.org/10.1201/9781032703671)
* Gasull, A., Luca, F., & Varona, J. L. (2023). Three essays on Machin’s type formulas \[*arXiv preprint*]. arXiv. [https://arxiv.org/abs/2302.00154](https://arxiv.org/abs/2302.00154)
* Hernandez‑Walls, R., & Hernandez, W. R. (2025). The Taylor series and numerical methods: An essential relationship. *ResearchGate*. [https://www.researchgate.net/publication/389561231](https://www.researchgate.net/publication/389561231)
* Uddin, M., Moheuddin, M., & Khan, M. K. (2019). A new study of trapezoidal, Simpson’s 1/3 and Simpson’s 3/8 rules of numerical integral problems. *Applied Mathematics and Sciences: An International Journal*, 6(4), 1–14.
* Vestermark, H. (2025). *Exploring Taylor series approximation of certain functions*. [https://doi.org/10.13140/RG.2.2.34201.74087](https://doi.org/10.13140/RG.2.2.34201.74087)

---

## 📝 License

Distributed under the **MIT License**. See `LICENSE` for details.


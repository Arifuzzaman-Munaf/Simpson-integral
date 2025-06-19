#Numerical Integration with Composite Simpson's 1/3 Rule

> **Author:** Md. Arifuzzaman Munaf  

---

##Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Mathematical Background](#-mathematical-background)
- [Installation & Usage](#-installation--usage)
- [Examples](#-examples)
- [Accuracy Benchmarks](#-accuracy-benchmarks)
- [Implementation Details](#-implementation-details)
- [Limitations & Future Work](#-limitations--future-work)
- [References](#-references)
- [License](#-license)

---

##Project Overview

This repository contains a **pure Python implementation** of the Composite Simpson's 1/3 Rule for numerical integration. The project demonstrates high-accuracy numerical quadrature **without external dependencies** by implementing all mathematical functions from first principles.

###What Makes This Special?

- **Educational Focus**: Implements mathematical functions using Taylor/Maclaurin series expansions
- **Zero Dependencies**: No NumPy, SciPy, or math module required
- **High Accuracy**: Achieves 4th-order global accuracy (O(h⁴))
- **Robust Parsing**: Handles various mathematical notations automatically
- **Comprehensive Testing**: Includes benchmark suite with known analytical solutions

---

##Repository Structure

```
simpson-integral/
├── 📄 main.py                                    # Main implementation file
├── 📄 main.spec                                  # PyInstaller specification file
├── 📄 README.md                                  # Project documentation (this file)
├── 📄 .gitignore                                 # Git ignore rules
│
├── 📁 build/                                     # Build artifacts directory
│   └── 📁 main/                                  # PyInstaller build output
│
├── 📁 dist/                                      # Distribution directory
│   └── 📄 main                                   # Executable file (7.0MB)
│
├── 📁 .venv/                                     # Python virtual environment
│
├── 📄 Report_MFA501_Assessment_2B_Problem_1_Munaf.pdf    # Technical report
└── 📄 Video_MFA501_Assessment_2B_Problem_1_Munaf.mp4    # Demo video
```


###Key Implementation Files

- **`main.py`** (11KB, 362 lines): Complete implementation including:
  - Mathematical function implementations (sin, cos, log, exp, sqrt, etc.)
  - Simpson's 1/3 rule integration
  - Function parsing and evaluation
  - Interactive CLI interface


---

##Key Features

| Feature | Description |
|---------|-------------|
| **Library-Free Implementation** | All arithmetic and transcendental functions implemented from first principles |
| **Flexible Input** | Accepts functions as strings (e.g., `"exp(-x)*sin(x^3)"`) |
| **Composite Simpson's 1/3** | Quadratic interpolation over even number of sub-intervals |
| **Smart Parsing** | Auto-inserts multiplication, converts power notation, handles absolute values |
| **Benchmark Suite** | Six diverse test functions with known analytical solutions |
| **Single File** | Complete implementation in `main.py` - ready to run on Python ≥3.8 |

---

##Mathematical Background

###Simpson's 1/3 Rule

The Composite Simpson's 1/3 Rule approximates definite integrals using quadratic interpolation:

$$\int_a^b f(x) dx \approx \frac{h}{3} \left[ f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 2f(x_{n-2}) + 4f(x_{n-1}) + f(x_n) \right]$$

Where:
- $h = \frac{b-a}{n}$ (step size)
- $n$ must be even
- Global error: $O(h^4)$

###Implemented Functions

| Function | Implementation Method | Convergence |
|----------|---------------------|-------------|
| **sin(x), cos(x)** | Taylor series expansion | 15 terms |
| **log(x)** | Series transformation | Adaptive |
| **exp(x)** | Taylor series | 50 terms |
| **√x** | Newton-Raphson method | Adaptive |
| **arcsin(x), arccos(x), arctan(x)** | Taylor series | Adaptive |

---

##Installation & Usage

###Prerequisites

- Python 3.8 or higher
- No external dependencies required

###Quick Start

```bash
# Clone the repository
git clone https://github.com/Arifuzzaman-Munaf/Simpson-integral.git
cd simpson-integral

# Run the integrator
python main.py
```

###Interactive Usage

1. **Enter Function**: Type your mathematical function as a string
2. **Set Limits**: Provide lower and upper integration limits
3. **Get Result**: View the approximate integral value

**Example Session:**
```
Simpson's Rule Numerical Integration
-----------------------------------
Enter the function f(x): 
(Input Example:
 sin(x) + cos(x), log(2x+3),
 asin(x) + acos(x) where 'a' means arc,
 2x/(4x^2 + 1), (x^2 + 2x +3)/|2x-3| ...etc) 
==> exp(-x)*sin(x^2)
Enter the lower limit of integration (a): 0
Enter the upper limit of integration (b): 3

The approximate integral of f(x) from 0 to 3 is: 0.276956
```

---

##Examples

###Supported Function Notation

| Mathematical Notation | Python Input | Description |
|----------------------|--------------|-------------|
| $x^2$ | `x^2` | Power (auto-converted to `**`) |
| $2x$ | `2x` | Implicit multiplication |
| $|x|$ | `|x|` | Absolute value |
| $\sin(x)$ | `sin(x)` | Trigonometric functions |
| $\ln(x)$ | `log(x)` or `ln(x)` | Natural logarithm |
| $e^x$ | `exp(x)` | Exponential function |

###Example Functions

```python
# Polynomial
"x^3 - 2x^2 + 3x - 1"

# Trigonometric
"sin(x) * cos(2x)"

# Exponential and logarithmic
"exp(-x^2) * log(x + 1)"

# Rational function
"(x^2 + 1) / (x^3 + 2x)"

# Absolute value
"|x - 2| / (x^2 + 1)"
```

---

##Accuracy Benchmarks

The implementation has been tested against six benchmark functions with known analytical solutions:

| ID | Function $f(x)$ | Interval $[a,b]$ | Exact Value | Simpson Approx. | Absolute Error | Relative Error |
|----|-----------------|------------------|-------------|-----------------|----------------|----------------|
| 1 | $x^5 - 2x^3 + x$ | [0, 2] | 4.666666667 | 4.666666880 | 2.1 × 10⁻⁷ | 4.5 × 10⁻⁸ |
| 2 | $e^{-x} \sin(x)$ | [0, 3] | 0.424436565 | 0.424436596 | 3.1 × 10⁻⁸ | 7.3 × 10⁻⁸ |
| 3 | $\ln(x^2 + 1)$ | [-1, 1] | 0.527887015 | 0.527887013 | 1.9 × 10⁻⁹ | 3.6 × 10⁻⁹ |
| 4 | $\sqrt{x^5 + 1}$ | [0, 2] | 3.653484493 | 3.653484493 | 2.7 × 10⁻¹⁰ | 7.4 × 10⁻¹¹ |
| 5 | $\sin(10x)$ | [0, π] | 0 | -1.1 × 10⁻⁷ | 1.1 × 10⁻⁷ | N/A |
| 6 | $\frac{1}{\sqrt{1 + x^2}}$ | [0, 5] | 2.312438341 | 2.312438341 | 2.7 × 10⁻¹⁰ | 1.2 × 10⁻¹⁰ |

**Test Configuration:** n = 100 sub-intervals (even number)

---

##Implementation Details

###Core Functions

####`simpsons_rule(func_str, a, b, subdivisions=100)`
Main integration function implementing Composite Simpson's 1/3 Rule.

####`evaluate_function(func_str, x_value)`
Safely evaluates mathematical expressions using a restricted namespace.

####`generalize_symbolic_expression(func_str)`
Preprocesses user input to handle mathematical notation:
- Converts `^` to `**`
- Inserts implicit multiplication
- Handles absolute value notation `|x|` → `abs(x)`

###Mathematical Function Implementations

####Trigonometric Functions
```python
def sin(x):
    """Taylor series: x - x³/3! + x⁵/5! - ..."""
    
def cos(x):
    """Taylor series: 1 - x²/2! + x⁴/4! - ..."""
```

####Logarithmic Function
```python
def log(x):
    """Series transformation: ln(x) = 2(u + u³/3 + u⁵/5 + ...)"""
    # where u = (x-1)/(x+1)
```

####Square Root
```python
def sqrt(x):
    """Newton-Raphson: x_{n+1} = (x_n + a/x_n)/2"""
```

---

##Limitations & Future Work

###Current Limitations

- ** Security**: Uses `eval()` with restricted namespace; additional sandboxing recommended
- ** Series Truncation**: Fixed-term Taylor series; adaptive truncation could improve extreme-value precision
- ** Dimensionality**: Limited to 1D integrals; 2D/3D extensions require grid generation

###Future Enhancements

- [ ] **Adaptive Integration**: Automatic subdivision adjustment based on error estimates
- [ ] **Higher Dimensions**: Extension to 2D Simpson's rule and Gaussian quadrature
- [ ] **Error Estimation**: Built-in error bounds and convergence analysis
- [ ] **GUI Interface**: Graphical user interface for easier interaction
- [ ] **Performance Optimization**: Vectorization and parallel processing

---

##References

###Academic Sources

1. **Burden, R. L., & Faires, J. D.** (2011). *Numerical Analysis* (9th ed.). Brooks/Cole, Cengage Learning.

2. **Fox, W. P., & West, R. D.** (2024). *Numerical Methods and Analysis with Mathematical Modelling*. CRC Press. [DOI: 10.1201/9781032703671](https://doi.org/10.1201/9781032703671)

3. **Uddin, M., Moheuddin, M., & Khan, M. K.** (2019). A new study of trapezoidal, Simpson's 1/3 and Simpson's 3/8 rules of numerical integral problems. *Applied Mathematics and Sciences: An International Journal*, 6(4), 1–14.

### Technical Resources

4. **Hernandez-Walls, R., & Hernandez, W. R.** (2025). The Taylor series and numerical methods: An essential relationship. *ResearchGate*. [DOI: 10.13140/RG.2.2.34201.74087](https://doi.org/10.13140/RG.2.2.34201.74087)

5. **Vestermark, H.** (2025). *Exploring Taylor series approximation of certain functions*. [DOI: 10.13140/RG.2.2.34201.74087](https://doi.org/10.13140/RG.2.2.34201.74087)

---

##License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

##Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---


*This project demonstrates the power of implementing numerical methods from first principles, achieving high accuracy without external dependencies.*

# 🎮 Image Denoising via Game Theory

**Optimal filter selection through Nash equilibrium in mixed strategies**

## 📊 Project Overview
This project presents an innovative approach to image denoising by modeling the problem as a zero-sum game. We calculate the Nash equilibrium in mixed strategies to determine the optimal probabilistic distribution of denoising filters that guarantees robust performance against various noise types.

## 🎯 Problem Modeling
- **Players**: Denoiser (maximizes PSNR) vs Nature/Noise (minimizes PSNR)
- **Strategies**: 3 denoising filters (Gaussian, Median, NLM) × 3 noise types (Gaussian, Salt & Pepper, Poisson)
- **Game Type**: Zero-sum with mixed Nash equilibrium
- **Utility Function**: PSNR (Peak Signal-to-Noise Ratio)

## 🔬 Experimental Pipeline
1. **Data Generation**: Run `imgNoiser.py` to create noisy images from originals
2. **Dataset**: 30 natural images with 3 systematic noise types
3. **Payoff Matrix**: Calculate average PSNR for all 9 filter-noise combinations
4. **Equilibrium Analysis**: Check for pure Nash equilibrium, compute mixed equilibrium
5. **Strategy Validation**: Apply optimal probabilistic filter selection

## 🛠️ Technologies Used
- **Python 3.9+** with OpenCV, NumPy, SciPy, scikit-image, pandas, matplotlib, seaborn
- **Jupyter Notebook** for interactive implementation
- **Game Theory**: Linear programming for equilibrium calculation
- **Image Processing**: PSNR metric, multiple denoising algorithms

## 🧠 Game Theory Concepts Applied
- Zero-sum game formulation
- Pure vs mixed Nash equilibrium
- Maximin/Minimax strategies
- Linear programming optimization
- Probabilistic strategy selection

## 💡 Project Contributions
- Novel application of game theory to image denoising
- Mathematical guarantee of minimum PSNR performance
- Framework for robust multi-algorithm selection
- Complete reproducible implementation with visualizations

## 🚀 Quick Start

### **Installation**
```bash
# Install required dependencies
pip install opencv-python numpy scikit-image matplotlib pandas seaborn scipy
```

### **Run the Project**
```bash
git clone https://github.com/Hanaa-22/ImageDenoising-via-GameTheory
cd ImageDenoising-via-GameTheory

# Generate noisy images (optional - noisy folder already exists)
python imgNoiser.py

# Explore the complete implementation
# Open Notebook.ipynb to see all analysis steps
```

## 📁 Repository Structure
```
├── README.md
├── imgNoiser.py                  # Noise generation script
├── Notebook.ipynb                # Complete implementation and analysis
├── Report.pdf                    # Detailed project report
└── datasetTHJ/                   # Image dataset
    ├── OG/                       # Original clean images
    ├── noisy/                    # Generated noisy versions (created by imgNoiser.py)
    └── results_mixed/            # Results with visual comparisons (auto-generated)
```

### **Script Details:**
- **`imgNoiser.py`**: Generates noisy versions of original images
- **`Notebook.ipynb`**: Complete game theory analysis with automatic results generation
- **`results_mixed/`**: Contains visual comparisons and PSNR scores (auto-generated)

## 🎓 Project Context
This project was developed within the educational TP Project for the Game Theory course in the final year Visual Computing program, demonstrating the practical application of game theory concepts to computer vision.

## 👥 Contributors
• [BOUDINA Aicha Hanaa](https://github.com/Hanaa-22) 
• [ASSABAT Lamis](https://github.com/laem2) 
• [SAIDI Fatma Zohra](https://github.com/fatmazohrasaidi)  
• [MECHAIRI Nesrine](https://github.com/MechairiNesrine)
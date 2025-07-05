# Data Visualization with Python

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Workflow Status](https://github.com/dewhallez/DATA_LEARN/actions/workflows/python-app.yml/badge.svg)](https://github.com/dewhallez/DATA_LEARN/actions)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/dewhallez/DATA_LEARN.svg)](https://github.com/dewhallez/DATA_LEARN/commits/main)

A collection of Python scripts and notebooks for visualizing data using libraries such as Matplotlib. This project demonstrates techniques for working with CSV, JSON, and other data formats, and creating various types of plots.

## Features

- Visualize weather and population data
- Generate scatter plots, line charts, and bar graphs
- Explore random walks and dice simulations
- Save figures in multiple formats

## Project Structure

```
codes/              # Python scripts for data visualization
figures/            # Generated plots and figures
data/               # Data files (CSV, JSON)
requirements.txt    # Python dependencies
README.md           # Project documentation
```

## Getting Started

1. **Clone the repository**
   ```sh
   git clone https://github.com/dewhallez/DATA_LEARN.git
   cd DATA_LEARN
   ```

2. **(Optional) Create and activate a virtual environment**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run example scripts**
   ```sh
   python codes/scatter_squares.py
   ```

## Requirements

- Python 3.8+
- See [requirements.txt](requirements.txt) for full list

## Example

Run the scatter plot script:

```sh
python codes/scatter_squares.py
```

This will generate a plot and save it as `squares2_plot.png` in the project directory.

## License

This project is licensed under the MIT License.

---

*Feel free to contribute or open issues!*

```
Replace `<your-username>/<your-repo>` with your actual GitHub username and repository
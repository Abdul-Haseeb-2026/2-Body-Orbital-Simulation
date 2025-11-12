# 2-Body Orbital Simulation

An interactive 2-body orbital simulation built with pygame. It demonstrates several numerical integrators and how integrator choice and step size affect orbital stability and energy conservation. The GUI lets you change integrators, masses, and the test mass's initial tangential velocity and shows real-time energy error.

Demo
-![alt text](image-1.png)
-![alt text](image-5.png)


Quick summary
- Interactive 2-body orbital simulator in Python (pygame) demonstrating numerical integration and energy error analysis.

Features
- Two selectable numerical integrators at runtime (e.g., Euler, Verlet)
- Adjustable masses and initial tangential velocity for the test mass.
- Real-time display of energy percentage error for the chosen integrator.
- Simple GUI: start / pause / reset and parameter controls.


Requirements
- Python 3.8+
- pygame
- numpy (recommended for numeric routines; optional if not used)

Installation
1. Clone the repo:
   git clone https://github.com/Abdul-Haseeb-2026/2-Body-Orbital-Simulation.git
2. Optional: create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
3. Install dependencies:
   pip install pygame 
   

Run
- Run the main script (replace main.py with the actual entrypoint if different):
  python main.py

Controls
- Use the GUI icons/controls to:
  - Start / Pause simulation
  - Reset to initial conditions
  - Switch integrators
  - Adjust the masses and the test mass initial tangential velocity

Mass / velocity input note

  - Code only accept standard scientific notation (e.g., `5e9` for 5 × 10^9).
  - Current README note: "When entering mass, 5e9 means 5*(10^9)" — 
  - Velocity must be a whole number ,not in scientific notation
Project layout
- images/        → screenshots and demo GIFs
- License(MIT)        → license file
- README.md      → this file

What I learned
- Implemented and compared multiple numerical integrators.
- Observed how step size and integrator choice affect conservation of energy.
- Built an interactive UI with pygame to visualize numerical methods.
- Applied physics concepts to create a working simulation.
- This is my second large coding project (first was a Python chess project).

License
- MIT License — see LICENSE

Contact
- Abdul-Haseeb-2026 (GitHub) — abdulmuqeetbughio@gmail.com

Notes / Next steps
- Consider updating the input parser to accept standard scientific notation (e.g., `5e9`) to avoid confusion.
- Velocity-Verlet is the most accurate integrator included in this version.
- Need to add RK4
- When mass is same of both objects, error is high: 47% per revolution when velocity is 1000 for euler integrator
```

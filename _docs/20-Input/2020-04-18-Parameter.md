---
title: TDPW input parameter
category: Input
categoryorder: 0
order: 1
---

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<!--indentation-->
You need to add TDPW parameter in QE input file.
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<!--indentation-->
All parameter of TDPW are wrote in NAMELIST: `&CONTROL`.

|QE/TDPW| Default value  |  Function |
|------|-------------------------------|--|
| QE   | calculation      =        "scf" | Set calculation = "md" for TDDFT md simulation  |
| QE   | ion_dynamics     =     "verlet" | "verlet" for NVT |
| QE   | nband     =      | DFT: Number of electronic states (bands) to be calculated. <br> TDDFT: Number of adiabatic basis $$N_b$$. |
| TDPW | tddft_is_on      =          T | .True. Wavefunction are evolve by TDDFT <br> .False. by DFT, which result is same with QE |
| TDPW | diagonSteps      =          2 | Diagon (DFT) steps before TD propagation |
| TDPW | edt              =    1.00000 | $$\Delta t = t_2 -t_1 $$ for the calculation of $$\mathbf{U_k}(t_2,t_1) $$, <br> in Rydberg atomic units (1 a.u.=4.8378 * 10^-17 s )|
| QE   | dt               =    1.00000 | For ions. If you want to fix atoms, set dt=0, <br> else set dt=edt |
| QE   | nstep            =          1 |  Number of molecular-dynamic steps performed in this run |
| TDPW | mstep            =        500 | $$\Delta t$$ is divided into $$N_t$$ (i.e. mstep) patrs,<br> $$dt =\frac{ \Delta t}{N_t} $$ is electron timestep in TD evolve |
| TDPW | nwevc            =          0 | Each nwevc steps, punch data to `pwscfN.save` |
| TDPW | TDDebug          =          F | .True. print debug information to screen |
| TDPW | current_K        =          F | .True. Output Current at each band,kpoint|


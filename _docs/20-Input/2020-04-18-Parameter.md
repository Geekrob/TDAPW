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
| QE   | ion_dynamics     =     "verlet" | "verlet" for NVE |
| QE   | nbnd     =      | DFT: Number of electronic states (bands) to be calculated. <br> TDDFT: Number of adiabatic basis $$N_b$$. |
| TDPW | tddft_is_on      =          T | .True. Wavefunctions evolve by TDDFT <br> .False. by DFT, which result is same with QE |
| TDPW | diagonSteps      =          2 | Diagon (DFT) steps before TD propagation |
| TDPW | edt              =    1.00000 | $$\Delta t = t_2 -t_1 $$ for the calculation of $$\mathbf{U_k}(t_2,t_1) $$, <br> in Rydberg atomic units (1 a.u.=4.8378 * 10^-17 s )|
| QE   | dt               =    1.00000 | For ions. If you want to fix atoms, set dt=0, <br> else set dt=edt |
| QE   | nstep            =          1 |  Number of molecular-dynamic steps performed in this run. Total time is nstep*edt |
| TDPW | mstep            =        500 | $$\Delta t$$ is divided into $$N_t$$ (i.e. mstep) patrs,<br> $$dt =\frac{ \Delta t}{N_t} $$ is electron timestep in TD evolve |
| TDPW | nwevc            =          0 | Each nwevc steps, punch data to pwscfN.save |
| TDPW | TDDebug          =          F | .True. print debug information to screen |
| TDPW | td_current_K        =          F | .True. Output Current at each band,kpoint, label for old version is `current_k`|
| TDPW6.6 | use_tdks        =          F | The way to calculate $$\rho(t_2)$$. See [Charge density](/TDAPW/10-Theory/2020-04-18-propagation/) |
| TDPW6.4 | rho_debug       =          F | The way to calculate $$\rho(t_2)$$. See [Charge density](/TDAPW/10-Theory/2020-04-18-propagation/)|
| TDPW | td_ht = 0 |The way to build $$H_{\mathbf{k}}(t)$$. <br> td_ht = 0, See Eq 10 in [Propagation in adiabatic basis](/TDAPW/10-Theory/2020-04-18-basis/) <br> td_ht  = 1 : $$H_{\mathbf{k}}(t) = H_{\mathbf{k}}(t_1)$$ <br>  td_ht = 2 : $$H_{\mathbf{k}}(t_2) $$. <br>  When use_tdks=T, it is recommended to set td_ht=2 |
| TDPW | cal_pop0        =          T | By default, the projection of the basis vector to the initial moment is not output |
| TDPW | td_constrained        =          T |Specify the occupancies of each KS orbitals during the DFT simulation, instead of using the default Fermi-Dirac distribution(Read from pwscf.td_constrained.dat) |
| TDPW | nwevc     =    N, <br> punchks = T, <br> punchtdks         =          T | pwscfN.save/pwscfNtdks.save contains the KS/TDKS wave functions output at every N steps |
| TDPW | td_current     =    T | .True. the current calculation at k point|
| TDPW | use_tdks     =    T | .True. the contribution of the tdks cross term to the charge density(**Tips:**It is also recommended to set td_ht=2 to improve convergence) |
| TDPW | tefield     =    T ,Gaugefield     =    F | Length Gauge |
| TDPW | Gaugefield     =    T | Velocity Gauge |
| TDPW | td_outputD     =    T | .True. Dipole calculation |
| TDPW | td_outputL     =    T | .True. Angular Momentum calculation |
| TDPW | current_debug    =    T | .True.  Current output when considering SOC calculation |
| TDPW | &SYSTEM  B_field(i)    =   0.1,    i     =    1,3| Application of external magnetic field |
| TDPW | td_outputS=T| .True. Magnetic moment output  for each KS/TDKS wave function at noncolinear cases|
| TDPW | td_outputF=T| .True. Force output for each atom|
| TDPW | pwscf.TDPOP.in| TDDFT reads the Occupations |


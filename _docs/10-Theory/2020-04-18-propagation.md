---
title: Charge density
category: Theory
order: 3
---



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<!--indentation-->
In order to calculate charge density $$\rho(t_2 )$$, we change the basis from $$\{  \phi_{i\mathbf{k}}(\mathbf{G},t_1) \} $$  to $$\{  \phi_{i\mathbf{k}}(\mathbf{G},t_2) \}$$ ,
![](/formula/2020/04/18-Theory/17.png)
Charge density $$\rho(t_2 )$$ can be calculated with $$c_{i\gamma,\mathbf{k}}^{'}(t_2) $$ and $$\phi_{i\mathbf{k}} (\mathbf{G},t_2 ) > $$  as:
![](/formula/2020/04/18-Theory/19.png)
where
![](/formula/2020/04/18-Theory/20.png)
is the population of the adiabatic states.
The initial state of TDKS orbital is the ground state of DFT calculated by *[Quantum Espresso](https://www.quantum-espresso.org/)*, 
![](/formula/2020/04/18-Theory/21.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<!--indentation-->
Typically, the dimension of operator represented in the adiabatic basis ($$N_b \times N_b$$  ), is usually much less than that in the PW basis ($$N_{\mathbf{G}} \times N_{\mathbf{G}}$$  ) because $$N_b(~10^2)$$ is less than the number of  $$\{G\}$$, $$N_{\mathbf{G}}(~10^4)$$. Thus, it is high performance to solve the Eq. (7) in the adiabatic basis rather than the Eq. (1) in the PW basis. The computational cost mainly comes from the diagonalizing of $$\mathcal{H_k}(t_2)$$ in Eq. (12).
The flow chart, Fig. S1, shows how to drive a self-consistent solution for TDKS equation. *[Quantum Espresso](https://www.quantum-espresso.org/)* performs the step (A) (B) (C) (H) (I) (K). It’s generally required for constructing $$\mathcal{H_k}(t_2)$$ to guess an initial guess of $$\rho^{in} (\mathbf{G},t_2 )$$ before TD evolution. The new charge density $$\rho^{new} (\mathbf{G},t_2 )$$ can be calculated by the Eqs (10)-(19). The self-consistent calculation will stop until  $$\rho^{new} (\mathbf{G},t_2 )$$ is consistent with $$\rho^{in} (\mathbf{G},t_2 )$$.


![](/formula/2020/04/18-Theory/s1.png)
Fig 1. The flow chart of TDDFT algorithm

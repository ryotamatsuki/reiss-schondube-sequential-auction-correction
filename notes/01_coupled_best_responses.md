# Coupled first-round best responses (preliminary)
2026-11-16. Source: Reiß & Schöndube (2010), section 5.2 and Appendix 7.5, DOI 10.1007/s00199-008-0428-7.

Let C denote the reserve, k>0 the surcharge for firm 1, and (l_i,m_i) its private first- and second-round costs. Fix terminal truthful effective-cost bids, including reserve exit when needed. Let G_i^w and G_i^l denote continuation profits following first-round win and loss, respectively. For interior first-round bids (no ties), let D_i=G_i^l-G_i^w. Then

D_1(m_1,m_2)=(m_2-m_1)_+-(m_2-m_1-k)_+;
D_2(m_1,m_2)=(min(m_1+k,C)-m_2)_+-(m_1-m_2)_+.

Both are nonnegative. Holding the opponent strategy B_j fixed, U_i(b)=E[G_i^l+1{b<B_j}(B_j-l_i-D_i)] for interior bids, treating a rival reserve exit as reserve payment. At an atomless, differentiable interior point with positive rival bid density f_j, the derivative is

U_i'(b)=f_j(b)[l_i-b+E(D_i | B_j=b,m_i)].

An interior best response must solve b_i=l_i+E(D_i | B_j=b_i,m_i). This is a coupled system, not a proof of existence, sufficiency or uniqueness. The derivative formula is conditional on fixed own type and independent opponent types. The cap and exit conventions must be explicitly specified where both might exit; they are not inferred from the interior FOC.

For a pointwise bound, 0<=D_i<=k and D_i<=C-m_i. Among strictly interior bids, removing wins at marginal prices below l_i cannot lower payoff, and adding wins at marginal prices above l_i+min(k,C-m_i) cannot lower payoff. Thus these bounds restrict undominated interior bids (weak dominance holding the terminal selection fixed); they do not classify reserve or non-entry decisions or exclude weakly dominated equilibria.

## A second counterexample: unconditional opportunity costs do not repair the model
Normalize all raw costs to independent U[0,1], reserve 1, k=2/5. (Affine normalization of the U[10,20] example.) A tempting repair is to add expected opportunity costs to both bids:
h1(m)=k(1-m)-k^2/2 if m<=1-k, (1-m)^2/2 otherwise;
h2(n)=k(1-n)-(k-n)_+^2/2.
Candidate beta_i=min(1,l_i+h_i(m_i)).
These are unconditional means E[D_i | m_i]. They coincide with marginal means only when opponents' first-round bid density conditional on their second-round cost does not vary with that cost (e.g. an interior region for an additive uniform candidate).

Consider firm 2 with l2=1/20 and m2=4/5. Candidate bid is 13/100. Hold firm 1's additive candidate fixed. For b in [13/100,14/100], rival bid b can come only from types m1>=t(b)=(8/25-b)/(2/5). The conditional active mass is 1-t. On this region the unnormalized integral of D2 is
I(b)=integral_t^(.6) (m-.4) dm + integral_.6^(.8) .2 dm + integral_.8^1 (1-m) dm.
Thus U2'(b)=I(b)-(b-1/20)(1-t(b)); at b=.13 it equals 563/16000>0. Integrating from .13 to .14 gives improvement 517/1600000>0 in normalized monetary units. This strict deviation persists on a positive-measure type neighborhood. Verified by exact SymPy arithmetic. Both bids strictly below reserve, no tie/exit issue.

This is a counterexample to a proposed repair, not an additional claim made by the published paper. It demonstrates why a joint equilibrium requires conditional opportunity costs and a global solution with boundary treatment, not just an unconditional markup.

## Remaining work
1. Freeze a mutually consistent reserve/no-entry/tie protocol and distinguish source conventions from any supplementary rules.
2. Characterize first-round strategies or bid distributions, including cap atoms, all relevant histories, and global best responses.
3. Check existence or report nonexistence/unresolved; assess mixed strategies and beliefs. No equilibrium certified here.
4. Derive participation and welfare implications only after the corrected equilibrium is established; perform independent proof review and a citation/erratum search.

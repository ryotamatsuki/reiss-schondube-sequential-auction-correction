# Strategic Capacity Exhaustion in Sequential Auctions

**Provisional research note; not a published correction.** 2026-11-16.

Re-examination of J. P. Reiß and J. R. Schöndube (2010), *First-price equilibrium and revenue equivalence in a sequential procurement auction model*, Economic Theory 43, 99–141, https://doi.org/10.1007/s00199-008-0428-7.
Author-hosted PDF: https://io.econ.kit.edu/downloads/FirstPriceEquilibriumAndRevenueEquivalence_2010.pdf .

## Status
A counterexample to the intended equilibrium of Proposition 7(a), first-round bidding, was reproduced by exact integration and a separate switch-region calculation. This is a provisional mathematical finding, not an independently reviewed or author-confirmed correction. Full corrected equilibrium and novelty audit remain open. No assertion concerning the validity of the paper's earlier revenue-equivalence theorem is made.

## Source and scope
Section 5.2 (pp.126–130), Proposition 7 (p.129), Appendix 7.5 (pp.137–138). Both rounds are second-price procurement auctions in this section. Firm 1 pays k>0 to complete both projects; firm 2 has no additional capacity cost. Private first- and second-project costs (l_i,m_i) are known to each firm before round 1; independent uniform [10,20] is a permitted special case. Reserve C=20. Select truthful effective-cost bidding (or reserve exit) at the final auction after every history, as in the source.

The first-round claim for firm 2 is b2=l2. In Proposition 7(c), max in the printed expression conflicts with the stated feasible reserve bound and the optimizer described at the end of Appendix 7.5. We test the intended min expression, not merely the printed typo.

## Exact deviation against the published intended profile
Set k=4 and firm 2 type (l2,m2)=(14,11). For rival second-round cost m:
- w1(m)=4(16-m)/10+8/10 for m<=16, and (20-m)^2/20 otherwise.
- rival first-round bid B1=min(20,l1+w1(m)).
- conditional second-round profits of firm 2: Gwin=(m-11)_+; Glose=(min(m+4,20)-11)_+ (win/lose refer to round 1).
- D2=Glose-Gwin.

For a deviation from bid 14 to 15, only rival bids between 14 and 15 switch the first allocation. Conditional on m the density of these bids is 1/10, because the maximum w1 is 3.2 and both endpoints are strictly interior. The expected improvement is integral over m and x in [14,15] of (D2-(x-14))/100 = 53/200. The expected D2 is 63/20. In this region the derivative is (17.15-b)/10.

Hence the profile cannot be a Bayesian equilibrium. The positive deviation is robust by continuity to an open neighborhood of types; an isolated measure-zero type is not the basis of the conclusion. All deviating bids are strictly below reserve. Against the original rival strategy the best interior reply is 17.15 (not a new joint equilibrium). The choice of cap/exit convention does not change this interior deviation.

## Follow-on investigation
Both firms' first-round continuation gaps depend on the rival's second-round type; correct first-round bids are coupled rather than independent. Derivation in notes/01_coupled_best_responses.md. Must resolve the reserve atom, simultaneous exit, ties and continuation beliefs before claiming a global Bayesian equilibrium; must check global deviations rather than only FOCs. The correction is a separate research branch from https://github.com/ryotamatsuki/dynamic-firm-location-competition .

AI-assisted research. No independent review, author correspondence, or exhaustive erratum/citation search completed. Public repository does not imply publication or priority certification.

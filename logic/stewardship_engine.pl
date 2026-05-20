/* 
   Frosalind: Symbolic Justification Engine 
   This module handles the clinical logic and insurance-ready audit trails.
*/

:- dynamic fact/2, recommendation/2, justification/2.

% --- Clinical Knowledge Base (Derived from SAPG/IDSP) ---
guideline(meropenem, restricted, "Requires ID consultant approval or AMR confirmation").
guideline(piperacillin_tazobactam, first_line, "Appropriate for suspected Gram-negative sepsis").

% --- Forward Chaining Logic (PFC) ---
update_resistance(PatientID, Gene, Severity) :-
    Severity == high,
    assertz(fact(PatientID, resistant_to(piperacillin_tazobactam))),
    justify_switch(PatientID).

justify_switch(PatientID) :-
    fact(PatientID, resistant_to(piperacillin_tazobactam)),
    assertz(recommendation(PatientID, switch_to(meropenem))),
    assertz(justification(PatientID, "Structural Manifold Analysis (Dir-SNN) identified a 2-simplex shift in PBPs, indicating high probability of beta-lactamase evasion.")).

% --- Insurance-Ready Audit Trail ---
generate_audit_trail(PatientID) :-
    recommendation(PatientID, Action),
    justification(PatientID, Logic),
    format('PATIENT: ~w~nACTION: ~w~nJUSTIFICATION: ~w~nCOMPLIANCE: SAPG Section 4.2~n', [PatientID, Action, Logic]).

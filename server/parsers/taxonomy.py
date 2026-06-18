"""
ForgeSign Clause Taxonomy.
Maps the standard universal clauses and contract-specific clauses for extraction.
"""

class ClauseTaxonomy:
    """
    Standard clause types across all commercial contracts.
    ForgeSign must detect and analyze ALL applicable types.
    """

    UNIVERSAL_CLAUSES = [
        "term_and_termination",         # contract duration, renewal, exit
        "payment_terms",                # amounts, timing, penalties
        "limitation_of_liability",      # liability caps, exclusions
        "indemnification",              # who protects whom from what
        "intellectual_property",        # ownership, license grants
        "confidentiality_nda",          # what's confidential, how long
        "governing_law_jurisdiction",   # which courts, which law
        "dispute_resolution",           # arbitration, mediation, courts
        "force_majeure",               # what excuses non-performance
        "entire_agreement",            # integration clause
        "amendment_procedure",         # how to change the contract
        "assignment",                  # can either party transfer rights?
        "notices",                     # how to give formal notice
        "severability",               # what happens if a clause is invalid
        "waiver",                      # effect of not enforcing a right
    ]

    CONTRACT_SPECIFIC = {
        "saas_agreement": [
            "service_level_agreement",  # uptime guarantees
            "data_processing",          # GDPR/data privacy obligations
            "acceptable_use_policy",    # what user can't do
            "subscription_auto_renewal", # auto-renewal mechanics
            "price_increase_rights",    # can vendor raise prices?
            "data_portability",         # can you export your data?
            "data_deletion",            # what happens on termination?
        ],
        "freelance_service": [
            "scope_of_work",           # what you must deliver
            "revision_policy",          # how many rounds of revisions
            "ip_ownership",            # does client own your work?
            "kill_fee",                # payment if project cancelled
            "late_payment_penalty",    # interest on late payment
            "non_solicitation",        # no poaching each other's clients
            "portfolio_rights",        # can you show this in your portfolio?
        ],
        "employment_offer": [
            "compensation_structure",  # base, variable, equity
            "at_will_vs_fixed_term",   # how easily can you be fired?
            "non_compete",             # post-employment restrictions
            "non_solicitation",        # can you hire former colleagues?
            "ip_assignment",           # does company own your ideas?
            "moonlighting_policy",     # can you do side work?
            "severance",               # what you get if terminated
        ],
        "commercial_lease": [
            "rent_escalation",         # how rent increases
            "security_deposit",        # amount, conditions for return
            "maintenance_obligations", # tenant vs landlord responsibilities
            "subletting_rights",       # can you sublet?
            "fit_out_allowance",       # who pays for improvements?
            "renewal_option",          # right to renew on what terms?
            "break_clause",            # early exit options
        ],
        "loan_agreement": [
            "interest_rate",           # fixed vs floating
            "prepayment_penalty",      # cost to pay early
            "acceleration_clause",     # when full amount becomes due
            "cross_default",           # other loans trigger this default
            "covenant_compliance",     # ongoing obligations
            "security_and_collateral", # what you're pledging
        ]
    }

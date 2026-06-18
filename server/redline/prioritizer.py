"""
Redline Prioritization.
Helps the user pick their battles based on leverage and deal importance.
"""
from pydantic import BaseModel
from typing import List, Literal
from loguru import logger
from .generator import ClauseRedline

class PrioritizedRedline(BaseModel):
    redline: ClauseRedline
    negotiation_strategy_note: str

class RedlinePrioritizer:

    def prioritize_redlines(
        self,
        redlines: List[ClauseRedline],
        user_leverage: float,          # 0-1, how much negotiating power?
        deal_importance: Literal["critical", "important", "routine"]
    ) -> List[PrioritizedRedline]:
        """
        Strategy:
        - High leverage + critical deal: fight for all must_have redlines
        - Low leverage + critical deal: fight only for top 3 must_have
        - Routine deal: suggest 2-3 must_have only (pick battles carefully)

        Output: ordered list with negotiation strategy note for each.
        """
        logger.info(f"Prioritizing {len(redlines)} redlines. Leverage: {user_leverage}, Deal: {deal_importance}")
        
        prioritized = []
        
        # Segregate by priority
        must_haves = [r for r in redlines if r.priority == "must_have"]
        nice_to_haves = [r for r in redlines if r.priority == "nice_to_have"]
        
        # Apply leverage logic
        if user_leverage > 0.7:
            # High leverage: push for everything
            for mh in must_haves:
                prioritized.append(PrioritizedRedline(
                    redline=mh,
                    negotiation_strategy_note="Hold firm on this. You have the leverage."
                ))
            for nth in nice_to_haves:
                prioritized.append(PrioritizedRedline(
                    redline=nth,
                    negotiation_strategy_note="Introduce this as a preference, but be willing to trade."
                ))
        elif user_leverage < 0.4 and deal_importance == "critical":
            # Low leverage, critical deal: pick battles
            top_3 = must_haves[:3]
            for mh in top_3:
                prioritized.append(PrioritizedRedline(
                    redline=mh,
                    negotiation_strategy_note="Critical risk. Frame this pushback carefully."
                ))
        else:
            # Routine: just the basics
            for mh in must_haves[:2]:
                prioritized.append(PrioritizedRedline(
                    redline=mh,
                    negotiation_strategy_note="Routine deal standard pushback. Should be acceptable."
                ))
                
        logger.success(f"Generated {len(prioritized)} prioritized negotiation strategies.")
        return prioritized

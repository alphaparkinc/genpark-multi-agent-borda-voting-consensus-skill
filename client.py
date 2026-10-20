"""Multi-Agent Borda Voting Consensus.
100% Python Standard Library.
"""

class MultiAgentBordaVotingConsensus:
    """Positional Borda Count voting and weighted multi-agent consensus engine."""

    @staticmethod
    def calculate_consensus(candidates: list, agent_ballots: list) -> dict:
        m = len(candidates)
        scores = {c: 0.0 for c in candidates}
        breakdown = {c: {} for c in candidates}

        for ballot in agent_ballots:
            agent = ballot.get("agent_id", "anonymous")
            weight = ballot.get("weight", 1.0)
            ranking = ballot.get("ranking", [])

            for rank_idx, cand in enumerate(ranking):
                if cand in scores:
                    points = (m - 1 - rank_idx) * weight
                    scores[cand] += points
                    breakdown[cand][agent] = points

        sorted_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        winner = sorted_results[0][0] if sorted_results else None
        is_tie = len(sorted_results) > 1 and sorted_results[0][1] == sorted_results[1][1]

        return {
            "winner": winner,
            "is_tie": is_tie,
            "rankings": [{"candidate": cand, "score": round(score, 4)} for cand, score in sorted_results],
            "candidate_scores": {k: round(v, 4) for k, v in scores.items()},
            "ballot_count": len(agent_ballots)
        }

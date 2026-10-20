"""Example usage for Multi-Agent Borda Voting Consensus."""
from client import MultiAgentBordaVotingConsensus
import json

cands = ["Design A: Microservices", "Design B: Modular Monolith", "Design C: Serverless"]
ballots = [
    {"agent_id": "architect_agent", "weight": 1.5, "ranking": ["Design B: Modular Monolith", "Design A: Microservices", "Design C: Serverless"]},
    {"agent_id": "security_agent", "weight": 1.0, "ranking": ["Design B: Modular Monolith", "Design C: Serverless", "Design A: Microservices"]},
    {"agent_id": "devops_agent", "weight": 1.2, "ranking": ["Design A: Microservices", "Design B: Modular Monolith", "Design C: Serverless"]}
]

consensus = MultiAgentBordaVotingConsensus.calculate_consensus(cands, ballots)
print(json.dumps(consensus, indent=2))

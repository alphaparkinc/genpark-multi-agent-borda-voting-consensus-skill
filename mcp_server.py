"""MCP Server for Multi-Agent Borda Voting Consensus.
100% Python Standard Library JSON-RPC.
"""
import sys
import json
from client import MultiAgentBordaVotingConsensus

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")

            if method == "tools/list":
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "tools": [
                            {
                                "name": "calculate_consensus",
                                "description": "Calculate consensus winner across multi-agent rankings using weighted Borda count",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {
                                        "candidates": {"type": "array", "description": "Candidate proposals list"},
                                        "agent_ballots": {"type": "array", "description": "Agent ranking ballots list"}
                                    },
                                    "required": ["candidates", "agent_ballots"]
                                }
                            }
                        ]
                    }
                }
            elif method == "tools/call":
                args = req.get("params", {}).get("arguments", {})
                res = MultiAgentBordaVotingConsensus.calculate_consensus(
                    candidates=args.get("candidates", []),
                    agent_ballots=args.get("agent_ballots", [])
                )
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
                }
            else:
                resp = {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()

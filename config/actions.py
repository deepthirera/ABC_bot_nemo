from typing import Optional

from nemoguardrails.actions import action

@action(is_system_action=True)
async def check_blocked_terms(context: Optional[dict] = None):
    user_message = context.get("user_message")
    proprietary_terms = ["SynapseAI", "NexusTech", "ZenithLabs", "client", "confidential", "password"]

    for term in proprietary_terms:
        if term in user_message:
            return True

    return False
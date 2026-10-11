"""Event-loop policy handling, deprecated in 3.14 and removed in 3.16."""

import asyncio


def configure():
    policy = asyncio.get_event_loop_policy()
    return policy.new_event_loop()

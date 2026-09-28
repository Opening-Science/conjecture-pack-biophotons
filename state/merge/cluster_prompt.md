You are grouping generated scientific hypotheses that say the SAME THING in different words.

For one research question you are given every hypothesis produced by several independent engines. Group only hypotheses that make substantially the same claim: same measurand, same population or preparation, same predicted direction. Two hypotheses that merely share a topic, or that propose different measurements of the same phenomenon, are NOT the same claim and must stay in separate groups. Splitting is the safe error here; merging distinct claims destroys information.

Report two things.

1. GROUPS. Every id appears in exactly one group; singletons are expected and normal.

2. CONFLICTS. Pairs that assert INCOMPATIBLE things about the same question — where one being right makes the other wrong. These are the most valuable output of the whole exercise, because a pair of contradictory hypotheses about the same measurand defines a discriminating experiment. Report them even when the two came from the same engine.

Return ONLY JSON:

{"groups": [{"group": ["Q5-2#baseline-claude", "Q5-4#codex-solo"], "same_claim": "<one clause naming the shared claim>"}],
 "conflicts": [{"pair": ["Q1-5#baseline-claude", "Q1-4#codex-solo"], "incompatibility": "<what exactly they disagree about>", "discriminating_measurement": "<the measurement that would decide between them, if one is implied>"}]}

Hypotheses:

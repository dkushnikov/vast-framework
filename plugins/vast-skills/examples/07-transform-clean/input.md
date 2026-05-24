# Project brief — Support Copilot

Our support agents are drowning. Every ticket means hunting through five
different systems — the help center, past tickets, the billing console, the
product changelog, internal runbooks — before they can even start typing a
reply. New hires take three months to get fast at it, and even veterans burn
most of their day on lookup rather than on the actual customer. We think a
support agent should spend their time on judgment and empathy, not on
information retrieval. So we want to build a copilot that does the hunting for
them: it reads the ticket, pulls the relevant context from all five systems,
and drafts a reply the agent can edit and send. The agent stays in control —
the copilot proposes, the human decides — but the grunt work disappears.

This is for our front-line support team specifically: the people who handle
tier-1 and tier-2 tickets all day. Not for engineers, not for the success team.

Under the hood it's a few cooperating pieces. There's a retriever that searches
across the five sources and ranks passages by relevance. There's a summarizer
that condenses a long ticket thread down to the actual question. There's a
drafter that writes the candidate reply grounded in the retrieved passages, in
the agent's tone. And there's a classifier up front that routes the ticket
(billing / technical / account) so the retriever knows where to look first.

A few things we are firm on no matter how the tech evolves. The drafter must
never send on its own — sending is always the agent clicking the button. Every
draft has to cite the sources it pulled from, so the agent can verify, no
ungrounded answers. If the retriever comes back with nothing confident, the
copilot says "no good context found" and steps back rather than hallucinating
a reply. And no customer data ever leaves our tenant to train anything.

On models and plumbing we'll stay flexible. Right now we're using a big
frontier model for the drafter and summarizer and a small cheap classifier
model for routing; retrieval is embeddings over a vector store. We'll swap any
of that as better/cheaper options show up — output is JSON via the model's
structured-output mode for now, retries are two attempts at an 8-second timeout.

How we'll roll it out: start with the classifier-plus-retriever piece alone,
no drafting, and put it in front of ten volunteer agents to see if the context
it surfaces is actually the context they'd have hunted for. Only once that's
trusted do we turn on the drafter, and we'll check tone-match with the same ten
before opening it to the floor. The action-extraction idea (auto-creating
follow-up tasks from a ticket) can wait — it's a nice-to-have, not part of the
core loop. We're front-loading the read-side pieces because they earn trust
without the risk of a bad outgoing reply; the write-side waits behind that.

In practice it adapts per agent. A billing-heavy agent gets routing tuned to
hit the billing console first; a technical agent's drafter primes on their last
twenty replies for tone; each agent can set how aggressively the copilot
auto-collapses low-relevance context versus showing everything.

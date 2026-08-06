from ai.reasoning import reasoning
from ai.memory import memory
from ai.conversation import conversation
from ai.responder import responder


class Brain:

    def think(self, text):

        #
        # Store user message
        #

        conversation.add(
            "user",
            text
        )

        #
        # Recall useful memory
        #

        facts = memory.recall(text)

        #
        # Reason
        #

        decision = reasoning.decide(
            text,
            facts
        )

        #
        # Generate response
        #

        reply = responder.respond(
            decision
        )

        #
        # Store reply
        #

        conversation.add(
            "jarvis",
            reply
        )

        return reply


brain = Brain()


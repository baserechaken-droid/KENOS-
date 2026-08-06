from core.memory import memory
from core.scheduler import scheduler
from core.action_engine import engine
from core.plugin_registry import registry


class Services:

    def __init__(self):

        self.memory = memory

        self.scheduler = scheduler

        self.engine = engine

        self.registry = registry


    def status(self):

        return {

            "plugins": len(
                self.registry.names()
            ),

            "memory": len(
                self.memory.all()
            ),

            "jobs": self.scheduler.running()

        }


services = Services()


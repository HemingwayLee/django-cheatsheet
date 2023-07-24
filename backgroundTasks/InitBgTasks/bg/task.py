from background_task import background
import logging

logger = logging.getLogger(__name__)

@background(schedule=10)
def demo_task():
    logger.info("in the background...")


@background(schedule=10)
def the_init_task():
    logger.info("init task in the background...")


import logging
import subprocess

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    gradle_setup_cmds = [
        ["gradle", "wrapper"],
        ["./gradlew", "updateDaemonJvm"],
    ]

    try:
        for cmd in gradle_setup_cmds:
            subprocess.run(cmd, check=True)
    except Exception as e:
        msg = f"Unable to setup gradle: {e}\nPlease manually run these commands in the project directory when the issue is fixed:\n"

        for cmd in gradle_setup_cmds:
            msg += " ".join(cmd) + "\n"

        logger.warning(msg)

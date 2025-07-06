import subprocess
import sys

def main():
    subprocess.check_call(
        [
            sys.executable,
            '-m', 'rl_zoo3.record_video',
            '--algo', 'ppo',
            '--env', 'SpaceInvadersNoFrameskip-v4',
            '--folder', 'logs/',
            '-n', '3000',
            '--load-best',
        ]
    )

if __name__ == "__main__":
    main()

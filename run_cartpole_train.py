import sys
from rl_zoo3.train import train
def main():
    sys.argv = [sys.argv[0]]
    sys.argv.extend([
        '--algo', 'ppo',
        '--env', 'CartPole-v1',
        '--log-folder', 'logs/',
        '-n', '5000',
         ])

    train()

if __name__ == "__main__":
    main()

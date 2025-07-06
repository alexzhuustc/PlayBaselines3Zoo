import sys

sys.argv = [sys.argv[0]]
sys.argv.extend([
    '--algo', 'dqn',
    '--env', 'CartPole-v1',
    '--folder', 'logs/',
    '-n', '1000',
     ])

from rl_zoo3.enjoy import enjoy

def main():
    enjoy()

if __name__ == "__main__":
    main()

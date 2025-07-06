import sys
from rl_zoo3.enjoy import enjoy

def main():
    sys.argv = [sys.argv[0]]
    sys.argv.extend([
        '--algo', 'ppo',
        '--env', 'CartPole-v1',
        '--folder', 'logs/',
        '-n', '1000',
         ])

    enjoy()




if __name__ == "__main__":
    main()

import sys
import pygame
from rl_zoo3.enjoy import enjoy



def main():

    pygame.init()

    sys.argv = [sys.argv[0]]
    sys.argv.extend([
        '--algo', 'ppo',
        '--env', 'SpaceInvadersNoFrameskip-v4',
        '-n', '5000',
        '--folder', 'logs/',
        '--load-best',
         ])

    enjoy()

if __name__ == "__main__":
    main()

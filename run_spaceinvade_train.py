import sys

sys.argv = [sys.argv[0]]
sys.argv.extend([
    '--algo', 'ppo',
    '--env', 'SpaceInvadersNoFrameskip-v4',
    '--conf-file', 'hyperparams/python/zhulei.py',
    '--tensorboard-log', 'tensorboard-log/',
    '--save-freq', '100000',
    # 恢复前一次 checkpoint
    # '-i', 'logs/a2c/SpaceInvadersNoFrameskip-v4_4/SpaceInvadersNoFrameskip-v4.zip',
    '-n', str(10*1000*1000),
     ])

from rl_zoo3.train import train

def main():
    train()

if __name__ == "__main__":
    main()

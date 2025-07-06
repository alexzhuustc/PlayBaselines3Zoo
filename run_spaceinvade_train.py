import sys
import rl_zoo3.record_video

sys.argv = [sys.argv[0]]
sys.argv.extend([
    '--algo', 'ppo',
    '--env', 'SpaceInvadersNoFrameskip-v4',
    '--vec-env', 'subproc',  # 设置为 subproc以启用多进程环境。进程数量在hyperparams/ppo.yml文件中指定n_envs。
    '--device', 'cuda',
    '--log-folder', 'logs/',
    '--tensorboard-log', 'tensorboard-log/',
    '--conf-file', 'hyperparams/ppo.yml',
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

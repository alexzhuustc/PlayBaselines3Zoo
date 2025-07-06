import sys
import my_utils
from rl_zoo3.train import train

def main():
    sys.argv = [sys.argv[0]]
    sys.argv.extend([
        '--algo', 'ppo',
        '--env', 'SpaceInvadersNoFrameskip-v4',
        '--vec-env', 'subproc',  # 设置为 subproc以启用多进程环境。进程数量在hyperparams/ppo.yml文件中指定n_envs。
        '--device', 'cuda',
        '--log-folder', 'logs/',
        '--log-interval', '2',
        '--tensorboard-log', 'tensorboard-log/',
        '--conf-file', 'hyperparams/ppo.yml',
        '--save-freq', '100000',
        '-n', str(10*1000*1000),
     ])

    # 恢复前次训练
    my_utils.continue_previous_checkpoint()

    # 训练
    train()

if __name__ == "__main__":
    main()

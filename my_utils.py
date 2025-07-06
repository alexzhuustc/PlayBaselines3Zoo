import os
import sys
import re


def continue_previous_checkpoint():
    # 恢复前一次 checkpoint
    # '--trained-agent', 'logs/a2c/SpaceInvadersNoFrameskip-v4_4/SpaceInvadersNoFrameskip-v4.zip',
    args_map = {}
    encounter_key_value = False
    for i in range(len(sys.argv)):
        if encounter_key_value:
            args_map[sys.argv[i-1]] = sys.argv[i]
            encounter_key_value = False
        elif (sys.argv[i].startswith('-')):
            encounter_key_value = True

    if '--log-folder' not in args_map or '--env' not in args_map or '--algo' not in args_map:
        print('请指定 --log-folder 和 --env 参数 和 --algo 参数')
        return

    alg_root = os.path.join(args_map['--log-folder'], args_map['--algo'])
    env_name = args_map['--env']
    last_exp_name = _find_latest_experiment(alg_root, env_name, '')
    if last_exp_name is None:
        return

    exp_dir = os.path.join(alg_root, last_exp_name)
    last_checkpoint_name = _find_latest_experiment(exp_dir, 'rl_model', 'steps.zip')
    if last_checkpoint_name is None:
        return

    last_checkpoint_path = os.path.join(exp_dir, last_checkpoint_name)
    print(f'use last checkpoint: {last_checkpoint_path}')
    sys.argv.extend(['--trained-agent', last_checkpoint_path])

def _find_latest_experiment(dir, prefix, suffix) -> str:
    childs =os.listdir(dir)
    seq_map = {}
    for child in childs:
        if not child.startswith(prefix) or not child.endswith(suffix):
            continue

        middle = child[len(prefix) : len(child) - len(suffix) ]
        m = re.search(r'\d+', middle)
        if m is None:
            continue

        seq = int(m.group())
        seq_map[seq] = child

    if len(seq_map) == 0:
        return None

    max_seq = max(seq_map.keys())
    return seq_map[max_seq]

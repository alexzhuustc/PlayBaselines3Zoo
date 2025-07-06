[TOC]

Play[BaselinesZoo是一个Windows中的项目。使用rl-stablebaseline3-zoo来体验一次训练模型玩游戏的过程。适合新手小白。

# 安装环境
 - 安装uv (比如：pip install uv)
 - 修改 `pyproject.toml`文件 ，把最下方的内容调整为如下内容。 
```
# 国内镜像：
url = https://mirror.nju.edu.cn/pytorch/whl/cu128

# 我的NAS缓存：
# url = "http://192.168.1.16:3320/pytorch/whl/cu128"
```
 - 运行`build_uv_sync.bat`。这个BAT会通过上面的uv准备python venv环境，并开始安装所有的依赖包。
 - 使用`.venv/Scripts/activate.bat` 激活Python venv环境。
 - 运行`check_gpu.py`。
   - 如果提示`PyTorch can use GPU`，说明安装成功，并且可以使用GPU加速。
   - 如果提示`PyTorch will use CPU`，同样说明安装成功，但是没有GPU加速，只能使用 CPU进行训练。


# 体验cartpole游戏

- 运行[run_cartpole_train.py](run_cartpole_train.py)将训练模型。训练耗时不到1分钟。
- 运行[run_cartpole_enjoy.py](run_cartpole_enjoy.py)，你可以看到刚才的模型玩游戏，观察训练结果

# 体验space invade游戏

- 运行[run_spaceinvade_train.py](run_spaceinvade_train.py)。由于Space Invade是一个较难的游戏，训练将耗费至少1个小时。
- 在此期间，你可以运行 [run_tensorboard.bat](run_tensorboard.bat)， 并打开地址 http://localhost:6006/ 来观测训练进度。当eval -> mean_reward达到900分时，说明模型已经玩得还不错了。此时，可以中止训练
- 当训练结束后，运行[run_spaceinvade_enjoy.py](run_spaceinvade_enjoy.py)，你可以看到模型玩游戏
- 你还可以通过[run_spaceinvade_enjoy_save_video.py](run_spaceinvade_enjoy_save_video.py)，将模型玩游戏的过程保存为视频。

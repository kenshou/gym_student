# 项目描述
主要实验gym深度学习环境
# 基础环境安装
* 建立环境  
conda create -n gym
* 激活环境  
conda activate gym
* 安装gym  
pip install gym
* 检查安装[00_test.py](/00_test.py) 如果出现平衡小棒棒就安装成功 
```python
import gym
# import time
env = gym.make('CartPole-v1')
#动作空间
print(env.action_space)

for i_episode in range(100):
    env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        # time.sleep(0.02)
        if done:
            # print("Episode finished after {} timesteps".format(t+1))
            break

```
# win10 安装atari
pip install --no-index -f https://github.com/Kojoley/atari-py/releases atari_py

# 游戏环境描述
https://gym.openai.com/envs/

# 其他
* [超级马里奥](/superMario/) 
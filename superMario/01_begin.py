from nes_py.wrappers import BinarySpaceToDiscreteSpaceEnv
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from tqdm import tqdm

def get_action(state,action_space):
    '''
    返回当前环境下的操作

        Args:
            state: 环境
            action_space: 操作空间

        Returns:
            操作
    '''
    return action_space.sample()


def main():
    env = gym_super_mario_bros.make('SuperMarioBros-v0')
    env = BinarySpaceToDiscreteSpaceEnv(env, SIMPLE_MOVEMENT)

    done = True
    max_step=5000
    #win下加ascii=True才会不换行
    qbar=tqdm(max_step,ascii=True)
    for step in range(max_step):
        qbar.update()
        if done:
            state = env.reset()
        action=get_action(state,env.action_space)
        state, reward, done, info = env.step(action)
        if done:
            print(str(step)+" 英雄请卷土重来"+str(info))
        # env.render()
    env.close()
    qbar.close()

if __name__ == '__main__':
  main()
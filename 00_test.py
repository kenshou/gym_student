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

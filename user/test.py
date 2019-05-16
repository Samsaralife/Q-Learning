import gym

env = gym.make('GridWorld-v1')
env.reset()
done = True
while done==True:
    env.render()

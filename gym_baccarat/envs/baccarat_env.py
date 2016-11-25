import gym
from gym import error, spaces, utils
from gym.utils import seeding


deck = [1,2,3,4,5,6,7,8,9,0,0,0,0]

def draw_card(np_random):
    return int(np_random.choice(deck))

def draw_hand(np_random):
    return [draw_card(np_random), draw_card(np_random)]

def sum_hand(hand):
    return (sum(hand) % 10)

class BaccaratEnv(gym.Env):
    metadata = {'render.modes':['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Tuple((spaces.Discrete(9),spaces.Discrete(9)))

        self._seed()
        self._reset()



    def __del__(self):
        self.env.act(hfo_py.QUIT)
        self.env.step()
        os.kill(self.server_process.pid, signal.SIGINT)

    def _step(self, action):
        assert self.action_space.contains(action)
        if action == 1:
            self.player.append(draw_card(self.np_random))
            if self.player[-1] in [2,3] and sum_hand(self.dealer) < 5:
                self.dealer.append(draw_card(self.np_random))
            elif self.player[-1] in [4,5] and sum_hand(self.dealer) < 6:
                self.dealer.append(draw_card(self.np_random))
            elif self.player[-1] in [6,7] and sum_hand(self.dealer) < 7:
                self.dealer.append(draw_card(self.np_random))
            elif self.player[-1] == 8 and sum_hand(self.dealer) < 3:
                self.dealer.append(draw_card(self.np_random))
            elif sum_hand(self.dealer) < 4:
                self.dealer.append(draw_card(self.np_random))
        else:
            if sum_hand(self.dealer) < 6:
                self.dealer.append(draw_card(self.np_random))

        reward = cmp(sum_hand(self.player), sum_hand(self.dealer))

        return self._get_obs(), reward, True, {}



    def _get_obs(self):
        return (sum_hand(self.player), sum_hand(self.dealer))

    def _reset(self):
        self.dealer = draw_hand(self.np_random)
        self.player = draw_hand(self.np_random)
        while (sum_hand(self.dealer) >7 or sum_hand(self.player)>7):
            self.dealer = draw_hand(self.np_random)
            self.player = draw_hand(self.np_random)
        return self._get_obs()

    def _render(self, mode='human', close=False):



